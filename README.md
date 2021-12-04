# Fyers API Access Token Generation V2

### Method1 (Without Selenium Webdriver): 
- With the help of the *get-post requests session*, we can get the access token.

#### Dependencies: 
- Fyers API V2 ```pip install fyers-apiv2```

### Note:
- If you are doing this the first time and don't have the pin, you can go to the following URL in a browser; you will be asked to create a pin there.
```
client_id = "******"  # '##########-$$$'
secret_key = "******"
redirect_uri = "******"

s = accessToken.SessionModel(client_id=client_id, secret_key=secret_key, redirect_uri=redirect_uri,
                                  response_type='code', grant_type='authorization_code')
url = s.generate_authcode()
```

### [***Depricated***] Method2 (With Selenium Webdriver):
- Download the appropriate (as per your Google Chrome version) selenium chrome webdriver from https://chromedriver.chromium.org/downloads. 
- Put the ***chromedriver.exe*** file in the same folder as the script.

#### Dependencies:
- Fyers API V2 ```pip install fyers-apiv2```
- Selenium ```pip install selenium```

*You can see Fyers official documentation at https://myapi.fyers.in/docs/*.
