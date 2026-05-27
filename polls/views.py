from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello doofus. You're at the polls index.")