import requests

url = "http://localhost:8000/stream"
params = {"type": "tech", "stream": True}

response = requests.post(url, json=params, stream=True)

for chunk in response.iter_lines():
    if chunk:
        print(chunk.decode("utf-8"))

