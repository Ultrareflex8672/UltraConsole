class HesapMakinesi:
    def hesap_islemi(self,v1,v2,islem):
        self.sonuc = 0
        if islem == 1: # islem == 1: toplama
            if isinstance(v1, int) and isinstance(v2, int):
                self.sonuc = v1 + v2
            else:
                self.sonuc = "Sadece Sayı Girişi Yapılmalıdır."
            return str(self.sonuc)
        elif islem == 2: # islem == 2: çıkarma
            if isinstance(v1, int) and isinstance(v2, int):
                self.sonuc = v1 - v2
            else:
                self.sonuc = "Sadece Sayı Girişi Yapılmalıdır."
            return str(self.sonuc)
        elif islem == 3: # islem == 3: çarpma
            if isinstance(v1, int) and isinstance(v2, int):
                self.sonuc = v1 * v2
            else:
                self.sonuc = "Sadece Sayı Girişi Yapılmalıdır."
            return str(self.sonuc)
        elif islem == 4: # islem == 4: bölme
            if isinstance(v1, int) and isinstance(v2, int):
                self.sonuc = v1 / v2
            else:
                self.sonuc = "Sadece Sayı Girişi Yapılmalıdır."
            return str(self.sonuc)
        elif islem == 5: # islem == 5: üs alma
            if isinstance(v1, int) and isinstance(v2, int):
                self.sonuc = 0
                for i in range(v2):
                    i = v1 * v1
                    self.sonuc += i
            else:
                self.sonuc = "Sadece Sayı Girişi Yapılmalıdır."
            return str(self.sonuc)
        elif islem == 6: # islem == 6: kare alanı
            if isinstance(v1, int) and isinstance(v2, int):
                self.sonuc = v1 * v2
            else:
                self.sonuc = "Sadece Sayı Girişi Yapılmalıdır."
            return str(self.sonuc)
        elif islem == 7: # islem == 7: karenin çevresi
            if isinstance(v1, int) and isinstance(v2, int):
                self.sonuc = (v1 + v2) * 2
            else:
                self.sonuc = "Sadece Sayı Girişi Yapılmalıdır."
            return str(self.sonuc)
        else:
            return "Geçersiz İşlem"
