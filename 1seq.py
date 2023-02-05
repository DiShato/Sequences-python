list_new = []
len_list = input('введите ко-во элементов списка : ')

for i in range(1, int(len_list)+1):
    element = input('введите элемент {} : '.format(i) )
    list_new.append(element)

list_new.sort()
print('сортируем элементы : ', list_new)