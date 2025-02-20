import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
print(response.text)
if(response.status_code == 200):
    json_file = response.json()
    hours = int(json_file['hours'])
    minutes = int(json_file['minutes'])
    seconds = int(json_file['seconds'])

    print(f"Current time: {hours} hrs {minutes} min and {seconds} sec")
else:
    print(response.status_code, "Something went wrong")
