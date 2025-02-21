from application.ultraconsole import UltraConsole as UC


def bmi_hesapla(kilo, boy):
    bmi = kilo / (boy ** 2)
    if bmi < 18.5:
        durum = "Zayıf"
    elif 18.5 <= bmi < 24.9:
        durum = "Normal"
    elif 25 <= bmi < 29.9:
        durum = "Fazla Kilolu"
    else:
        durum = "Obez"
    return bmi, durum



def bmihesaplama(**kwargs):
    while True:
        try:
            kilo = float(UC.create_frame("Vücut Kitle İndeksi Hesaplama", "Kilonuzu girin (kg)", "\n"))
            break
        except ValueError:
            UC.create_frame("Hatalı Giriş", "Lütfen geçerli bir değer girin. Girilen veri Integer ya da Float olmalıdır. Örn: 65 ya da 65.80", "info")
    while True:
        try:
            boy = float(UC.create_frame("Vücut Kitle İndeksi Hesaplama", "Boyunuzu girin (metre)", "\n"))
            break
        except ValueError:
            UC.create_frame("Hatalı Giriş", "Lütfen geçerli bir değer girin. Girilen veri Integer ya da Float olmalıdır. Örn: 1 ya da 1.65", "info")
                          
    bmi, durum = bmi_hesapla(kilo, boy)

    UC.create_frame("Vücut Kitle İndeksi Hesaplama", f"Vücut Kitle İndeksiniz (BMI): {bmi:.2f} - {durum}", "info")

