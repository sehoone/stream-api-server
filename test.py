import requests

url = "http://192.168.1.29:8000/stream"
params = {"stream": False}

# response = requests.post(url, json=params, stream=True)

# for chunk in response.iter_lines():
#     if chunk:
#         print(chunk.decode("utf-8"))

response = requests.post(url, json=params)

for chunk in response.iter_lines():
    if chunk:
        print(chunk.decode("utf-8"))