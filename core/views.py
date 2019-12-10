from django.shortcuts import render, redirect
from .models import Flor
from .forms import FlorForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
# Create your views here.
 
def home(request):
    data = {
        'flores':Flor.objects.all()
    }
    return render(request, 'core/home.html', data)

def galeria(request):
    return render(request, 'core/galeria.html')

def listado_flor(request):
    flores = Flor.objects.all()
    data = {
        'flores' : flores
    }
    return render(request, 'core/listado_flores.html',data)

@permission_required('core.add_flor')
def nueva_flor(request):
    data = {
        'form':FlorForm()
    }
    if request.method == 'POST':
        formulario = FlorForm(request.POST, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
        data['form'] = formulario

    return render(request, 'core/nueva_flor.html', data)

def modificar_flor(request, id):
    flor = Flor.objects.get(id=id)
    data = {
        "form" : FlorForm(instance=flor)
    }

    if request.method == 'POST':
        formulario = FlorForm(data = request.POST, instance= flor, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
        data['form'] = FlorForm(instance=Flor.objects.get(id=id))

    return render (request, 'core/modificar_flor.html', data)

def eliminar_flor(request, id):
    flor =  Flor.objects.get(id = id)
    flor.delete()

    return redirect(to = 'listado_flores')

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password= password)
            login(request, user)
            return redirect(to='home')

    return render(request, 'registration/registrar.html', data)