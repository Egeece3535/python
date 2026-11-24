# GÖREV 2 | Üç Uçuş Görevi 

# Öğrenciden istenen: Geminin 3 uçuş yapmasını sağla. Her uçuş 5 yakıt tüketsin. Yakıt yetmezse görev sonlansın.
sayi = 15
while sayi > 0:
    print(sayi)
    sayi -= 5

if yakıt < 5:
    print(input('uçuş yapabilirsiniz'))
else:
    print('yakıtınız yetersiz')