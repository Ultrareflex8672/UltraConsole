import json
import os
from application.ultraconsole import UltraConsole as UC
import modules.oyunlar as oyunlar
 
try:
    from termcolor import cprint
except ImportError:
    def cprint(*args, **kwargs):
        print(*args)
name = ""
surname = ""
user_data = {}
kelimeler = ["vantilatör", "adaptör", "kalem", "fare", "telefon", "kulaklık", "pervane", "merdane", "kestane"]
 
 
def oyun_hazirlik():
    """Oyun için gerekli değişkenleri tanımlar"""
    global secilen_kelime, gorunen_kelime, can
    import random
    secilen_kelime = random.choice(kelimeler)
    gorunen_kelime = ["-"] * len(secilen_kelime)
    can = 5
 
 
def harf_al():
    """Kullanıcıdan bir harf alır, alana kadar gerekirse hata verir, birisi quit yazarsa programı kapatır"""
    devam = True
    while devam:
        harf = input("Bir harf giriniz: ")
        if harf.lower() == "quit":
            # cprint("Gidiyor gönlümün efendisi...", color="red", on_color="on_blue")
            # exit()
            ana_menu()
        elif len(harf) == 1 and harf.isalpha() and harf not in gorunen_kelime:
            devam = False
        else:
            # cprint("Hatalı Giriş", color="red", on_color="on_grey")
            UC.create_frame("Hatalı Giriş", "Lütfen tek harf giriniz ve daha önce girilmemiş bir harf giriniz.", "info")
 
    # noinspection PyUnboundLocalVariable
    return harf.lower()

def ana_menu():
        UC.create_frame("Oyun Bitti", "Hoşçakal "+name, "info")      # Kapatma işlemi öncesinde mesaj yazdır
        oyunlar.oyunlar_menu(user_data=user_data)                                          # Ana menüye dön
 
def oyun_dongusu():
    """Oyunun ana döngüsü, harf alır, tutarsa görünen karakterler listesi güncellenir,
     tutmazsa can azaltılır, ve bu can bitene kadar ya da kelime bilinene kadar devam eder..."""
    global gorunen_kelime, can
    while can > 0 and secilen_kelime != "".join(gorunen_kelime):
        # cprint("kelime: " + "".join(gorunen_kelime), color="cyan", attrs=["bold"])
        # cprint("can   : <" + "❤" * can + " " * (5 - can) + ">", color="cyan", attrs=["bold"])
        UC.create_frame("Adam Asmaca", "Kelime: " + "".join(gorunen_kelime) + "          Can: " + "❤" * can)
 
        girilen_harf = harf_al()
        pozisyonlar = harf_kontrol(girilen_harf)
        if pozisyonlar:
            for p in pozisyonlar:
                gorunen_kelime[p] = girilen_harf
        else:
            can -= 1
 
 
def harf_kontrol(girilen_harf):
    """Gelen harfin seçilen kelimede nerelerde olduğunu bulur"""
    poz = []
    for index, h in enumerate(secilen_kelime):
        if h == girilen_harf:
            poz.append(index)
    return poz
 
 
def skor_tablosunu_goster():
    """Skor tablosunu gösterir"""
    veri = ayar_oku()
    # cprint("|Skor\t\tKullanıcı|", color="white", on_color="on_grey")
    # cprint("|------------------------|", color="white", on_color="on_grey")
    # for skor, kullanici in veri["skorlar"]:
    #     cprint("|"+str(skor) +"\t\t"+ kullanici+" "*(9-len(kullanici))+"|", color="white", on_color="on_grey")
    # cprint("|------------------------|", color="white", on_color="on_grey")
    skor_tablosu = []
    for skor, kullanici in veri["skorlar"]:
        skor_tablosu.append(kullanici+": "+str(skor))
    skor_tablosu = skor_tablosu + ["Devam etmek istiyormusunuz? (e/h)"]
    tekrar = UC.create_frame("Skor Tablosu", skor_tablosu, "menu")
    return tekrar
 
 
def skor_tablosunu_guncelle():
    """Skor tablosunu son kullanıcının ismiyle ve skoruyla günceller"""
    veri = ayar_oku()
    veri["skorlar"].append((can, veri["son_kullanan"]))
    veri["skorlar"].sort(key=lambda skor_tuplei: skor_tuplei[0], reverse=True)
    veri["skorlar"] = veri["skorlar"][:5]
    ayar_yaz(veri)
 
 
