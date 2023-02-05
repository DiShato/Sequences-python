list_new = input('Введите элементы списка через запятую, точку или точку с запятой:  ')
list_split = ['.', ',', ';']

for i in range(len(list_split )):

 if list_split[i] in list_new:

     list_new = list(list_new.split(list_split[i]))

print([x for x in set(list_new) if x not in list_split ])
