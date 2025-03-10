from application.ultraconsole import UltraConsole as UC
import requests
from bs4 import BeautifulSoup
import re
import random
import os
from gtts import gTTS
from playsound import playsound
import webbrowser

menu_data = {
    "Sesli Asistan": {
        "Konu Araştırması": "sesli_asistan",
        "Ürün Tavsiyesi": "sesli_asistan",
        "Özel Arama Motoru": "sesli_asistan"
    }
}

def sesli_asistan(**kwargs):
    while True:
        if UC.from_main_menu(**kwargs):
            kwargs.update({"menu_data": menu_data})
            UC.go_custom_menu(0, **kwargs)
        elif UC.selected_key(1, **kwargs):
            konu_arastir(**kwargs)
            UC.go_custom_menu(0, **kwargs)
        elif UC.selected_key(2, **kwargs):
            urun_tavsiye(**kwargs)
            UC.go_custom_menu(0, **kwargs)
        elif UC.selected_key(3, **kwargs):
            ozel_arama(**kwargs)
            UC.go_custom_menu(0, **kwargs)
        else:
            del kwargs["menu_data"]
            break

def extract_data_from_url(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        data_page_div = soup.find('div', {'data-page': '1'})
        
        if data_page_div:
            first_a = data_page_div.find('a', class_=lambda x: x and 'container' in x)
            first_a_href = first_a['href'] if first_a else None

            first_h = data_page_div.find('h3', class_=lambda x: x and 'title' in x)
            first_h_value = first_h.text.strip() if first_h else None
            
            first_p = data_page_div.find('p', class_=lambda x: x and 'price' in x)
            first_p_value = first_p.text.strip() if first_p else None
            
            first_img = first_p.find_next('img') if first_p else None
            img_alt = first_img.get('alt') if first_img else None

            img_url = first_img.get('src') if first_img else None
            
            return first_h_value, first_a_href, first_p_value, img_alt, img_url
        else:
            return None, None, None
    else:
        return None, None, None

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

def get_cleaned_text_from_url(url):
    # URL'ye HTTP isteği gönderiyoruz
    response = requests.get(url)

    if response.status_code == 200:
        # Sayfa içeriğini BeautifulSoup ile parse ediyoruz
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # "mw-content-ltr mw-parser-output" class'ına sahip elementleri alıyoruz
        content_div = soup.find_all(class_='mw-content-ltr mw-parser-output')
        
        # Eğer içerik bulunduysa, metinleri alalım
        if content_div:
            full_text = ""
            for div in content_div:
                # İçerikteki tüm metinleri alıyoruz
                text = div.get_text(separator="\n", strip=True)
                
                # Anlamsız semboller ve fazla boşlukları temizleme
                text = clean_text(text)
                
                # Paragrafları düzgün bir şekilde birleştiriyoruz
                full_text += text + "\n\n"
            
            return full_text.strip()  # Sonunda fazla boşluk bırakmamak için strip()
        else:
            return "Belirtilen class ile ilgili içerik bulunamadı."
    else:
        return f"Sayfa yüklenirken bir hata oluştu. Status code: {response.status_code}"

def clean_text(text):
    # HTML etiketlerini temizle (başka etiketler varsa onları da temizler)
    text = re.sub(r'<[^>]+>', '', text)
    
    # Anlamsız semboller ve karakterleri temizle (örneğin, &nbsp;, \xa0, vb.)
    text = re.sub(r'[\r\n\t\x0b\x0c]+', ' ', text)  # Satır başı, tab, form feed temizle
    text = re.sub(r'&[a-z]+;', ' ', text)  # HTML sembollerini temizle (örneğin, &amp;)
    text = re.sub(r'\s+', ' ', text)  # Birden fazla boşluk varsa tek boşluğa indir
    text = re.sub(r'\s*[\.,;!?()\[\]{}"]+\s*', ' ', text)  # Noktalama işaretlerini düzgün hale getir
    text = re.sub(r'\s+', ' ', text)  # Boşlukları tek bir boşluğa indir
    text = text.strip()  # Baş ve son boşlukları temizle
    return text

def konu_arastir(**kwargs):
    user_data = kwargs.get("user_data")
    speak_ = f"Merhaba {user_data[4]}, konu araştırma asistanına hoş geldin. Lütfen araştırma konusunu gir."
    speak(speak_)
    konu = UC.create_frame("Konu Başlığı", "Araştırma Yapılacak Konu Başlığını Yazınız.","")
    if konu:
        url = f"https://tr.wikipedia.org/wiki/{konu}"  # Bu URL'yi kendi ihtiyacınıza göre değiştirebilirsiniz
        read = UC.create_frame("Sesli Okuma", "Araştırma Sonucunun Özeti Sesli Olarak Okunsun İster misiniz? (Not: Sesli yanıt bekleme sürenizi uzatabilir.)","(E/H)\n")
        if read.lower() == "e":
            print("Araştırma yapılıyor...")
            cleaned_text = get_cleaned_text_from_url(url)
            UC.create_frame(f"Konu: {konu}", cleaned_text+" - (Sesli Özeti Dinlemek için 'Enter')")
            print("Ses modeli yükleniyor... (Bu biraz zaman alabilir)")
            speak_ = cleaned_text[:487]+f". {konu} konusunda özet bilgi dinlediniz. UltraKonsol sesli asistanı kullandığınız için teşekkürler {user_data[4]}, hoşçakal."
            speak(speak_)
        else:
            print("Araştırma yapılıyor...")
            cleaned_text = get_cleaned_text_from_url(url)
            UC.create_frame(f"Konu: {konu}", cleaned_text)

def urun_tavsiye(**kwargs):
    user_data = kwargs.get("user_data")
    speak_ = f"Merhaba {user_data[4]}, ürün bulucu fonksiyonuna hoş geldin. Lütfen arama yapmak istediğin ürünü gir."
    speak(speak_)
    product = UC.create_frame("Ürün Bulucu", "Satıcı tavsiyesi almak istediğiniz ürünü giriniz.", "")
    url = F"https://www.cimri.com/arama?q={product}"
    title, a_href, span_value, img_alt, img = extract_data_from_url(url)

    if title or a_href or span_value or img_alt:
        speak_ = f"{title} ürünü, {img_alt} adlı mağazada {span_value}. Sizi ürünün bulunduğu siteye yönlendirmemi ister misiniz?"
        speak(speak_)
        site = UC.create_frame(title, f"{img_alt} adlı mağazada fiyatı: {span_value}", "İnternet Sitesine Yönlendirmemi İstermisiniz (E/H)")
        # print("Ürün:", title)
        # print("URL:", "https://www.cimri.com/"+a_href)
        # print("Fiyat:", span_value)
        # print("Mağaza:", img_alt)
        if site.lower() == "e":
            webbrowser.get().open("https://www.cimri.com/"+a_href)
        speak_ = f"UltraKonsol sesli asistanı kullandığınız için teşekkürler {user_data[4]}, hoşçakal."
        speak(speak_)
    else:
        speak_ = f"Malesef girilen ürün için bilgi sağlayamadım {user_data[4]}. Lütfen ürün adını farklı bir şekilde girerek tekrar dene"
        speak(speak_)

def ozel_arama(**kwargs):
    user_data = kwargs.get("user_data")
    sub_menu_items = ["Film/Video", "Kitap", "Müzik", "Program/ISO/Oyun", "Görsel", "Diğer"] + ["Geri Dön"]
    engine = "https://www.google.com/search?q="
    speak(f"Merhaba {user_data[4]}, UltraKonsol arama motoruna hoş geldin.")

    while True:
        while True:
            try:
                speak(f"Lütfen arama yapılacak kategori seçimini yap.")
                UC.cls()
                selected_item = int(UC.create_frame("Aranak Dosya Türü", sub_menu_items, "menu"))
                break
            except:
                print("Lütfen numerik bir seçim yapınız.")

        if selected_item == 1:
            title = "Film/Video Arama"
            parameter = "%20%2B(mkv%7Cmp4%7Cavi%7Cmov%7Cmpg%7Cwmv%7Cdivx%7Cmpeg)%20-inurl%3A(jsp%7Cpl%7Cphp%7Chtml%7Caspx%7Chtm%7Ccf%7Cshtml)%20intitle%3Aindex.of%20-inurl%3A(listen77%7Cmp3raid%7Cmp3toss%7Cmp3drug%7Cindex_of%7Cindex-of%7Cwallywashis%7Cdownloadmana)"
        elif selected_item == 2:
            title = "Kitap Arama"
            parameter = "%20%2B(MOBI%7CCBZ%7CCBR%7CCBC%7CCHM%7CEPUB%7CFB2%7CLIT%7CLRF%7CODT%7CPDF%7CPRC%7CPDB%7CPML%7CRB%7CRTF%7CTCR%7CDOC%7CDOCX)%20-inurl%3A(jsp%7Cpl%7Cphp%7Chtml%7Caspx%7Chtm%7Ccf%7Cshtml)%20intitle%3Aindex.of%20-inurl%3A(listen77%7Cmp3raid%7Cmp3toss%7Cmp3drug%7Cindex_of%7Cindex-of%7Cwallywashis%7Cdownloadmana)"
        elif selected_item == 3:
            title = "Müzik Arama"
            parameter = "%20%2B(mp3%7Cwav%7Cac3%7Cogg%7Cflac%7Cwma%7Cm4a%7Caac%7Cmod)%20-inurl%3A(jsp%7Cpl%7Cphp%7Chtml%7Caspx%7Chtm%7Ccf%7Cshtml)%20intitle%3Aindex.of%20-inurl%3A(listen77%7Cmp3raid%7Cmp3toss%7Cmp3drug%7Cindex_of%7Cindex-of%7Cwallywashis%7Cdownloadmana)"
        elif selected_item == 4:
            title = "Program/ISO/Oyun Arama"
            parameter = "%20%2B(exe%7Ciso%7Cdmg%7Ctar%7C7z%7Cbz2%7Cgz%7Crar%7Czip%7Capk)%20-inurl%3A(jsp%7Cpl%7Cphp%7Chtml%7Caspx%7Chtm%7Ccf%7Cshtml)%20intitle%3Aindex.of%20-inurl%3A(listen77%7Cmp3raid%7Cmp3toss%7Cmp3drug%7Cindex_of%7Cindex-of%7Cwallywashis%7Cdownloadmana)"
        elif selected_item == 5:
            title = "Görsel Arama"
            parameter = "%20%2B(jpg%7Cpng%7Cbmp%7Cgif%7Ctif%7Ctiff%7Cpsd)%20-inurl%3A(jsp%7Cpl%7Cphp%7Chtml%7Caspx%7Chtm%7Ccf%7Cshtml)%20intitle%3Aindex.of%20-inurl%3A(listen77%7Cmp3raid%7Cmp3toss%7Cmp3drug%7Cindex_of%7Cindex-of%7Cwallywashis%7Cdownloadmana)"
        elif selected_item == 6:
            title = "Diğer Türler Arama"
            parameter = "%20-inurl%3A(jsp%7Cpl%7Cphp%7Chtml%7Caspx%7Chtm%7Ccf%7Cshtml)%20intitle%3Aindex.of%20-inurl%3A(listen77%7Cmp3raid%7Cmp3toss%7Cmp3drug%7Cindex_of%7Cindex-of%7Cwallywashis%7Cdownloadmana)"
        elif selected_item == 0:
            speak_ = f"Başka bir aramada görüşmek üzere, hoşçakal {user_data[4]}."
            speak(speak_)
            break
        else:
            UC.create_frame("Geçersiz Seçim", "Lütfen listedeki seçenekler dahilinde bir numerik seçim yapın", "info")

        while True:
            speak_ = f"Lütfen {title}sı yapmak için aranacak nesneyi gir."
            speak(speak_)
            search_object = UC.create_frame(title, "Arama yapmak istediğiniz anahtar kelimeyi/kelimeleri giriniz.", "")
            if search_object:
                webbrowser.get().open(engine+search_object+parameter)
                speak_ = f"İşte {search_object} ile ilgili {title} sonuçları. Başka bir aramada görüşmek üzere, hoşçakal {user_data[4]}."
                speak(speak_)
                break
            else:
                speak_ = f"İşte {search_object} ile ilgili {title} sonuçları."
                speak(speak_)
        
        if search_object:
            break
