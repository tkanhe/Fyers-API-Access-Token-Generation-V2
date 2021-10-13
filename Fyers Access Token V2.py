import os
import sys
from urllib.parse import urlparse, parse_qs
from fyers_api import fyersModel
from fyers_api import accessToken
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

username = "******"
password = "******"
pan = "******"
client_id = "******"
secret_key = "******"
redirect_uri = "******"


def read_file():
    with open("tokenf.txt", "r") as f:
        token = f.read()
    return token


def write_file(token):
    with open('tokenf.txt', 'w') as f:
        f.write(token)


def setup():
    session = accessToken.SessionModel(client_id=client_id, secret_key=secret_key, redirect_uri=redirect_uri,
                                       response_type='code', grant_type='authorization_code', state='abcdefg')
    response = session.generate_authcode()

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument('--headless')
    driver = webdriver.Chrome('chromedriver.exe', options=options)
    driver.get(response)
    driver.maximize_window()

    driver.find_element_by_id('fyers_id').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('pancard').send_keys(pan)

    driver.find_element_by_xpath("//button[@id='btn_id']").click()
    WebDriverWait(driver, 20).until((EC.url_changes(driver.current_url)))

    parsed = urlparse(driver.current_url)
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
        print('Getting a access token !')
        setup()
    else:
        print('You already have a access token !')
        print(response)


if __name__ == '__main__':
    check()
