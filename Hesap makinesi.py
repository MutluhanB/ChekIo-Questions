#%% Mutluhan Boz 10.10.2017 
def toplama(x,y) :
    sonuc=x+y
    return sonuc 
def cıkartma(x,y) :
    sonuc=x-y
    return sonuc 
def carpma(x,y) :
    sonuc=x*y 
    return sonuc                      ##İşlemler için fonksiyonlar
def bolme(x,y) :
    sonuc = x/y 
    return sonuc 
def mod(x,y):
    sonuc=x%y
    return sonuc 

print("Toplama için +")
print ("Çıkartma için -")
print ("Çarpma için *")                                             ##Menü kısmı
print ("Bölme için /")
print ("Mod alma işlemi için lütfen %")
print ("Çıkış yapmak için lütfen c giriniz.")
seçim=input("Hesap makinesine hoş geldiniz. Lütfen İşlem Seçiniz.")     
if seçim == "c" :
    exit 
elif (seçim != "+" and seçim != "-" and seçim != "*" and seçim != "/" and  seçim !="%") :
 print("Geçersiz bir işlem yapmaya çalıştınız")    
 input("Çıkmak için bir tuşa basınız")                                             ##c seçildiğinde çıkış yapmak için if else döngüsü
else :
 say1=int(input("Birinci Sayiyi Girin: "))
 say2=int(input("İkinci Sayiyi Girin"))
 
 if (seçim == "+") :
   işlemdevam = 0
   while işlemdevam != "k" :
       print(toplama(say1,say2+işlemdevam))                             ## işlemlerin devamı veya çıkışı için döngüler hepsinde aynı şekilde.
       devam=int(input("Devam etmek için yeni sayı,çıkmak için 0 giriniz"))
       if devam != 0 :
           işlemdevam+=devam
       else :
           işlemdevam = "k"
 elif (seçim == "-") :
    işlemdevam=0
    while işlemdevam!="k" :                                                
       print (cıkartma(say1,say2+işlemdevam))
       devam=int(input("Devam etmek için yeni sayı, çıkmak için 0 giriniz"))
       if devam != 0 :
           işlemdevam+=devam
       else :
           işlemdevam = "k"
     
 elif (seçim == "*") :
    işlemdevam = 1
    while işlemdevam !="k" :
       print (carpma(say1,say2)*işlemdevam)
       devam=float(input("Devam etmek için yeni sayı, çıkmak için 0 giriniz"))
       if devam !=0 :
           işlemdevam=işlemdevam*devam
       else :
           işlemdevam ="k" 
 elif (seçim =="/") :
    işlemdevam = 1
    while işlemdevam != "k" : 
       print (bolme(say1,say2)/işlemdevam)                                         ##Bölme işleminde devam/çıkış döngüsü diğerlerinden biraz daha farklı.
       devam=float(input("Devam etmek için yeni sayı, çıkmak için 0 giriniz"))
       if devam != 0 :
           say1=bolme(say1,say2)
           say2=devam
       else :
           işlemdevam = "k"
 elif (seçim =="%") :
    print (mod(say1,say2))
    

