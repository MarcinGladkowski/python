import requests

from plotly.graph_objs import Bar
from plotly import offline

api_url = 'https://api.github.com/search/repositories?q=language:php&sort=stars'

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


selected_repo = response_dict['items'][0]

print(f"\nRepo details")
print(f"Name: ${selected_repo['name']}")
print(f"Owner: ${selected_repo['owner']['login']}")
print(f"Stars: ${selected_repo['stargazers_count']}")
print(f"Created at: ${selected_repo['created_at']}")
print(f"Updated: ${selected_repo['updated_at']}")
print(f"Description ${selected_repo['description']}")

# create visualization
names, stars = [], []

for repo in response_dict['items'][:10]:
    names.append(repo['name'])
    stars.append(repo['stargazers_count'])

data = [{
    'type': 'bar',
    'x': names,
    'y': stars
}]

layout = {
    'title': 'Best 10 PHP repositories',
    'xaxis': {'title': 'Repo name'},
    'yaxis': {'title': 'Stars'}
}

fig = { 'data': data, 'layout': layout}
offline.plot(fig, filename='php_repos.html')
