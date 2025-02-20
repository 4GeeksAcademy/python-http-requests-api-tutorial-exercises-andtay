import requests

# Your code here

url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
response = requests.get(url)

if( response.status_code == 200):
    posts = response.json()['posts']
    first_post = posts[0] # first post from the list
    author = first_post['author']
    name = author ['name']
    print(name)
else: 
    print("Something went wrong")