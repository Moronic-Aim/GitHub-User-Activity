import argparse
import requests
import json
parse = argparse.ArgumentParser()
parse.add_argument("username", help="Enter the username")
args = parse.parse_args()

username = args.username

def get_user_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
data = get_user_activity(username)
print(type(data))
print(json.dumps(data[0], indent=4))