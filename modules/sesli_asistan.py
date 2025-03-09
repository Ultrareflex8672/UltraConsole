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
        "Ürün Tavsiyesi": "sesli_asistan"
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

