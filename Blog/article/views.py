from django.shortcuts import render # type: ignore
import requests  # type: ignore

URL=f'https://www.googleapis.com/blogger/v3/blogs/2399953/posts'
API_KEY = 'AIzaSyCV3RhAfKZv_w_1VUnpCOfXb26pgDGqA2w'
parameters = {
    'max_results':30,
    'fields': 'items',
    'key': API_KEY 
    }


response = requests.get(URL, params=parameters)
data=response.json()

# Create your views here.
def home(request):
    return render(request, 'home.html',context=data)
def result(request,id):
    for item in data['items']:
        if item['id']==id:
            return render(request, 'result.html',context=item)

