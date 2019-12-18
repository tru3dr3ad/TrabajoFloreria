from django.shortcuts import render, redirect
from .models import Flor
from .forms import FlorForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate

from rest_framework import viewsets
from .serializers import FlorSerializer

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
import json

from fcm_django.models import FCMDevice
# Create your views here.

@csrf_exempt
@require_http_methods(['POST'])
def guardar_token(request):
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    token = bodyDict['token']
    existe = FCMDevice.objects.filter(registration_id = token, active=True)
    if len(existe) > 0:
        return HttpResponseBadRequest(json.dumps({'mensaje':'el token ya existe'}))
    
    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True

    # SOLO SI EL USUARIO ESTA LOGEADO PROCEDEREMOS A ENLAZAR
    if request.user.is_authenticated:
        dispositivo.user = request.user

    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje':'token guardado'}))
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'No se ha podido guardar'}))



def home(request):
    data = {
        'flores':Flor.objects.all()
    }
    template_name = 'core/home.html'
    return render(request, 'core/home.html', data)

def galeria(request):
    flores = Flor.objects.all()
    data = {
        'flores' : flores
    }
    return render(request, 'core/galeria.html', data)

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
            #OBTENER DISPOSITIVOS
            dispositivos = FCMDevice.objects.filter(active=True)
            dispositivos.send_message(
                title = "Producto Agregado!!",
                body = "Se ha agregado: "+ formulario.cleaned_data['nombre'],
                icon = "/static/core/img/FlorLoto.png"
            )

            data['mensaje'] = "Guardado Correctamente"
        data['form'] = formulario

    return render(request, 'core/nueva_flor.html', data)

@permission_required('core.change_flor')
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

@permission_required('core.delete_flor')
def eliminar_flor(request, id):
    flor =  Flor.objects.get(id = id)
    flor.delete()

    return redirect(to = 'core:listado_flores')

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
            return redirect(to='core:home')

    return render(request, 'registration/registrar.html', data)

class FlorViewSet(viewsets.ModelViewSet):
    queryset = Flor.objects.all()
    serializer_class = FlorSerializer