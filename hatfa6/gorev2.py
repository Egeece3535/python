# GÖREV 02 | Yakıt İstasyonu

# Süre: 10 dakika
# Zorluk: Kolay – Orta

# Öğrenciden Beklenenler
# -Başlangıç yakıtı 10 olsun.
# -Maksimum yakıt kapasitesini 25 olarak belirle.
# -Kullanıcıdan yakıt doldurmak isteyip istemediğini öğren.
# -Yakıt doldurulursa 10 birim ekle.
# -Yakıtın 25'i geçmesini engelle.



yakit = 10
maksimum_yakit = 25
yakit_doldur = input("Yakıt Doldurmak İster misiniz? (evet/hayır): ")

if yakit_doldur == "evet":
    yakit += 10
    if yakit > maksimum_yakit:
        yakit = maksimum_yakit
        else:
            print("Yakıt Doldurulmadı.")