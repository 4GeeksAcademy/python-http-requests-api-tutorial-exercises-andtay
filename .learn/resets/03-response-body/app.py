import requests

url = "https://assets.breatheco.de/apis/fake/sample/random-status.php"
response = requests.get(url= url)
print(response.text)