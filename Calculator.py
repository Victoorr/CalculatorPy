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
print (' Vamos come�ar a usar a calculadora?')
print ('   1 = Adi��o')
print ('   2 = Subtra��o')
print ('   3 = Multiplica��o')
print ('   4 = Divis�o')
print ('')

primeiro = input('Insira o primeiro n�mero: ')
calcular = int(input('Insira a forma de calcula��o: '))
segundo = input('Insira o segundo n�mero: ')
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
