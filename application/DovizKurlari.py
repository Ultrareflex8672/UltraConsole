import xml.etree.ElementTree as ET
from urllib.request import urlopen

class DovizKurlari():
    def __init__(self):
        self.son = {}
        self.Kur_Liste = []

    def __veri_update(self, zaman="Bugun"):
        try:
            # Bugün veya belirli bir tarih için URL seçimi
            if zaman == "Bugun":
                self.url = "http://www.tcmb.gov.tr/kurlar/today.xml"
            else:
                self.url = zaman

            # URL'den XML verisini al
            tree = ET.parse(urlopen(self.url))
            root = tree.getroot()

            # Veriyi temizle ve güncelle
            self.son = {}
            self.Kur_Liste = []

            for kurlars in root.findall('Currency'):
                Kod = kurlars.get('Kod')
                Unit = kurlars.find('Unit').text
                isim = kurlars.find('Isim').text
                CurrencyName = kurlars.find('CurrencyName').text
                ForexBuying = kurlars.find('ForexBuying').text
                ForexSelling = kurlars.find('ForexSelling').text
                BanknoteBuying = kurlars.find('BanknoteBuying').text
                BanknoteSelling = kurlars.find('BanknoteSelling').text
                CrossRateUSD = kurlars.find('CrossRateUSD').text

                # Listeye ekle
                self.Kur_Liste.append(Kod)
                self.son[Kod] = { 
                    "Kod": Kod,
                    "isim": isim,
                    "CurrencyName": CurrencyName,
                    "Unit": Unit,
                    "ForexBuying": ForexBuying,
                    "ForexSelling": ForexSelling,
                    "BanknoteBuying": BanknoteBuying,
                    "BanknoteSelling": BanknoteSelling,
                    "CrossRateUSD": CrossRateUSD
                }
            
            return self.son

        except Exception as e:
            print(f"Hata: {e}")
            return "HATA"

    def DegerSor(self, *sor):
        # Veriyi güncelle
        self.__veri_update()

        # Parametre verilmediyse tüm veriyi döndür
        if not sor:
            return self.son
        else:
            # Verilen parametreyle veriyi döndür
            try:
                return self.son.get(sor[0]).get(sor[1])
            except KeyError:
                return "Geçersiz kod veya parametre."

    def Arsiv(self, Gun, Ay, Yil, *sor):
        url = self.__Url_Yap(Gun, Ay, Yil)
        a = self.__veri_update(url)

        if not sor:
            if a == "HATA":
                return {"Hata": "TATIL GUNU"}
            return self.son
        else:
            if a == "HATA":
                return "Tatil Gunu"
            else:
                try:
                    return self.son.get(sor[0]).get(sor[1])
                except KeyError:
                    return "Geçersiz kod veya parametre."

    def Arsiv_tarih(self, Tarih="", *sor):
        # Tarih formatını çöz
        takvim = Tarih.split(".")
        Gun = takvim[0]
        Ay = takvim[1]
        Yil = takvim[2]

        # Veriyi güncelle
        a = self.__veri_update(self.__Url_Yap(Gun, Ay, Yil))
        if not sor:
            if a == "HATA":
                return {"Hata": "TATIL GUNU"}
            return self.son
        else:
            if a == "HATA":
                return "Tatil Gunu"
            else:
                try:
                    return self.son.get(sor[0]).get(sor[1])
                except KeyError:
                    return "Geçersiz kod veya parametre."

    def __Url_Yap(self, Gun, Ay, Yil):
        # URL'yi oluştur
        if len(str(Gun)) == 1:
            Gun = "0" + str(Gun)
        if len(str(Ay)) == 1:
            Ay = "0" + str(Ay)

        return f"http://www.tcmb.gov.tr/kurlar/{Yil}{Ay}/{Gun}{Ay}{Yil}.xml"

