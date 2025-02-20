import requests

# Your code here

url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"
response = requests.get(url=url)
if (response.status_code == 200):
    json_info = response.json()[1]['name']
    print(json_info)
else:
    print("Something went wrong")