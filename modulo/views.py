from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.

class SuccessView(View):

    def get(self, request, pk):
        return JsonResponse({
            "success": True,
            "mensaje": "Guardado Correctamente",
            "pk": pk
        })
