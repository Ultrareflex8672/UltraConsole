import turtle
import time
import random
import atexit
from application.ultraconsole import UltraConsole as UC
import modules.oyunlar as oyunlar

def _pong(**kwargs):
    user_data = kwargs.get("user_data")
    UC.create_frame("Pong", "Pong Oyununa Hoş Geldiniz. Çıkış için 'q' basınız.", "info")
    pencere = turtle.Screen()
    pencere.title("Pong")
    pencere.bgcolor("black")
    pencere.setup(800, 600)
    pencere.tracer(0)

    r1 = turtle.Turtle()
    r1.shape("square")
    r1.color("white")
    r1.shapesize(stretch_wid=5, stretch_len=1)
    r1.penup()
    r1.goto(-350, 0)

    r2 = r1.clone()
    r2.goto(350, 0)

    T = turtle.Turtle()
    T.shape("square")
    T.color("white")
    T.penup()
    T.dx = 2
    T.dy = -2
    PAUSE = False
    bekleme = 0.009
    skor1 = 0
    skor2 = 0

    kalem = turtle.Turtle()
    kalem.color("white")
    kalem.penup()
    kalem.hideturtle()
    kalem.goto(0, 260)
    kalem.write("0 - 0", align="center", font=("Courier", 18, "normal"))

    def r1_yukarı():
        r1.sety(r1.ycor() + 20)

    def r1_asagi():
        r1.sety(r1.ycor() - 20)

    def r2_yukarı():
        r2.sety(r2.ycor() + 20)

    def r2_asagi():
        r2.sety(r2.ycor() - 20)

    def durdur():
        nonlocal PAUSE  # Global yerine nonlocal kullanıldı çünkü iç fonksiyon içinde
        PAUSE = not PAUSE

    def cikis():
        pencere.bye()  # Turtle penceresini kapat
        ana_menu()

    def ana_menu():
        UC.create_frame("Oyun Bitti", "Hoşçakalın...", "info")      # Kapatma işlemi öncesinde mesaj yazdır
        oyunlar.oyunlar_menu(user_data=user_data)

    # Çıkış işlemini izlemek için atexit kullan
    atexit.register(lambda: ana_menu())

    pencere.listen()
    pencere.onkeypress(r1_yukarı, "w")
    pencere.onkeypress(r1_asagi, "s")
    pencere.onkeypress(r2_yukarı, "Up")
    pencere.onkeypress(r2_asagi, "Down")
    pencere.onkey(durdur, "p")
    pencere.onkey(cikis, "q")  # Çıkış için "q" tuşu eklendi

    while True:
        try:
            pencere.update()
            if PAUSE == False:
                T.setx(T.xcor() + T.dx)
                T.sety(T.ycor() + T.dy)

            if T.ycor() > 285:
                T.sety(285)
                T.dy *= -1

            if T.ycor() < -285:
                T.sety(-285)
                T.dy *= -1

            if T.xcor() > 390:
                T.goto(0, 0)
                T.dx *= -1
                skor1 += 1
                kalem.clear()
                kalem.write(f"{skor1} - {skor2}", align="center", font=("Courier", 18, "normal"))

            if T.xcor() < -390:
                T.goto(0, 0)
                T.dx *= -1
                skor2 += 1
                kalem.clear()
                kalem.write(f"{skor1} - {skor2}", align="center", font=("Courier", 18, "normal"))

            if (340 > T.xcor() > 330 and r2.ycor() + 60 > T.ycor() > r2.ycor() - 60):
                T.setx(330)
                T.dx *= -1 + random.randint(-5, 5) * 0.01

            if (-330 > T.xcor() > -340 and r1.ycor() + 60 > T.ycor() > r1.ycor() - 60):
                T.setx(-330)
                T.dx *= -1 + random.randint(-5, 5) * 0.01

            time.sleep(bekleme)
        except turtle.Terminator:
            break  # Pencere kapatıldığında döngüyü kır