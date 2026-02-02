from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Construct a dictionary to pass to template engine as its content
    # Note that the key matches to __ in the template
    context_dict = {"boldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to client.
    return render(request, "rango/index.html", context=context_dict)

def about(request):
    return render(request, "rango/about.html")