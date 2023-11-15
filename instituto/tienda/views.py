from django.shortcuts import render, redirect

from .models import Producto



class Usuario:
    #constructor
    def __init__(self, nombre, contraseña, correo, telefono, admin):
        self.nombre = nombre
        self.contraseña = contraseña
        self.correo = correo
        self.telefono = telefono
        self.admin = admin

    def __str__(self):
        return self.nombre+", "+self.contraseña+", "+self.correo+", "+self.telefono+", "+self.admin


u1 = Usuario("juan", "12", "juanmendez@gmail.com", "+56987663212", "si")
u2 = Usuario("jose","moreno", "josemoreno@gmail.com", "+5678986543", "no")
u3 = Usuario("matias", "1234", "matiaslopezcoc@gmail.com", "+56997148119", "no")

usuarios = [u1,u2,u3]


def index(request):
    print("hola index...")
    context ={}
    return render(request, 'tienda/index.html', context)

def quienes_somos(request):
    print("Estoy en quienes somos")
    context={}
    return render(request,"tienda/quienes.html",context)

def producto(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, "tienda/productos.html", context)

def comprar(request, pk):
    try:
        producto = Producto.objects.get(id=pk)
        context = {'producto': producto}
        return render(request, "tienda/comprar.html", context)
    except Producto.DoesNotExist:
        context = {'mensaje': "Error, ese producto no existe..."}
        return render(request, 'tienda/productos.html', context)



def login(request):
    print("Hola estoy en el login")
    context = {}

    return render(request, "tienda/login.html",context)

def validar(request):
    context = {}
    if request.method == "POST":
        user = request.POST['users']
        clave = request.POST['passwords']

        print(user, " ", clave)
        for obj in usuarios:
            if obj.nombre == user and obj.contraseña == clave:
                request.session["usuario"] = user
                usuario = request.session["usuario"]
                if obj.admin == "si":
                    request.session["admin"] = True 
                else:
                    request.session["admin"] = False  
                context = {'usuario': usuario}
                return render(request, "tienda/index.html", context)
        return render(request, "tienda/error.html", context)
    
def cerrar(request):
    print("Estoy en cerrar")
    request.session["usuario"]=""
    usuario=request.session["usuario"]
    context={'usuario':usuario}
    return render(request, "tienda/login.html", context)

def crud_usuarios(request):
    print("Hola estoy en crud de usuarios")
    context={'usuarios':usuarios}
    return render(request, "tienda/usuarios_listar.html",context)

def usuario_añadir(request):
    context={}

    if request.method == "POST":
        nombre = request.POST['nombre']
        contraseña = request.POST['contraseña']
        correo = request.POST['correo']
        telefono  = request.POST['telefono']
        admin = request.POST['admin']
        opcion = request.POST['opcion']

        if opcion == "Añadir":
            usuario = Usuario(nombre,contraseña,correo,telefono,admin)
            usuarios.append(usuario)
            context={'usuarios':usuarios}
            return render(request, "tienda/usuario_añadir.html", context)

        if opcion == "Volver al crud":
            context={'usuarios':usuarios}
            return render(request, "tienda/usuarios_listar.html", context)
    return render(request, "tienda/usuario_añadir.html", context)

def usuario_eliminar(request, pk):
       
    for usuario in usuarios:
        if usuario.telefono == pk:
            usuarios.remove(usuario)
            break
    context={'usuarios':usuarios}
    return render(request, "tienda/usuarios_listar.html",context)

def usuario_editar(request,pk):
    context={}

    for usuario in usuarios:
        if usuario.telefono == pk:
            context={'usuario':usuario}
            break

    return render(request, 'tienda/usuario_editar.html',context)

def usuario_actualizar(request):
    context={}
    if request.method == "POST":
        nombre = request.POST['nombre']
        contraseña = request.POST['contraseña']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        admin = request.POST['admin']
        opcion = request.POST['opcion']
        
    
    if opcion == "Actualizar":
        usuario = Usuario(nombre,contraseña,correo,telefono,admin)
        for obj in usuarios:
            if obj.admin == usuario.admin:
                obj.contraseña = usuario.contraseña
                obj.correo = usuario.correo
                obj.nombre = usuario.nombre
                obj.telefono= usuario.telefono
                break
        context={'usuarios':usuarios}
        return render(request,"tienda/usuarios_listar.html",context)
    
    if opcion == "Volver al crud":
        context={'usuarios':usuarios}
        return render(request,"tienda/usuarios_listar.html",context)

