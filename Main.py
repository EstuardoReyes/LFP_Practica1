from tkinter import Tk     
from tkinter.filedialog import askopenfilename
import Automata
import copy
import webbrowser
archivo_Seleccionado = False
salida = False
listaAlpha = []
def cls():
    r=0
    while r<10:
        print("")
        r=r+1 
def salir():
    print("201709015 Edwin Estuardo Reyes Reyes")
    print("       tato961122@gmail.com")
    print("Lenguajes Formales de Programacion A-") 
    print("            17/02/21")

def carga():
    root = Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    filename = askopenfilename(initialdir="/",
                           filetypes =(("Archivo de LFP", "*.lfp"),("All Files","*.*")),
                           title = "Busque su archivo.")
    root.update()
    root.destroy()
    archivo = open(filename,'r')
    while True: 
        linea = archivo.readline()  # lee línea
        if not linea: 
          break  # Si no hay más se rompe bucle
        list = Automata.AFD(linea)
        x=1
        listaElementos = []
        listaSolicutudes = []
        while  x < len(list):
            if list[x] == 'BUSCAR' or list[x] == 'buscar' or list[x] == 'ordenar' or list[x] == 'ORDENAR':
              break
            else:
               listaElementos.append(list[x])
               x=x+1
        while  x < len(list):
               listaSolicutudes.append(list[x])
               x=x+1
        dic1 = {'nombre' : list[0] , 'lista' : listaElementos, 'solicitud' : listaSolicutudes}
        listaAlpha.append(dic1)       
    archivo.close()  # Cierra archivo
    print("Archivo cargado correctamente")

def despli_orden():
    if (archivo_Seleccionado == False):
        print("Error archivo no fue cargado previamente")
    else:
        x = 0
        while x < len(listaAlpha):
            lis_auxiliar = listaAlpha[x]['solicitud'] 
            if lis_auxiliar[0] == 'ORDENAR' or lis_auxiliar[len(lis_auxiliar)-1] == 'ORDENAR' or lis_auxiliar[0] == 'ordenar' or lis_auxiliar[len(lis_auxiliar)-1] == 'ordenar':
                lis_int = list(listaAlpha[x]['lista'])
                for i in range(1,len(lis_int)):
                    for j in range(0,len(lis_int)-i):
                        if(lis_int[j+1] < lis_int[j]):
                            aux=lis_int[j]
                            lis_int[j]=lis_int[j+1]
                            lis_int[j+1]=aux
                print(listaAlpha[x]['nombre']+": Lista Ordenada = ", end="")
                for q in range (0,len(lis_int)-1):
                    print(lis_int[q]+", ", end="")
                print(lis_int[len(lis_int)-1])
                x=x+1
            else:
                x=x+1
           
def despli_busqueda():
    if (archivo_Seleccionado == False):
        print("Error archivo no fue cargado previamente")
    else:
        x = 0
        while x < len(listaAlpha):
            encontrado = False
            lis_auxiliar = listaAlpha[x]['solicitud'] 
            if lis_auxiliar[0] == 'BUSCAR' or lis_auxiliar[len(lis_auxiliar)-2] == 'BUSCAR' or lis_auxiliar[0] == 'buscar' or lis_auxiliar[len(lis_auxiliar)-2] == 'buscar':
                lis_int = listaAlpha[x]['lista']
                if lis_auxiliar[0] == 'BUSCAR' or lis_auxiliar[0] == 'buscar':
                    comparativa = lis_auxiliar[1]
                else:
                    comparativa = lis_auxiliar[len(lis_auxiliar)-1]
                for i in range(0,len(lis_int)):
                    if comparativa == lis_int[i]:
                        encontrado = True
                if encontrado == False:
                    print(listaAlpha[x]['nombre']+' '+comparativa+ " no encontrado")
                elif encontrado == True:
                    print(listaAlpha[x]['nombre']+": Posiciones de "+comparativa+" = ", end="")
                    for q in range (0,len(lis_int)-1):
                        if comparativa == lis_int[q]:
                            r = q+1
                            print(str(r)+", ", end="")
                    if comparativa == lis_int[len(lis_int)-1]:
                        f = len(lis_int)
                        print (f)
                x=x+1
            else:
                x=x+1

def despli_todos():
    if (archivo_Seleccionado == False):
        print("Error archivo no fue cargado previamente")
    else:
        x = 0
        while x < len(listaAlpha):
            lis_auxiliar = listaAlpha[x]['solicitud'] 
            if lis_auxiliar[0] == 'ORDENAR' or lis_auxiliar[len(lis_auxiliar)-1] == 'ORDENAR' or lis_auxiliar[0] == 'ordenar' or lis_auxiliar[len(lis_auxiliar)-1] == 'ordenar':
                lis_int = list(listaAlpha[x]['lista'])
                for i in range(1,len(lis_int)):
                    for j in range(0,len(lis_int)-i):
                        if(lis_int[j+1] < lis_int[j]):
                            aux=lis_int[j]
                            lis_int[j]=lis_int[j+1]
                            lis_int[j+1]=aux
                print(listaAlpha[x]['nombre']+": Lista Ordenada = ", end="")
                for q in range (0,len(lis_int)-1):
                    print(lis_int[q]+", ", end="")
                print(lis_int[len(lis_int)-1])
            encontrado = False
            lis_auxiliar = listaAlpha[x]['solicitud'] 
            if lis_auxiliar[0] == 'BUSCAR' or lis_auxiliar[len(lis_auxiliar)-2] == 'BUSCAR' or lis_auxiliar[0] == 'buscar' or lis_auxiliar[len(lis_auxiliar)-2] == 'buscar':
                lis_it = listaAlpha[x]['lista']
                if lis_auxiliar[0] == 'BUSCAR' or lis_auxiliar[0] == 'buscar':
                    comparativa = lis_auxiliar[1]
                else:
                    comparativa = lis_auxiliar[len(lis_auxiliar)-1]
                for i in range(0,len(lis_it)):
                    if comparativa == lis_it[i]:
                        encontrado = True
                if encontrado == False:
                    print(listaAlpha[x]['nombre']+' '+comparativa+ " no encontrado")
                elif encontrado == True:
                    print(listaAlpha[x]['nombre']+": Posiciones de "+comparativa+" = ", end="")
                    for q in range (0,len(lis_it)-1):
                        if comparativa == lis_it[q]:
                            r = q+1
                            print(str(r)+", ", end="")
                    if comparativa == lis_it[len(lis_it)-1]:
                        f = len(lis_it)
                        print (f)
                x=x+1
                
            else:
                x=x+1
            print(" ")        

