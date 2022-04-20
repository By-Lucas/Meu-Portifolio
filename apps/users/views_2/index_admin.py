from django.shortcuts import render, redirect, get_object_or_404

def home_admin(request):
    return render(request, 'index_adm.html')