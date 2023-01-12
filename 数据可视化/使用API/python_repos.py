import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)
print("Status code:", response.status_code)

# 将API响应存储在一个变量中
response_dict = response.json()
print(response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dicts['name'])
    stars.append(repo_dicts['stargazers_count'])

# 可视化
my_style = LS('#333366', base_style=LCS)
