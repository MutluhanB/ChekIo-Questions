

## Mutluhan Boz 24.10.2017
import random 
L=[]
lu=0 #ortalamaya uzaklık
count = 0 #deneme sayısı
u=0  #en uyumsuz eleman
i=0
j = int(input("Kaç adet sayi girmek istiyorsunuz ?(10 ve sonrası için uzun sürebilir) : "))
while len(L) < j :
    x=int(input("Bir tamsayi giriniz: "))
    L.append(x)
while L != sorted(L) :
    random.shuffle(L)      #Bogo sort : L,düzenlenmiş L haline gelene kadar rastgele olarak L yi karıştırır.
    count += 1           
ortalama=(sum(L)/len(L))
while i < len(L) :                    #Listenin tüm elemanlarının kontrolü için döngü.
        if (abs(L[i]-ortalama)>lu) :
            lu=abs(L[i]-ortalama)         # L'nin her elemanını ortalamadan çıkartıp mutlak değer içine alır.
            u = L[i]                      # Ortalamaya uzaklığı en uzak olan sayıyı ve ortalamaya uzaklığı değişkenlere atar.
        i+=1         
print("Düzenlenmiş Hali", L)
print("Toplam deneme sayisi", count)
print("-------------------------")
print("En uyumsuz eleman",u)                              #çıktılar
print("ort",ortalama)
print("En uyumsuz elemanın ortalamadan uzaklığı",lu)
