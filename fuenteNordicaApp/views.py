from django.shortcuts import render

# Create your views here.
def renderInicio(request):
    return render(request, 'fuenteNordicaApp/index.html')

def renderCatalogo(request):
    return render(request, 'fuenteNordicaApp/catalogo.html')

def renderClub(request):
    return render(request, 'fuenteNordicaApp/club.html')

def renderAbout(request):
    return render(request, 'fuenteNordicaApp/about.html')

def renderContacto(request):
    return render(request, 'fuenteNordicaApp/contacto.html')