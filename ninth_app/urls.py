from django.urls import path, re_path
from . import views
#from ninth_app.views import *

# app_name = 'ninth_app' # Ex TAG to use {% url 'ninth_app:index' %}

urlpatterns = [
    # path('index',views.index,name='index'),
    # re_path(r'^$', 'views.index', name='index'),
    path('resume',views.resume,name='resume'),
    path('recibo',views.recibo,name='recibo'),
    path('recibosimplesdados',views.recibosimplesdados,name='recibosimplesdados'),
    path('resumetemp',views.resumetemp,name='resumetemp'),
    # path('modelos/<docName1>/', views.resumetemp, name='resumetemp'),
    path('resumedownload',views.resumedownload,name='resumedownload'),
    # path('teste1',views.teste1,name='teste1'),
    # path('teste2',views.teste2,name='teste2'),
    # path('sucesso',views.sucesso,name='sucesso'),
    path('contratosimples',views.contratosimples,name='contratosimples'),
    path('contratosimplesdados',views.contratosimplesdados,name='contratosimplesdados'),
    path('vveiculossimples',views.vveiculossimples,name='vveiculossimples'),
    path('procsimples',views.procsimples,name='procsimples'),
    path('procsimplesdados',views.procsimplesdados,name='procsimplesdados'),
    path('automenor',views.automenor,name='automenor'),
    path('automenordados',views.automenordados,name='automenordados'),
]
