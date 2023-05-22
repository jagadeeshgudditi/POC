import requests

response=request.post("http://localhost:8000/api/stop/")

print(response.json())