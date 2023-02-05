#примеры с методами и списками
name_exp = 'список'
list_metod = ['4_cat','1_dog', '3_lemon', '2_book', '5_tree']

print('объявленный {} игрушек :'.format(name_exp ), list_metod)

#методы со списками
list_metod.append('6') # добавляем элемент
print('1. добавляем элемент : ', list_metod)

list_metod.remove('6') # удаляем элемент
print('2. удаляем элемент : ', list_metod)

# считаем кол-во элементов x
print('3. считаем кол-во элементов 6: ', list_metod.count('6'))

# сортируем элементы
list_metod.sort()
print('4. сортируем элементы : ', list_metod)

# отбираем элемент по индексу
print('5. отбираем элемент по индексу 2 : ', list_metod[2])

print()

#примеры с методами и словарями
name_exp = 'словарь'
dict_metod = {4 :'cat',
              1 :['dog','keys'],
              3 :'lemon',
              2 :'book',
              5 :'tree'}

print('объявленный {} игрушек : '.format(name_exp ), dict_metod)

#методы со списками
dict_metod[6] = 'car' # добавляем элемент
print('1. добавляем элемент : ', dict_metod)

del dict_metod[6] # удаляем элемент
print('2. удаляем элемент : ', dict_metod)

# считаем кол-во элементов
print('3. считаем кол-во элементов по ключу 1 и игрушке dog: ', dict_metod.get(1).count('dog'))

# сортируем элементы
dict_metod_sort = list(dict_metod.keys())
dict_metod_sort.sort()
print('4. сортируем элементы ключа: ', dict_metod_sort)

# отбираем элемент
print('5. отбираем элемент по ключу 1: ', dict_metod.get(1))

print()

# примеры со строками
name_exp = 'строка'
str_metod = '4_cat_8'

print('объявленная {} :'.format(name_exp ), str_metod)

#методы со списками
str_metod = str_metod + '6' # добавляем элемент
print('1. добавляем элемент : ', str_metod)

str_metod = str_metod.replace('6','') # удаляем элемент
print('2. удаляем элемент : ', str_metod)

# считаем кол-во элементов x
print('3. считаем кол-во элементов через список: ', len(str_metod))

# сортируем элементы
str_metod_sort = list(str_metod)
str_metod_sort.sort()
print('4. сортируем разделенные элементы списка: ', str_metod_sort)

# отбираем элемент по индексу
print('5. отбираем элемент по индексу 2 : ', str_metod[2])

print()

#примеры с методами и множествами
name_exp = 'множество'
set1_metod = {'4_cat','1_dog', '5_tree'}

print('объявленно {}  игрушек :'.format(name_exp ), set1_metod)

#методы со списками
set1_metod.add('2564')
print('1. добавляем элементы : ',set1_metod)

# удаляем элемент
set1_metod.remove('2564')
print('2. отбираем значение по срезам(удаляем элементы) : ', set1_metod)

# считаем кол-во элементов x
print('3. считаем кол-во элементов множества: ', len(set1_metod))

# сортируем элементы
# элементы сортируются по умолчанию

# отбираем элемент по индексу
print('5. отбираем элементы по индексу через список 2 : ', list(set1_metod)[2] )
