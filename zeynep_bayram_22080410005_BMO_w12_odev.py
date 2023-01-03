def notekleme():
    #fonksiyon tanimladim
    x=0
     #bir x degeri tanimlayip olusturdugumuz sozlukteki değerleri siraladik
    for x in range(len(sinav_sonuc['vize'])):
        #bir döngü olusturup geçme notunu hesapladık
        vize=sinav_sonuc['vize'][x]
        final=sinav_sonuc['Final'][x]
        gec=(vize*0.3)+(final*0.7)
        #geçme notunu sınav_sonuc sozlugune ekledik
        sinav_sonuc['gecmenotu'].append(gec)
        #kullanıcıdan istenen degrleri aldık ve sozluge atadık
    Z=input("isim griniz=")
    sinav_sonuc['isim'].append(Z)
    cinsiyet=input("cinsiyet giriniz=(E/K):")
    sinav_sonuc['cinsiyet'].append(cinsiyet)
    vize=int(input("vize notu giriniz:"))
    final=int(input("final notu giriniz:"))
    sinav_sonuc['vize'].append(vize)
    sinav_sonuc['Final'].append(final)
    gec=(vize*0.3)+(final*0.7)
    sinav_sonuc['gecmenotu'].append(gec)
#sınav_sonuc adlı sozluk olusturduk ve tabloyu sınav_sonuc sozlugunda tanımladık
sinav_sonuc = {'isim':['Ayşe K.','Ahmet M.','Nuri C.','Nawar T.','Suzan T.','Ala B.'],
'cinsiyet':['K','E','E','E','K','K'] ,
'vize':[80,60,77,25,36,75],
'Final':[90,50,53,100,98,66],
'gecmenotu':[]}

#fonksiyonu çagırdık iki kere çagırdık çunku iki kullanıcı istemişsiniz
notekleme()
notekleme()
#print ile ekrana yazdık 

print(sinav_sonuc)
                                                        #   E N D   #