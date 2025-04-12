requirements.txt
requests.post
import os
import requests
from datetime import datetime

# Notion Info
NOTION_KEY = os.environ['NOTION_KEY']
DB_ID = os.environ['NOTION_DB_ID']

headers = {
    "Authorization": f"Bearer {NOTION_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Dummy example data — replace this with your scraped data
data = {
    "object": "page",
    "parent": { "database_id": DB_ID },
    "properties": {
        "Target": { "title": [{ "text": { "content": "M45 Pleiades" } }] },
        "Date": { "date": { "start": datetime.utcnow().isoformat() } },
        "Mission": { "rich_text": [{ "text": { "content": "Spitzer" } }] },
        "Waveband": { "rich_text": [{ "text": { "content": "Infrared" } }] }
    }
}

# Send to Notion
response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)

if response.status_code == 200:
    print("Logged star data successfully to Notion!")
else:
    print("Failed to log star data:", response.text)
