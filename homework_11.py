import requests
import json


url = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=setbalance&user=21&balance=320493"
get_url="https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=getdata&user=21"
res = requests.get(url)
json = res.json()

res2 = requests.get(id)
json = res2.json()
#print(json)

for q in range(len(json)):
   if json[q]["id"] is None:
      print("Error")
   else:
      print(
        "id", "=", json[q]["id"], "\n"+
        "name", "=", json[q]["name"], "\n"+
        "surname", "=", json[q]["surname"], "\n"+
        "email", "=", json[q]["email"], "\n"+
        "school_group", "=", json[q]["school_group"], "\n"+
        "balance", "=", json[q]["balance"], "\n")

