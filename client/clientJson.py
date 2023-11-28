import requests

url = "http://localhost:8000/stream"
params = {"type": "tech", "stream": False}

response = requests.post(url, json=params)

for chunk in response.iter_lines():
    if chunk:
        print(chunk.decode("utf-8"))