from django.shortcuts import render
from django.http import JsonResponse

def profile(request):
    data = {}
    data['id'] = request.user.id
    return JsonResponse(data)