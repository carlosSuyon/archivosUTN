import os
import io


def fun_uno(fd):
    m = open(fd,'at')
    m.seek(0,io.SEEK_SET)
    print('<Enter> para para cargar linea .')
    print('La carga termina con ".-".')
    linea = input('Cargar :')

    while  not linea.endswith('.-'):

        if linea[-1]=='.-':
            break
        linea = linea+'\n'
        m.write(linea)
        linea= input('Cargar :')
    linea = linea[:-1]
    m.write(linea)

    m.close()
    return fd


def mostrar(fd):
    if not  os.path.exists(fd):
        print('El archivo no existe ')
        return
    else:
        m = open(fd,'rt')
        for linea in m :
            print(linea,end='')

        print()
        print('Este es el texto completo')
        m.close()
        return


def truncar(fd):
    if not os.path.exists(fd):
        print('El archivo no existe ')
        return
    else:
         m = open(fd,'r+t')
         cont = 0
         x = int(input('Cuantas lineas desea leer : '))
         txt = m.readline()
         while txt !=' ':
             cont+=1
             if cont == x:
                 break
             txt = m.readline()
         if cont == x:
             m.truncate(m.tell())
             print('Se trunco el archivo en ',x,'lineas')
         else:
              print('no se pudo trucan el archivo ')
    m.close()

def menu():
    fd = 'Archivos. dat'

    x = -1

    while x !=0:
        print('1 cargar texto')
        print('2 mostrar archivo')
        print('truncar archivo')

        x = int(input(' Op : '))
        if x == 1:
            print('Op 1')
            fd = fun_uno(fd)
        if x ==2:
            print('Op 2')
            mostrar(fd)
        if x ==3:
            print('Op 3')
            truncar(fd)
        if x ==0:

            print('hasta luego .. ')

menu()