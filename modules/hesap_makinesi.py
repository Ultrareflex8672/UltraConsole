def hesap_makinesi(islem):
    soru1 = ""
    soru2 = ""
    if islem == 2:
        soru1 = int(input("1. Sayıyı Giriniz: "))
        soru2 = int(input("Çıkarılacak Sayıyı Giriniz: "))
    elif islem == 6 or islem == 7:
        soru1 = int(input("1. Kenar Uzunluğunu Giriniz: "))
        soru2 = int(input("2. Kenar Uzunluğunu Giriniz: "))
    elif islem == 5:
        soru1 = int(input("Tabanı Giriniz: "))
        soru2 = int(input("Üssü Giriniz: "))
    elif islem == 4:
        soru1 = int(input("Bölüneni Giriniz: "))
        soru2 = int(input("Böleni Giriniz: "))
    else:
        soru1 = int(input("1. Sayıyı Giriniz: "))
        soru2 = int(input("2. Sayıyı Giriniz: "))
    
    v1 = soru1
    v2 = soru2
    sonuc = 0
    
    if islem == 1:  # Toplama
        if isinstance(v1, int) and isinstance(v2, int):
            sonuc = v1 + v2
        else:
            sonuc = "Sadece Sayı Girişi Yapılmalıdır."
        return str(sonuc)
    
    elif islem == 2:  # Çıkarma
        if isinstance(v1, int) and isinstance(v2, int):
            sonuc = v1 - v2
        else:
            sonuc = "Sadece Sayı Girişi Yapılmalıdır."
        return str(sonuc)
    
    elif islem == 3:  # Çarpma
        if isinstance(v1, int) and isinstance(v2, int):
            sonuc = v1 * v2
        else:
            sonuc = "Sadece Sayı Girişi Yapılmalıdır."
        return str(sonuc)
    
    elif islem == 4:  # Bölme
        if isinstance(v1, int) and isinstance(v2, int):
            sonuc = v1 / v2
        else:
            sonuc = "Sadece Sayı Girişi Yapılmalıdır."
        return str(sonuc)
    
    elif islem == 5:  # Üs Alma
        if isinstance(v1, int) and isinstance(v2, int):
            sonuc = 0
            for i in range(v2):
                i = v1 * v1
                sonuc += i
        else:
            sonuc = "Sadece Sayı Girişi Yapılmalıdır."
        return str(sonuc)
    
    elif islem == 6:  # Kare Alanı
        if isinstance(v1, int) and isinstance(v2, int):
            sonuc = v1 * v2
        else:
            sonuc = "Sadece Sayı Girişi Yapılmalıdır."
        return str(sonuc)
    
    elif islem == 7:  # Karenin Çevresi
        if isinstance(v1, int) and isinstance(v2, int):
            sonuc = (v1 + v2) * 2
        else:
            sonuc = "Sadece Sayı Girişi Yapılmalıdır."
        return str(sonuc)
    
    else:
        return "Geçersiz İşlem"
