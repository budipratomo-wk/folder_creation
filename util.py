import io
import json
from time import time
import requests
import pandas as pd
import os

def init():
    os.environ["TOKEN_API_URL"] = "https://api.demo.wdesk.com/iam/v1/oauth2/token"
    os.environ["SHEET_API_URL"] = "https://api.demo.wdesk.com/platform/v1/spreadsheets"
    os.environ["FILES_API_URL"] = "https://api.demo.wdesk.com/platform/v1/files"
    os.environ["CLIENT_ID"] = "4928e1f9e40e473090ae598d6e5f0c67"
    os.environ["CLIENT_SECRET"] = "2086b160da6cd5263e462e5b6aa8173c7537480043ca1df7"


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
        return  pd.read_csv(io.StringIO(s.decode('utf-8')))
    else:
        time.sleep(15)
        return download_export(operation_url)


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

    print(download_export(r.headers["Location"]))

def create_folder(name):
    files_url = os.environ["FILES_API_URL"]
    body =  {"kind":"Folder","name":name}
    token = get_token()
    headers = {"Accept": "application/json", "Authorization": "Bearer {}".format(token)}
    r = requests.post(files_url,headers=headers,data=json.dumps(body))
    return(r.json()["id"])

def move_folder(folderId,parentId):
    url =  "{}/{}".format(os.environ["FILES_API_URL"],folderId)
    body = {"container":parentId}
    token = get_token()
    headers = {"Accept": "application/json", "Authorization": "Bearer {}".format(token)}
    r = requests.put(url,headers=headers,data=json.dumps(body))

init()
get_token()
get_spreadsheet("8dcef8239bb44978a6a396c538d2ffcb", "b6f7eef8165e4c67b0fbe43096cbf5b6")
