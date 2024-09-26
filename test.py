from datetime import datetime, timedelta

import requests

url = f"https://api.github.com/users/nicolepavlova9/events"
response = requests.get(url)
temp = response.json()
print(response)
now = datetime.utcnow()
last_day = now - timedelta(days=1)
recent_events = [
    event
    for event in temp
    if datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ") > last_day
]
for event in recent_events:
    print(event)
