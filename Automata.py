def AFD(cadena):
    lista = []
    state = 0 
    auxiliar=''
    actual=''
    x=0
    while x < len(cadena):
        actual = cadena[x]
        if state == 0:
            if ord(actual) >= 48 and ord(actual) <= 57: #numeros
                state = 1
                auxiliar = auxiliar + actual
                x=x+1
              
            elif ord(actual)>=65 and ord(actual)<=90 or ord(actual)>=97 and ord(actual)<=122 or ord(actual)==164 or ord(actual)==165: #letras
                state = 2
                auxiliar = auxiliar + actual
                x=x+1
            else:
                x=x+1
    ###########################################################################
        elif state == 1:   
            if ord(actual) >= 48 and ord(actual) <= 57 or actual =='.':
                auxiliar = auxiliar + actual  
                x=x+1                                      #Estado 3
            else:
                lista.append(auxiliar)
                auxiliar = ''
                state = 0

    ############################################################################
        elif state == 2:     #Imprime solo palalabras
            if  ord(actual)>=65 and ord(actual)<=90 or ord(actual)>=97 and ord(actual)<=122 or ord(actual)==164 or ord(actual)==165  or ord(actual) >= 48 and ord(actual) <= 57:
                auxiliar = auxiliar + actual
                x=x+1
            else:
                lista.append(auxiliar)
                auxiliar = ''
                state = 0
    return lista