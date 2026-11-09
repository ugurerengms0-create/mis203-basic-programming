# # # products = ["Notebook", "Pen", "Folder"]

# # # print(products[0]) 
# # # print(products[1])
# # # print(products[2])

# # # products.append("Marker")
# # # print(products)


# # # products[1] = "Blue Pen"
# # # products[0] = "Red Notebook"
# # # products[2] = "Green Folder"
# # # products[3] = "Black Marker"

# # # print(products)
# # # count_of_products = len(products)
# # # print(count_of_products)

# # # alisveris_listesi = ["Ekmek", "Çiğköfte", "Sigara", "Peynir", "Kahve"]
# # # print(alisveris_listesi[2])
# # # print(alisveris_listesi[0])
# # # print(alisveris_listesi[-2])

# # # alisveris_listesi.append("Pide")
# # # print(alisveris_listesi)

# # # count_of_alisveris = len(alisveris_listesi)
# # # print(count_of_alisveris)

# # # alisveris_listesi.insert(2, "Patates")
# # # print(alisveris_listesi)

# # # alisveris_listesi.remove("Ekmek")
# # # print(alisveris_listesi)

# # # silinen = alisveris_listesi.remove("Peynir")
# # # print("Silinen ürün:", silinen)
# # # print(alisveris_listesi)

# # # silinen_pop = alisveris_listesi.pop(1)
# # # print("Silinen ürün:", silinen_pop)
# # # print(alisveris_listesi)

# sayilar = [5, 2, 9, 1, 7, 3, 8, 4, 6]
# # print(sayilar)
# # sayilar.sort()
# # print(sayilar)

# # sorted_sayilar = sorted(sayilar)
# # print("Sıralanmış liste:", sorted_sayilar)

# # reverse_sayilar = sayilar.sort(reverse=True)
# # print("Ters sıralanmış liste:", sayilar)

# # print(sayilar.count(5))

# # sayilar.clear()
# # print(sayilar)

sayilar2 = [1, 2, 3]
sayilar3 = [4, 5, 6]
# #sayilar2.extend(sayilar3)
# print(sayilar2)

sayilar2.append(sayilar3)
# print(sayilar2[3][1])
# # sayilar2.append(sayilar)
print(sayilar2)

sayilar = [1, 2, 3, [4, 5, 6, [7, 8]]]
print(sayilar[0])
print(sayilar[1])
print(sayilar[2])
print(sayilar[3])
print(sayilar[3][0])
print(sayilar[3][1])
print(sayilar[3][2])
print(sayilar[3][3])
print(sayilar[3][3][0])
print(sayilar[3][3][1])