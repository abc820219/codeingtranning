import urllib.request as request 
import json 
src = "https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire"  
with request.urlopen(src) as response: 
  data = json.load(response) 
  results = data["result"]["results"] 
  print(results)
with open("result.txt", mode="w",encoding="utf-8") as file: 
  for res in results: 
    file.write(res["stitle"]+","+res["longitude"]+","+res["latitude"]+","+"http"+res["file"].split('http')[1]+"\n") 