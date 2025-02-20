import requests

def get_attachment_by_id(attachment_id):
    # Your code here
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response =  requests.get(url)
    tags = []
    if response.status_code == 200:
        data = response.json()
        for post in data['posts']:  # loop a list of posts
            attachment_post = post['attachments']
            for file in attachment_post:    # loop a list of dicts attachment
                if(file['id'] == attachment_id):
                    return file['url']
        
    else:
        print("Something went wrong.")    

    return None

print(get_attachment_by_id(137))