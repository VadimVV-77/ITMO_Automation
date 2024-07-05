a=[5,10,15,29,25,30,35,40]
# a[2]=15
print("a[2]=",a[2])
#a[0:3]=[5,10,15]
print("a[0:3]=",a[0:3])
# изменение элемента
b=[11,12,13]
b[2]=4
print(b)

test_list=['один','два','три','четыре', 'пять']
#цикл
for elem in test_list:
    print(elem)

# длина списка
print(len(test_list))

# дополнеие списка
test_list.append('шесть')
print(test_list)

test_list.append(7)
print(test_list)

test_list.append(True)
print(test_list)