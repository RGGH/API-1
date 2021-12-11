import requests

url = "https://neuro-2fle3wxkia-nw.a.run.app/vars"

params = {
  "weeks": 6,
  "years": 0,
  "books": 0,
  "projects": 0,
  "earn": 0
}

answer = requests.post(url, json = params)

print(answer.text)