from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def redirect_chat(request):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "avacadoPage.html", context)

def redirect_logout(request):
    return redirect("login-user")