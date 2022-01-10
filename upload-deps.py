#!/usr/bin/env python3

"""
Upload a locally built dependency bundle to Workiva Scripting.

Dependency bundles can be built using the following commands:

    0. mkdir dependencies
    1. docker run --asdf ... --target dependencies
    2. pushd dependencies
    3. zip -o ../dependencies.zip
    4. popd
    5. rm -r dependencies

Optional Environment Variables:

    BEARER_TOKEN
    CLIENT_ID
    CLIENT_SECRET
    IAM_HOST
    SCRIPT_HOST
    SCRIPT_ID

Example Invocations

    # Assuming CLIENT_ID, CLIENT_SECRET, IAM_HOST environment variables are specified specified
    ./upload-deps.py --script-id 00000000-0000-0000-0000-000000000000

    # Already have a JWT?
    ./upload-deps.py --script-id 00000000-0000-0000-0000-000000000000 \\
                     --bearer-token $MY_BEARER_TOKEN \\
                     --scripting-host https://app.wdesk.com/s/scripting

"""

import argparse
import os
import sys


try:
    # TODO: reduce dependencies
    import requests
except ImportError:
    print("This script requires the requests library")
    print("Run the following to resolve: `pip install requests`")
    sys.exit(1)


__version__ = "0.0.0"


def fetch_jwt(iam_host, client_id, client_secret):
    print(f"Fetching authentication ...", end=" ")
    sys.stdout.flush()
    res = requests.post(
        f"{iam_host}/iam/v1/oauth2/token",
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
        },
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        },
    )
    if not res.ok:
        print("FAIL")
        print("Failed to fetch Authentication token")
        print(res.text)
        sys.exit(1)
    print("DONE")
    return res.json().get("access_token")


def upload_deps(scripting_host, bearer_token, script_id, bundle):
    files = f"{scripting_host}/v0/scripts/{script_id}/files"
    session = requests.Session()
    session.headers["Authorization"] = f"Bearer {bearer_token}"

    print("Check for existing file ...", end=" ")
    sys.stdout.flush()
    res = session.get(files)
    if not res.ok:
        print("FAIL")
        print("Unable to fetch file listing")
        print(res.text)
        sys.exit(1)
    print("DONE", end=" ")

    try:
        file_id = next(
            file.get("id")
            for file in res.json()
            if file.get("path") == "dependencies.zip"
        )
        print("(existing file detected)")
    except StopIteration:
        print("(no existing file found)")
        print("Creating scripting file ...", end=" ")
        sys.stdout.flush()
        res = session.post(files, json={"path": "dependencies.zip"})
        if not res.ok:
            print("FAIL")
            print("Unable to create file")
            print(res.text)
            sys.exit(1)
        print("DONE")
        file_id = res.json().get("id")

    print("Uploading binary source ...", end=" ")
    sys.stdout.flush()
    res = session.put(files + "/" + file_id, data=bundle)
    if not res.ok:
        print("FAIL")
        print("Unable to upload data")
        print(res.text)
        sys.exit(1)
    print("DONE")


class EnvDefault(argparse.Action):
    def __init__(self, envvar=None, required=False, default=None, **kwargs):
        if not envvar:
            envvar = kwargs["option_strings"][-1].strip(
                "-").upper().replace("-", "_")
        if not default and envvar:
            default = os.environ.get(envvar)
        if required and default:
            required = False
        super(EnvDefault, self).__init__(
            default=default, required=required, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


def main():
    v = sys.version_info[:2]
    if v < (3, 4):
        print(
            "This script requires at least python v3.4; detected v{0}.{1}".format(*v))
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Copyright Workiva 2021",
    )
    parser.add_argument("-v", "--version",
                        action="version", version=__version__)
    parser.add_argument(
        "--bearer-token",
        action=EnvDefault,
        help="use bearer token instead of fetching on (env: BEARER_TOKEN)",
    )
    parser.add_argument(
        "--client-id", action=EnvDefault, help="used to fetch authorization token"
    )
    parser.add_argument(
        "--client-secret", action=EnvDefault, help="used to fetch authorization token"
    )
    parser.add_argument(
        "--iam-host",
        action=EnvDefault,
        required=True,
        help="host to exchange credentials with for a BEARER_TOKEN",
    )
    parser.add_argument(
        "--script-host",
        action=EnvDefault,
        help="override scripting host (default: IAM_HOST)",
    )
    parser.add_argument(
        "--script-id",
        action=EnvDefault,
        required=True,
        help="attach dependencies.zip to this script",
    )
    parser.add_argument(
        "--bundle",
        default="dependencies.zip",
        type=argparse.FileType("rb"),
        help="Name of the dependency bundle to upload (default: dependencies.zip)",
    )
    args = parser.parse_args()

    missing_client_args = args.client_id is None or args.client_secret is None
    if args.bearer_token is None and missing_client_args:
        parser.error(
            "missing --bearer-token or both --client-id and --client-secret")

    if not args.script_host:
        args.script_host = args.iam_host + "/s/scripting"

    if not args.bearer_token:
        args.bearer_token = fetch_jwt(
            args.iam_host, args.client_id, args.client_secret)

    upload_deps(args.script_host, args.bearer_token,
                args.script_id, args.bundle)


if __name__ == "__main__":
    main()
