from django.shortcuts import render
from django.urls import path

# Create your views here.
from django.http import HttpResponse
from.models import  cuencas


def index(request):
    all_cuencas=cuencas.objects.all()
    html = ''
    for cuencas in all_cuencas:
        path='/news/'+str(cuencas.id)+'/'
        html+='< a href="'+path+'">'+cuencas.nombrecuenca+'</a><br>'

    return HttpResponse(html)

def detail(request,cuencas_id):
    return HttpResponse("<h2> details of cuencas:"+str(cuencas_id)+"</h2>")