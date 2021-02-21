info = {}
studentsName = []
studentsGrades = []

for i in range(5): #öğrencilerin bilgileri kullanıcıdan alınıyor.
    studentsName.append(input("Öğrencinin adını giriniz:"))
    studentsName.append(input("Öğrencinin soyadını giriniz:"))
    studentsGrades.append(int(input("Öğrencinin vize notunu giriniz:")))
    studentsGrades.append(int(input("Öğrencinin ödev notunu giriniz:")))
    studentsGrades.append(int(input("Öğrencinin final notunu giriniz:")))
    info[studentsName[0] + " " + studentsName[1]] = studentsGrades.copy()
    studentsName.clear()
    studentsGrades.clear()

ortalama = 0
ortalamalar = {}
for i in info.items(): #öğrencilerin ortalamasının alındığı for döngüsü.
    ortalama = sum(i[1])/len(i[1])
    ortalamalar[i[0]] = ortalama

ortalamalarSirali = sorted(ortalamalar.items(), key=lambda x: x[1], reverse=True) #ortalamalara göre öğrencileri sıralamak için.

enIyiOgrenci = ' '
maxNot = 0
print("\n")
for i in ortalamalarSirali: #en yüksek ortalamaya sahip öğrencinin bulunması ve ekrana öğrencilerin yazdırılması.
    print(str(i[0]) + " ortalamanız : " + str(i[1]))
    if i[1] > maxNot:
        maxNot = i[1]
        enIyiOgrenci = i[0]
   
print(enIyiOgrenci + " Tebrikler!!")