import sys
if len(sys.argv) == 4:
    print('El primer parametro es', sys.argv[1])
    print('El segundo parametro es', sys.argv[2])
    print('El tercer parametro es', sys.argv[3])
else:
    print('la cantidad de parametros es', len(sys.argv), 'este script requiere 3 parametros')