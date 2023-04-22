import os
import random
import pickle

fd='Datos.dat'
class Hoteles :
    def __init__(self,a ,b ,c ,d , e):
        self.nombre = a
        self.hotel = b
        self.categoria = c
        self.puntuacion = d
        self.m_precio = e

def carga_automatica(fd,x):
    hoteles=['arr','ff','ddd','zzz','ddddd','jjj']
    nom=['carlos','gero','guille','nico','eia']
    m=open(fd,'wb')
    for i in range(x):
        hotel=random.choice(hoteles)
        nombre=random.choice(nom)
        categoria=random.randint(0,5)
        puntuacion=random.randint(0,10)
        m_precio=random.randint(100,10000)
        aux =(Hoteles(nombre,hotel,categoria,puntuacion,m_precio))
        pickle.dump(aux,m)
        m.flush()
        print ('Se cargo el archivo nro',str(i+1))
    m.close()

def cargar_vector(fd):
    vec=[]
    m=open(fd,'r+b')
    t=os.path.exists(fd)
    if t == 0:
        print ('El archivo no existe ')
    else:
         aux=os.path.getsize(fd)

         while m.tell() < aux:
             a = pickle.load(m)

             vec.append(a)

    return vec
def     ordenar(vec):
    for i in range(len(vec)):
        for j in range(len(vec)-1):
            if vec[i].puntuacion > vec[j].puntuacion :
                vec[i],vec[j]=vec[j],vec[i]
    return  vec


def punto_uno(vec):
        for i in vec :
            if vec.puntuacion >= 9 :
                print(vec.hotel)+'  |Puntuacion >='+str(vec.puntuacion)+'-> Exelente '
            #asi con todos los tipos de puntuacion


def to_string(a):
    sal=' '
    sal='Hotel :'+a.hotel+' |Categoria :'+str(a.categoria)+' |Puntuacion'+str(a.puntuacion)+'  |Mejor Precio'+str(a.m_precio)
    return  sal


def punto_dos(x,vex):
    v_aux=list()
    for i in range(len(vex)):
        if vex[i].m_precio < x:
            v_aux.append(vex[i])

    v_aux = ordenar(v_aux)
    for j in range(len(v_aux)):
        print(to_string(v_aux[j]))

def espacios(x):
    print(' '*x)
    pass

def punto_tres(vec,x):

    for i in vec :
        if vec.puntuacion == x:
            pass

def menu():
    print('1. Consultar por popularidad')
    print('2. Consultar por precio')
    print('3. Rango de precios')
    print('4. Mejor puntuacion')
    print('5. Estadistica')
    print('6. Reservar')


def validar(param, param1):
    x=int(input(param1))
    while x < param:
        print('Error')
        print('Debe cargar como minimo "10" hoteles ')
        x = int(input(param1))
    return  x

def main():
    x = -1
    vec = []
    while x != 0:
        print('Bienvenido')
        menu()
        aux=validar(10,'Ingrese cantidad de hoteles :')

        carga_automatica(fd,aux)

        vec=cargar_vector(fd)

        x = int(input('Ingrese una opcion : '))

        if x == 1:
            print('Opcion 1  ')
            espacios(4)
        elif x == 2:
            print('Opcion 2  ')
            espacios(4)
        elif x == 3:
            print('Opcion 3  ')
            espacios(4)
        elif x == 4:
             print('Opcion 4 ')
             espacios(4)
        elif x == 5:
             print('Opcion 5 ')
             espacios(4)
        elif x == 6:
             print('Opcion 6 ')
             espacios(4)
        elif x == 7:
             print('Opcion 7 ')
             espacios(4)
main()