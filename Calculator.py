print ('Calculadora iniciada! by Victor696')

def adicionar(x, y):
    return (x + y)

def subtrair(x, y):
    return (x - y)

def multiplicar(x, y):
    return (x * y)

def divisao(x, y):
    return (x / y)

print ('')
print (' Vamos começar a usar a calculadora?')
print ('   1 = Adição')
print ('   2 = Subtração')
print ('   3 = Multiplicação')
print ('   4 = Divisão')
print ('')

primeiro = input('Insira o primeiro número: ')
calcular = int(input('Insira a forma de calculação: '))
segundo = input('Insira o segundo número: ')
total = adicionar(primeiro, segundo)
total2 = subtrair(primeiro, segundo)
total3 = multiplicar(primeiro, segundo)
total4 = divisao(primeiro, segundo)

if calcular == 1:
    print ('Resultado: ', total)
elif calcular == 2:
    print ('Resultado: ', total2)
elif calcular == 3:
    print ('Resultado: ', total3)
elif calcular == 4:
    print ('Resultado: ', total4)
else:
    print ('Sintaxe errada, tente novamente!')
