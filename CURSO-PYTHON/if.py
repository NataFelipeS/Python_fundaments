age = int(input("Digite sua idade: "))

if age > 0 and age < 18:
    print("Menor de idade")
elif age >= 18 and age < 150:
    print("Maior de idade")
else:
   print("idade invalida")    
