from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'siteoficial/index.html', {})

def oficina(request):
	return render(request, 'siteoficial/oficina.html', {})

def producto(request):
	return render(request, 'siteoficial/producto.html', {})

def contactos(request):
	return render(request, 'siteoficial/contactos.html', {})

def login(request):
	return render(request, 'siteoficial/login.html', {})

def registro(request):
	return render(request, 'siteoficial/registro.html', {})

def institucional(request):
	return render(request, 'siteoficial/institucional.html', {})

def exportacion(request):
	return render(request, 'siteoficial/exportacion.html', {})