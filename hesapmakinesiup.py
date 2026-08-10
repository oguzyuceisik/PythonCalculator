print("!!Hesap Makinesine Hoş Geldiniz!!")

def islem(sayi1,sayi2,isaret):
    if isaret =="+":
        sonuc = sayi1+sayi2
        return sonuc
    elif isaret =="-":
        sonuc = sayi1-sayi2
        return sonuc
    elif isaret =="*":
        sonuc = sayi1*sayi2
        return sonuc
    elif isaret =="/":
        sonuc = sayi1/sayi2
        return sonuc
    else:
        return "Geçersiz İşlem girildi"


def hesap():
    icerik = []
    devammi = True
    while devammi:
        sayi = input("Sayı giriniz(Sonlandırmak için " + "'son'" +" yazınız): ")
        if sayi != "son":
            sayi = float(sayi)
            icerik.append(sayi)
        else:
            icerik.pop()
            devammi = False
            break
        islems = input("İslemi Giriniz: ")
        if islems == "+" or islems =="-" or islems == "*" or islems =="/":
            icerik.append(islems)
        else:
            print("Geçersiz Değer Girildi")
            devammi = False
    while len(icerik)!=1:
        while "*" in icerik:
            sira = icerik.index("*")
            sonuc = islem(icerik[sira - 1],icerik[sira + 1],icerik[sira])
            icerik[sira -1 : sira +2] = [sonuc]
        while "/" in icerik:
            sira = icerik.index("/")
            sonuc = islem(icerik[sira - 1],icerik[sira + 1],icerik[sira])
            icerik[sira -1 : sira +2] = [sonuc]
        while "+" in icerik:
            sira = icerik.index("+")
            sonuc = islem(icerik[sira - 1],icerik[sira + 1],icerik[sira])
            icerik[sira -1 : sira +2] = [sonuc]
        while "-" in icerik:
            sira = icerik.index("-")
            sonuc = islem(icerik[sira - 1],icerik[sira + 1],icerik[sira])
            icerik[sira -1 : sira +2] = [sonuc]
    else:
        print(f"Sonucunuz: {icerik}")

hesap()