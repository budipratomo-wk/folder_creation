import io
import json
from time import sleep
import requests
import pandas as pd
import os
from urllib.parse import quote

def init():
    os.environ["TOKEN_API_URL"] = "https://api.demo.wdesk.com/iam/v1/oauth2/token"
    os.environ["SHEET_API_URL"] = "https://api.demo.wdesk.com/platform/v1/spreadsheets"
    os.environ["FILES_API_URL"] = "https://api.demo.wdesk.com/platform/v1/files"
    os.environ["WDATA_API_URL"] = "https://h.demo.wdesk.com/s/wdata/prep/api/v1"
    os.environ["ENTITY_API_URL"] = "https://h.demo.wdesk.com/s/wdata/prep/api/v1/entity"


def get_token():
    api_url = os.environ["TOKEN_API_URL"]
    client_id = os.environ["CLIENT_ID"]
    client_secret = os.environ["CLIENT_SECRET"]

    body = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }

    r = requests.post(api_url, headers=headers, data=body)
    # print(r.json())
    return r.json()["access_token"]

def download_export(operation_url):
    token = get_token()
    headers = {"Accept": "application/json", "Authorization": "Bearer {}".format(token)}
    r = requests.get(operation_url,headers=headers)
    if r.json()["status"] == "completed":
        s=requests.get(r.json()["resourceUrl"],headers=headers).content
        dftemp= pd.read_csv(io.StringIO(s.decode('utf-8')),chunksize=100)
        chunks=[]
        for chunk in dftemp:
            chunks.append(chunk)
        df= pd.concat(chunks,ignore_index=True)

        return df
    else:
        sleep(5)
        return download_export(operation_url)

# Spreadsheets
def get_spreadsheet(spreadsheet_id, sheet_id):
    sheet_url = "{}/{}/export".format(
        os.environ["SHEET_API_URL"], spreadsheet_id
    )

    body = {"format": "csv", "sheets": ["{}".format(sheet_id)]}
    token = get_token()
    headers = {"Accept": "application/json", "Authorization": "Bearer {}".format(token)}

    print(sheet_url)
    print(body)
    r = requests.post(sheet_url, headers=headers,data=json.dumps(body))
    print(r.headers["Location"])
    df = download_export(r.headers["Location"])
    print(df)
    return df
# GENERAL


# FOLDERS
def search_folder(name,description=None,type="600"):
    url = os.environ["ENTITY_API_URL"] + "?name=" + quote(name) +  "&type=" +  quote(type)
    token = get_token()
    headers = {"Accept": "application/json", "Authorization": "Bearer {}".format(token)}
    r = requests.get(url,headers=headers)
    return r.json()["body"]


def get_existing_folder_id(name):

    folder_array=search_folder(name)
    folder_id = None
    for i in range(0,len(folder_array)):
        if  name == folder_array[i]["name"]:
            folder_id = folder_array[i]["id"]
    return folder_id



def create_folder_if_not_exists(name):
    files_url = os.environ["WDATA_API_URL"] + "/folder"
    body =  {"name":name}
    token = get_token()
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
     ,"Authorization": "Bearer {}".format(token)}
    print("==============================================================")
    print("Creating folder {}".format(name))
    print("With body")
    print(body)
    print("to endpoint {}".format(files_url))
    print("==============================================================")
    existing_folder_id = get_existing_folder_id(name)
    if (existing_folder_id is None):
        r = requests.post(files_url,headers=headers,data=json.dumps(body))
        print(r.json())
        return(r.json()["body"]["id"])
    else:
        return existing_folder_id

def delete_folder(folder_id):
    files_url = os.environ["WDATA_API_URL"] + "/folder/" + folder_id
    token = get_token()
    headers = {
  'Accept': '*/*',
     "Authorization": "Bearer {}".format(token)}
    print("==============================================================")
    print("Deleting folder{}".format(folder_id))
    print("to endpoint {}".format(files_url))
    print("==============================================================")
    r = requests.delete(files_url,headers=headers)
    print(r.json())


def move_folder(folder_id,parent_id):
    files_url = os.environ["WDATA_API_URL"] + "/folder/" + parent_id + "/children"
    body = [{"id":folder_id,"type":600}]
    token = get_token()
    headers = {"Accept": "application/json", "Content-Type":'application/json',"Authorization": "Bearer {}".format(token)}
    print("==============================================================")
    print("Moving folder {}".format(folder_id))
    print("With body")
    print(body)
    print("to endpoint {}".format(files_url))
    print("==============================================================")
    r = requests.post(files_url,headers=headers,data=json.dumps(body))
    print(r.json())

def get_folder_contents(folder_id):
    files_url = os.environ["WDATA_API_URL"] + "/folder/" + folder_id + "/children"
    token = get_token()
    headers = {
  'Accept': 'application/json',
     "Authorization": "Bearer {}".format(token)}
    print("==============================================================")
    print("Retrieving contents of folder{}".format(folder_id))
    print("to endpoint {}".format(files_url))
    print("==============================================================")
    r = requests.get(files_url,headers=headers)
    print(r.json()["body"])
    return (r.json()["body"])

def copy_templates(template_folder_id,target_folder_id):
    content_list = get_folder_contents(template_folder_id)
    for content in content_list:
        print(content)
def create_folder_and_subfolders(level_param_names,df,parent_id,template_folder_id):
    current_level_param,*tail = level_param_names
    folders_in_current_level = df[current_level_param].unique()
    for folder in folders_in_current_level:
        filtered_df = df[df[current_level_param]==folder]
        print("==================================================")
        print("Starting folder creation run for {}".format(folder))
        print("with subfolders to be processed:")
        print(filtered_df)
        print("With level param names:")
        print(tail)
        print("==================================================")
        folder_id = create_folder_if_not_exists(folder)
        if parent_id:
            move_folder(folder_id,parent_id)
        copy_templates(template_folder_id,folder_id)
        if len(tail)>0:
            create_folder_and_subfolders(tail,filtered_df,parent_id=folder_id,template_folder_id=template_folder_id)

# MONITOR 

def create_levels():
    input = get_spreadsheet("8dcef8239bb44978a6a396c538d2ffcb", "b6f7eef8165e4c67b0fbe43096cbf5b6")
    cleaned_input = input.dropna(how="all")
    config = get_spreadsheet("8dcef8239bb44978a6a396c538d2ffcb","5e38b19cd9ee44c68ad82558b711be39")
    levels = config[config["Parameter name"].str.contains("Level")]
    # get the level as integer
    levels["Level"] = levels["Parameter name"].str[-1].map(lambda x: int(x))
    maxlevel = levels["Level"].max()
    BaseFolderId = config[config["Parameter name"]=="BaseFolderId"]["Parameter value"].iloc[0]
    TemplateFolderId = config[config["Parameter name"]=="TemplateFolderId"]["Parameter value"].iloc[0]
    print("Base folder id is {BaseFolderId}")
    levels.sort_values(by=["Level"],inplace=True)
    print(levels)
    create_folder_and_subfolders(levels["Parameter value"].tolist(),cleaned_input,BaseFolderId,TemplateFolderId)






























init()
create_levels()
