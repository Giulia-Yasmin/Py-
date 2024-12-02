x= int(input("Sua idade: "))
if x<=15: 
    print("não pode votar")
elif x==16:
    print("pode votar de maneira opcional")
elif x==17:
    print("pode votar de maneira opcional")
elif x<60:
    print("já pode votar de maneira obrigatória")
else:
    print("pode votar de maneira opcional")