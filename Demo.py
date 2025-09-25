import requests  # type: ignore

URL=f'https://www.googleapis.com/blogger/v3/blogs/2399953/posts'
API_KEY = '##########################################'
parameters = {
    'max_results': 5,
    'fields': 'items',
    'key': API_KEY
    
    }


response = requests.get(URL, params=parameters)
print(response.json())
