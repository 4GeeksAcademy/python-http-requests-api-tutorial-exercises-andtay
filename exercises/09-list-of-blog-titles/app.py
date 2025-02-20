import requests

def get_titles():
    # Your code here
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response =  requests.get(url)
    titles = []
    if response.status_code == 200:
        posts = response.json()['posts']
        for post in posts:     # loop a list
            titles.append(post['title'])
    else:
        print("Something went wrong.")    

    return titles


print(get_titles())