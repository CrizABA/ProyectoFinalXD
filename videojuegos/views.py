from django.shortcuts import render
from django.conf import settings
from .models import VideoJuego
from django.core.mail import send_mail

def busqueda_productos(request):
    return render(request, "buscar.html")

def buscar(request):
    mensaje = None
    productos = None
    guardaprod = request.GET.get("prd", "").strip()

    if guardaprod:
        if len(guardaprod) > 20:
            mensaje = 'Texto de búsqueda demasiado largo, vuelve a intentar.'
        else:
            
            productos = VideoJuego.objects.filter(nombre__icontains=guardaprod)
            if not productos:
                mensaje = 'No se encontraron productos que coincidan con la búsqueda.'
    else:
        mensaje = 'No has capturado nada en el campo de búsqueda.'

            # modelo de vista para poder mandar el correo 
    if request.method == 'POST':
        var_asunto = request.POST["asunto"]
        var_mensaje = request.POST["mensaje"] + " " + request.POST["email"]
        var_email_from = settings.EMAIL_HOST_USER 
        receptor = ["cristian.gonzalezmarcos@cesunbc.edu.m"]  #mi correo que este recibira el mensaje

        # manera de enviar el correo y que se le mande a una pagina de garcias
        send_mail(var_asunto, var_mensaje, var_email_from, receptor)
        return render(request, "gracias.html")

    return render(request, "resultado.html", {"productos": productos, "query": guardaprod, "mensaje": mensaje})

def gracias(request):
    return render(request, "gracias.html")
