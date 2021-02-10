import requests

api_url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(api_url, headers=headers)
response_dict = r.json()

print(response_dict.keys())

print(f"Number of repos {response_dict['total_count']}")

best_ten_of_repos = response_dict['items'][:10]

for repo in best_ten_of_repos:
    print(f"Owner {repo['owner']['login']}")
    print(f"Repo {repo['html_url']}")
    print(f"Stars {repo['stargazers_count']}")



