import math



def D(a, b, c):
    return (b*b) - (4*a*c)


def x1(a, b, D):
    result1 = (-b + math.sqrt(D)) / (2*a)
    result2 = (-b - math.sqrt(D)) / (2*a)

    return "%s, %s" % (result1, result2)

def start():
    a = float(input("Masukkan nilai a : "))
    b = float(input("Masukkan nilai b : "))
    c = float(input("Masukkan nilai c : "))

    if(a > 0):
        d = D(a, b, c)

        if(d >= 0):
            print(x1(a, b, c))
        else:
            print("imaginer")
    else:
        start()


start()