def oyun_sonucu():
    """Oyun bittiğinde kazanıp kazanamadığımızı ekrana yazar."""
    if can > 0:
        UC.create_frame("Kazandınız","Kelime: "+secilen_kelime)
        skor_tablosunu_guncelle()
    else:
        UC.create_frame("Kaybettiniz","Kelime: "+secilen_kelime)
    tekrar = skor_tablosunu_goster()
    return tekrar
 
 
def dosyay_kontrol_et_yoksa_olustur():
    """Ayar dosyası var mı kontrol eder, varsa sağlam mı diye bakar,
    bozuk ya da olmayan durum için dosyayı öntanımlı değerlerle oluşturur"""
    yaz = False
    if os.path.exists("modules/oyunlar/adamasmaca.json"):
        try:
            ayar_oku()
        except ValueError as e:
            cprint("Hata: ValueError(" + ",".join(e.args) + ")", color="red", on_color="on_blue", attrs=["bold"])
            os.remove("modules/oyunlar/adamasmaca.json")
            yaz = True
    else:
        yaz = True
 
    if yaz:
        ayar_yaz({"skorlar": [], "son_kullanan": ""})
 
 
def ayar_oku():
    """Ayarlar dosyasını okur"""
    with open("modules/oyunlar/adamasmaca.json") as f:
        return json.load(f)
 
 
def ayar_yaz(veri):
    """Ayarlar dosyasına gönderilen veriyi yazar"""
    with open("modules/oyunlar/adamasmaca.json", "w") as f:
        json.dump(veri, f)
 
 
def kullanici_adini_guncelle():
    """Kullanıcıdan isim alıp ayarlara yazdırmaya gönderir"""
    veri = ayar_oku()
    # veri["son_kullanan"] = str(UC.create_frame("Kullanıcı Adı Güncelleme", "Lütfen bir kullanıcı adı giriniz", "\n"))
    name_surname = name+" "+surname
    veri["son_kullanan"] = name_surname[:9]
    while not veri["son_kullanan"] or len(veri["son_kullanan"]) > 9:
        veri["son_kullanan"] = str(UC.create_frame("Kullanıcı Adı Güncelleme", "Kullanıcı adı 9 karakterden uzun olamaz. Lütfen bir kullanıcı adı giriniz.", "\n"))
    ayar_yaz(veri)
 
# orjinal fonksiyon
# def kullanici_kontrol():
#     """Bir önce giriş yapan kullanıcı ismini gösterip kullanıcıya bu siz misiniz diye sorar"""
#     veri = ayar_oku()
#     user_input = UC.create_frame("Kullanıcı Kontrol", "Son giriş yapan: " + veri["son_kullanan"], "Bu siz misiniz? (e/h)\n")
#     if not veri["son_kullanan"]:
#         kullanici_adini_guncelle()
#     elif user_input.lower() == "h":
#         kullanici_adini_guncelle()

def kullanici_kontrol():
    """Bir önce giriş yapan kullanıcı ismini gösterip kullanıcıya bu siz misiniz diye sorar"""
    veri = ayar_oku()
    user_input = "h"
    if not veri["son_kullanan"]:
        kullanici_adini_guncelle()
    elif user_input.lower() == "h":
        kullanici_adini_guncelle()
 
 
def adamasmaca(**kwargs):
    """Programın ana döngüsü, oyunun çalışmasından yükümlü"""
    global user_data
    user_data = kwargs.get("user_data")
    global name
    name = user_data[4]
    global surname
    surname = user_data[5]
    tekrar_edecek_mi = True
    dosyay_kontrol_et_yoksa_olustur()
    UC.create_frame("Adam Asmaca", "Merhaba "+name+", Adam Asmacaya hoşgeldiniz.")
    UC.create_frame("Yardım", "Oyun sırasında quit diyerek çıkabilirsiniz")
    # skor_tablosunu_goster()
    kullanici_kontrol()
    while tekrar_edecek_mi:
        oyun_hazirlik()
        oyun_dongusu()
        tekrar = oyun_sonucu()
        if tekrar.lower() == "h":
        # if input("Devam?(e/h) ").lower() == "h":
            tekrar_edecek_mi = False
    # cprint("Gidiyor gönlümün efendisi...", color="red", on_color="on_blue")