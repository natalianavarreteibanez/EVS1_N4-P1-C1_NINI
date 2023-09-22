from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def vistaUno(request):
   html=""" <!DOCTYPE html>
    <html>
    <head>
        <title>Vista Uno NINI </title>
    </head>
    <body>
        <h1>Vista UNO NINI</h1>
        <p>Este es un párrafo de texto de la vista 1</p>
        <ul>
            <li>Elemento de lista 1</li>
            <li>Elemento de lista 2</li>
            <li>Elemento de lista 3</li>
        </ul>
        <ol>
            <li>Elemento numerado 1</li>
            <li>Elemento numerado 2</li>
            <li>Elemento numerado 3</li>
        </ol>
        <a href="https://www.inacap.cl/">Enlace al sitio web de INACAP</a>
        
        <br>
        <br>
        <form action="procesar_formulario" method="POST">
            <input type="text" name="nombre" placeholder="Nombre">
            <input type="email" name="correo" placeholder="Correo electrónico">
            <button type="submit">Enviar</button>
        </form>
        <br>
        <br>
        <p>Natalia Navarrete</p>
    </body>
    </html>
   """
   return HttpResponse(html)
    
def vistaDos(request):
   html=""" <!DOCTYPE html>
    <html>
    <head>
        <title>Vista DOS NINI </title>
    </head>
    <body>
        <h1>Vista DOS NINI </h1>
        <p>Este es un párrafo de texto de la vista 2</p>
        <ul>
            <li>Elemento de lista 1</li>
            <li>Elemento de lista 2</li>
            <li>Elemento de lista 3</li>
        </ul>
        <ol>
            <li>Elemento numerado 1</li>
            <li>Elemento numerado 2</li>
            <li>Elemento numerado 3</li>
        </ol>
        <a href="https://www.inacap.cl/">Enlace al sitio web de INACAP</a>
        
        <br>
        <br>
        <form action="procesar_formulario" method="POST">
            <input type="text" name="nombre" placeholder="Nombre">
            <input type="email" name="correo" placeholder="Correo electrónico">
            <button type="submit">Enviar</button>
        </form>
        <br>
        <br>
        <p>Natalia Navarrete</p>
    </body>
    </html>
   """
   return HttpResponse(html)
   