import sys
if len(sys.argv) == 3:
    sys.argv.append(False)
if len(sys.argv) == 4 :
    import datetime
    import csv
    temperatura = str(sys.argv[1])
    humedad = str(sys.argv[2])
    lluvia = bool(sys.argv[3])

    tiempo = datetime.datetime.now()
    marca_tiempo = int(datetime.datetime.timestamp(tiempo))

    linea = str(marca_tiempo) + ',' + str(temperatura) + ',' + str(humedad) + ',' + str(lluvia) + '\n'
    with open('clase09_ej2_mio.csv', 'a', encoding='UTF8') as f:
        f.write(linea)
else:
    print('Parametros incorrectos, se requiere temperatura humedad y lluvia como <int> <int> <True/False>')
    
