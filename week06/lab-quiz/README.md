Projenin Amacı ve Özellikleri

Bu otomasyon sistemi, bir öğrenci kulübünün üye kayıt, branş yönetimi ve sıralama işlemlerini simüle eder. Projede kullanılan temel Python yetenekleri:
- **Tuple (Demet) Kullanımı:** Değiştirilemeyen (`immutable`) ana branş tanımlamaları (`"Yazılım"`, `"Tasarım"`, `"Pazarlama"`).
- **İç İçe Listeler (Nested Lists):** Öğrencilerin ad soyad bilgileri ile seçtikleri branşların bir arada tutulması (`["İsim", ["Branş1", "Branş2"]]`).
- **Veri Temizleme (`strip()`):** Kullanıcı girdilerindeki gereksiz boşlukların ve karakter hatalarının temizlenmesi.
- **Liste Operasyonları:** 
  - `insert(0, ...)` ile en başa özel rol (Başkan) ekleme.
  - `len()` ile toplam öğrenci sayısını hesaplama.
  - `remove()` ile belirli bir öğrenciyi isme göre silme.
  - `pop()` ile listenin sonundaki elemanı çıkarıp raporlama.
- **Sıralama Algoritmaları:** `sorted()` ile orijinal listeyi bozmadan geçici sıralama ve `.sort()` ile kalıcı alfabetik sıralama.
