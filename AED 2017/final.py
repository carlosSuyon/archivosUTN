import os
import random
import pickle

__author__ = 'carlos_suyon'


class Empresa:
    def __init__(self, a, b, c, d, e):
        self.nro = a
        self.des = b
        self.tip = c
        self.cal = d
        self.tar = e


def string(i):
    print()
    sal = ''
    sal += '|nro : ' + str(i.nro)
    sal += '|des : ' + i.des
    sal += '|tipo  : ' + str(i.tip)
    sal += '|cal : ' + str(i.cal)
    sal += '|tar : ' + str(i.tar)
    return sal


def main():
    print('1 cargar n datos')
    print('2 mostrar los datos')
    print('3 generar otro areglo ')
    print('4 Mostrar el nuevo arreglo, a razón de un registro por línea. ')
    print(
        '5 mostrar los datos de todos los productos cuyo precio sea menor o igual a un valor p que se carga por teclado')
    print('6 matriz')
    print('7 crear archivo')
    print('8 mostrar archivo')
    print('0 salir ')


def validar(param):
    while param < 0 or 0 > param > 8:
        print('Error ')
        param = int(input('Selecione una op  : '))
    return param


def add_in_order_secuencial(aux, vec):
    n = len(vec)
    pos = n
    for i in range(n):
        if aux.nro < vec[i].nro:
            pos = i
            break
    vec[pos:pos] = [aux]


def cargar_datos(y, vec):
    for i in range(y):
        a = random.randint(0, 200)
        b = 'Descripcion nro' + str(i)
        c = random.randint(0, 14)
        d = random.randint(0, 4)
        e = random.randint(200, 40000)
        aux = Empresa(a, b, c, d, e)
        add_in_order_secuencial(aux, vec)
    print('Carga realizada ')
    print()
    return vec


def mostrar(vec):
    n = len(vec)
    if n == 0:
        print('No se cargo el vector ..')
        print('use el punto  1')
        return
    else:
        for i in vec:
            print(string(i))


def add_in_order_binario(aux, v):
    izq = 0
    der = len(v) - 1
    pos = len(v)

    while izq <= der:
        centro = (izq + der) // 2
        if aux.tar == v[centro].tar:
            pos = centro
            break
        if aux.tar < v[centro].tar:
            der = centro - 1
        else:
            izq = centro + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [aux]


def generar_new_arreglo(vec):
    v = list()
    n = len(vec)
    if n != 0:
        print('Generando nuevo vector ...')
        for i in vec:
            if i.tip > 10:
                add_in_order_binario(i, v)

        return v
    else:
        print('use la fucion uno para generar el primer arreglo')
        return


def punto_cinco(v, y):
    if len(v) != 0:
        for i in v:
            if i.tar >= y:
                print(string(i))

    else:
        print('No existe vector')
    return


def matriz(v):
    mat = [[0] * 5 for i in range(16)]
    print(mat)
    col, fi = 0, 0
    for i in v:
        fi = i.tip
        col = i.cal
        mat[fi][col] += 1

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != 0:
                print('Para el tipo : ', i)
                print('y la calidad nro : ', j)
                print('existen :', mat[i][j])


def grabar(v, fd):
    m = open(fd, 'wb')
    for i in v:
        pickle.dump(i, m)
    print('Se grabaron los archivos en el archivo ', fd)
    m.close()
    return fd


def mostrar_archivo(fd):
    if os.path.exists(fd):
        print('Archivo ', fd)
        m = open(fd, 'rb')
        t = os.path.getsize(fd)

        while m.tell() < t:
            aux = pickle.load(m)
            print(string(aux))
        m.close()
    else:
        print('No existe archivo ')
    return


def menu():
    print('Bienvenido ..')

    x = -1

    vec = list()

    fd = 'Archivo .dat '

    while x != 0:

        main()

        x = validar(int(input('Selecione una op  : ')))

        if x == 1:
            print('Opcion 1 ')
            print()
            y = int(input('cuantos datos desea procesar    : '))

            vec = cargar_datos(y, vec)
        if x == 2:
            print('Opcion 2 ')
            print()
            mostrar(vec)
        if x == 3:
            print('Opcion 3 ')
            print()
            v = generar_new_arreglo(vec)

        if x == 4:
            print('Opcion 4 ')
            print()
            mostrar(v)
        if x == 5:
            print('Opcion 5 ')
            print()
            y = int(input('precio P : '))
            punto_cinco(v, y)
        if x == 6:
            print('Opcion 6 ')
            print()
            matriz(v)
        if x == 7:
            print('Opcion 7')
            print()
            fd = grabar(v, fd)
        if x == 8:
            print('Opcion 8')
            print()
            mostrar_archivo(fd)


menu()