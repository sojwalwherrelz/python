import requests
import json

apikey = "%APIKEY%"
response = requests.get("https://api.cricapi.com/v1/cricScore?apikey="+apikey)
def myobj(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    data = json.loads(text)['data']
    print("----------------------------E Cric Score -----------------")
    if(data):
     for val in data:
      print(" dateTimeGMT - "+val['dateTimeGMT'] +" matchType - "+ str(val['matchType'])+"\n " +"status - "+ str(val['status']) )    
      print(" ms - "+val['ms'] +" t1 - "+ str(val['t1'])+"\n " +"t2 - "+ str(val['t2']) )    
      print(" t1img - "+val['t1img'] +" t2img - "+ str(val['t2img'])+"\n " +"t1s - "+ str(val['t1s']) )    
    
myobj(response.json())
