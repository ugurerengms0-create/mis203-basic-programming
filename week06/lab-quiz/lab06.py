branches = ("Yazılım", "Tasarım", "Pazarlama")

tum_ogrenciler = []

ogrenci_1 = [" İrem ".strip(), [branches[1]]]
ogrenci_2 = ["Baran ".strip(), [branches[2], branches[0]]]
ogrenci_3 = ["Emir".strip(), [branches[2], branches[0], branches[1]]]
ogrenci_4 = ["  Furkan ".strip(), [branches[0]]]
tum_ogrenciler.append(ogrenci_1)
tum_ogrenciler.append(ogrenci_2)
tum_ogrenciler.append(ogrenci_3)
tum_ogrenciler.append(ogrenci_4)

baskan_ogrenci = ["  Uğur ".strip(), [branches[0], branches[1], branches[2]]]
tum_ogrenciler.insert(0, baskan_ogrenci)

# print("Baskan eklendikten sonra tüm öğrenciler ve branşları:", tum_ogrenciler)  

toplam_ogrenci_sayisi = len(tum_ogrenciler)
print("Toplam öğrenci sayısı:", toplam_ogrenci_sayisi)

silinecek = "Baran".strip()
for ogrenci in tum_ogrenciler:
    if ogrenci[0] == silinecek:
        tum_ogrenciler.remove(ogrenci)
        break
# kontrol edelim
print("Silindikten sonra tüm öğrenciler ve branşları:", tum_ogrenciler)
print("**"*50)

cikan_oğrenci = tum_ogrenciler.pop()
print(f"Çıkan öğrenci ve branşları: {cikan_oğrenci}")

# Ekleme
tum_ogrenciler.append(["Burak Tan".strip(), [branches[1]]])
print("---"*30)

gecici_siralama = sorted(tum_ogrenciler)
print("Sıralanmış liste:", gecici_siralama)

# Orjinal listenin değişmediğini kontrol edelim
print("{\nOrjinal liste:", tum_ogrenciler)
# Kalıcı olarak sıralama
tum_ogrenciler.sort()
print("\nKalıcı olarak sıralanmış liste:", tum_ogrenciler)

