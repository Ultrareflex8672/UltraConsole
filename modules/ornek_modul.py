# UltraConsole Kemal Burak YILDIRIM tarafından sunulmuş ve hala geliştirilmeye devam edilen açık kaynak bir kütüphanedir.
# Güncel Sürümler için: https://github.com/Ultrareflex8672/Console-Application


# UltraConsole Orta Düzey Kullanım Örneği
# 1. Modül olarak kullanacağınız yazılımı aşağıdaki bilgilere göre düzenleyin
# 2. Kodlarınızı aşağıdaki gibi en az bir ana fonksiyon içine yazın
# 3. .py uzantılı dosyanızı ana fonsiyon adınız ile aynı isimle "modules" klasörüne kaydedin
# 4. Eğer varsa alt menülerden çağırılacak fonsiyonları örenkteki gibi farklı .py dosyalarına kaydederek bu dosyalarıda "modules" klasörüne alın
# 5. Modülünüzde Class çağırma, init yapma, farklı kalsörden yada farklı fonk. adı ile çağırma işlemleri yapacaksanız go_custom_menu() ileri seviye parametrelerine bakın
# 6. config klasörü içindeki menu.cfg dosyasında ana menü altına key= modül adı, value= fonksiyon adı şeklinde ekleyin. Örn: Benim Modülüm: my_modul
# 7. Eğer modülünüz kendi içinde menü gerektiriyor ise modülünüz içine aşağıdaki menu_data örneğindeki gibi bir menü datası hazırlayın yada madde 8 i uygulayın
# 8. Aşağıdaki menu_data verisi formatında hazırlanmış menü verisini config/menu.cfg dosyasının root düzeyinde en sonuna ekleyin ve rootta kaçıncı sırada olduğuna bakın
# 9. Eğer tek seviyeden oluşan bir menünüz var ise herbir seçeneği 6. maddedeki gibi ekleyebilirsiniz. Seçeneklerin hepsi tekbir dosyada farklı fonksiyonlar çalıştıracaksa kwargs.get("selected_key") kullanarak seçimleri yakalayabilirsiniz
# 10. Genel kullanım örneği aşağıda verilmiştir.

from application.ultraconsole import UltraConsole as UC


def ornek_modul(**kwargs):                                                                                              # ornek_modul.py modülü, ornek_modul fonksiyonu.
    menu_data_ = {                                                                                                      # Menüyü modül içindeoluşturma öreneği.
        "Örnek Modül": {
        "Seçenek M.1": "ornek_modul", 
        "Seçenek M.2": "ornek_modul", 
        "Seçenek M.3": "ornek_modul",
        "Seçenek M.4": "ornek_modul",
        "Seçenek M.5": {
            "Seçenek M.5.1": "ornek_modul_alt_fonkisyon", 
            "Seçenek M.5.2": "ornek_modul_alt_fonkisyon"
            }
        }
    } 

    if UC.from_main_menu(**kwargs) == True:                                                                             # İstek ana meüden geliyorsa True gelmiyorsa False.

        # go_custom_menu() Fonksiyonu parametre şeması aşağıdaki açıklama satırında verilmiştir.
        # Eğer menü elemanları menu.cfg dosyasında ise tek paremetre olarak menünün root sırasını girebilirsiniz.
        # Eğer menü elemanlarını modül dosyasından gönderecekseniz 2. parametre dict olmalıdır.
        # Daha ileri seviye parametreleri de gönderebileceğiniz örnek aşağıdaki gibidir.
        # go_custom_menu(menu_root, menu_data=None, module_name=None, func_name=None, module_path=None, class_name=None, init_data=None, **kwargs)

        # UC.go_custom_menu(0, menu_data=menu_data_)                                                                    # Modül içinden menü elemanı gönderimi örneği.
        UC.go_custom_menu(2)                                                                                            # menu.cfg içindeki menü elemanlarını çağırma örneği.

    if UC.selected_key(1, **kwargs) == True:                                                                            # Eğer menüden seçilen anahtar 1 ise True döner.
        UC.create_frame("ornek_modul.py Dosyası", "'ornek_modul' fonksiyonu çalıştı ve 'Seçenek 1' seçildi", "info")    # Bir bilgi ekrarnı basar Params: (Başlık, Bilgi, "info")
    
    if UC.selected_key(2, **kwargs) == True:                                                                            # Eğer menüden seçilen anahtar 2 ise True döner.
        UC.cls() # os.system('cls' if os.name == 'nt' else 'clear')                                                     # Konsol temizlenmek istenirse.
        options = ["ornek_modul.py Dosyası", "'ornek_modul' fonksiyonu çalıştı ve", "'Seçenek 2' seçildi"]+["Geri Dön"] # Fonksiyona gönderilecek List verisi.
        sel = UC.create_frame("Başlık", options, "menu")                                                                # List içindeki verilerle kullanıcıdan seçmeli veri alır.
        input(sel+" . Seçeneği seçtiniz")
    
    if UC.selected_key(3, **kwargs) == True:                                                                            # Eğer menüden seçilen anahtar 3 ise True döner.
        name = UC.create_frame("ornek_modul.py Dosyası", "'ornek_modul' fonk. 'Seçenek 3'", "Adnızı Girin: ")           # Bilgi vererek input alır Params:(Başlık, Bilgi, Soru)
        input("Merhaba "+name)

    if UC.selected_key(4, **kwargs) == True:                                                                            # Eğer menüden seçilen anahtar 4 ise True döner.
        input("Ana Menüye Dönmek için 'Enter'...")
        UC.go_main_menu()                                                                                               # UltraConsole ana menüsüne gider.
    
