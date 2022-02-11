import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}

request = requests.get(url, headers=headers)

print(f"Status code: {request.status_code}")

response_data = request.json()

print(f"Total repositories: {response_data['total_count']}")

print(f"Repositories returned: {len(response_data['items'])}")

repos = response_data['items']

first_repo = repos[0]

# print(f"First repo keys: {first_repo.keys()}")
#print(response_data.keys())

print(f"Repo name: {first_repo['name']}")
print(f"Repo owner: {first_repo['owner']['login']}")
print(f"Repo description: {first_repo['description']}")