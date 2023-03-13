import json
import csv
import datetime
from prettytable import PrettyTable

# Ürün bilgilerinin olduğu JSON dosyası
with open("bilgiler.json", "r") as f:
    veri = json.load(f)

print(open("logo.txt", "r").read())  # Pizza Logosu

x = PrettyTable()  # Pizza PrettyTable oluşturma
y = PrettyTable()  # SOS PrettyTable oluşturma

# PrettyTable Pizza Menüsü
x.field_names = ["Pizza Kodu", "Pizza Adı", "Fiyat"]

x.align["Pizza Kodu"] = "c"
x.align["Pizza Adı"] = "l"
x.align["Fiyat"] = "l"

# PrettyTable Pizza Menüsü
for i in range(1, len(veri["pizzaBilgileri"])+1):
    x.add_row([veri["pizzaBilgileri"][str(i)][0]["idBilgisi"], veri["pizzaBilgileri"][str(
        i)][0]["pizzaAdi"], veri["pizzaBilgileri"][str(i)][0]["pizzaFiyat"]])
print(x)  # PrettyTable Pizza tablosunu yazdırma

pizzaTuru = input("Pizza numarasını giriniz: ")  # Pizza bilgisini öğrenme

# PrettyTable Sos Menüsü
y.field_names = [" Sos Kodu ", "Pizza Adı", "Fiyat"]
for i in range(1, len(veri["sosBilgileri"])+1):
    y.add_row([veri["sosBilgileri"][str(i)][0]["idBilgisi"], veri["sosBilgileri"][str(
        i)][0]["sosAdi"], veri["sosBilgileri"][str(i)][0]["sosFiyat"]])
print(y)  # PrettyTable Sos tablosunu yazdırma

sosTuru = input("Sos numarasını giriniz: ")  # Sos bilgisini öğrenme


class Pizza:  # Üst pizza sınıfı
    def __init__(self, urunBilgisi, urunFiyati):
        self.urunBilgisi = urunBilgisi
        self.urunFiyati = urunFiyati

    def get_urunBilgisi(self):
        return self.urunBilgisi

    def get_urunFiyati(self):
        return self.urunFiyati


class PizzaTuru(Pizza):  # Alt pizza sınıfı
    def __init__(self):
        super().__init__(veri["pizzaBilgileri"][str(
            pizzaTuru)][0]["pizzaAdi"], veri["pizzaBilgileri"][str(pizzaTuru)][0]["pizzaFiyat"])


class Soslar(Pizza):  # Üst sos sınıfı
    def __init__(self, sosBilgisi, urunBilgisi, urunFiyati):
        super().__init__(urunBilgisi, urunFiyati)
        self.sosBilgisi = sosBilgisi

    def get_urunFiyati(self):
        return self.sosBilgisi.get_urunFiyati() + super().get_urunFiyati()

    def get_urunBilgisi(self):
        return super().get_urunBilgisi() + ' ' + self.sosBilgisi.get_urunBilgisi()


class SosBilgileri(Soslar):  # Alt sos sınıfı
    def __init__(self, sosBilgisi):
        super().__init__(sosBilgisi, 'Zeytinli', 5.0)


pizzaBilgileri = PizzaTuru()
siparisOzeti = f"{SosBilgileri(pizzaBilgileri).get_urunBilgisi()} - Toplam Ücret: {SosBilgileri(pizzaBilgileri).get_urunFiyati()}TL"
print("Sipariş Özeti:", siparisOzeti)
print("Ödeme adımına yönlendiriliyorsunuz....")
adiniz = input("Adınızı yazınız: ")
tcNo = input("TC Kimlik bilgileriniz girinizi: ")
kKartiBilgiler = input("Kredi kartı bilginizi girinizi: ")
kKartiSifresi = input("Kredi kartı şifrenizi girinizi: ")
siparisZamani = datetime.datetime.now()
print("Siparişiniz onaylandı, siparişinizi en kısa sürede size ulaştıracağız. İyi günler.")

with open("SiparisBilgileri.csv", "a", newline="", encoding="utf-8") as dosya:
    yazilacak = csv.writer(dosya)
    yazilacak.writerow([adiniz, tcNo, kKartiBilgiler, kKartiSifresi, SosBilgileri(
        pizzaBilgileri).get_urunBilgisi(), SosBilgileri(pizzaBilgileri).get_urunFiyati(), siparisZamani])
