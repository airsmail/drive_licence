

isim=(input("isimgiriniz: "))

yas=int(input("yasiniz: "))

egitim_durumu=(input("egitim durumunuzu giriniz: "))


if yas >= 18  and egitim_durumu == "lise" or "universite":
    print("yasiniz ve egitim durumunuz ehliyet almak icin uygundur.")

elif yas < 18 : 
    print("yasiniz ehliyet almak icin uygun değildir.")    

elif egitim_durumu != "lise" or "universite":
    print("egitim durumunuz uygun degildir.")

else:
    print("yasiniz yada egitim durumunuz uygun degildir.") 
