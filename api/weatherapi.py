import requests
import json

def get_weather_api_data(ciudad, fecha):
  url = "https://weatherapi-com.p.rapidapi.com/history.json"
  querystring = {"q":ciudad,"dt":fecha,"lang":"en"}
  headers = {
    "X-RapidAPI-Key": "5857429c1emsh3e1e9e2832ed106p1cc15ajsn61bd2297d936",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  jsonResponse = json.loads(response.text)
  #print(json.dumps(jsonResponse, indent=2 ))
  location = jsonResponse["location"]
  #print(json.dumps(location, indent=2 ))
  return location
