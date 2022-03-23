> Added ```Fyers_Access_Token_with_User_Agent.py``` to solve the captcha problem. Although I didn't get any captcha error, you might get one if you run the script multiple times a day OR multiple times logging into the Fyers website (Google might think you are a robot). Once the token is generated, it's valid for the day, so create a token once in the morning, and you are good to go for the rest of the day.

### *Note:*
If you have just created the app and first time using it, then try the following:
```
session = accessToken.SessionModel(client_id=client_id, secret_key=secret_key, redirect_uri=redirect_uri, response_type='code', grant_type='authorization_code')

url = session.generate_authcode()
```
Go to the above URL manually in the browser and give permissions to access the app. It is a one-time process. After that, you can use the script.

### Input parameters:
- ```username(fyers_id)```, ```password```, ```pin```, ```client_id```, ```secret_key```, ```redirect_uri```
### Dependencies: 
- Fyers API V2 ```pip install fyers-apiv2```


*You can see Fyers official documentation at https://myapi.fyers.in/docs/*.  
*You can create an APP using the Fyers API dashboard at https://myapi.fyers.in/dashboard/*.
