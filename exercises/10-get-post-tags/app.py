import requests

def get_post_tags(post_id):
    # Your code here
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response =  requests.get(url)
    tags = []
    if response.status_code == 200:
        posts = response.json()['posts']
        for post in posts:     # loop a list of posts
            if (post['id'] == post_id):
                for tag in post['tags']:    # loop a list of tags
                    tags.append(tag['id'])
    else:
        print("Something went wrong.")    

    return tags


print(get_post_tags(146))