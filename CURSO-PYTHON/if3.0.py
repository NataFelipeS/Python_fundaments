regra = input("Digite seu cargo: ")

if regra == "admin":
    print("Acesso total")
elif regra == "user":
    print("Acesso função")
elif regra == "guest":
    print("Visualização")
else:
    print("Cargo não reconhecido")            