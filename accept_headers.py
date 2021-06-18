import requests
import os
import json
import re

def accept_header(languages, pattern='.*'):
    if len(languages) == 0:
        return False
    token = os.getenv('GITHUB_TOKEN')
    base_url =  "https://api.github.com"
    header = {'Authorization' : f'token {token}',
             'Accept-Language': ','.join(get_filtered_languages(languages,pattern))}
    owner = 'basicbooknerd'
    response = requests.get(f'{base_url}/users/{owner}/events', headers=header)
    print(json.dumps(response.json(), indent =4))
    print(response.status_code)
    return response.status_code

def get_filtered_languages(languages, pattern):
    regex_p = re.compile(pattern)
    return list(filter(regex_p.match, languages))

accept_header(['en', 'da', 'fr', 'en-US'])