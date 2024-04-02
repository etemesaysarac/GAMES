import turtle
import random

# Pencere oluştur
win = turtle.Screen()
win.title("Catch the Turtle")
win.bgcolor("gray")

# Kaplumbağa oluştur
kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.color("green")
kaplumbaga.penup()

# Skor
skor = 0

# Skor yazısı oluştur
skor_yazısı = turtle.Turtle()
skor_yazısı.speed(0)
skor_yazısı.color("orange")
skor_yazısı.penup()
skor_yazısı.hideturtle()
skor_yazısı.goto(0, 260)
skor_yazısı.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))

# Zaman sayacı
zaman = 15

# Zaman yazısı oluştur
zaman_yazısı = turtle.Turtle()
zaman_yazısı.speed(0)
zaman_yazısı.color("orange")
zaman_yazısı.penup()
zaman_yazısı.hideturtle()
zaman_yazısı.goto(0, -260)
zaman_yazısı.write("Zaman: {}".format(zaman), align="center", font=("Courier", 24, "normal"))

# Pencere boyutları
max_x = win.window_width() // 2
max_y = win.window_height() // 2


# Rastgele hareket fonksiyonu
def rastgele_hareket():
    global zaman
    if zaman > 0:
        # Rastgele x ve y koordinatları seç
        yeni_x = random.randint(-max_x, max_x)
        yeni_y = random.randint(-max_y, max_y)

        # Kaplumbağayı yeni konuma yerleştir
        kaplumbaga.goto(yeni_x, yeni_y)

        # Zaman sıfır olana kadar hareket etmeyi sürdür
        win.ontimer(rastgele_hareket, 900)  # Yeni hareketi planla


# Rastgele hareketi başlat
rastgele_hareket()


# Zamanı azaltma işlevi
def zamanı_azalt():
    global zaman
    zaman -= 1
    zaman_yazısı.clear()
    zaman_yazısı.write("Zaman: {}".format(zaman), align="center", font=("Courier", 24, "normal"))
    if zaman > 0:
        win.ontimer(zamanı_azalt, 1000)  # 1 saniye sonra tekrar çağır
    else:
        kaplumbaga.onclick(None)  # Fare tıklama işlevini kaldır


# Zamanı başlat
zamanı_azalt()


# Kaplumbağayı yakalama işlevi
def kaplumbaga_yakala(x, y):
    global skor
    if zaman > 0:
        skor += 1
        skor_yazısı.clear()
        skor_yazısı.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))


# Fare tıklama işlevini belirt
kaplumbaga.onclick(kaplumbaga_yakala)

# Pencereyi kapat
win.mainloop()