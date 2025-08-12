for i in range(5):
    num = int(input('Digite um número: '))
    if i == 0:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
print(menor, maior)