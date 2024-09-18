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
    
def dispaly_activity(data):
    for event in data:
        match event["type"]:
            case "PushEvent":
                print(f"Pushed {event['payload']['size']} {'commit' if event['payload']['size'] == 1 else 'commits'} to {event['repo']['name']}")
            case "IssuesEvent":
                print(f"Opened an issue for {event['repo']['name']}")
            case "WatchEvent":
                print(f"Starred {event['repo']['name']}")
            case default:
                print(f"Performed {event['type']} on {event['repo']['name']}")


data = get_user_activity(username)
dispaly_activity(data)
