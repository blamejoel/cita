import sys
import requests
import json
import base64

url = 'https://api.clarifai.com/v1/tag/'
image = '/home/udooer/cita/images/' + sys.argv[1]
client = '_lU738vc9I26-7maXim-UbjYe0g9NztV6Msdwj3q'
secret = '6jzYsuqZh85eqyK4rSfYsG0Z3qaedLmHVj1SRXg0'
#token = 'i6XBZg6Ue9DdPWAd88ZzNoj8mG4jhp'
auth_data = {'client_id':client, 'client_secret':secret,'grant_type':'client_credentials'}

response = requests.post('https://api.clarifai.com/v1/token/', data=auth_data)
response = json.loads(response.text)
token = response['access_token']

bear = 'Bearer ' + token
auth = {'Authorization':bear,'Content-Type':'application/xml'}

encoded = base64.b64encode(open(image, 'rb').read())
#files = {'file': open(image, 'rb')}
files = {'file': 'image/jpeg;base64,' + encoded}
r = requests.post(url, data=open(image, 'rb'), headers=auth)
#r = json.loads(r.text)
print r
print image
