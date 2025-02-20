import requests
mydata = {
    "id": 2323,
    "title": "Very big project"
}
myheader = {"Content-Type": "application/json"}
response = requests.post(
    url="https://assets.breatheco.de/apis/fake/sample/save-project-json.php",
    json = mydata,
    headers=myheader
    )
print(response.text)
