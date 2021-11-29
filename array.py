array_list = [1,2,3,4,5,6,7,8,9]


#Mengganti item
array_list[3] = 111

#Menambah item
array_list.append(20000)

#Menghapus item sesuai isi item bukan index
array_list.remove(3)

#sort
array_list.sort(reverse=True)

#Menambah item pada list
array_list.insert(3, 2)

#Menambah list pada list
array_list2 = [11,22,33,44]
data = (array_list + array_list2)

print(len(data))





# set
# array_set = {1,2,3,4,5}
# print(array_set)

# tuple
tuple_array = (3,2,5)

#jika item cuma 1 kasih koma di ujung jika tidak maka
# akan dianggap tipe data biasa
tuple_array2 = (3,)

print(tuple_array2)
print(type(tuple_array))