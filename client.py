import requests

res = requests.get("http://127.0.0.1:8000/0")
print(res.json())
print('\n')
res = requests.delete("http://127.0.0.1:8000/1")
print(res.json())
print('\n')
res = requests.post("http://127.0.0.1:8000/1", json={"name": "Programming", "price": 100})
print(res.json())
print('\n')
res = requests.put("http://127.0.0.1:8000/2", json={"name": "Biology", "price": 150})
print(res.json())