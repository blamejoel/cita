import serial
import time
import os
import subprocess
import sys
import requests
import json

keyword = 'cat'
image = '/home/udooer/cita/images/cita.jpg'
#keyword = sys.argv[2]
#image = '../images/' + sys.argv[1]
client = '_lU738vc9I26-7maXim-UbjYe0g9NztV6Msdwj3q'
secret = '6jzYsuqZh85eqyK4rSfYsG0Z3qaedLmHVj1SRXg0'
auth_data = {'client_id':client, 'client_secret':secret,'grant_type':'client_credentials'}
response = requests.post('https://api.clarifai.com/v1/token/', data=auth_data)
response = json.loads(response.text)
token = response['access_token']
curl_post = 'curl -H "Authorization: Bearer ' + token + '" -F "encoded_data=@' + image + '" "https://api.clarifai.com/v1/tag/"'

ser = serial.Serial('/dev/ttyMCC',9600,timeout=1)  # Defining the port to be used for commo

samples = 10
count = 0
while count < samples:
    #ser.flushOutput()                                  # Ensuring that there is no bytes left over in the output
    incoming =  ser.read(1)
    if incoming == 'i':                                        # Read one byte from the Arduino 

        count = count + 1
        #Instruct Camera to take pic, and send the pic to be compared 
        subprocess.call('/home/udooer/cita/src/./capture.sh')
        print 'capturing image'
        FNULL = open(os.devnull, 'w')
        SUBOUT = subprocess.PIPE
        r = subprocess.Popen(curl_post, shell=True, stdout=SUBOUT, stderr=FNULL).stdout.read()
        r = json.loads(r)
        results = r['results']
        result = results[0]
        result = result['result']
        tag = result['tag']
        classes = tag['classes']
        #if the pic matches a tag for a cat, return char 'C' to the Arduino
        if keyword in classes:
            ser.write(chr(67))                                 # ASCII for 'C' 
            #print 'cat detected!'
            print keyword + ' detected'
        #else send the char 'N'
        else:
            ser.write(chr(78))                                   # ASCII for 'N'
            #print 'no cat!'
            print 'false alarm'
            print classes
    time.sleep(1)                                      # delay for 1 second
print 'max samples reached!'
