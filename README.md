
# UltraConsole

## 🚀 UltraConsole Nedir?

UltraConsole, kullanıcı dostu bir modüler komut satırı arayüzü sunarak üreteceğiniz modülleri ve çeşitli işlemleri yönetmenizi sağlayan güçlü bir araçtır. Gelişmiş otomatik menü sisteminden bilgi penceresine, kullanıcı yönetiminden kişiselleştirmeye, kolay modül yönetiminden otomatik güncelleştirmelere kadar birçok işlevi destekler.

----------

## 🔥 Özellikler

### 🏗️ Menü ve Yapılandırma
-   Basit, orta ve ileri düzeyde otomatik menü yapıları oluşturulabilir.

-   Menü sistemi `menu.cfg` dosyasından otomatik oluşturulur.
    
-   Varsayılan `config.cfg` ile farklı menü yapıları veya ana menüler aktif hale getirilebilir.
    
-   "Geri" ve "Çıkış" seçenekleri sabittir.
    
-   Menü renkleri ve görselleri ayar dosyası üzerinden değiştirilebilir.
    

### 🛠️ Modüler Sistem

-   Yeni modüller eklenebilir, silinebilir veya düzenlenebilir.
    
-   Modüller parametre alabilir ve ana uygulama ile veri paylaşabilir.
    
-   Framework 'ün nasıl çalıştığını analiz edebileceğiniz bazı örnek dahili modüller:
    
    -   🧮 Hesap Makinesi
        
    -   🎭 Adam Asmaca Oyunu
        
    -   ✂️ Taş, Kağıt, Makas
        
    -   📅 Takvim Modülü
        
    -   🚩 Bayrak Çizme Modülü
        
    -   🏓 Pong Oyunu
        
    -   🎲 Sayı Tahmin Oyunu
        
    -   🔢 Ritmik Sayma Modülü
        
    -   📊 Not Hesaplama Modülü
        
    -   🔢 Çarpım Tablosu
        
    -   ⚖️ BMI Hesaplama Modülü
        
    -   🌡️ Sıcaklık Birim Çevirici
        
    -   💱 Döviz Hesaplama Modülü (API ile anlık veri)
        

### ⚙️ Ayarlar ve Konfigürasyon

-   JSON tabanlı terminal arayüzünden ayar yönetimi.
    
-   Menü ve pencere genişliği ve ayarları değiştirilebilir.
    
-   Modüller `config.cfg` ile ilişkilendirilebilir.
    

### 👤 Kullanıcı Yönetimi

-   SQLite tabanlı veritabanı altyapısı.
    
-   Şifreler güvenli şekilde saklanır.
    
-   İlk açılışta kullanıcı otomatik oluşturulur.
    
-   Kullanıcı bilgileri düzenlenebilir.
    
-   Yönetici yetkileri:
    
    -   Kullanıcı listeleme
        
    -   Yeni kullanıcı ekleme
        
    -   Kullanıcı silme
        
    -   Uygulama ayarlarını değiştirme

	-   Modül ekle, sil, değiştir
        

### 🖥️ Gelişmiş Konsol İşlevleri

-   Kullanıcı bilgilerini modüller ile paylaşabilme.

-   Basit menü, bilgi ve input pencereleri oluşturabilme.

-   İleri seviye menü oluşturma.

-   Konsol temizleme fonksiyonu.
    
-   Açıklamalı örnek modüller.
    
-   Basit, Orta ve İleri Seviye modları.
    
-   Stabilize edilmiş menü çağırma fonksiyonu.

-   Gelişmiş LOG kayıtları.
    

----------

## 📥 Kurulum

### 💾 [UltraConsole 'u İndirin](https://github.com/Ultrareflex8672/UltraConsole/releases/download/V3.5.0.2/UltraConsole_Setup.exe)

