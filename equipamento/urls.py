from django.urls import path, include
from . import views

app_name = 'equipamento'

urlpatterns = [
    path('adicionar/',   views.AdicionarEquipamentoView.as_view(),
         name='adicionar-equipamento'),
    path('marcas/',   views.MarcaView.as_view(), name='marcas'),
    path('modelo/<int:pk>/',   views.ModeloView.as_view(), name='modelo'),

]
