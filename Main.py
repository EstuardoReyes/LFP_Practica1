from tkinter import Tk     
from tkinter.filedialog import askopenfilename

def carga():
    Tk().withdraw() 
    filename = askopenfilename()
    print(filename)


salida = False
while salida == False:
    print("Menu")
    print("1. Cargar Archivo de entrada")
    print("2. Desplegar listas Ordenadas")
    print("3. Desplegar Busquedas")
    print("4. Desplegar todas")
    print("5. Desplegar todas a archivo")
    print("6. Salir")
    a = input("Seleccione una opcion ")
    if (a == '1'):
        carga()
    if (a == '2'):
        salida = True
    if (a == '3'):
        salida = True
    if (a == '4'):
        salida = True
    if (a == '5'):
        salida = True
    if (a == '6'):
        salida = True
    else:
        print("Opcion "+a+" no se encuentra entre las opciones")