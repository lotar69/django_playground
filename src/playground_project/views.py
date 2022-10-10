from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "playground_project/index.html", context={"name": "Project Context"})
