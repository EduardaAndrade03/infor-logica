senha=int(1234)
sen2= int(input("digite a senha em numero"))
while sen2 != senha:
    print("senha incorreta")
    sen2= int(input("digite novmente"))
    continue
print("senha correta")