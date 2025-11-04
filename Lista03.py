# # Questâo 1   

# peso=float(input("informe seu peso em kilos "))
# altura=float(input("informe sua altura em metros "))
# imc= peso/(altura*altura)
# print(f"Seu imc é {imc}")
# if imc< 18.5:
#     print("Abaixo do Peso")
# elif imc>= (18.5) and imc <= (24.9):
#     print("Peso normal")
# elif imc >=25 and imc<= 29.9:
#     print("Sobrepeso")
# elif imc>=30:
#     # print("Obeso")


# Questâo 2

# n = int(input("digite um numero "))
# for num in range(1, n+1):
#     if num%2 ==0:
#         print(f"{num} é par")
#     else:
#         print(f"{num} é impar")

# Questão 3

# num = int(input("digite um numero "))
# for u in range(1, 11):
#     tabu= u*num
#     print(f"{u} * {num} = {tabu}")

# Questão 4

# cont=0
# num=int(input("digite um numero: "))
# for x in range(1,num+1):
#     if num%x==0:
#         cont+=1
# if cont<=2:
#     print(f"{num} é primo")
# else:
#     print(f"{num} não é primo")

# Questão 5

# soma=0
# maior=0
# menor=0
# alunos=int(input("digite a quantidade de alunos: "))
# for x in range(1,alunos+1):
#     nota=int(input(f"digite a nota do aluno {x}: "))
#     soma+=nota
#     if nota>=6:
#         maior+=1
#     elif nota<6:
#         menor+=1
# med=soma/alunos
# print(f"alunos com nota acima da média: {maior}")
# print(f"alunos com nota abaixo da média: {menor}")
# print(f"média total: {med}")

# Questão 6

# import random
# numerocerto=random.randint(1,20)
# tentativa=int(input("tente acertar o numero: "))
# while tentativa!=numerocerto:
#     if tentativa>numerocerto:
#         tentativa=int(input("muito alto! tente um numero mais baixo: "))
#     elif tentativa<numerocerto:
#         tentativa=int(input("muito baixo! tente um numero mais alto: "))
# print(f"Você acertou! o número era: {numerocerto}")
        