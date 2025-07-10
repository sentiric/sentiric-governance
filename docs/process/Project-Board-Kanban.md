# 📋 Sentiric: Proje Yönetim Panosu (Kanban) Kurulumu

Bu doküman, GitHub Projects'te oluşturulacak olan Sentiric proje panosunun yapısını ve kullanım kurallarını tanımlar.

## 1. Pano Kurulumu

1.  `sentiric` organizasyonunun ana sayfasında, "Projects" sekmesine gidin.
2.  "New Project" butonuna tıklayın ve "Board" şablonunu seçin.
3.  Proje adını "Sentiric Platform Geliştirme" olarak belirleyin.

## 2. Sütunlar ve Anlamları

Aşağıdaki sütunlar oluşturulacaktır:

*   **`📚 Backlog` (Fikirler):** Henüz önceliklendirilmemiş, gelecekte yapılabilecek tüm fikirler ve `feature_request`'lar burada toplanır.
*   **`🎯 To Do` (Yapılacaklar):** `NEXT_STEPS_PRIORITIES.md` belgesine göre, Proje Sahibi tarafından yapılmasına karar verilen ve bir sonraki sprint'e/faza dahil edilen görevler (Issue'lar) bu sütuna taşınır.
*   **`⚙️ In Progress` (Geliştiriliyor):** Bir geliştiricinin üzerinde aktif olarak çalışmaya başladığı görevler bu sütuna alınır. Bir görevin bu sütunda birden fazla kişi tarafından aynı anda alınmaması esastır.
*   **`🔍 In Review` (İnceleniyor):** Geliştirme tamamlandığında ve bir Pull Request (PR) açıldığında, ilgili görev bu sütuna taşınır. Kod incelemesi (code review) bu aşamada yapılır.
*   **`✅ Done` (Tamamlandı):** PR onaylanıp `develop` veya `main` branch'ine birleştirildiğinde, görev bu sütuna taşınır.

## 3. Otomasyon Kuralları

*   Yeni oluşturulan bir `Issue`, otomatik olarak `Backlog` sütununa eklenecektir.
*   Bir `Issue`'ya birisi atandığında (`assignee`), otomatik olarak `To Do` sütununa taşınacaktır.
*   Bir `Issue` ile ilişkili bir `Pull Request` açıldığında, `In Progress` sütununa taşınacaktır.
*   `Pull Request` onaylanıp birleştirildiğinde, `Done` sütununa taşınacak ve `Issue` otomatik olarak kapatılacaktır.

Bu yapı, proje ilerlemesinin şeffaf bir şekilde takip edilmesini sağlar.
```

---