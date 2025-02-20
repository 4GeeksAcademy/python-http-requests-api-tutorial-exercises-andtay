import requests

# Your code here
url = "https://assets.breatheco.de/apis/fake/sample/project1.php"
response = requests.get(url = url)
if (response.status_code == 200):
    json_name = response.json()['name']
    print(json_name)
else:
    print("Something went wrong")
    