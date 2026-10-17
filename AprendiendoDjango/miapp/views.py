from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category
from django.db.models import Q

# Create your views here.
# MVC = Modelo Vista Contrlador -> Acciones (metodos)
# MVT = Modelos Template Vista -> Acciones (metodos)

layout = """ 
<h1>Sitio Web con Django | ADSO SENA</h1>
<hr>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Pagina de pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>
</ul>
<hr>
    
"""

def index(request):

    html = """
            <h1>Inicio</h1>
            <p>Años hasta el 2050</p>
            <ul>
    """
    year = 2024
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1   
    html += "</ul>"
    
    nombre = 'Emanuel Merchan'
    lenguajes = ['Python', 'JavaScript', 'Java', 'C#', 'C++', 'PHP']
    

    return render(request, 'index.html', {
        'title': "Inicio",
        'mi_variable': "Soy un dato que esta en la vista",
        'nombre': nombre,
        'lenguajes': lenguajes
        }
    )

def hola_mundo(request):
    return render(request, 'hola-mundo.html')

def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('/inicio/')

    return render(request, 'pagina.html') 

def contacto(request, nombre="", apellido=""):

    html=""

    if nombre and apellido:
        html += "El nombre completo es:"
        html += f"<h3> {nombre} {apellido}</h3>"

    return HttpResponse(layout+f"<h2>Contacto </h2>" + html)

def crear_articulo(request, title, content, public):

    articulo = Article(
        title  = title,
        content = content,
        public = public
    )
    articulo.save()
    return HttpResponse(f"Artículo creado: <strong> {articulo.title} - {articulo.content}</strong>")

def articulo(request):

    try:
        articulo = Article.objects.get(title = "Matrix", public = False)
        response = f"Articulo: <br/>{articulo.id}. {articulo.title}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo {articulo.id} editado: <strong>{articulo.title} - {articulo.content}</strong>")

def articulos(request):

    articulos = Article.objects.all()

    articulos = Article.objects.filter(title__iexact = "articulo")

    articulos = Article.objects.filter(
                                        title = "Articulo",
                                        ).exclude(
                                            public = True
                                        )

    articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title = 'Articulo' AND public=0")

    articulos = Article.objects.filter(
        Q(title__contains = "Primer") | Q(title__contains = "Batman")
    )

    return render(request, 'articulos.html', { 

        'articulos': articulos
    })

def borrar_articulo(request, id):

    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')