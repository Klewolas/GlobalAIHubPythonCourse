import random

kontrol = False #asal sayıyı tutan boolean.
primeNumbers = []
for j in range(2,100): #asal sayılar bulunması için for döngüleri.
   for i in range(2,j):
       if (j % i) == 0:  
           break  
   else:
       kontrol = True
   if kontrol == True:
       primeNumbers.append(j)
       kontrol = False
        
matrix = [[0 for i in range(3)] for j in range(3)] #matris oluşturuldu.

for i in range(3): #oluşturulan matrisin içine rastgele asal sayılar atandı.
    for j in range(3):
        matrix[i][j] = primeNumbers[random.randint(0,(len(primeNumbers))-1)]
        
print(matrix)