from django.http import HttpResponse

def index(request):
    return HttpResponse("ola mundo")

