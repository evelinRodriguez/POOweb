from django.urls import path
from . import views


urlpatterns = [
    #/news/
    path('', views.index, name = "index"),

    #/news/id/
     path('<cuencas_id>/', views.detail,name='detail'),
]
