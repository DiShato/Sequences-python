list_new_1 = input('Введите элементы списка1 через запятую, точку или точку с запятой:  ')
list_new_2 = input('Введите элементы списка1 через запятую, точку или точку с запятой:  ')

list_split = ['.', ',', ';']

for i in range(len(list_split )):

 if list_split[i] in list_new_1:
     list_new_1 = list(list_new_1.split(list_split[i]))

for i in range(len(list_split)):
 if list_split[i] in list_new_2:
     list_new_2 = list(list_new_2.split(list_split[i]))

list_new_1 = [x for x in list_new_1 if x not in list_split]
list_new_2 = [x for x in list_new_2 if x not in list_split]

print('Результат : ', set([x for x in (list_new_1) if x not in list_new_2]))
