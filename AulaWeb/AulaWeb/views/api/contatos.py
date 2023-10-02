from django.http import JsonResponse
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

        try:
            c.save()
            return JsonResponse({"salvo:OK"})
        
        except:
            return JsonResponse({"salvo:erro"})

    def put(self, request):
        pass

    def delete(self, request):
        c = get_object_or_404(Contato, pk=id)
        c.delete
        return JsonResponse({
            "excluido":"OK"
        })