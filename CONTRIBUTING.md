# UltraConsole Modülü Eklemek ve Kullanmak<a id="0"></a>

Bu yazıda UltraConsole modülünde yeni modüller nasıl eklenir, menü nasıl oluşturulur ve modül içerisinde hangi fonksiyonlar kullanılabilir gibi detayları bulabilirsiniz.

## 1. Modül Ekleme<a id="1"></a>

Modül eklemek için öncelikle yeni bir Python dosyası (.py uzantılı) oluşturmalısınız. Bu dosya, modülünüzü içeren fonksiyonları ve sınıfları barındıracaktır.

### Adımlar:

1.  **Python Dosyası Oluşturma:**<a id="1.1"></a>
    
    -   Modülünüz için bir Python dosyası oluşturun (örneğin `ornek_modul.py`).
    -   Bu dosya içerisinde modülünüzü çalıştıracak fonksiyonlar veya sınıflar yer almalıdır.
2.  **Modülünüzü UltraConsole’a Dahil Etme:**<a id="1.2"></a>
    
    -   UltraConsole içerisinde modülünüzü kullanabilmek için ```from application.ultraconsole import UltraConsole as UC``` kodu ile UltraConsole modülünü içe aktarın.
3.  **Fonksiyon İsimlendirmesi:**<a id="1.3"></a>
    
    -   Modülünüzdeki ana fonksiyon, dosya ismiyle aynı isme sahip olmalıdır. Örneğin, `ornek_modul.py` dosyasındaki ana fonksiyon `ornek_modul()` olmalıdır.
    -   Ayrıca, modülünüzde sınıf yapısı oluşturabilir ve `_init_` fonksiyonuna parametreler gönderebilirsiniz. Bunun detaylı açıklaması için [buraya tıklayın](#2.5).
4.  **Modülü Modül Klasörüne Yerleştirme:**<a id="1.4"></a>
    
    -   Oluşturduğunuz Python dosyasını `modules` klasörüne yerleştirin.
5.  **Modül Ekleme:**<a id="1.5"></a>
    
    -   UltraConsole modül ayarlarından "Modül Ekle" seçeneğini seçin. Burada, oluşturduğunuz modülü göreceksiniz.
    -   Modülünüzü seçip menü adı vererek ekleme işlemini tamamlayın.

----------

## 2. Menü Oluşturma - (Basit - Orta ve İleri Düzeylerde)<a id="2"></a>

Modülünüzde kullanıcıya seçim yapma imkanı veren menüler oluşturmak için birkaç farklı yöntem bulunmaktadır. Aşağıda iki ana seçenek açıklanmıştır.

### 2.1. Basit Menü Yapısı (Liste Kullanarak)<a id="2.1"></a>

Basit bir menü oluşturmak için aşağıdaki gibi bir liste veri yapısı kullanabilirsiniz:

```menu_elemanlari = ["1. Seçenek", "2. Seçenek", "3. Seçenek", "4. Seçenek"]``` 

Eğer "Geri Dön" veya "Ana Menü" gibi seçenekler eklemek isterseniz, bunları şu şekilde ekleyebilirsiniz:

```menu_elemanlari = menu_elemanlari + ["Geri Dön"]  # Veya menu_elemanlari.append("Ana Menü")``` 

Kullanıcı seçimlerini almak için aşağıdaki gibi bir kod yapısı kullanabilirsiniz:

```kullanici_secimi = UC.create_frame("Menü Başlığı", menu_elemanlari, "menu")``` 

### 2.2. JSON Yapısı ile Menü<a id="2.2"></a>

Bir menüyü JSON formatında tanımlamak, daha büyük ve dinamik menüler için ideal bir yöntemdir. Menü seçeneklerini JSON formatında aşağıdaki gibi tanımlayabilirsiniz:

```json
{
    "Örnek Modül": { 
        "Seçenek 1": "ornek_modul",
        "Seçenek 2": "ornek_modul",
        "Seçenek 3": "ornek_modul",
        "Seçenek 4": "ornek_modul"
    }
}
```

Bu yapıda, her seçeneğin karşılığı olan modül veya fonksiyon belirlenmiştir. Alt modüller çalıştırılacak şekilde de yapılandırabilirsiniz. Örneğin:

```json
{
    "Örnek Modül": { 
        "Seçenek 1": "_ornek_modul1", 
        "Seçenek 2": "_ornek_modul2", 
        "Seçenek 3": "_ornek_modul3", 
        "Seçenek 4": "_ornek_modul4" 
    }
}
``` 

Yukarıdaki JSON verisini, `config/menu.cfg` dosyasına ekleyebilirsiniz.

### 2.3. Menüyü Modül İçerisinde Kullanma<a id="2.3"></a>

Menüyü modülünüzde kullanmak için şu adımları takip edebilirsiniz:

```munu.cfg``` dosyası içeriğinin aşağıdaki gibi olduğunu varsayalım

```json
{
    "Ana Menü": {
        "Hesap Makinesi": "hesap_makinesi",
        "Oyunlar": "oyunlar",
        "Bayrak Çiz": "bayrak"
    },
    "Oyunlar": {
        "Adam Asmaca": "_adamasmaca",
        "Pong": "_pong",
        "Sayı Tahmin Etme": "_sayitahmin",
        "Taş Kağıt Makas": "_taskagitmakas"
    },
    "Örnek Modül": {
        "Seçenek 1": "ornek_modul",
        "Seçenek 2": "ornek_modul",
        "Seçenek 3": "ornek_modul",
        "Seçenek 4": "ornek_modul"
    }
}
```
Yukarıdaki menü yapılandırılmasına göre 'Ana Menü' 0. Index, 'Oyunlar' 1. Index ve yeni eklenen 'Örnek Modül' 2. Index.
Bu durum da index değerimizi ilk parametresine yazarak ```UC.go_custom_menu(2, **kwargs)``` fonksiyonu ile menümüzü çağırabiliriz.
Örneğin:

```
from application.ultraconsole import UltraConsole as UC

def ornek_modul(**kwargs):
   if UC.from_main_menu(**kwargs):
      UC.go_custom_menu(2, **kwargs) # 2. index
``` 

Kullanıcı seçimlerini yakalamak için aşağıdaki yapıyı kullanabilirsiniz:

```
if UC.selected_key(1, **kwargs): 
    print("1 seçildi")
if UC.selected_key(2, **kwargs): 
    print("2 seçildi")
``` 

### 2.4. JSON Yapısını Dinamik Olarak Kullanma<a id="2.4"></a>

Menüyü dinamik olarak oluşturmak için JSON verisini bir değişkene atayıp kullanabilirsiniz:

Aşağıda verilen örnekte olduğu gibi menü verisini ```menu.cfg``` dosyasından çağırmak yerine bir değişken üzerinden de gönderebilirsiniz.


```
menu_json = {
    "Örnek Modül": { 
        "Seçenek 1": "_ornek_modul1", 
        "Seçenek 2": "_ornek_modul2", 
        "Seçenek 3": "_ornek_modul3", 
        "Seçenek 4": "_ornek_modul4" 
    }
}

def ornek_modul(**kwargs):
   if UC.from_main_menu(**kwargs):
      kwargs.update({"menu_data": menu_json})
      UC.go_custom_menu(0, **kwargs) # Gönderilen menü verisinde hangi ana menü çalıştırılmak isteniyorsa o anahtarın index değeri girilmelidir. (Bu örenekte index 0)
``` 

Yukarıdaki örnekte menü yapısı ```menu_json``` değişkenine doğrudan tanımlanmıştır ancak dilerseniz menü yapısı json verisini kendi oluşturacağınız bir dosyadan da okuyarak ```menu_json``` değişkenide atayabilirsiniz. Örneğin:

```
from application.ultraconsole import UltraConsole as UC

menu_json = UC.load_json("kendi_menu_dosyam.cfg")

def ornek_modul(**kwargs):
   if UC.from_main_menu(**kwargs):
      kwargs.update({"menu_data": menu_json})
      UC.go_custom_menu(0, **kwargs) # Gönderilen menü verisinde hangi ana menü çalıştırılmak isteniyorsa o anahtarın index değeri girilmelidir.
```

### 2.5. `_init_` Fonksiyonu ile Parametre Gönderme<a id="2.5"></a>

Sınıf yapısı kullanıyorsanız, `_init_` fonksiyonuna parametreler gönderebilirsiniz. Bunun için aşağıdaki yapıyı kullanabilirsiniz:

```
def ornek_modul(**kwargs):
   if UC.from_main_menu(**kwargs):
      kwargs.update({"class_name": "OrnekSinif"})
      kwargs.update({"init_data": "parametre"})
      UC.go_custom_menu(2, **kwargs)
``` 

```UC.go_custom_menu(menu_index, **kwargs)``` fonksiyonuna gönderebileceğiniz diğer parametreler:
```module_name``` , ```func_name``` , ```module_path``` Örneğin:

```
from application.ultraconsole import UltraConsole as UC

def ornek_modul(**kwargs):
    if UC.from_main_menu(**kwargs):
        kwargs.update({"menu_data": menu_json})		        # Özel json verisi ile menü oluşturma
	kwargs.update({"module_name": "modul_dosyası_adi"})	# Bağımsız modül dosyası adı tanımlamam
	kwargs.update({"func_name": "fonksiyon_adi"})		# Modül dosyası adından bağımsız fonsiyon tanımlama
	kwargs.update({"module_path": "modul_konumu"})	        # 'modules' kalsöründen farklı modül klasörü tanımlama
        kwargs.update({"class_name": "OrnekSinif"})		# Modül içinde çalıştırılacak sınıfı tanımlama
        kwargs.update({"init_data": "parametre"})		# Sınıf içinde init yapısına gönderilecek parametre
        UC.go_custom_menu(2, **kwargs)
```

----------

## 3. Bilgi Penceresi Oluşturma<a id="3"></a>

Kullanıcıya bilgi göstermek için aşağıdaki kodu kullanabilirsiniz:

```UC.create_frame("Başlık", "Bilgi içeriği", "info")``` 

Bu, ekrana bir bilgi penceresi açacaktır.

----------

## 4. Kullanıcıdan Input Alma<a id="4"></a>

Kullanıcıdan input almak için şu kodu kullanabilirsiniz:

```UC.create_frame("Başlık", "Input talebi açıklaması", "")``` 

Örneğin, kullanıcıdan adını almak için:

```UC.create_frame("Bilgi Girişi", "İsim Bilginiz Gereklidir", "Adınız: ")``` 

----------

## 5. Giriş Yapmış Kullanıcının Bilgilerini Kullanma<a id="5"></a>

Giriş yapmış bir kullanıcının bilgilerini modülünüzde kullanmak için şu şekilde `kwargs.get("user_data")` ifadesini kullanabilirsiniz:

```
def ornek_modul(**kwargs):
   user_data = kwargs.get("user_data")
   isim = user_data[4]  # 4. index isim bilgisi
   if UC.selected_key(1, **kwargs): 
      print(f"Merhaba {isim}")
``` 

### user_data İndeksleri:<a id="5.1"></a>

-   0 -> ID
-   1 -> Kullanıcı Adı
-   2 -> Kriptolu Parola
-   3 -> Kullanıcı Rolü
-   4 -> İsim
-   5 -> Soyisim
-   6 -> E-Posta
-   7 -> Telefon

----------

## 6. Menü Pencere Boyutları ve Renklerini Değiştirme<a id="6"></a>

Menü pencere boyutları ve renklerini Ayar -> Ayar Değiştir menüsünden değiştirebilirsiniz.

-   `menu_min_screen_width`: Minimum ekran genişliği.
-   `menu_max_screen_width`: Maksimum ekran genişliği.
-   `menu_title_color`, `menu_content_color`, `menu_frame_color`: Menü başlık, içerik ve çerçeve renklerini değiştirme.

----------

## 7. Bilgi ve Input Pencere Boyutları ve Renklerini Değiştirme<a id="7"></a>

Bilgi ve input pencere boyutlarını ve renklerini de Ayar -> Ayar Değiştir menüsünden değiştirebilirsiniz:

-   `info_min_screen_width` ve `info_max_screen_width`: Bilgi ve input penceresinin ekran genişliklerini ayarlayabilirsiniz.
-   `info_title_color`, `info_content_color`, `info_frame_color`: Bilgi ve input penceresi başlık, içerik ve çerçeve renklerini değiştirme.

----------

## 8. Modülde Kullanabileceğiniz Diğer Fonksiyonlar<a id="8"></a>

-   **```UC.cls()```**: Konsolu temizler.
-   **```UC.go_main_menu(**kwargs)```**: Ana menüye geri gider.
-   **```UC.get_pass(1)```**: Kullanıcıdan şifre girişi ister.
-   **```UC.get_pass(2)```**: Kullanıcıdan tekrar şifre girişi ister.
-   **```UC.load_json("dosya_yolu")```**: JSON dosyası yükler.
-   **```UC.create_file("dosya_yolu")```**: Dosya oluşturur.
-   **```UC.load_file("dosya_yolu")```**: Dosya yükler.
-   **```UC.load_lines("dosya_yolu")```**: Dosyayı satır satır yükler.
-   **```UC.write_file("dosya_yolu", "içerik")```**: Dosyayı kaydeder.

----------

## 9. Yönetici Kullanıcı Adı ve Şifremi Unuttum<a id="9"></a>

Eğer giriş yapamıyorsanız, `database` klasöründeki `users_db.db` dosyasını silebilirsiniz. Uygulama açıldığında yeni bir yönetici hesabı tanımlamanız istenecektir.

----------

## 10. Ayar ve Menü Yapısı Sıfırlama<a id="10"></a>

-   Sadece **ayarları sıfırlamak** için: `config/config.cfg` dosyasını silebilirsiniz.
-   Sadece **menü yapısını sıfırlamak** için: `config/menu.cfg` dosyasını silebilirsiniz.
-   Her ikisini de sıfırlamak için: `config` klasörünü silebilirsiniz.