def despli_html():
    mensajefinal = ""
    if (archivo_Seleccionado == False):
        print("Error archivo no fue cargado previamente")
    else:
        x = 0
        while x < len(listaAlpha):
            mensajefinal = mensajefinal +"""<tr style="color:#F8F8FF"> <td>"""+ listaAlpha[x]['nombre'] +"""</td>"""
            lis_auxiliar = listaAlpha[x]['solicitud'] 
            if lis_auxiliar[0] == 'ORDENAR' or lis_auxiliar[len(lis_auxiliar)-1] == 'ORDENAR' or lis_auxiliar[0] == 'ordenar' or lis_auxiliar[len(lis_auxiliar)-1] == 'ordenar':
                lis_int = list(listaAlpha[x]['lista'])
                for i in range(1,len(lis_int)):
                    for j in range(0,len(lis_int)-i):
                        if(lis_int[j+1] < lis_int[j]):
                            aux=lis_int[j]
                            lis_int[j]=lis_int[j+1]
                            lis_int[j+1]=aux
                mensajefinal = mensajefinal+"<td> Lista Ordenada = "
                for q in range (0,len(lis_int)-1):
                    mensajefinal = mensajefinal + str(lis_int[q])+", "
                mensajefinal = mensajefinal + str(lis_int[len(lis_int)-1]) + "</td>"
            else:
                mensajefinal = mensajefinal + "<td> OPCION NO SOLICITADA </td>"
            encontrado = False
            lis_auxiliar = listaAlpha[x]['solicitud'] 
            if lis_auxiliar[0] == 'BUSCAR' or lis_auxiliar[len(lis_auxiliar)-2] == 'BUSCAR' or lis_auxiliar[0] == 'buscar' or lis_auxiliar[len(lis_auxiliar)-2] == 'buscar':
                lis_it = listaAlpha[x]['lista']
                if lis_auxiliar[0] == 'BUSCAR' or lis_auxiliar[0] == 'buscar':
                    comparativa = lis_auxiliar[1]
                else:
                    comparativa = lis_auxiliar[len(lis_auxiliar)-1]
                for i in range(0,len(lis_it)):
                    if comparativa == lis_it[i]:
                        encontrado = True
                if encontrado == False:
                    mensajefinal = mensajefinal + "<td> "+str(comparativa) +" NO ENCONTRADA </td>"
                elif encontrado == True:
                    mensajefinal = mensajefinal + "<td> Posiciones de "+str(comparativa) +" ="
                    for q in range (0,len(lis_it)-1):
                        if comparativa == lis_it[q]:
                            r = q+1
                            mensajefinal = mensajefinal + str(r)+", "
                    if comparativa == lis_it[len(lis_it)-1]:
                        f = len(lis_it)
                        mensajefinal = mensajefinal + str(f)+"</td>"
                x=x+1
                
            else:
                x=x+1
                mensajefinal = mensajefinal + "<td> OPCION NO SOLICITADA </td>"
            mensajefinal = mensajefinal + "</tr>"
        f = open('DesplieguedeListas.html','wb')
        mensaje = """<html>
                        <head><title>Listas Desplegadas</title></head>
                        <body bgcolor=#00AAE4>
                        <h2 align="center">Listas Desplegadas</h2>
                        <div style="text-align:center;">
	                    <table border="1" style="margin: 0 auto;">
	                    <tr style="color:#F8F8FF">
                        <td>Nombre</td>
		                <td>Ordenadas</td>
                        <td>Buscadas</td>
	                    </tr>"""
        mensaje = mensaje + mensajefinal
        ms = """</table></div></body></html>""" 
        mensaje= mensaje + ms
        f.write(bytes(mensaje,"ascii"))
        f.close()
        webbrowser.open_new_tab('DesplieguedeListas.html')

while salida == False:
    cls()
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
        archivo_Seleccionado = True
        a = input()
    elif (a == '2'):
        despli_orden()
        a = input()
    elif (a == '3'):
        despli_busqueda()
        a = input()
    elif (a == '4'):
        despli_todos()
        a = input()
    elif (a == '5'):
        despli_html()
        a = input()
    elif (a == '6'):
        salir()
        a=input()
        salida = True
    else:
        print("Opcion "+a+" no se encuentra entre las opciones")