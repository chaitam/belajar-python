bil_1 = int(input("Masukkan bilangan 11 : "))
bil_2 = int(input("Masukkan bilangan 12 : "))
bil_3 = int(input("Masukkan bilangan 13 : "))
bil_4 = int(input("Masukkan bilangan 14 : "))
bil_5 = int(input("Masukkan bilangan 15 : "))
bil_6 = int(input("Masukkan bilangan 21 : "))
bil_7 = int(input("Masukkan bilangan 22 : "))
bil_8 = int(input("Masukkan bilangan 23 : "))
bil_9 = int(input("Masukkan bilangan 24 : "))
bil_10 = int(input("Masukkan bilangan 25 : "))

mat1 = int(input("Masukkan bilangan matriks k 11 : "))
mat2 = int(input("Masukkan bilangan matriks k 12 : "))
mat3 = int(input("Masukkan bilangan matriks k 21 : "))
mat4 = int(input("Masukkan bilangan matriks k 22 : "))

alfab = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
         "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

hasilmod1 = ((mat1 * bil_1) + (mat2 * bil_6)) % 26
hasilmod2 = ((mat1 * bil_2) + (mat2 * bil_7)) % 26
hasilmod3 = ((mat1 * bil_3) + (mat2 * bil_8)) % 26
hasilmod4 = ((mat1 * bil_4) + (mat2 * bil_9)) % 26
hasilmod5 = ((mat1 * bil_5) + (mat2 * bil_10)) % 26
hasilmod6 = ((mat3 * bil_1) + (mat4 * bil_6)) % 26
hasilmod7 = ((mat3 * bil_2) + (mat4 * bil_7)) % 26
hasilmod8 = ((mat3 * bil_3) + (mat4 * bil_8)) % 26
hasilmod9 = ((mat3 * bil_4) + (mat4 * bil_9)) % 26
hasilmod10 = ((mat3 * bil_5) + (mat4 * bil_10)) % 26

print("------------------Enkrip-------------------")
print("hasil Perkalian Enkrip")
print("%s+%s %s+%s %s+%s %s+%s %s+%s" % ((mat1 * bil_1), (mat2 * bil_6), (mat1 * bil_2), (mat2 *
      bil_7), (mat1 * bil_3), (mat2 * bil_8), (mat1 * bil_4), (mat2 * bil_9), (mat1 * bil_5), (mat2 * bil_10)))
print("%s+%s %s+%s %s+%s %s+%s %s+%s" % ((mat3 * bil_1), (mat4 * bil_6), (mat3 * bil_2), (mat4 *
      bil_7), (mat3 * bil_3), (mat4 * bil_8), (mat3 * bil_4), (mat4 * bil_9), (mat3 * bil_5), (mat4 * bil_10)))

print("hasil Penjumlahan Enkrip")
print("%s %s %s %s %s" % (((mat1 * bil_1) + (mat2 * bil_6)), ((mat1 * bil_2) + (mat2 * bil_7)),
      ((mat1 * bil_3) + (mat2 * bil_8)), ((mat1 * bil_4) + (mat2 * bil_9)), ((mat1 * bil_5) + (mat2 * bil_10))))
print("%s %s %s %s %s" % (((mat3 * bil_1) + (mat4 * bil_6)), ((mat3 * bil_2) + (mat4 * bil_7)),
      ((mat3 * bil_3) + (mat4 * bil_8)), ((mat3 * bil_4) + (mat4 * bil_9)), ((mat3 * bil_5) + (mat4 * bil_10))))


print("Hasil Modulus Enkrip")
print("%s %s %s %s %s" % (hasilmod1, hasilmod2,
                          hasilmod3, hasilmod4, hasilmod5))
print("%s %s %s %s %s" % (hasilmod6, hasilmod7,
      hasilmod8, hasilmod9, hasilmod10))

print("Hasil Modulus Enkrip Alphabet")
print("%s %s %s %s %s %s %s %s %s %s" % (alfab[hasilmod1], alfab[hasilmod2],
                                         alfab[hasilmod3], alfab[hasilmod4], alfab[hasilmod5], alfab[hasilmod6], alfab[hasilmod7],
      alfab[hasilmod8], alfab[hasilmod9], alfab[hasilmod10]))


