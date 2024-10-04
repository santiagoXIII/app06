import flet as ft
#Se importa la libreria random
import random

def main(page: ft.Page):
    #Se crean las variables globales
    global numero_secreto,entrada_numero,text_resultado,boton_adivinar
    
    page.title = "adivina el número"
    page.bgcolor = "blue"
    #se genera un número aleatorio del 1 al 100
    numero_secreto = random.randint(1,100)
    
    #se genera ña omterfaz grafica
    titulo = ft.Text("adivina el número", size=25,color="white")
    entrada_numero=ft.TextField(label = "Tu adivinanza entre 1 y 100", width=300)
    boton_adivinar=ft.ElevatedButton("Adivinar")
    text_resultado=ft.Text("",color="white")
    
    contenedor_principal=ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                text_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=350,
                    height=300
                )
            ],alignment="CENTER",
            horizontal_alignment="CENTER",
            spacing=20
        ),
        bgcolor="green",
        width=page.window.width,
        height=page.window.height,
        padding=20
    )
    page.add(contenedor_principal)
    
ft.app(main)
