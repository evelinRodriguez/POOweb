from .models import Cuencas
from django.shortcuts import render
from django.http import Http404


def index(request):
    allCuencas = Cuencas.objects.all()
    context = {'allCuencas': allCuencas}
    return  render(request,'news/index.html', context)



def detail(request,cuencas_id):
   try:
       cuencas= Cuencas.objects.get(id=cuencas_id)
   except Cuencas.DoesNotExist:
       raise  Http404("CUENCAS NO EXISTEN")
   return render(request, 'news/detail.html',{'cuencas' : cuencas})