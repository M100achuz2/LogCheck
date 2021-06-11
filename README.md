# LogCheck

+ Install the requirements packages:

`pip3 install -r requirements.txt`

+ Create `token.ini` file and enter the following syntax:
```bazaar
[slack]
token = <your token>
```
+ Run the app, using waitress:
```bazaar
waitress-serve --call 'app:app'
```