import os
import random
import pickle

__author__ = 'A3'
class Equipos():
    def __init__(self,a,b,c,d,e):
        self.cod = a
        self.des = b
        self.pre = c
        self.tipo = d
        self.ori = e


def fun_uno(fd):
    print('Listo par realizar la carga ')
    print()

    y = int(input('Cuatos datos desea cargar : '))

    if not os.path.exists(fd):
        m = open(fd,'wb')
    else:
         m  = open(fd,'ab')
    for i in range(y):
        a = random.randint(0,300)
        b = 'descripcion nro '+str(random.randint(0,300))
        c = random.randint(100,30000)
        d = random.randint(0,19)
        e = random.randint(0,24)
        aux = Equipos(a,b,c,d,e)
        pickle.dump(aux,m)
        m.flush()
    m.close()
    print('Carga realizada ')
    print()
    t = os.path.exists(fd)
    return fd,t


def string(aux):
    print()
    sal = ''
    sal+='|Precio :'+str(aux.pre)
    sal+='| Descrip :'+str(aux.des)
    sal+='| Codigo  :'+str(aux.cod)
    sal+='| Tipo    :'+str(aux.tipo)
    sal+='| Origen :'+str(aux.ori)
    print()
    return sal



def fun_dos(fd):
    m = open(fd,'rb')
    t = os.path.getsize(fd)

    while m.tell()< t:
        aux = pickle.load(m)
        print(string(aux))


def add_in_order(a, vec):
    n = len(vec)
    pos= n
    for i in range(n):
        if a.cod < vec[i].cod :
            pos = i
            break
    vec[pos:pos] = [a]



def fun_tres(fd,vec):
    m = open(fd,'rb')
    t = os.path.getsize(fd)
    while m.tell()< t:
        a = pickle.load(m)
        add_in_order(a,vec)
    m.close()
    return vec


def fun_cuatro(vec):
    for i in vec:
        print(string(i))

    print('Listado completo ')
    print()
    return

def fun_cinco(vec):
    fi = 20
    col = 25
    mat = [[0]*col for i in range(fi)]
    for i in vec:
        mat[i.tipo][i.ori] =i.cod
    for i in range(len(mat)):
        for j in range(len(mat[0])):
          if mat[i][j]!=0:
            print('Para el tipo ',i)
            print(' Y origen ', j)
            print('Existen ',mat[i][j])
            print()


def menu():

    fd = 'ARCHIVO .DAT '

    vec = list()

    x = -1

    t = os.path.exists(fd)
    while x!=0:
        print('1 Crear archivo ..')
        print('2 Mostrar archivo ')
        print('3 Pasar datos a vec')
        print('4 Listar datos del vec')
        print('5 Matriz')
        print('0 Salir')


        x = int (input('Eliga una op : '))

        if x == 1:
            print('Opcion 1 ')
            fd ,t= fun_uno(fd)
        if x == 2 and t :
            print('Opcion 2 ')
            print()
            fun_dos(fd)
        else:
             print('EL archivo no existe use la op "1"')
             print()

        if x == 3 and t :
            print('Opcion 3 ')
            print()
            fun_tres(fd,vec)
        else:
             print('EL archivo no existe use la op "1"')
             print()
        if x ==4 and len(vec)!=0:
            print('Opcion 4 ')
            fun_cuatro(vec)
        if x ==5 and len(vec )!=0:
            print('Opcion 5')
            fun_cinco(vec)
            print()
        if x ==0:
            print()
            print('Vuelva pronto')


menu()