#Program perkalian matriks dengan for
print ('Program perkalian matriks [A]*[B]=[C]')

from numpy import *
A = array([[1,2,3],\
           [5,6,7],\
           [8,9,10],\
           [11,12,13],\
               ]) # A berukuran 4x3
B = array([[1,2,3,4],\
           [5,6,7,8],\
           [9,10,11,12]]) # B berukuran 3x4

print(A*B)

# n=4 # jumlah baris matrik A
# m=4 # jumlah kolom matrik B
# p=3 # jumlah kolom matrik A sekaligus jumlah baris matrik B
# C = zeros((n,m))
# for i in range(0,n):
#     for j in range(0,m):
#         for k in range(0,p):
#             C[i][j]=C[i][j]+A[i][k]*B[k][j]

# print ()
# print ('matriks A')
# print (A)
# print ()
# print ('matriks B')
# print (B)
# print ()
# print ('matriks C (hasil)')
# print (C)