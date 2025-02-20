import requests

# Your code here

url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"
response = requests.get(url)
if( response.status_code == 200):
    image = response.json()[-1]['images'][-1] # extracting last project and last image
    print(image)
else:
    print("Something went wrong")
