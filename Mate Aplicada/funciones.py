import random 

def determinaNumero(num):
    if num < 0:
        print(f'{num} es negativo')
    elif num > 0:
        print(f'{num} es positivo')
    else:
        print('El numero es cero')

def parImpar(num):
    if num % 2 != 0:
        print('El numero es impar')
    else:
        print('El numero es par')

def sumaNum():
    cont = suma = 0
    while cont < 100: 
        cont += 1
        suma += cont
        print(suma)

def encontrarPassw():
    password = 'sade12345'
    passw = input('Ingrese password: ')
    while passw != password:
        passw = input('Ingrese password: ')

def tablaMult(num):
    for i in range(1,13):
        print(f'{num} * {i} = {num * i}')

def productoNum(num1, num2):
    return num1 * num2

def redondear(num):
    print(round(num))

def conversorTemp(grds):
    fahrenheit = ((9/5) * grds) + 32
    print(f'{grds} grados Celsius equivale a {round(fahrenheit, 2)} grados Fahrenheit')

def generarNumeros():
    listNum = []
    for i in range(10):
        numRand = random.randint(1,101)
        listNum.append(numRand)
    print(listNum)
    print(f'Segundo elemento: {listNum[1]}')
    print(f'Sexto elemento: {listNum[5]}')

def calcularIMC(peso, altura):
    imc = peso / altura ** 2
    print(f'Tu IMC: {imc}')
    if imc < 18.5:
        print('Bajo peso')
    elif 18.5 <= imc < 24.9:
        print('Peso normal')
    elif 25 <= imc <= 29.9:
        print('Sobrepeso')
    else:
        print('Obesidad')

def infoListas(listP, listIMC):
    print('Bajo peso: ')
    for n in range(len(listIMC)):
        if listIMC[n] < 18.5:
            print(f'IMC {listIMC[n]} en indice: {n + 1}')
