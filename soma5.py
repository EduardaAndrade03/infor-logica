
soma=0
num=int(input("fala um numero"))
for n in range(4):
    soma+=num
    num=int(input("diz outro"))
    
soma+=num
print(soma)