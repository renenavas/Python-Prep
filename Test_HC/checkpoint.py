# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def ListaEnteros(inicio, tamanio):
    '''
    Esta función devuelve una lista de números enteros
    Recibe dos argumentos:
        inicio: Numero entero donde inicia la lista
        tamanio: Cantidad de números enteros consecutivos
    Ej:
        ListaEnteros(10,5) debe retornar [10,11,12,13,14]
    '''
    lista = []
    #Tu código aca:
    if tamanio < 1:
        raise  ValueError('el tamanio debe ser enteros positivos')
    try:
        for i in range(inicio,inicio+tamanio):
            lista.append(i)
        return lista
    except:
        raise ValueError('Los parametros deben ser enteros positivos')

def DividirDosNumeros(dividendo, divisor):
    '''
    Esta función devuelve dos valores, la parte entera de la división y su resto
    Recibe dos argumentos:
        dividendo: El número que va a ser dividido
        divisor: El número que va a dividir
    Ej:
        DividirDosNumeros(10,3) debe retornar 3, 1
    '''
    parte_entera = None
    resto = None
    #Tu código aca:
    try:    
        parte_entera = dividendo // divisor
        resto = dividendo % divisor
        return parte_entera, resto
    except ZeroDivisionError:
        print('El divisor no puede ser 0')
    except TypeError:
        print('Los parametros deben ser enteros')

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    if type(numero) != int or numero < 1:
        return None
    else:
        if numero == 1:
            return 1
        else:
            return numero * Factorial(numero-1)

def ProximoPrimo(actual_primo):
    '''
    Esta función devuelve el número primo siguiente al enviado como parámetro.
    En caso de que el parámetro no sea de tipo entero y/o no sea un número primo, debe retornar nulo.
    Recibe un argumento:
        actual_primo: Será el número primo a partir del cual debo buscar el siguiente
    Ej:
        ProximoPrimo(7) debe retornar 11
        ProximoPrimo(8) debe retornar nulo
    '''
    #Tu código aca:
    if type(actual_primo) != int:
        return None
    
    def es_primo(x):
        if x == 1 or x == 0:
            return False
        primo = True
        j = 2
        while j < x:
            if x % j == 0:
                return False
            j += 1
        return primo
    
    if es_primo(actual_primo) == False:
        return None
    else:
        n = actual_primo +1
        while es_primo(n) == False:
            n += 1
        return n
   

def NumeroCapicua(numero):
    '''
    En matemáticas, la palabra capicúa (del catalán cap i cua, 'cabeza y cola')​ 
    se refiere a cualquier número que se lee igual de izquierda a derecha que 
    de derecha a izquierda.
    Esta función devuelve el valor booleano True si el número es capicúa, de lo contrario
    devuelve el valor booleano False 
    En caso de que el parámetro no sea de tipo entero, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número sobre el que se evaluará si es capicúa o no lo es.
    Ej:
        NumeroCapicua(787) debe retornar True
        NumeroCapicua(108) debe retornar False
    '''
    #Tu código aca:
    if type(numero) != int:
        return None
    backwards = str(numero)
    backwards = backwards[::-1]
    backwards = int(backwards)
    
    if numero == backwards:
        return True
    else:
        return False