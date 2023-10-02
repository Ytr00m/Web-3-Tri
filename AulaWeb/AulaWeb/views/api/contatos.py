from django.http import JsonResponse, QueryDict
from django.shortcuts import get_object_or_404
from django.views import View

from AulaWeb.models import Contato

class ContatoView(View):
    def get(self, request):
        contatos = list()
        for c in Contato.objects.all():
          contatos.append({
                "id": c.id,
                "nome": c.nome,
                "telefone": c.telefone,
                "email": c.email,
            })
        print(contatos)
        return JsonResponse({"contatos" :contatos}) 
        

    def post(self, request):
        c = Contato()
        c.nome = request.POST.get("nome")
        c.telefone = request.POST.get("telefone")
        c.email = request.POST.get("email")
        print(request.POST)
        try:
            c.save()
            return JsonResponse({"salvo":"OK"})
        
        except Exception as e:
            print(e)
            return JsonResponse({"salvo":"erro"})

    def put(self, request, id):
        dados = QueryDict(request.body)
        c = get_object_or_404(Contato, pk=id)

        c.nome = dados.get("nome", c.nome)
        c.telefone = dados.get("telefone", c.telefone)
        c.email = dados.get("email", c.email)
        try:
            c.save()
            return JsonResponse({"atualizado": "OK"})
        except:
            return JsonResponse({"atualizado": "Erro"})

    def delete(self, request, id):
        c = get_object_or_404(Contato, pk=id)
        c.delete
        return JsonResponse({
            "excluido":"OK"
        })