from django.urls import path
from . import views


urlpatterns = [
    #/news/
    path('', views.index, name = "index"),

    #/music/1/
     path('<int:cuencas_id>', views.detail)
    #path(r'^(?P<cuencas_id>[0-9]+)/$',views.detail,name='detail'),version anterioe url
   #re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail')﻿,
]
