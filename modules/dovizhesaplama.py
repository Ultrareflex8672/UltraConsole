from application.ultraconsole import UltraConsole as UC
import http.client
import json
import os

def dovizhesaplama(**kwargs):
    # API'ye bağlantı kurulacak URL ve endpoint
    api_url = "hasanadiguzel.com.tr"
    endpoint = "/api/kurgetir"

    # HTTP bağlantısı
    conn = http.client.HTTPSConnection(api_url)

    # API'den veri çek
    conn.request("GET", endpoint)

    # API yanıtı
    response = conn.getresponse()

    # Veriyi oku
    data = response.read()

    # Bağlantıyı kapat
    conn.close()

    # JSON verisini işle
    if response.status == 200:
        # JSON verisini yükleyelim
        json_data = json.loads(data.decode('utf-8'))

        # Döviz kurlarını al
        tcmb_data = json_data['TCMB_AnlikKurBilgileri']

        # İlk döviz kuru bilgisi örneği
        currency_1 = tcmb_data[0]
        currency_name_1 = currency_1['CurrencyName']
        currency_forex_buying_1 = currency_1['ForexBuying']
        currency_forex_selling_1 = currency_1['ForexSelling']

    else:
        # print(f"API isteği {response.status} kodu ile hata verdi: {data.decode('utf-8')}")
        UC.create_frame("Bağlantı Hatası", f"API isteği {response.status} kodu ile hata verdi: {data.decode('utf-8')}", "info")

    currency_types = ["Amerikan Doları - USD", 
                      "Avusturalya Doları - AUD", 
                      "Danimarka Kronu - DKK", 
                      "Euro - EUR", 
                      "İsviçre Frangı - CHF", 
                      "İsveç Kronu - SEK", 
                      "Kanada Doları - CAD", 
                      "Kuveyt Dinarı - KWD", 
                      "Norveç Kronu - NOK", 
                      "Suudi Arabistan Riyali - SAD", 
                      "Japon Yeni - JPY", 
                      "Bulgar Levası - BGN", 
                      "Rumen Leyi - RON", 
                      "Rus Rublesi - RUB", 
                      "Çin Yuanı - CNY", 
                      "Pakistan Rupisi - PKY", 
                      "Katar Riyali - QAR", 
                      "Güney Kore Wonu - KRW", 
                      "Azerbaycan Manatı - AZN", 
                      "BEA Dirhemi - AED", 
                      "Geri Dön" ]
    os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
    type_ = int(UC.create_frame("Dönüşüm Türü", ["₺ ➔  Döviz", "Döviz ➔  ₺", "Çıkış"], "menu"))
    if type_ != 0:
        os.system('cls' if os.name == 'nt' else 'clear')  # Konsolu temizle
        currency_type = int(UC.create_frame("Para Birimi Seçimi", currency_types, "menu"))
        if currency_type != 0:
            selected_n = currency_types[currency_type-1]
            selected_ = selected_n.split(" - ")
            name_ = selected_[0]
            short_ = selected_[1]
            if type_ == 1:
                while True:
                    try:
                        base_money = float(UC.create_frame("Döviz Hesaplayıcı", f"{selected_n} karşılığını öğrenmek istediğiniz Türk Lirası miktarını Giriniz (Kuruş için '.' (Nokta) kullanınız. Örn: 50.65)", ""))
                        break
                    except ValueError:
                        UC.create_frame("Hatalı Giriş", "Lütfen geçerli bir değer girin. Girilen veri Integer ya da Float olmalıdır. Örn: 65 ya da 65.80", "info")
                
                selected_currency = tcmb_data[currency_type-1]['ForexSelling']
                convertion = base_money / selected_currency
                UC.create_frame("Döviz Hesaplayıcı", f"{base_money} ₺ = {convertion} {short_}                          1 {name_} = {selected_currency} ₺")
            elif type_ == 2:
                while True:
                    try:
                        base_money = float(UC.create_frame("Döviz Hesaplayıcı", f"Türk Lirası karşılığını öğrenmek istediğiniz {selected_n} miktarını Giriniz (Küsürat '.' (Nokta) kullanınız. Örn: 50.65)", ""))
                        break
                    except ValueError:
                        UC.create_frame("Hatalı Giriş", "Lütfen geçerli bir değer girin. Girilen veri Integer ya da Float olmalıdır. Örn: 65 ya da 65.80", "info")

                selected_currency = tcmb_data[currency_type-1]['ForexSelling']
                convertion = base_money * selected_currency
                UC.create_frame("Döviz Hesaplayıcı", f"{base_money} {short_} = {convertion} ₺                          1 {name_} = {selected_currency} ₺")
        else:
            dovizhesaplama(**kwargs)
    else:
        pass