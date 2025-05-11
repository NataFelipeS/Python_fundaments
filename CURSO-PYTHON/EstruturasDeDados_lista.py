empty_list = []
print(empty_list)

numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[4])
print(numbers[-1])
print(numbers[2])

names = ["DANIEL", "CARLOS", "CHAMA", "ROGERIO"]

print(names)
print(names[1])
print(names[2])

mixed = [1, "Carlos", 3.14, True]
print(mixed)
print(mixed[0])
print(mixed[2])
print(mixed[1])
print(mixed[3])

list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
print(list_of_lists)
print(list_of_lists[2])
print(list_of_lists[1])
print(list_of_lists[1][-1])
print(list_of_lists[1][1])

# Adicionar itens na lista, append() adiciona um item no final da lista
print(names)
names.append("Eduardo")
print(names)

# Removendo itens de uma lista, pop() remove o último item da lista
print(names)
print(names.pop(1))
print(names)

# remove() remove o primeiro item da lista
print(names)
names.remove(names[0]) 
# ou
names.remove("ROGERIO")
print(names)

# del remove um item da lista pelo índice
print(names)
del names[0]
print(names)

# Limpar lista, clear() remove tudo da lista

print(names)
print(names.clear())
print(names)

# Ordenar lista, sort()
numbers = [5,2,1,8,4,3]
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)






