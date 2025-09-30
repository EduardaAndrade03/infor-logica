# q1

# cont=0
# nomesa=[]
# nomes=[]
# for x in range(1, 6):
#     nome = str(input(f"digite o nome {x}: "))
#     nomes.append(nome)
# print(nomes)
# for x in nomes:
#     if x[0]=="a" or x[0]=="A":
#         cont+=1
#         nomesa.append(x)
# print(f"palavras com letra A: {cont}")
# print(f"palavras: {nomesa}")

# q2

# def calcular_media(notas):
#     med=0
#     for n in notas:
#         med+=n
#     med/=4
#     if med>=7:
#         return(f"aprovado, média: {med}")
#     elif med<7:
#         return(f"reprovado, média: {med}")
#     else:
#         return(f"ta errado isso ai man: {med}")
    
# notas4=[]
# for x in range(1, 5):
#     nota=int(input(f"diz ai a nota {x}: "))
#     notas4.append(nota)
# print(calcular_media(notas4))

# q3

# numeros=[]
# for x in range(1,7):
#     num=int(input(f"digite o numero {x}: "))
#     numeros.append(num)
# tentativa=int(input("agora digite outro: "))

# if tentativa in numeros:
#     print("você acertou!")
#     print(f"posição: {numeros.index(tentativa)+1}")
# else:
#     print("não encontrado")
     
# q4

# def filtrar_pares(lista):
#     listapares=[]
#     for x in lista:
#         if x%2==0:
#             listapares.append(x)
#     return print(listapares)

# numeros=[]
# for x in range(1,11):
#     numero=int(input(f"digite o numero {x}: "))
#     numeros.append(numero)

# filtrar_pares(numeros)

# q5

# numeros=[]
# for x in range(1,9):
#     inteiro=int(input(f"digite o numero {x}: "))
#     numeros.append(inteiro)
# soma=0
# med=0
# for x in numeros:
#     soma+=x
#     if x==numeros[0]:
#         maior=x
#         menor=x
#     elif x>maior:
#         maior=x
#     elif x<menor:
#         menor=x
# med=soma/8
# print(f"número maior: {maior}")
# print(f"número menor: {menor}")
# print(f"soma de todos os numeros: {soma}")
# print(f"média: {med}")
    
# q6

# def remover_elemento(lista, valor):
#     for v in lista:
#         if v==valor:
#             lista.remove(v)
#     return print(lista)
    

# numeros=[]
# for x in range(1,11):
#     numero=int(input(f"digite o numero {x}: "))
#     numeros.append(numero)
# remover=int(input("digite um numero para remover: "))
# remover_elemento(numeros, remover)

# q7

# nomes=[]
# for x in range(1,6):
#     nome=str(input(f"digite o {x}º nome: "))
#     nomes.append(nome)
# checar=str(input("qual nome você quer verificar?: "))
# if checar in nomes:
#     print('Convidado confirmado!')
# else:
#     print("convidado não encontrado")

# q8

# cont = 0
# nm = int(input("bota o numero ai: "))
# for i in range(1, nm +1):
#     if nm % i == 0:
#         cont +=1
# if cont > 2:
#     print("numero nao é primo")
# else:
#     print("primo.")