import os
import sys
from urllib.parse import urlparse, parse_qs
from fyers_api import fyersModel
from fyers_api import accessToken
import requests

username = "******"  # fyers_id
password = "******"
pan = "******"
client_id = "******"  # '##########-$$$'
secret_key = "******"
redirect_uri = "******"  # 'http://localhost:4000/'

app_id = client_id[:-4]  # '##########'


def read_file():
    with open("token_fyers.txt", "r") as f:
        token = f.read()
    return token


def write_file(token):
    with open('token_fyers.txt', 'w') as f:
        f.write(token)


def setup():
    session = accessToken.SessionModel(client_id=client_id, secret_key=secret_key, redirect_uri=redirect_uri,
                                       response_type='code', grant_type='authorization_code')

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'content-type': 'application/json; charset=UTF-8',
        'accept-language': 'en-US,en;q=0.9'}

    data = f'{{"fyers_id":"{username}","password":"{password}","pan_dob":"{pan}","app_id":"{app_id}","redirect_uri":"{redirect_uri}","appType":"100","code_challenge":"","state":"abcdefg","scope":"","nonce":"","response_type":"code","create_cookie":true}}'
    resp = requests.post('https://api.fyers.in/api/v2/token', headers=headers, data=data)

    parsed = urlparse(resp.json()['Url'])
    auth_code = parse_qs(parsed.query)['auth_code'][0]
    session.set_token(auth_code)
    response = session.generate_token()
    token = response["access_token"]
    write_file(token)
    print('Got the access token!!!')
    fyers = fyersModel.FyersModel(client_id=client_id, token=token, log_path=os.getcwd())
    print(fyers.get_profile())


def check():
    try:
        token = read_file()
    except FileNotFoundError:
        print('Getting the access token!')
        setup()
        sys.exit()
    fyers = fyersModel.FyersModel(client_id=client_id, token=token, log_path=os.getcwd())
    response = fyers.get_profile()
    if 'error' in response['s'] or 'error' in response['message'] or 'expired' in response['message']:
        print('Getting a access token!')
        setup()
    else:
        print('You already have a access token!')
        print(response)


if __name__ == '__main__':
    check()
