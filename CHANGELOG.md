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
	<li><b>07.03.2025 - V3.8.0.3</b></li>
	<ul>
		<li>Log sistemi eklendi</li>
		<li>Profil ayarlarından ana menüye dönüşte bir hata düzeltildi</li>
	</ul>
	<li><b>07.03.2025 - V3.8.5.5</b></li>
	<ul>
		<li>Modül oluşturucudaki key value döngü hatası giderildi</li>
		<li>Daha kapsamlı örnek modül yerleştirildi</li>
	</ul>
	<li><b>07.03.2025 - V3.8.5.8</b></li>
	<ul>
		<li>Modül ekle, sil, değiştir işlemlerinden sonra uygulamanın yeniden başlatma zorunluluğu kaldırıldı.</li>
		<li>LOG Sistemi bazı hatalar giderildi</li>
		<li>Eklenmiş modülleri görüntüle farklı seçeneğe taşındı</li>
		<li>Geliştiriciler için kaynak kodlar 'UltraConsole_Setup.exe' içine dahil edildi.</li>
	</ul>
	<li><b>08.03.2025 - V3.9.5.8</b></li>
	<ul>
		<li>Artılışmış dahili kütüphane sayısı.</li>
	</ul>
	<li><b>08.03.2025 - V3.9.5.9</b></li>
	<ul>
		<li>Hata düzeltmesi.</li>
	</ul>
	<li><b>09.03.2025 - V3.9.6.9</b></li>
	<ul>
		<li>Sesli Asistan modülü eklendi.</li>
	</ul>
	<li><b>10.03.2025 - V3.9.7.0</b></li>
	<ul>
		<li>Bilgi penceresinde başlık taşma sorunu düzeltildi.</li>
		<li>Sesli Asistan modülüne özel arama fonksiyonu eklendi</li>
	</ul>
	<li><b>10.03.2025 - V4.0.0.0</b></li>
	<ul>
		<li>Dahili kütüphane sayısı artırıldı</li>
	</ul>
	<li><b>10.03.2025 - V4.0.0.1</b></li>
	<ul>
		<li>Bir dizi hata düzeltmesi</li>
	</ul>
	<li><b>12.03.2025 - V4.1.0.0</b></li>
	<ul>
		<li>Updater fonksiyonu EXE haline getirilerek pyhon yüklü olma bağımlılığı kaldırıldı.</li>
		<li>Updater fonksiyonuda Linux ve Windows sistemlerinin algılanarak doğru fonksiyonun otomatik seçilmesi sağlandı</li>
		<li>UltraConsole hakkında ve dökümanlara kısa erişim eklendi</li>
		<li>İsteğe bağlı kaynak kod indirme seçeneği eklendi</li>
		<li>Uygulama içinde manuel güncelleştirme kontrolü eklendi</li>
	</ul>
	<li><b>12.03.2025 - V4.1.0.4</b></li>
	<ul>
		<li>Yazım hatası düzeltmesi.</li>
		<li>Exe düzeltmesi.</li>
	</ul>
    <li><b>13.03.2025 - V4.1.0.5</b></li>
	<ul>
		<li>UltraConsole Hakkında Menüsü Güncellemesi.</li>
	</ul>
	<li><b>13.03.2025 - V4.1.0.6</b></li>
	<ul>
		<li>UltraConsole Updater for Windows hizmetinde iyileştirme.</li>
	</ul>
	<li><b>13.03.2025 - V4.1.0.7</b></li>
	<ul>
		<li>UltraConsole Updater for Linux hizmetinde iyileştirme.</li>
	</ul>
	<li><b>17.03.2025 - V4.1.1.7</b></li>
	<ul>
		<li>Şifreli Dosya Kasa modülü eklendi.</li>
	</ul>
	<li><b>18.03.2025 - V4.1.2.7</b></li>
	<ul>
		<li>Dosya Kasası modülü için ek güvenlik paketi</li>
		<li>Dosya Kasası modülü için ek iyileştirmeler</li>
	</ul>
	<li><b>18.03.2025 - V4.1.3.7</b></li>
	<ul>
		<li>Dosya Kasası modülü kasa kurtarma seçenekleri eklendi</li>
	</ul>
	<li><b>18.03.2025 - V4.1.3.8</b></li>
	<ul>
		<li>Dosya Kasası modülü ek güvenlik paketi</li>
	</ul>
	<li><b>18.03.2025 - V4.1.4.0</b></li>
	<ul>
		<li>Dosya Kasası modülü iyileştirmesi</li>
	</ul>
	<li><b>08.05.2025 - V</b><b id="version">4.2.0.0</b></li>
	<ul>
		<li>Başlangıçta yapılan güncelleştirme kontrolü sırasında alınan hata düzeltildi</li>
	</ul>
</ul>

</div>