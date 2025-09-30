# q1 

# def saudacao(nome : str):
#     return f"olá {nome}, seja bem vindo ao curso de lógica de programação"
# nome=str(input("digite seu nome: "))
# print(saudacao(nome))

# q2

# def par_impar(n1):
#     if n1%2 == 0:
#         msg=f"o numero {n1} é par"
#     elif n1%2!=0:
#         msg=f"o numero {n1} é impar"
#     else:
#         msg="numero indeterminado"
#     return msg
# n=int(input("digite um numero "))
# print(par_impar(n))

# q3

# def maior(n1 : int, n2: int):
#     if n1>n2:
#         msg= f"{n1} é maior que {n2}"
#     elif n2>n1:
#         msg = f"{n2} é maior que {n1}"
#     else:
#         msg = f"{n1} é igual a {n2}"
#     return msg
# n1=int(input("digite o numero 1 "))
# n2=int(input("digite o numero 2 "))
# print(maior(n1, n2))

# q4

# tabu=1
# n=int(input("fala um numero: "))
# for num in range(1, 11):
#     tabu= num*n
#     print(f"{n}x{num}={tabu}")

# q5

# for num in range(10, -1, -1):
#     if num ==0:
#         print("Explosão!")
#     else:
#         print(f"{num}")

# q6

# def media(n1, n2, n3):
#     med= ((n1+n2+n3)/3)
#     return med
# n1=int(input("nota 1"))
# n2=int(input("nota 2"))
# n3=int(input("nota 3"))
# print(media(n1, n2, n3))

# q7

# def fatorial(n:int):
#     fato=1
#     for num in range(1, n+1):
#       fato*=num
#     msg= f"fatorial de {n} é {fato}"
#     return msg
# print(fatorial(5))

# q8

# def vogais(palavra:str):
#     contvogais=0
#     for l in palavra:
#         if l == "a" or l=="e" or l == "i" or l == "o" or l=="u":
#             contvogais+=1
#     return f"vogais totais: {contvogais}"

# palavra = str(input("digite uma palavra(apenas letras minúsculas): "))
# print(vogais(palavra))

# q9

# import random
# numeroaleatorio= random.randint (1, 20)
# tentativa= int(input("faça uma tentativa "))
# while tentativa!=numeroaleatorio:
#     if tentativa>=21:
#         print("ValueError")
#         tentativa=int(input("tente novamente "))
#     elif tentativa>numeroaleatorio:
#         print("o numero é menor")
#         tentativa=int(input("tente novamente "))
#     elif tentativa<numeroaleatorio:
#         print("o numero é maior")
#         tentativa=int(input("tente novamente "))
    

# print("parabens, voce acertou!")

# q10

# pares=0
# num = int(input("digite um número: "))
# for x in range(1, num+1):
#     if x%2==0:
#         pares+=x
# print(f"a soma dos números pares antes de {num} é igual a: {pares}")


# # q11

# def calculadora(n1:int, n2:int, operacao):
#     if operacao=="+" :
#         result= n1+n2
#     elif operacao== "-" :
#         result= n1-n2
#     elif operacao== "*":
#         result= n1*n2
#     elif operacao=="/":
#         result= n1/n2
#     else:
#         result="operacao indeterminada"
#     return result

# print("soma: +")
# print("subtração: -")
# print("multiplicação: *")
# print("divisão: /")

# n1=int(input("digite o numero 1 "))    
# n2=int(input("digite o numero 2 "))    
# op=str(input("digite a operação "))
# print(calculadora(n1, n2, op))

# q12

# def primo(num):
#     resto=0
#     for x in range(1, num+1):
#         if num%2==0:
#             resto+=1
#     if resto>2:
#         msg = f"{num} não é primo"
#     else:
#         msg = f"{num} é primo"

#     return msg

# n = int(input("digite um numero: "))
# print(primo(n))

# # q13
# list=[]
# def inversao(palavra: str):
#     invertida= palavra[ : : -1]
#     return invertida

# palavr=str(input("digite uma palavra: "))
# print(inversao(palavr))

# q14

# num=0
# somapares=0
# somaimpares=0
# listap=[]
# listai=[]
# for a in range(1, 11):
#     num=int(input("digite um numero: "))
#     if num%2==0:
#         somapares+=1
#         listap+=[num]
#     else:
#         somaimpares+=1
#         listai+=[num]
# print(f"numero de pares: {somapares}, {listap}")
# print(f"numero de impares: {somaimpares}, {listai}")

# q15

def fibo(num : int):
    f = 2
    for i in range(0, num):
        x = f
        f += f+x
    
        

n = int(input('digite um numero '))
fibo(n)