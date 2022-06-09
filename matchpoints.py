import requests
import json

apikey = "%APIKEY%"
id = "1f16f05e-e25c-43a1-ba00-331b1d2c3b8a"
response = requests.get("https://api.cricapi.com/v1/match_points?apikey="+apikey+"&id="+id)
def myobj(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    data = json.loads(text)['data']['innings']
    print("----------------------------Fantacy Squad Score -----------------")
    if(data):
     for val in data:
      print(" inning - "+val['inning'])    
      print("----------------------------Batting -----------------")
     for bat in val['batting']:
      print(" name - "+bat['name'] +" points - "+ str(bat['points'])+"\n" )  

      print("----------------------------Catching -----------------")  
     for cat in val['catching']: 
        print(" name - "+cat['name'] +" points - "+ str(cat['points'])+"\n" )    

        print("----------------------------bowling -----------------")  
     for bowl in val['bowling']: 
        print(" name - "+bowl['name'] +" points - "+ str(bowl['points'])+"\n" )    
    
myobj(response.json())
