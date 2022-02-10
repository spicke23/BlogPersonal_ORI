from django.shortcuts import render
from .models import Usuario
from .forms import RegistroForm

# Create your views here.
def index(request):
    return render(request, 'usuarios/index.html')

def recibir(request):
    print(request.GET["dato"])
    numero = request.GET["dato"]
    return render(request, 'usuarios/index.html',{'numero' : numero})

def registro(request):
    return render(request, 'usuarios/registro.html')

def sumar(request, numero1, numero2):
    print(f"{numero1}  {numero2}")
    resultado = numero1 + numero2
    return render(request, 'usuarios/index.html', {'numero2' : resultado})

def usuarios(request):
    data_user = Usuario.objects.all() ## le entregamos a la variable data_user toda la info de usuarios
    return render(request, 'usuarios/usuarios.html', {'data' : data_user})

def procesarRegistro(request):
    ##datos = request.GET
    datos = request.POST
    rut = datos['numID']
    name = datos['name']
    lastname = datos['lastname']
    email = datos['email']
    age = datos['age']
    #print(datos, name, lastname, age)
    return render(request, 'usuarios/registro.html', {'mensaje': 'Datos recibidos', 'rut':rut, 'email': email})

def procesarRegistroForm(request):
    if request.method == 'POST':
        form = RegistroForm(data=request.POST) ##Se inicializa un formulario con los datos obtenidos del metodo POST
        if form.is_valid():
#            rut = form['numID']
#            name = form['name']
#            lastname = form['lastname']
#            email = form['email']
#            age = form['age']
            form.save()
        return render(request, 'usuarios/registroPOST.html', {'respuesta': 'ok'})
    else:
        form = RegistroForm()
        return render(request, 'usuarios/registroPOST.html', {'form': form})