num = int(input("diz um numero ")) 
fato= num 
apoio=num 

while num > 0: 
    if fato == num: 
        num-=1 
        fato*=num 
        num-=1 
        continue 

    else: fato*=num 
    num-=1 
    continue 

print(f"fatorial de {apoio} é {fato}")


