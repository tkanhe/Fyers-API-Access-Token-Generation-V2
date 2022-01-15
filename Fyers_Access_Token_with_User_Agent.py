import os
import sys
from urllib.parse import urlparse, parse_qs
from fyers_api import fyersModel
from fyers_api import accessToken
import requests

username = "******"         # fyers_id
password = "******"         # fyers_password
pin = 1551                  # your integer pin
client_id = "******"        # "L9NY****W-100" (Client_id here refers to APP_ID of the created app)
secret_key = "******"       # app_secret key which you got after creating the app
redirect_uri = "******"     # redircet_uri you entered while creating APP.

app_id = client_id[:-4]  # '##########'


def read_file():
    with open("tokenf.txt", "r") as f:
        token = f.read()
    return token


def write_file(token):
    with open('tokenf.txt', 'w') as f:
        f.write(token)


def setup():
    session = accessToken.SessionModel(client_id=client_id, secret_key=secret_key, redirect_uri=redirect_uri,
                                       response_type='code', grant_type='authorization_code')

    s = requests.Session()
    headers = {
        'accept': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'accept-language': 'en-US,en;q=0.9'
    }
    s.headers.update(headers)

    data1 = f'{{"fy_id":"{username}","password":"{password}","app_id":"2","imei":"","recaptcha_token":""}}'
    r1 = s.post('https://api.fyers.in/vagator/v1/login', data=data1)
    assert r1.status_code == 200, f'Error in r1:\n {r1.json()}'
    request_key = r1.json()["request_key"]

    data2 = f'{{"request_key":"{request_key}","identity_type":"pin","identifier":"{pin}","recaptcha_token":""}}'
    r2 = s.post('https://api.fyers.in/vagator/v1/verify_pin', data=data2)
    assert r2.status_code == 200, f'Error in r2:\n {r2.json()}'

    headers = {'authorization': f"Bearer {r2.json()['data']['access_token']}",
               'content-type': 'application/json; charset=UTF-8'}

    data3 = f'{{"fyers_id":"{username}","app_id":"{app_id}","redirect_uri":"{redirect_uri}","appType":"100","code_challenge":"","state":"abcdefg","scope":"","nonce":"","response_type":"code","create_cookie":true}}'
    r3 = s.post('https://api.fyers.in/api/v2/token', headers=headers, data=data3)
    assert r3.status_code == 308, f'Error in r3:\n {r3.json()}'

    parsed = urlparse(r3.json()['Url'])
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
