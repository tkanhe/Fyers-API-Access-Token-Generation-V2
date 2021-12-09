> Added ```Fyers Access Token with added User Agent.py``` to solve the captcha problem. Although I didn't get any captcha error, you might get one if you run the script multiple times a day OR multiple times logging into the Fyers website (Google might think you are a robot). Once the token is generated, it's valid for the day, so create a token once in the morning, and you are good to go for the rest of the day.
### Input parameters:
- ```username(fyers_id)```, ```password```, ```pin```, ```client_id```, ```secret_key```, ```redirect_uri```
### Dependencies: 
- Fyers API V2 ```pip install fyers-apiv2```


*You can see Fyers official documentation at https://myapi.fyers.in/docs/*.  
*You can create an APP using the Fyers API dashboard at https://myapi.fyers.in/dashboard/*.
