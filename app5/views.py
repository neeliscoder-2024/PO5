from django.shortcuts import render
from django.http import HttpResponse
def rohit(request):
    return HttpResponse("<marquee style=background-color:lightblue><p style=color:blue>Hitman of cricket</p></marquee>")