# menentukan suatu bilangan genap atau ganjil

def nilaiTerbesar(nilaiA, nilaiB):
    if(nilaiA > nilaiB):
        print("%i adalah nilai terbesar" % nilaiA)
    else:
        print('%i adalah nilai terbesar' % nilaiB)


nilaiA = int(input("Masukkan Nilai A:"))
nilaiB = int(input("Masukkan Nilai B:"))
nilaiTerbesar(nilaiA, nilaiB)


def ganjilGenap(x):
    if(x % 2 == 0):
        print("%i adalah genap" % x)
    else:
        print("%i adalah ganjil" % x)


nilai1 = int(input('Masukkan nilai : '))
ganjilGenap(nilai1)


def rumusPersegi(p, l):
    print(p * l)


panjang = int(input('masukkan besaran panjang : '))
lebar = int(input('masukkan besaran lebar : '))
rumusPersegi(panjang, lebar)


def volumeBalok(p, l, t):
    print(p * l * t)


p = int(input('masukkan besaran panjang : '))
l = int(input('masukkan besaran lebar : '))
t = int(input('masukkan besaran tinggi : '))
volumeBalok(p, l, t)


def luasSegitiga(a, t):
    print(a * t * (1/2))


a = float(input('masukkan besaran alas : '))
t = float(input('masukkan besaran tinggi : '))
luasSegitiga(a, t)