```
# Seçenek 1: Kurulum dosyasını indirin ve yükleyin
https://github.com/Ultrareflex8672/UltraConsole/releases/download/V3.8.0.3/UltraConsole_Setup.exe

# Seçenek 2: Depoyu klonlayın
git clone https://github.com/Ultrareflex8672/UltraConsole.git

# Bağımlılıkları yükleyin (gerekliyse)
python -m pip install -r requirements.txt
```

----------

## 🎯 Kullanım

```
UltraConsole.exe
```

### [UltraConsole Modülü Eklemek ve Kullanmak](#0)

1. [ **Modül Ekleme**](#1)
    
    -   [Python Dosyası Oluşturma](#1.1)
    -   [Modülünüzü UltraConsole’a Dahil Etme](#1.2)
    -   [Modül Ekleme](#1.3)
    -   [Modül Klasörüne Yerleştirme](#1.4)
    -   [Fonksiyon İsimlendirmesi](#1.5)
2.  [**Menü Oluşturma**](#2)
    
    -   [Basit Menü Yapısı (Liste Kullanarak)](#2.1)
    -   [JSON Yapısı ile Menü](#2.2)
    -   [Menüyü Modül İçerisinde Kullanma](#2.3)
    -   [JSON Yapısını Dinamik Olarak Kullanma](#2.4)
    -   [`_init_` Fonksiyonu ile Parametre Gönderme](#2.5)
3.  [**Bilgi Penceresi Oluşturma**](#3)
    
4.  [**Kullanıcıdan Input Alma**](#4)
    
5.  [**Giriş Yapmış Kullanıcının Bilgilerini Kullanma**](#5)
    
    -   [`user_data` İndeksleri](#5.1)
6.  [**Menü Pencere Boyutları ve Renklerini Değiştirme**](#6)
    
7.  [**Bilgi ve Input Pencere Boyutları ve Renklerini Değiştirme**](#7)
    
8.  [**Modülde Kullanabileceğiniz Diğer Fonksiyonlar**](#8)
    
9.  [**Yönetici Kullanıcı Adı ve Şifremi Unuttum**](#9)
    
10.  [**Ayar ve Menü Yapısı Sıfırlama**](#10)

----------

## 📌 Katkıda Bulunma

Katkılarınızı bekliyoruz! Yeni modüller ekleyerek veya mevcut kodu geliştirerek projeye destek olabilirsiniz. PR'lerinizi açabilirsiniz.

----------

## 📜 Lisans

Bu proje [MIT Lisansı](https://github.com/Ultrareflex8672/UltraConsole/tree/main?tab=MIT-1-ov-file) altında lisanslanmıştır.

----------

🚀 **UltraConsole ile komut satırını daha güçlü hale getirin!**


<hr>

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

## 2. Menü Oluşturma<a id="2"></a>

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

```
from application.ultraconsole import UltraConsole as UC

def ornek_modul(**kwargs):
   if UC.from_main_menu(**kwargs):
      UC.go_custom_menu(2, **kwargs)
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
      UC.go_custom_menu(None, **kwargs)
``` 

### 2.5. `_init_` Fonksiyonu ile Parametre Gönderme<a id="2.5"></a>

Sınıf yapısı kullanıyorsanız, `_init_` fonksiyonuna parametreler gönderebilirsiniz. Bunun için aşağıdaki yapıyı kullanabilirsiniz:

```
def ornek_modul(**kwargs):
   if UC.from_main_menu(**kwargs):
      kwargs.update({"class_name": "OrnekSinif"})
      kwargs.update({"init_data": "parametre"})
      UC.go_custom_menu(None, **kwargs)
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

<hr>

## Versiyon Geçmişi
<div  align="left"  id="workflow">

<ul>
	<li><b>14.02.2025 - V0.0.0.1</b></li>
	<ul>
		<li>Menuler Oluşturulmaya Başlandı</li>
	</ul>
	<li><b>14.02.2025 - V0.0.0.2</b></li>
	<ul>
		<li>Hesap Makinesi Fonksiyonu Eklendi (Şimdilik Basit Bir Tane Yazıldı Daha Sonra Hazır Hesap Makinesi ile Değiştirilebilir)</li>
	</ul>
	<li><b>18.02.2025 - V0.1.0.0</b></li>
	<ul>
		<li>Otomatik Menü Sistemi ve Modüler Yapı Tasarımına Geçildi</li>
		<li>Menülerin "menu.cfg" dosyasından okunarak otomatik oluşturlması sağlandı</li>
		<li>"Ayarlar" ve "Geri"/"Çıkış" seçenekleri sSabit Olarak Eklendi</li>
		<li>Genel ayarların "config.cfg" dosyasından okunması sağlandı</li>
		<li>"config.cfg" mevcut olamasa programın dahi varsayılan ayarlarla çalışması ve otomatik "config.cfg" oluşturulması sağlandı</li>
		<li>"config.cfg" dosyası ile farklı menü dosyaları yada aynı menu dosyası içerisinde farklı ana menülerin aktifleştirilebilmesi sağlandı</li>
		<li>"menu.cfg" dosyasındaki seçenekler ile otomatik olarak iilgili nesnenin çağırılması üzerinde çalışılıyor</li>
		<li>Yeni tasarıma göre otomatik çerçeveli konsol ekranı sağlandı</li>
		<li>Geri dön ve Çıkış eylemlerine sıra numarası yerine sabit olarak "0" seçeneği atandı</li>
		<li>Menü görselliği ayarlar dosyasına bağlandı ve renklendirme için yeni fonksiyonlar eklendi. Sadeleştirildi</li>
		<li>Ayrıca Gerektiğinde input alabilen menü harici Genel Maksatlı Çerçeve Oluşturma Ekranı Tasarlandı</li>
		<li>İlk version için yazdığım hesap makinesi bu versiyona uyarlanıp ilk modül olarak entegre edildi (Geliştirme Devam Ediyor)</li>
		<li>Hazır olarak indirilen Adam Asmaca Oyunu birkaç düzenleme yapılarak modül olarak eklendi</li>
		<li>Modülden return varsa genel maksatlı çerçeveye alındı. Modül kendi içinde çalışıp bitmişse modül sonu uyarısı verildi</li>
		<li>Eğer menü tanımlanmış ancak modül yok ise uyarı mesajı verildi</li>
		<li>Eğer modül tanımlanmış ancak fonksiyon adı uyuşmuyor ise uyarı mesajı verildi (Modül Kurulum Klavuzunda Detaylı Anlatacağım)</li>
		<li>Bir taş,kağıt,makas oyunu tam uyumlu modül örneği olacak şekilde yazılarak modül olarak eklendi</li>
		<li>Modül Yükleyicinin "config.cfg" ilişkisi oluşturuldu</li>
	</ul>
	<li><b>19.02.2025 - V0.1.0.5</b></li>
	<ul>
		<li>Ayarlar Yapısı tasarlanmaya başlandı ve ekran görünümleri ayawrlandı</li>
		<li>Menü ve Info ekranları için max, min ve auto genişlikler düzenlendi</li>
		<li>Program içinden ayarların değiştirilmesi entegrasyonu yapıldı geliştiriliyor.</li>
		<li>Program içinden ayarların değiştirilmesi entegrasyonu tamamlandı</li>
		<li>Modüllere gönderilen argümanlarda geliştirme yapıldı (Kullanma Klavuzu Videosunda Açıklanacak)</li>
		<li>Hesap Makinesi Modülünde Geliştirmeler Yapıldı</li>
		<li>Adam Asmaca Modülünde Geliştirmeler Yapıldı</li>
		<li>Taş Kağıt Makas Modülündeki büyük-küçük harf duyarlılığı hatası düzeltildi</li>
	</ul>
	<li><b>20.02.2025 - V0.9.0.0</b></li>
	<ul>
		<li>Ayarlar Yapısı Son Halini Aldı</li>
		<li>Menü sistemi ve fonksiyon çağırıma motorları her türlü veri ve argümanı paylaşabilecek şekilde yeniden yazıldı</li>
		<li>Ayarlar menüsü de JSON dan okunmak üzere yeniden yazıldı. Ayar menüsü ayıklanması için yeni config anahtarı eklendi</li>
		<li>Takvim Modülü</li>
		<li>Min genişliği 50 karakter olan bilgi ekranı için Takvim istisnası eklendi</li>
		<li>Bayrak Çizme Modülü Eklendi (Hazır Alındı - Uyarlandı)</li>
		<li>Pong Oyunu Eklendi (Hazır Alındı - Uyarlandı)</li>
		<li>Sayı Tahmin Oyunu Eklendi (Hazır Alındı - Uyarlandı)</li>
		<li>Ritmik Sayma Modülü Eklendi</li>
		<li>Adam Asmaca Oyunu Hataları Düzeltildi</li>
		<li>Eğer menu dosyası yoksa/silinmişse varsayılan ayarlarla menu dosyası oluşturma özelliği eklendi</li>
		<li>Program başlatıcı ve modüllerde kütüphane olarak kullanılacak tüm sınıfların misrasçısı bir modül oluşturuldu</li>
		<li>Not Hesaplama Modülü Eklendi</li>
		<li>Çarpım Tablosu Eklendi</li>
		<li>BMI Hesaplama Modülü Eklendi</li>
		<li>Sıcaklık Birim Çevirici Modülü Eklendi</li>
		<li>API Bağlantısı ile anlık veri alan döviz hesaplama modülü eklendi</li>
		<li>UltraConsole V1.0 Adı Verdiğim Sürüm Pyinstaller ile build edildi ancak henüz exe versiyonda sorunlar var</li>
		<li>Ayarlar Menüsünde Geri Gelindiğinde func_name argümanının boş dönmesi sorunu giderildi</li>
	</ul>
	<li><b>22.02.2025 - V1.0.9.0</b></li>
	<ul>
		<li>Menü Çağırma Fonksiyonunda Köklü İyileştirme</li>
		<li>Parametre döngüleri stabil hake getirildi</li>
		<li>Tek parametre ile menü döndürme kolaylığı sağlandı</li>
		<li>Basit, Orta ve İleri Seviyeye uygun modlar oluşturuldu</li>
		<li>Kullanıcılara klavuzluk etmesi için açıklamalı örnek modül oluşturuldu</li>
		<li>Konsol temizleme işlemi fonksiyon haline getirildi</li>
	</ul>
	<li><b>23.02.2025 - V1.9.0.0</b></li>
	<ul>
		<li>Menü işleyişinde köklü değişiklikler</li>
		<li>Parametreli modül çağırma iyileştirildi</li>
		<li>Örnek Modülün yanısıra Hesap Makinesi ve Oyunlar da farklı modül ekleme örnekleri olarak değiştirildi</li>
		<li>Uygulama içerisinden modül ekle/sil/düzelt fonksiyonu eklendi</li>
	</ul>
	<li><b>24.02.2025 - V1.9.5.0</b></li>
	<ul>
		<li>Kullanıcı Girişi Tsarlanmaya Başlandı</li>
		<li>SQL lite için fonsiyonlar oluşturuldu</li>
		<li>Kullanı işlemlerini kontrol edeccek sınıf oluşturuldu</li>
		<li>Kullanıcı giriş işlemleri fonksiyoanları oluşturuldu</li>
		<li>Eğer database yok yada hasarlı ise ilk kurulum ve kullanıcı oluşturma fonksiyonları oluşturuldu</li>
		<li>Şifre girilirken konsolda görünmesi engellendi</li>
		<li>Veri tabanında saklanan kullanıcı şifresi kriptolandı</li>
		<li>Kullanıcı datalarının modüllere aktarımı sağlandı</li>
	</ul>
	<li><b>25.02.2025 - V1.9.5.5</b></li>
	<ul>
		<li>Kullanıcının Profil Düzenlemesi Eklendi</li>
		<li>İsim değişikliği imkanı eklendi</li>
		<li>Soyisim değişikliği imkanı eklendi</li>
		<li>Kullanıcı adı değişikliği imkanı eklendi</li>
	</ul>
	<li><b>26.02.2025 - V1.9.9.0</b></li>
	<ul>
		<li>Kullanıcının Yönetici Rolü Olması Halinde Diğer Kullanıcıları Düzenleme Eylemleri</li>
		<li>Bilinen bağzı hatalar giderildi</li>
		<li>Diğer kullanıcıları listele eklendi</li>
		<li>Yeni kullanıcı ekle eklendi</li>
		<li>İlk çalışma kullanıcısı oluştuktan sonra login ekranı zorunlu kılındı</li>
		<li>Kullanıcı Sil Eklendi</li>
	</ul>
	<li><b>28.02.2025 - V2.0.0.0</b></li>
	<ul>
		<li>SQL deki hatalar giderildi</li>
		<li>Modül yöneticideki hatalar giderildi</li>
		<li>Genel kararlılık çalışması yapıldı</li>
		<li>Diğer kullanıcı bilgilerinin yöneticiler tarafından güncellenebilmesi eklendi</li>
	</ul>
	<li><b>28.02.2025 - V2.0.5.2</b></li>
	<ul>
		<li>Açılış ekranında hesap oluşturma imkanı sağlandı</li>
		<li>Çeşitli menü hataları giderildi</li>
		<li>Hesap oluşturma şifre tekrarı hatası giderildi</li>
		<li>Ayarlar menüsü işlemlerinde Standart Kullanıcı ve Yönetici yetkilerine göre işlemler atandı</li>
		<li>Giriş seçenekleri döngü hatası giderildi</li>
		<li>Otomatik menü config dosya oluşturma hatası giderildi</li>
	</ul>
	<li><b>28.02.2025 - V2.5.0.6</b></li>
	<ul>
		<li>Otomatik Versiyon Güncelleme Özelliği Eklendi</li>
		<li>Giriş seçenekleri döngü hatası giderildi</li>
		<li>Güncelleme sonrası otomatik yeniden başlatma eklendi</li>
	</ul>
	<li><b>28.02.2025 - V2.5.0.7</b></li>
	<ul>
		<li>Varsayılan menü hatası düzeltildi</li>
	</ul>
	<li><b>05.03.2025 - V3.0.0.2</b></li>
	<ul>
		<li>Ayarlar menüsü modül formatından integrated formatına çevrildi</li>
		<li>Modül kalsörünün ve dosyalarının mevcut olup olmadığı kontrolü fonksiyonu eklendi</li>
		<li>Bağzı küçük hatalar düzeltildi</li>
		<li>EXE paketi olarak yayımlandı</li>
	</ul>
	<li><b>05.03.2025 - V3.5.0.0</b></li>
	<ul>
		<li>Exe dosyasının otomatik update modülü eklendi</li>
		<li>Modül ekle ayarları için otomatik modül algılama eklendi</li>
	</ul>
	<li><b>05.03.2025 - V3.5.0.1</b></li>
	<ul>
		<li>Exe dosyasının otomatik update modülü eklendi</li>
	</ul>
	<li><b>06.03.2025 - V3.5.0.2</b></li>
	<ul>
		<li>Turtle kütüphanesi sabitlendi</li>
	</ul>
	<li><b>07.03.2025 - V</b><b id="version">3.8.0.3</b></li>
	<ul>
		<li>Log sistemi eklendi</li>
		<li>Profil ayarlarından ana menüye dönüşte bir hata düzeltildi</li>
	</ul>
</ul>

</div>

