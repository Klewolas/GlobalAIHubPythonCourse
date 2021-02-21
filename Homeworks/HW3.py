def prime_first(number): #gerekli işlemlerden sonra bulunan sayı asal ve 500'den küçükse yazdıran fonksiyon.
    kontrol = False
    for j in range(2,number):
       if (number % j) == 0:  
           break
    else:
        kontrol = True
    if kontrol == True and i < 500:
        print(number)

def prime_second(number): #gerekli işlemlerden sonra bulunan sayı asal ve 500'den büyükse yazdıran fonksiyon.
    kontrol = False
    for j in range(2,number):
       if (number % j) == 0:  
           break
    else:
        kontrol = True
    if kontrol == True and i >= 500:
        print(number)

for i in range(2,1000): #2 fonksiyonada for ile 1000'e kadar olan sayıları yolladığımız for döngüsü.
    prime_first(i)
    prime_second(i)
