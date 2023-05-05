from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import PostIt



# Create your views here.


def index(request):

    data = {"data": [{"title": "Notes",
            "content": "This is the content of the notes page"}, 
            {"title": "Notes 2",
            "content": "This is the way"},             
            ]}
    
    for nota in PostIt.objects.all():
        data["data"].append({"title": nota.title, "content": nota.content})

    return render(request, "notes/index.html", data)


def raw(request):
    return HttpResponse("Pure text typed here")

# @csrf_exempt
def insert_post_it(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        nota = PostIt(title=title, content=content)
        nota.save() 

        print(title, content)
        return HttpResponse("Inserted: " + title + " " + content)

