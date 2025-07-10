# 🚀 Sentiric: Dağıtım (Deployment) Stratejisi

Bu doküman, Sentiric platformunun farklı ortamlara (geliştirme, test, üretim) nasıl dağıtılacağını ve sürüm yönetiminin nasıl yapılacağını tanımlar.

## 1. Ortamlar

*   **Geliştirme (Development):** Geliştiricilerin yerel makinelerinde `docker-compose` ile çalıştırdığı ortam. Hızlı iterasyon için tasarlanmıştır.
*   **Staging (Test):** Üretim ortamının birebir kopyası olan, ancak gerçek kullanıcı trafiği almayan ortam. Yeni sürümler, üretime geçmeden önce burada test edilir.
*   **Üretim (Production):** Müşterilere hizmet veren canlı sistem.

## 2. Konteyner ve İmaj Yönetimi

*   **Dockerfile Yapısı:** Tüm servisler, **çok aşamalı (multi-stage) Dockerfile'lar** kullanacaktır.
    *   **`builder` Aşaması:** Geliştirme bağımlılıklarını kurar, kodu derler/hazırlar.
    *   **`final` Aşaması:** Sadece uygulamanın çalışması için gerekli olan runtime bağımlılıklarını ve derlenmiş kodları içeren, minimal ve güvenli bir imaj oluşturur.
*   **İmaj Kayıt Merkezi (Registry):** Tüm Docker imajları, `GitHub Container Registry` veya `Docker Hub` gibi merkezi bir kayıt merkezinde versiyon etiketleriyle saklanacaktır.

## 3. Sürüm ve Dağıtım Akışı (GitFlow'dan ilhamla)

1.  **Özellik Geliştirme:** Her yeni özellik veya hata düzeltmesi, `develop` branch'inden açılan kendi `feature/...` veya `fix/...` branch'inde geliştirilir.
2.  **Pull Request (PR):** Geliştirme tamamlandığında, `develop` branch'ine bir PR açılır. CI testleri (Birim, Entegrasyon) otomatik olarak çalışır.
3.  **`develop` Branch'i:** Onaylanan PR'lar `develop` branch'ine birleştirilir. Bu branch, her zaman en son geliştirilen ama henüz yayınlanmamış özellikleri içerir. `develop` branch'ine yapılan her birleştirme, otomatik olarak **Staging** ortamına dağıtılır.
4.  **Sürüm Hazırlığı:** Yeni bir sürüm yayınlanmaya karar verildiğinde, `develop` branch'inden `release/v1.1.0` gibi bir sürüm branch'i oluşturulur. Bu branch üzerinde sadece son dakika hata düzeltmeleri yapılır.
5.  **Sürüm Yayınlama:** `release` branch'i stabil olduğunda:
    a. `main` branch'ine birleştirilir.
    b. **`semantic-release`** bu birleştirmeyi algılar, `main` branch'ine `v1.1.0` gibi bir Git etiketi atar.
    c. Bu etiket, **Üretim** ortamına dağıtımı tetikleyen bir CI/CD işini (job) başlatır.
    d. `release` branch'i, `develop` branch'ine de geri birleştirilerek yapılan son düzeltmelerin geliştirme ortamına aktarılması sağlanır.

Bu akış, hem hızlı ve sürekli entegrasyonu (CI) hem de kontrollü ve güvenli dağıtımı (CD) bir arada sunar.

---