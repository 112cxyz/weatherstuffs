import requests
from datetime import datetime

now = datetime.now()


def fetchweather(location='Portsmouth', country='UK', time='now'):
  if time == "now":
    now = datetime.now()
    currenttime = now.strftime("%H")
  else:
    currenttime = int(time)-1
  locationapi = 'http://api.positionstack.com/v1/forward?access_key=a1c0f877887f8c716c8847fa402b589d&query=' + location + "%20" + country
  resp = requests.get(url=locationapi)
  data = resp.json()
  weather = 'https://api.open-meteo.com/v1/forecast?latitude=' + str(
    data["data"][0]["latitude"]) + '&longitude=' + str(
      data["data"][0]
      ["longitude"]) + '&hourly=temperature_2m,precipitation,cloudcover&timeformat=unixtime'
  resp = requests.get(url=weather)
  data = resp.json()
  if data['hourly']['precipitation'][int(currenttime) + 1] >= 0.1:
    chanceofrain = True
  else:
    chanceofrain = False
  temp = data['hourly']['temperature_2m'][int(currenttime) + 1]
  cloudcover = data['hourly']['cloudcover'][int(currenttime) + 1]
  if cloudcover >= 50.0:
    cloudy = True
  else:
    cloudy = False
  weektemp = data['hourly']['temperature_2m']
  dt = datetime.fromtimestamp(data['hourly']['time'][int(currenttime) + 1])
  return[temp,cloudy,chanceofrain,weektemp,dt]
