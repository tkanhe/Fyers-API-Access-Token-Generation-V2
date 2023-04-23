First, you will have to register for External 2FA TOTP at https://myaccount.fyers.in/ManageAccount.
While enabling External 2FA TOTP, you can scan the QR code using Google or Microsoft Authenticator and copy the TOTP KEY, as shown in the figure below. *If you don't want to use the Authenticator app, you can generate TOTP using the code in the repo https://github.com/tkanhe/totp-generator*

![alt text](https://github.com/tkanhe/Fyers-API-Access-Token-Generation-V2/blob/main/Screenshot.png?raw=true)

### *Note:*
If you have just created the app and first time using it, then try the following:
```
session = accessToken.SessionModel(client_id=client_id, secret_key=secret_key, redirect_uri=redirect_uri, response_type='code', grant_type='authorization_code')

url = session.generate_authcode()
```
Go to the above URL manually in the browser and give permissions to access the app. It is a one-time process. After that, you can use the script.

### Input parameters:
- ```username(fyers_id)```, ```totp_key```, ```pin```, ```client_id```, ```secret_key```, ```redirect_uri```
### Dependencies: 
- Fyers API V2 ```pip install fyers-apiv2```


*You can see Fyers official documentation at https://myapi.fyers.in/docs/*.  
*You can create an APP using the Fyers API dashboard at https://myapi.fyers.in/dashboard/*.
