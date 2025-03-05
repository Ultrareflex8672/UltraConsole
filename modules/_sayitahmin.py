import random
from application.ultraconsole import UltraConsole as UC
import modules.oyunlar as oyunlar

def _sayitahmin(**kwargs):
    user_data = kwargs.get("user_data")
    name = user_data[4]
    surname = user_data[5]

    UC.create_frame("Sayı Tahmin Oyunu", "Sayı Tahmin Oyununa Hoş Geldin "+name, "info")

    hak=3
    sayı=random.randint(0,10)
    bilindi=False
    for i in range(hak):
        
        # tahmin=int(input("0-10 arasında bir sayı tahmin ediniz."))
        tahmin = int(UC.create_frame("Tahmin", "0-10 arasında bir sayı tahmin ediniz", "\n"))
        if sayı==tahmin:
            # print("Tebrikler bildiniz.")
            UC.create_frame("Tebrikler "+name, "Tebrikler bildiniz.", "info")
            bilindi=True
            oyunlar.oyunlar_menu(user_data=user_data)
        elif sayı>tahmin and i!=hak-1:
            # print("Daha büyük bir sayı tahmin ediniz.")
            UC.create_frame("Daha Büyük", "Daha büyük bir sayı tahmin ediniz.", "info")
            
        elif sayı<tahmin and i!=hak-1:
            # print("Daha küçük bir sayı tahmin ediniz.")
            UC.create_frame("Daha Küçük", "Daha küçük bir sayı tahmin ediniz.", "info")
    if not bilindi:
        # print("Sayı ",sayı," idi.")
        UC.create_frame("Bilgi", "Sayı "+str(sayı)+" idi.", "info")