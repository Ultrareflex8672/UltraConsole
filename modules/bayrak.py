import turtle
import atexit
from application.ultraconsole import UltraConsole as UC  

def bayrak(**kwargs):
    UC.create_frame("Bayrak", "Şanlı Sancağı Görmek İçin Tıklayın (Çıkış: 'q')", "info")
    t = turtle.Turtle()
    w = turtle.Screen()
    w.title("ŞANLI SANCAK")         # Başlık
    w.setup(width=720, height=420)  # Pencere Boyutu
    w.bgcolor("red")                # Arka Plan Kırmızı Yap

    # İlk daire
    t.up()
    t.goto(-100, -100)              # Fare imleci lokasyonu
    t.color('white')                # Beyaz renk
    t.begin_fill()                  # Beyaz rengi doldur
    t.circle(120)                   # Çapı
    t.end_fill()

    # Hilal yapabilmek için ikinci daire
    t.goto(-70, -80)                # Fare imleci lokasyonu
    t.color('red')                  # Kırmızı renk
    t.begin_fill()                  # Kırmızı rengi doldur
    t.circle(100)                   # Çapı
    t.end_fill()                    # Dolguyu Bitir

    # Yıldız için hazırlık
    t.goto(0, 35)
    t.fillcolor("white")
    t.begin_fill()

    # Yıldız için tekrar eden üçgen çizimi
    for _ in range(5):
        t.forward(150)
        t.right(144)
    t.end_fill()

    t.goto(-130, -190)
    t.color("white")
    t.write("K. Burak YILDIRIM", font=("Verdana", 17, "bold"))

    # Fare imlecini uzaklaştırarak görüntüyü bozmamasını sağlıyoruz
    t.goto(-999, 0)

    # Çıkış fonksiyonu
    def cikis():
        print("Bayrak kapatıldı.")  # Konsola mesaj yazdır
        w.bye()  # Turtle penceresini kapat
        ana_menu()

    # Sağ üst çarpı tuşuyla kapatıldığında da "Bayrak kapatıldı." mesajı yazdırılır
    atexit.register(lambda: ana_menu())

    def ana_menu():
        UC.create_frame("Bayrak", "Hoşçakalın...", "info")      # Kapatma işlemi öncesinde mesaj yazdır
        UC.go_main_menu()                                       # Ana menüye dön
        
    # "q" tuşuna basıldığında çıkış yapsın
    w.listen()
    w.onkey(cikis, "q")

    # Ekrana tıklanınca programın kapanmasını sağlar
    w.exitonclick()