def lin():
    print('-'*30)


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


# Programa Principal
titulo('CURSO EM VIDEO')
titulo('PYTHON')
lin()


def soma(a, b):
    s = a + b
    print(s)


soma(4, 5)
soma(8, 9)
soma(2, 1)
lin()


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
lin()


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
lin()
