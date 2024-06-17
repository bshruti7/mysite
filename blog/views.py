from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def starting_page(request):
    response = "Index Page response"
    return HttpResponse(response)


def posts(request):
    response = "All Posts"
    return HttpResponse(response)


def post_detail(request):
    response = "Post details"
    return HttpResponse(response)



