from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi you are at Mysite's Poll App Landing Page")

# Create your views here.
def detail(request,question_id):
    return HttpResponse("You are looking at question %s. " % question_id)

def results(request,question_id):
    response = "You are looking at the result of question %s. "
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s. " % question_id)

