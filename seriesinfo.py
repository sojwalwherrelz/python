import requests
import json

apikey = "%APIKEY%"
id="b290fb86-aae9-4284-9a52-854a8c4fe19c"
response = requests.get("https://api.cricapi.com/v1/series_info?apikey="+apikey+"&offset=0&id="+id)
def myobj(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    data = json.loads(text)['data']['info']
    print("----------------------------Series Info -----------------")
    print(" Name - "+data['name']+" \n "+"End Date -   "+data['enddate']+" \n ")    
    print(" ODI - "+ str(data['odi']) +" Matches - "+ str(data['matches']) +" Test - "+ str(data['test']) )    

myobj(response.json())
