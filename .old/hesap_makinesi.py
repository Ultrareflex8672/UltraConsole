class HesapMakinesi:
    def hesap_islemi(self,islem):
        self.soru1 = ""
        self.soru2 = ""
        if islem == 2:
            self.soru1 = int(input("1. Sayıyı Giriniz: "))
            self.soru2 = int(input("Çıkarılacak Sayıyı Giriniz: "))
        elif islem == 6 or islem == 7:
            self.soru1 = int(input("1. Kenar Uzunluğunu Giriniz: "))
            self.soru2 = int(input("2. Kenar Uzunluğunu Giriniz: "))
        elif islem == 5:
            self.soru1 = int(input("Tabanı Giriniz: "))
            self.soru2 = int(input("Üssü Giriniz: "))
        elif islem == 4:
            self.soru1 = int(input("Bölüneni Giriniz: "))
            self.soru2 = int(input("Böleni Giriniz: "))
        else:
            self.soru1 = int(input("1. Sayıyı Giriniz: "))
            self.soru2 = int(input("2. Sayıyı Giriniz: "))
        self.v1 = self.soru1
        self.v2 = self.soru2
        self.sonuc = 0
        if islem == 1: # islem == 1: toplama
            if isinstance(self.v1, int) and isinstance(self.v2, int):
                self.sonuc = self.v1 + self.v2
            else:
                self.sonuc = "Sadece Sayı Girişi Yapılmalıdır."
            return str(self.sonuc)
        elif islem == 2: # islem == 2: çıkarma
            if isinstance(self.v1, int) and isinstance(self.v2, int):
                self.sonuc = self.v1 - self.v2
            else:
                self.sonuc = "Sadece Sayı Girişi Yapılmalıdır."
            return str(self.sonuc)
        elif islem == 3: # islem == 3: çarpma
            if isinstance(self.v1, int) and isinstance(self.v2, int):
                self.sonuc = self.v1 * self.v2
            else:
                self.sonuc = "Sadece Sayı Girişi Yapılmalıdır."
            return str(self.sonuc)
        elif islem == 4: # islem == 4: bölme
            if isinstance(self.v1, int) and isinstance(self.v2, int):
                self.sonuc = self.v1 / self.v2
            else:
                self.sonuc = "Sadece Sayı Girişi Yapılmalıdır."
            return str(self.sonuc)
        elif islem == 5: # islem == 5: üs alma
            if isinstance(self.v1, int) and isinstance(self.v2, int):
                self.sonuc = 0
                for i in range(self.v2):
                    i = self.v1 * self.v1
                    self.sonuc += i
            else:
                self.sonuc = "Sadece Sayı Girişi Yapılmalıdır."
            return str(self.sonuc)
        elif islem == 6: # islem == 6: kare alanı
            if isinstance(self.v1, int) and isinstance(self.v2, int):
                self.sonuc = self.v1 * self.v2
            else:
                self.sonuc = "Sadece Sayı Girişi Yapılmalıdır."
            return str(self.sonuc)
        elif islem == 7: # islem == 7: karenin çevresi
            if isinstance(self.v1, int) and isinstance(self.v2, int):
                self.sonuc = (self.v1 + self.v2) * 2
            else:
                self.sonuc = "Sadece Sayı Girişi Yapılmalıdır."
            return str(self.sonuc)
        else:
            return "Geçersiz İşlem"
