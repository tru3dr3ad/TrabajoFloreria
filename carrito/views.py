from django.shortcuts import render,get_object_or_404, redirect
from carrito.models import Carrito,Pedido,Flor
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required 

# Create your views here.
def AgregarAlCarrito(request, id):
    item = get_object_or_404(Flor, id=id)
    pedido_item, creacion = Carrito.objects.get_or_create(
        item=item,
        usuario = request.user
    )
    pedido_qs= Pedido.objects.filter(usuario=request.user,ordenado=False)
    if pedido_qs.exists():
        pedido = pedido_qs[0]
        # Ver si los items del pedido estan en el pedido
        if pedido.itemsPedido.filter(item__id=item.id).exists():
            pedido_item.cantidad += 1
            pedido_item.save() 
            messages.info(request, "La cantidad de este item fue actualizada.")
            return redirect("core:galeria")
        else:
            pedido.itemsPedido.add(pedido_item)
            messages.info(request, "Este item ha sido agregado a tu carro.")
            return redirect("core:galeria")
    else:
        pedido = Pedido.objects.create(
            usuario=request.user
        )
        pedido.itemsPedido.add(pedido_item)
        messages.info(request, "Este item ha sido agregado a tu carro.")
        return redirect("core:galeria")

def EliminarDelCarrito(request, id):
    item = get_object_or_404(Flor, id=id)
    carrito_qs = Carrito.objects.filter(usuario=request.user, item=item)
    if carrito_qs.exists():
        carrito=carrito_qs[0]
        #Revisar la cantidad de carros
        if carrito.cantidad  > 1:
            carrito.cantidad  -= 1
            carrito.save()
        else:
            carrito_qs.delete()
    pedido_qs = Pedido.objects.filter(
        usuario = request.user,
        ordenado=False
    )
    if pedido_qs.exists():
        pedido = pedido_qs[0]
        #revisar si los items del pedido estan en el pedido
        if pedido.itemsPedido.filter(item__id=item.id).exists():
            pedido_item = Carrito.objects.filter(
                item = item,
                usuario = request.user,
            )[0]
            pedido.itemsPedido.remove(pedido_item)
            messages.info(request, "El item ha sido removido de tu carro.")
            return redirect("core:galeria")
        else:
            messages.info(request, "Ese item no esta en tu carro")
            return redirect("core:galeria")
    else:
        messages.info(request, "No tienes un pedido activo")
        return redirect("core:galeria")

# def CarritoVista(request):
#     usuario = request.user

#     carritos = Carrito.objects.filter(usuario = usuario)
#     pedidos = Pedido.objects.filter(usuario=usuario, ordenado=False)

#     if carritos.exists():
#         pedido = pedidos[0]
#         return render(request, 'carrito/home.html'), {"carritos":carritos, 'pedido':pedido}
#     else :
#         messages.warning(request, "No tienes un pedido activo")
#         return redirect("carrito:home")