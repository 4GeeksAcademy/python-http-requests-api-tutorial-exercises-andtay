import requests

# Your code here
url = "https://assets.breatheco.de/apis/fake/sample/post.php"
response = requests.post(url=url)
print(response.text)