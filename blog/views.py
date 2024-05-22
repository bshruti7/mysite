from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def fetchBlogFeed(request):

    response = "This is a sample blog feed"
    return HttpResponse(response)
