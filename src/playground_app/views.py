from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "playground_app/index.html", context={"name": "App Context"})


def page(request, numero):
    if numero in ["01", "02", "03"]:
        return render(request, f"playground_app/page_{numero}.html", context={"numero": numero})
    else:
        return render(request, "playground_app/page_not_found.html", context={"numero": numero})