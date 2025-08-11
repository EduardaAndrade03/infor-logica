media=0
nota3=float(input("Me de uma nota"))
for n in range(2):
    media+=nota3
    nota3=float(input("me da outra"))
media+=nota3
media/=3
if media>=7:
    print("aprovado")
elif media<7:
    print("reprovado")
    