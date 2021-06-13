# LogCheck

+ Install the requirements packages:

`pip3 install -r requirements.txt`

+ Create `token.ini` file and enter the following syntax:
```bazaar
[slack]
token = <your token>
```
+ Set the nginx configuration by the following settings:
```bazaar
location / {
       proxy_pass http://localhost:8080/;
}
```
+ Give the right access to the user in `user` section at nginx conf:
```
user www-data
```
+ Run the app, using waitress:
```bazaar
waitress-serve 'app:app'
```
> congratulations!
