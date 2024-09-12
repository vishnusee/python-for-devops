import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_data = response.json()

for i in range(len(complete_data)):
    print(complete_data[i]["user"]["login"])

#print(response.json())