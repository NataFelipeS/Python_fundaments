# Dicionários são coleções de itens em uma ordem especifica. Cada item é composto por um par chave-valor.
# A chavee é um identificador único e o valor é o item associado á chave.

# Dicionários são definidos por chaves {} e os itens são separados por vírgula.
# Cada item é comósto por uma chave ee um valor, separados por dois pontos :

# Dicionários são mutáveis, ou seja, os itens podem ser alterados, adicionados ou removidos.

# Dicionários podem conteer qualquer tipo de dado, inclusive outros dicionários

empyt_dict = {}
print(empyt_dict)

# Dicionário de números, onde as chaves são números inteiros e os valores são strings
numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
print(numbers)

# Dicionário de strings, onde as chaves são strings e os valores são números inteiros
names = {"Natã": 1, "Marcos": 2, "Micael": 3, "Vânia": 4}
print(names)

user = {"name": "Natã", "age": 21, "email": "nfelipe05@gmail.com", "phone": "123456789"}
print(user)
print(user["name"])
print(user["age"])
print(user["email"])
print(user["phone"])

# Adicionando itens a um dicionário
# Basta atribuir um valor a uma chave que não existe

print(user)
user["city"] = "São Paulo"
print(user)

# Modificar um valor de um dicionário
# Basta atribuir um novo valor a uma chave que já existe
print(user)
user["age"] = 22
print(user)

# Removando itens de um dicionário
# O método pop() remove o item associado a uma chave
print(user.pop("age"))
print(user)

# O método pop() pode receber um seegundo argumento, que é retornado caso a chave não exista
# user["age"] = 25
print(user.pop("age", "Chave não existe"))
print(user)

# O método popitem() remove o último item do dicionário
print(user)
print(user.popitem())
print(user)