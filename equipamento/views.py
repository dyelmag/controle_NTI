from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from .models import Marca, Modelo


class AdicionarEquipamentoView(LoginRequiredMixin, TemplateView):

    template_name = 'equipamentos/adicionar.html'


class MarcaView(TemplateView):

    def post(self, request):

        nome = request.POST['nome']
        obs = request.POST['obs']

        if not Marca.objects.filter(nome=nome):
            m = Marca.objects.create(nome=nome, obs=obs)
            return JsonResponse({'evento_id': 1, 'id_marca': m.id})

        return JsonResponse({'evento_id': 2, 'msg': 'Marca ja está cadastrada'})

    def get(self, request):

        marcas = Marca.objects.all()

        marcaArray = []
        for marca in marcas:
            marcaArray.append(
                {'id': marca.id, 'nome': marca.nome, 'obs': marca.obs})

        return JsonResponse(marcaArray, safe=False)


class ModeloView(TemplateView):

    def post(self, request, pk):

        nome = request.POST['nome']
        tipo = request.POST['tipo']
        desc = request.POST['desc']
        obs = request.POST['obs']
        marcar = Marca.objects.get(id=pk)

        if not Modelo.objects.filter(marca=marcar, nome=nome):
            m = Modelo.objects.create(
                marca=marcar, tipo=tipo, nome=nome, descricao=desc, obs=obs)
            return JsonResponse({'evento_id': 1, 'id_modelo': m.id})

        return JsonResponse({'evento_id': 2, 'msg': 'Modelo ja está cadastrada'})

    def get(self, request, pk):
        modelos = Modelo.objects.filter(marca=pk)

        modeloArray = []
        for modelo in modelos:
            modeloArray.append(
                {'id': modelo.id, 'nome': modelo.nome, 'obs': modelo.obs})

        return JsonResponse(modeloArray, safe=False)
