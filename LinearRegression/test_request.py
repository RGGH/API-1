import requests

url = "http://127.0.0.1:8000"

params = {
	'cigs':55
}

answer = requests.get(url, params = params)

print(answer.text)