# 🚀 Sentiric: Dağıtım (Deployment) Stratejisi (V2.2 - 26 Repo Uyumlu)

Bu doküman, Sentiric platformunun farklı ortamlara (geliştirme, test, üretim) nasıl dağıtılacağını ve sürüm yönetiminin nasıl yapılacağını tanımlar.

## 1. Ortamlar

*   **Geliştirme (Development):** Geliştiricilerin yerel makinelerinde `sentiric-governance` reposundaki `docker-compose.yml` ile çalıştırdığı ortam. Hızlı iterasyon için tasarlanmıştır.
*   **Staging (Test):** Üretim ortamının birebir kopyası olan, ancak gerçek kullanıcı trafiği almayan ortam. Yeni sürümler, üretime geçmeden önce burada test edilir. Bu ortamın altyapı konfigürasyonları `sentiric-infrastructure` reposunda yer alır.
*   **Üretim (Production):** Müşterilere hizmet veren canlı sistem. Bu ortamın altyapı konfigürasyonları `sentiric-infrastructure` reposunda yer alır.

## 2. Konteyner ve İmaj Yönetimi

*   **Dockerfile Yapısı:** Ekosistemdeki tüm **26 ayrı mikroservis/kütüphane deposu**, kendi `Dockerfile`'ları ile paketlenecektir. Bu Dockerfile'lar, **çok aşamalı (multi-stage) Dockerfile'lar** kullanacaktır:
    *   **`builder` Aşaması:** Geliştirme bağımlılıklarını kurar, kodu derler/hazırlar.
    *   **`final` Aşaması:** Sadece uygulamanın çalışması için gerekli olan runtime bağımlılıklarını ve derlenmiş kodları içeren, minimal ve güvenli bir imaj oluşturur.
*   **İmaj Kayıt Merkezi (Registry):** Tüm Docker imajları, `GitHub Container Registry` (ghcr.io) veya `Docker Hub` gibi merkezi bir kayıt merkezinde versiyon etiketleriyle (örn: `sentiric/agent-worker:v1.1.0`) saklanacaktır.

## 3. Sürüm ve Dağıtım Akışı (GitFlow'dan ilhamla)

1.  **Özellik Geliştirme:** Her yeni özellik veya hata düzeltmesi, `develop` branch'inden açılan kendi `feature/...` veya `fix/...` branch'inde geliştirilir. Her bir mikroservis reposunda bağımsız olarak çalışılır.
2.  **Pull Request (PR):** Geliştirme tamamlandığında, ilgili mikroservis reposunun `develop` branch'ine bir PR açılır. Kendi CI testleri (Birim, Entegrasyon) otomatik olarak çalışır ve Docker imajı oluşturulup kayıt merkezine push edilir.
3.  **`develop` Branch'i:** Onaylanan PR'lar `develop` branch'ine birleştirilir. Bu branch, her zaman en son geliştirilen ama henüz yayınlanmamış özellikleri içerir. `develop` branch'ine yapılan her birleştirme, ilgili mikroservisin Docker imajının yenilenmesini tetikler ve otomatik olarak **Staging** ortamına dağıtılır. Bu dağıtım, `sentiric-infrastructure` reposundaki staging konfigürasyonları (Kubernetes YAML'ları veya Docker Compose dosyaları) tarafından yönetilir.
4.  **Sürüm Hazırlığı:** Yeni bir platform sürümü yayınlanmaya karar verildiğinde, tüm ilgili mikroservis repolarının `develop` branch'lerinden `release/v1.1.0` gibi bir sürüm branch'i oluşturulur. Bu branch üzerinde sadece son dakika hata düzeltmeleri yapılır.
5.  **Sürüm Yayınlama:** `release` branch'i stabil olduğunda:
    a. Tüm ilgili mikroservis repolarının `main` branch'lerine birleştirilir.
    b. **`semantic-release`** bu birleştirmeyi algılar, `main` branch'lerine `v1.1.0` gibi bir Git etiketi atar. Bu aynı zamanda Docker imajlarının "release" etiketleriyle de işaretlenmesini sağlar.
    c. Bu etiket, **Üretim** ortamına dağıtımı tetikleyen bir CI/CD işini (job) başlatır. Bu dağıtım, **`sentiric-infrastructure`** reposundaki üretim konfigürasyonları (Kubernetes YAML'ları veya Terraform scriptleri) tarafından yönetilir.
    d. `release` branch'i, `develop` branch'ine de geri birleştirilerek yapılan son düzeltmelerin geliştirme ortamına aktarılması sağlanır.

Bu akış, hem hızlı ve sürekli entegrasyonu (CI) hem de kontrollü ve güvenli dağıtımı (CD) bir arada sunar.

## 4. Dağıtım Otomasyonu Vizyonu (CI/CD)

Mevcut manuel `git pull` ve `docker compose up --build` süreci, geliştirme ve ilk kurulum aşamaları için yeterlidir. Ancak, platform olgunlaştıkça ve güncellemeler sıklaştıkça, bu sürecin otomatize edilmesi kritik öneme sahip olacaktır.

**Hedef:** Herhangi bir servis reposunun `main` branch'ine bir commit atıldığında, bu değişikliğin **otomatik olarak** sunucuya dağıtılmasını sağlayan bir CI/CD pipeline'ı kurmak.

### Örnek CI/CD Akışı (GitHub Actions ile)

1.  **Tetikleyici (Trigger):** Geliştirici, `sentiric-agent-service` reposunun `main` branch'ine yeni bir commit gönderir.

2.  **GitHub Actions Başlar:**
    a. **İnşa (Build):** GitHub'ın kendi sanal sunucusu üzerinde, `sentiric-agent-service`'in Dockerfile'ı kullanılarak yeni bir Docker imajı oluşturulur.
    b. **Etiketleme (Tagging):** Bu imaj, commit hash'i veya sürüm numarası ile etiketlenir (örn: `ghcr.io/sentiric/sentiric-agent-service:v0.1.3`).
    c. **Yayınlama (Push):** Etiketlenen imaj, `GitHub Container Registry` (ghcr.io) gibi merkezi bir Docker kayıt merkezine gönderilir.

3.  **Sunucuyu Bilgilendirme (Webhook/SSH):**
    a. **Webhook Yöntemi:** GitHub Actions, sunucumuzda çalışan küçük bir "webhook dinleyici" servisine (örn: `webhookd`) "Yeni bir `agent-service` imajı var!" diye bir sinyal gönderir.
    b. **SSH Yöntemi:** GitHub Actions, sunucumuza güvenli bir şekilde SSH ile bağlanır.

4.  **Sunucuda Otomatik Güncelleme:**
    a. Webhook dinleyicisi veya SSH komutu, sunucuda basit bir `update.sh` script'ini tetikler.
    b. Bu script, `sentiric-infrastructure` klasörüne gider ve şu komutları çalıştırır:
       ```bash
       # En son imajı çek
       docker compose pull sentiric-agent-service
       # Sadece değişen servisi yeniden başlat
       docker compose up -d --no-deps sentiric-agent-service
       ```

Bu otomasyon, güncellemeleri saniyeler içinde, hatasız ve insan müdahalesi olmadan canlıya almamızı sağlayacaktır. Bu, projemizin **Faz 2 - Platformlaşma ve Geliştirici Deneyimi (DX)** hedeflerinin bir parçası olarak ele alınacaktır.