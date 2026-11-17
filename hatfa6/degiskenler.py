yakit = 15

print("Başlangıç Yakıtı:",yakit)



print(input("Uçuş yapmak istermisin?")(evet, hayır))

if:
    (input("Uçuş yapmak istermisin?") == "evet"):
    yakit -= 5 
else: 
    print("Uçuş iptal edildi.")


# Koşullarla karar verme
# Uzay gemisinin uçabilmesi için en az 50 birim yakıt gerekmektedir.

if yakit >= 50:
    print("Uçuş Başarılı!")
else:
    print("Yetersiz Yakıt! Gerekli Olan Yakıt Miktarı:",50-yakit)

# =     | Atama işartedir. ve değişkenlere bilgi atar.
# ==    | Soru operatörüdür. bilgiler birbirine eşit mi dye sorar. x == Y y x e eşit mi
# >=    | Büyük veya eşit mi operatörüdür. x >= y. x y ifadesine ya eşittir ya da büyüktür diye sorar
# <=    | Küçük veya eşit mi operatörüdür. x <= y. x y ifadesine ya eşittir ya da küçüktür diye sorar

 