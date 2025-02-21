from application.ultraconsole import UltraConsole as UC

def nothesaplama(**kwargs):
    myName = UC.create_frame("Not Hesaplama Programı", "Not: vize notunun %30 final notunun %70", "Lütfen isminizi giriniz:\n")
    # print('Basit Not Hesaplama Programı')
    # print('Not: vize notunun %30 final notunun %70'"\n")

    # print('Lütfen isminizi giriniz:'"\n")
    # myName = input()
    print('Merhaha , ' + myName)
    print("\n")

    # vize = float(input(' Lütfen vize notunuzu giriniz : '))
    while True:
        try:
            vize = float(UC.create_frame(f"Merhaba {myName}", "Lütfen vize notunuzu giriniz (Integer / Float)", "\n"))
            break
        except ValueError:
            UC.create_frame("Hatalı Giriş", "Lütfen geçerli bir değer girin. Girilen veri Integer ya da Float olmalıdır. Örn: 65 ya da 65.80", "info")
    # final = float(input('Lütfen final notunuzu giriniz : '))
    while True:
        try:
            final = float(UC.create_frame(f"Vize notunuz: {str(vize)}", "Lütfen final notunuzu giriniz (Integer / Float)", "\n"))
            break
        except ValueError:
            UC.create_frame("Hatalı Giriş", "Lütfen geçerli bir değer girin. Girilen veri Integer ya da Float olmalıdır. Örn: 65 ya da 65.80", "info")

    # print("\n")
    ortalama=(float(vize)*0.3)+(float(final)*0.7)

    if final>=50:
        if(ortalama>=85 and final>=50):
            # print("Harf Notunuz AA GEÇTİNİZ  " +myName)
            UC.create_frame(f"Tebrikler {myName}", "Harf Notunuz AA GEÇTİNİZ", "info")
        elif ortalama>=75 and ortalama<85 :
            # print("Harf Notunuz BA GEÇTİNİZ  " +myName)
            UC.create_frame(f"Tebrikler {myName}", "Harf Notunuz BA GEÇTİNİZ", "info")
        elif ortalama>= 70 and ortalama < 75:
            # print("Harf Notunuz BB GEÇTİNİZ " +myName)
            UC.create_frame(f"Tebrikler {myName}", "Harf Notunuz BB GEÇTİNİZ", "info")
        elif ortalama >= 65 and ortalama < 70:
            # print("Harf Notunuz CB GEÇTİNİZ  " +myName)
            UC.create_frame(f"Tebrikler {myName}", "Harf Notunuz CB GEÇTİNİZ", "info")
        elif ortalama >= 60 and ortalama < 65:
            # print("Harf Notunuz CC GEÇTİNİZ  " +myName)
            UC.create_frame(f"Tebrikler {myName}", "Harf Notunuz CC GEÇTİNİZ", "info")
        elif ortalama >= 55 and ortalama < 60:
            # print("Harf Notunuz DC KOŞULLU GEÇTİNİZ  " +myName)
            UC.create_frame(f"Koşullu Geçtiniz {myName}", "Harf Notunuz DC KOŞULLU GEÇTİNİZ", "info")
        elif ortalama >= 50 and ortalama < 55:
            # print("Harf Notunuz DD KOŞULLU GEÇTİNİZ " +myName)
            UC.create_frame(f"Koşullu Geçtiniz {myName}", "Harf Notunuz DD KOŞULLU GEÇTİNİZ", "info")
        
    else:
        # print("Harf notunuz FF KALDINIZ " +myName )
        UC.create_frame(f"Üzgünüm {myName}", "Harf Notunuz FF KALDINIZ", "info")
        

    # print("Ortalama :{0} ".format(ortalama))
    # print("\n")




    # time.sleep(7)
    UC.create_frame("Not Hesaplama Programı", f"Ortalamanız: {ortalama}", "info")