print("------------------Deskrip-------------------")
print("hasil Perkalian Deskrip")
print("%s+%s %s+%s %s+%s %s+%s %s+%s" % ((mat4 * hasilmod1), (-mat2 * hasilmod6), (mat4 * hasilmod2), (-mat2 *
      hasilmod7), (mat4 * hasilmod3), (-mat2 * hasilmod8), (mat4 * hasilmod4), (-mat2 * hasilmod9), (mat4 * hasilmod5), (-mat2 * hasilmod10)))


print("%s+%s %s+%s %s+%s %s+%s %s+%s" % ((-mat3 * hasilmod1), (mat1 * hasilmod6), (-mat3 * hasilmod2), (mat1 *
      hasilmod7), (-mat3 * hasilmod3), (mat1 * hasilmod8), (-mat3 * hasilmod4), (mat1 * hasilmod9), (-mat3 * hasilmod5), (mat1 * hasilmod10)))

print("hasil Penjumlahan Deskrip")
print("%s %s %s %s %s" % (((mat4 * hasilmod1) + (-mat2 * hasilmod6)), ((mat4 * hasilmod2) + (-mat2 *
      hasilmod7)), ((mat4 * hasilmod3) + (-mat2 * hasilmod8)), ((mat4 * hasilmod4) + (-mat2 * hasilmod9)), ((mat4 * hasilmod5) + (-mat2 * hasilmod10))))

print("%s %s %s %s %s" % (((-mat3 * hasilmod1) + (mat1 * hasilmod6)), ((-mat3 * hasilmod2) + (mat1 *
      hasilmod7)), ((-mat3 * hasilmod3) + (mat1 * hasilmod8)), ((-mat3 * hasilmod4) + (mat1 * hasilmod9)), ((-mat3 * hasilmod5) + (mat1 * hasilmod10))))


print("Hasil Modulus Deskrip")
hasilmodulus1 = ((mat4 * hasilmod1) + (-mat2 * hasilmod6)) % 26
hasilmodulus2 = ((mat4 * hasilmod2) + (-mat2 * hasilmod7)) % 26
hasilmodulus3 = ((mat4 * hasilmod3) + (-mat2 * hasilmod8)) % 26
hasilmodulus4 = ((mat4 * hasilmod4) + (-mat2 * hasilmod9)) % 26
hasilmodulus5 = ((mat4 * hasilmod5) + (-mat2 * hasilmod10)) % 26
hasilmodulus6 = ((-mat3 * hasilmod1) + (mat1 * hasilmod6)) % 26
hasilmodulus7 = ((-mat3 * hasilmod2) + (mat1 * hasilmod7)) % 26
hasilmodulus8 = ((-mat3 * hasilmod3) + (mat1 * hasilmod8)) % 26
hasilmodulus9 = ((-mat3 * hasilmod4) + (mat1 * hasilmod9)) % 26
hasilmodulus10 = ((-mat3 * hasilmod5) + (mat1 * hasilmod10)) % 26


print("%s %s %s %s %s" % ((((mat4 * hasilmod1) + (-mat2 * hasilmod6)) % 26), (((mat4 * hasilmod2) + (-mat2 *
      hasilmod7)) % 26),
                          (((mat4 * hasilmod3) + (-mat2 * hasilmod8)) % 26), (((mat4 * hasilmod4) + (-mat2 * hasilmod9)) % 26), (((mat4 * hasilmod5) + (-mat2 * hasilmod10)) % 26)))

print("%s %s %s %s %s" % ((((-mat3 * hasilmod1) + (mat1 * hasilmod6)) % 26), (((-mat3 * hasilmod2) + (mat1 *
      hasilmod7)) % 26),
      (((-mat3 * hasilmod3) + (mat1 * hasilmod8)) % 26), (((-mat3 * hasilmod4) + (mat1 * hasilmod9)) % 26), (((-mat3 * hasilmod5) + (mat1 * hasilmod10)) % 26)))


print("Hasil Modulus Deskrip Alphabet")
print("%s %s %s %s %s %s %s %s %s %s" % (alfab[hasilmodulus1], alfab[hasilmodulus2],
                                         alfab[hasilmodulus3], alfab[hasilmodulus4], alfab[hasilmodulus5], alfab[hasilmodulus6], alfab[hasilmodulus7],
      alfab[hasilmodulus8], alfab[hasilmodulus9], alfab[hasilmodulus10]))
