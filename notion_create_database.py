
import requests

headers = {
    "Authorization": "Bearer YOUR_INTEGRATION_TOKEN",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

data = {
    "parent": { "type": "page_id", "page_id": "YOUR_PAGE_ID" },
    "title": [{ "type": "text", "text": { "content": "Suivi Santé" } }],
    "properties": {
        "Date": { "date": {} },
        "Symptômes": { "rich_text": {} },
        "Médication": { "rich_text": {} }
    }
}

res = requests.post("https://api.notion.com/v1/databases", headers=headers, json=data)
print(res.json())
