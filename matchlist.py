import requests
import json

apikey = "%APIKEY%"
response = requests.get("https://api.cricapi.com/v1/matches?apikey="+apikey+"&offset=0")
def myobj(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    data = json.loads(text)['data']
    # print(data)
    print("----------------------------Match List -----------------")
    for value in data:
        print(" Name - "+value['name']+"\n"+" status - "+value['status']+"\n"+" venue -  "+value['venue']+"\n"+"dateTimeGMT - "+value['dateTimeGMT']+"\n")    

myobj(response.json())
