from django.shortcuts import redirect, render
from .models import Usuario
from .forms import RegistroForm, LoginFormUsuario, Usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

#myBackend = MyBackend()
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
            rut      = form.cleaned_data['rut']
            nombre   = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo    = form.cleaned_data['email']
            clave    = form.cleaned_data['password']
            user = User.objects.create_user(username=rut,first_name=nombre,last_name=apellido,email=correo,password=clave)
            user.save()
        return render(request, 'usuarios/bienvenido.html', {'respuesta': 'Usuario registrado exitosamente'})
    else:
        form = RegistroForm()
        return render(request, 'usuarios/registroPOST.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginFormUsuario(data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['nombre']
            clave = form.cleaned_data['password']
            user = authenticate(request, username=usuario, password=clave)
            if user is not None:
                auth_login(request,user)
                return render(request, 'usuarios/bienvenido.html', {'user': user})
            else:
                return redirect('/login')
    else:
        form = LoginFormUsuario()
        return render(request, 'usuarios/login.html', {'form': form})

@login_required(login_url='/login')
def bienvenido(request):
    return render(request,'usuarios/bienvenido.html')


def salir(request):
    logout(request)
    #return redirect('/logout')
    return redirect('/login')


#def login2(request):
#    if request.method == 'POST':
#        form = LoginForm(data=request.POST)
#        if form.is_valid():
#            usuario = form.cleaned_data['nombre']
#            clave = form.cleaned_data['password']
#            user = myBackend.authenticate(request, username=usuario, password=clave)
#            if user is not None:
#                auth_login(request,user)
#            return render(request, 'usuarios/bienvenido.html', {'user': user})
#    else:
#        form = LoginForm()
#        return render(request, 'usuarios/login.html', {'form': form})

def listadoUsuarios(request):
    usuarios = Usuario.objects.raw('SELECT * FROM usuario;')
    print(usuarios)