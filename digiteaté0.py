numero=int(input("Escreva um numero"))
cont=0
while numero !=0:
    print("Numero errado,digite novamente")
    cont+=1
    numero=int(input("digite novamente"))
    continue
print("Numero correto")
print(f"Você digitou outros {cont} numeros")   