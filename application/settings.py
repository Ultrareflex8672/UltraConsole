import os

CONFIG_FILE = "config.txt"  # Dosya adını burada belirleyin

def oku_ve_goster():
    """Dosyayı okuyarak içeriğini ekrana yazdırır."""
    if not os.path.exists(CONFIG_FILE):
        print("Konfigürasyon dosyası bulunamadı, yeni bir tane oluşturuluyor...")
        with open(CONFIG_FILE, "w") as f:
            f.write("menu_file = config/menu.cfg\nmenu_root = 0\nmodule_path = modules\n")
    
    with open(CONFIG_FILE, "r") as f:
        lines = f.readlines()
    
    config_dict = {}
    for line in lines:
        if "=" in line:
            key, value = line.strip().split("=", 1)
            config_dict[key.strip()] = value.strip()
    
    return config_dict

def ayarlari_goster(ayarlar):
    """Ayarları ekrana listeler."""
    print("\nMevcut Ayarlar:")
    for i, (key, value) in enumerate(ayarlar.items(), 1):
        print(f"{i}. {key} = {value}")

def ayar_degistir(ayarlar):
    """Kullanıcının belirli bir ayarı değiştirmesine izin verir."""
    while True:
        ayarlari_goster(ayarlar)
        secim = input("\nDeğiştirmek istediğiniz ayarın numarasını girin (Çıkış için 'q'): ")
        
        if secim.lower() == "q":
            break
        
        if secim.isdigit() and 1 <= int(secim) <= len(ayarlar):
            secim_index = int(secim) - 1
            secilen_anahtar = list(ayarlar.keys())[secim_index]
            yeni_deger = input(f"{secilen_anahtar} için yeni değeri girin: ")
            ayarlar[secilen_anahtar] = yeni_deger
        else:
            print("Geçersiz seçim, tekrar deneyin.")

def ayarlari_kaydet(ayarlar):
    """Ayarları dosyaya kaydeder."""
    with open(CONFIG_FILE, "w") as f:
        for key, value in ayarlar.items():
            f.write(f"{key} = {value}\n")
    print("Ayarlar başarıyla kaydedildi!")

def main():
    """Programın ana akışı."""
    ayarlar = oku_ve_goster()
    ayar_degistir(ayarlar)
    ayarlari_kaydet(ayarlar)

if __name__ == "__main__":
    main()
