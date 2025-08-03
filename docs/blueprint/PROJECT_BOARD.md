### **Sentiric Platformu: Bütünleşik Eylem Planı (v3.0)**

Bu belge, stratejik yol haritasını, taktiksel görev panosunu ve teknik iyileştirme önerilerini tek bir yerde birleştiren, projenin ana eylem planıdır.

#### **Nasıl Okunmalı?**

*   **[Mevcut Görev]:** Orijinal `PROJECT_BOARD.md`'den gelen görev.
*   **[Zenginleştirilmiş Görev  enriquecido]:** Orijinal bir görevin, AI analizinden gelen önerilerle detaylandırılmış ve kapsamı genişletilmiş hali.
*   **[Yeni Görev 🚀]:** AI analizinde tespit edilen ve projenin kalitesini artırmak için eklenen yeni, kritik görev.

---

### **FAZ 1: GÜVENLİ VE DAĞITIK OMURGA**

**Hedef:** Platformun temel iskeletini, çoklu sunucu ortamlarında güvenli, dayanıklı, gözlemlenebilir ve **test edilebilir** bir şekilde çalışacak hale getirmek. Bu, üzerine inşa edilecek tüm servislerin sağlam zeminidir.

| ID | Görev | Öncelik | Repo(lar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P1-T01**| **[Mevcut Görev]: Altyapı:** Profil Tabanlı Dağıtım Stratejisi Oluşturma | **Kritik** | `infrastructure` | `[ ✔️ ] Done` |
| **P1-T02**| **[Mevcut Görev]: Altyapı:** Dayanıklı Başlatma için `healthcheck` ve `depends_on` entegrasyonu | **Kritik** | `infrastructure` | `[ ✔️ ] Done` |
| **P1-T03**| **[Zenginleştirilmiş Görev  enriquecido]: Güvenlik:** Tüm gRPC İletişimini mTLS ile Güvenli Hale Getirme<br>*(**Ek:** Dış dünyadan gelen tüm girdiler için daha sağlam ayrıştırma (parsing) ve doğrulama kütüphaneleri kullanarak güvenlik katmanını artırmak.)*| **Kritik** | Tüm gRPC servisleri | `[ ] To Do` |
| **P1-T04**| **[Mevcut Görev]: DevOps:** Ortama Duyarlı (Console/JSON) Loglama Yapısını Tüm Servislere Uygulama | **Yüksek** | Tüm servisler | `[ ] To Do` |
| **P1-T05**| **[Zenginleştirilmiş Görev enriquecido]: API:** `api-gateway-service` iskeletini oluşturma ve mTLS ile güvenli hale getirme<br>*(**Ek:** Dış istekler için **Kimlik Doğrulama (JWT/OAuth2)**, **Yetkilendirme (RBAC)** ve **Rate Limiting** katmanlarını implemente etmek.)*| Yüksek | `api-gateway-service` | `[ ] To Do`|
| **P1-T06**| **[Mevcut Görev]: Test:** `cli` üzerinden `api-gateway` aracılığıyla `user-service`'e ulaşan ilk uçtan uca testi yazma | Yüksek | `cli`, `api-gateway-service`, `user-service` | `[ ] To Do` |
| **P1-T07**| **[Mevcut Görev]: Kod Kalitesi:** Go servislerinde versiyon tutarlılığını sağlama | Orta | Go Servisleri | `[ ] To Do` |
| **P1-T08**| **[Mevcut Görev]: Kod Kalitesi:** Ortam değişkeni isimlendirmesini standartlaştırma | Orta | `infrastructure`, Tüm servisler | `[ ] To Do` |
| **P1-T09**| **[Mevcut Görev]: DevOps:** Tüm CI/CD pipeline'larına Docker build cache ekleme | Orta | Tüm servisler | `[ ] To Do` |
| **P1-T10**| **[Yeni Görev 🚀]: Test:** Tüm servisler için **Birim Testi (Unit Test)** altyapısını kurmak ve kritik fonksiyonlar için testler yazmak. | **Kritik**| Tümü | `[ ] To Do` |
| **P1-T11**| **[Yeni Görev 🚀]: DevOps:** Tüm CI/CD pipeline'larına **Test** (`go test`) ve **Linting** (`golangci-lint`) adımlarını eklemek. | **Kritik**| Tümü | `[ ] To Do` |
| **P1-T12**| **[Yeni Görev 🚀]: Kod Kalitesi:** Monolitik `main.go` dosyalarını, `internal` paket yapısını kullanarak **modüler hale getirmek** ve "sihirli değişkenleri" (magic strings) `const` olarak tanımlamak.| **Yüksek**| Go Servisleri | `[ ] To Do` |
| **P1-T13**| **[Yeni Görev 🚀]: DevOps:** Üretim ortamı için **Kubernetes geçişini planlamak** ve ilk manifestoları oluşturmak. | **Orta**| `infrastructure` | `[ ] To Do` |
| **P1-T14**| **[Yeni Görev 🚀]: Güvenlik:** Üretim ortamı için **HashiCorp Vault** veya benzeri merkezi bir **sır yönetimi (secret management)** çözümünü araştırmak ve planlamak. | **Orta**| `infrastructure`, Tüm Servisler | `[ ] To Do` |

---

### **FAZ 2: FONKSİYONEL İSKELET**

**Hedef:** Omurga üzerine, bir telefon çağrısını baştan sona yönetebilen temel servisleri (iskeleti) yerleştirmek.

| ID | Görev | Öncelik | Repo(lar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P2-T01**| **[Mevcut Görev]: Veritabanı:** `init.sql` ile "Genesis Bloğu" (tüm tablolar) mantığını tamamlama| **Kritik**| `infrastructure` | `[ ] To Do` |
| **P2-T02**| **[Mevcut Görev]: Çekirdek:** `dialplan-service`'in DB'den okuyarak dinamik karar verme yeteneği | **Kritik**| `dialplan-service` | `[ ] To Do` |
| **P2-T03**| **[Mevcut Görev]: Çekirdek:** `user-service`'in DB'den `GetUser` ve `CreateUser` yetenekleri | **Kritik**| `user-service` | `[ ] To Do` |
| **P2-T04**| **[Mevcut Görev]: Telekom:** `sip-signaling`'in `dialplan`, `user`, `media` servislerini orkestre etmesi | **Yüksek**| `sip-signaling-service` | `[ ] To Do` |
| **P2-T05**| **[Mevcut Görev]: Telekom:** `media-service`'in `Allocate/ReleasePort` ve temel SRTP hazırlıklarını tamamlaması | **Yüksek**| `media-service` | `[ ] To Do` |
| **P2-T06**| **[Mevcut Görev]: Olaylaşma:** `sip-signaling`'in `call.started` ve `call.ended` olaylarını RabbitMQ'ya atması| Yüksek| `sip-signaling-service`| `[ ] To Do` |
| **P2-T07**| **[Mevcut Görev]: Raporlama:** `cdr-service`'in bu olayları dinleyip DB'ye temel kayıtları atması | Yüksek| `cdr-service` | `[ ] To Do` |
| **P2-T08**| **[Mevcut Görev]: Test:** `cli` ile tam bir çağrı akışını (INVITE -> BYE) simüle edip DB'de CDR kaydını doğrulama | Yüksek| `cli`, `cdr-service` | `[ ] To Do` |

---

### **FAZ 3: CANLANAN PLATFORM**

**Hedef:** İskelete "beyin" ve "ses" ekleyerek platformu canlandırmak.

| ID | Görev | Öncelik | Repo(lar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P3-T01**| **[Zenginleştirilmiş Görev enriquecido]: AI Çekirdek:** `agent-service`'de Durum Makinesi implementasyonu<br>*(**Ek:** Bu implementasyon, çağrı durumunu **Redis**'te saklayarak servisi "stateless" (durumsuz) hale getirmelidir.)*| **Kritik**| `agent-service` | `[ ] To Do` |
| **P3-T02**| **[Mevcut Görev]: AI Çekirdek:** `llm-service`'in `agent-service` ile entegrasyonu | **Kritik**| `llm-service`, `agent-service` | `[ ] To Do` |
| **P3-T03**| **[Mevcut Görev]: AI Duyular:** `tts-service` ve `stt-service` iskeletlerinin oluşturulması ve entegrasyonu | **Yüksek**| `tts-service`, `stt-service`, `agent-service` | `[ ] To Do` |
| **P3-T04**| **[Mevcut Görev]: Akış:** `agent-service`'in `dialplan` kararına göre `media-service`'e `PlayAudio` komutu göndermesi | **Yüksek**| `agent-service`, `media-service` | `[ ] To Do` |
| **P3-T05**| **[Mevcut Görev]: UI:** `dashboard-ui`'nin `api-gateway` üzerinden `cdr-service` verilerini göstermesi | Yüksek| `dashboard-ui`, `api-gateway-service` | `[ ] To Do` |
| **P3-T06**| **[Mevcut Görev]: Test:** Gerçek bir telefonla arama yapıp sistemin ilk anonsunu duyma (Uçtan Uca Test) | Yüksek| Tümü | `[ ] To Do` |
| **P3-T07**| **[Mevcut Görev]: AI Akışı:** `agent-service`'in gelecekteki "streaming" API'leri destekleyecek şekilde tasarlanması| Orta | `agent-service` | `[ ] To Do` |

---

### **FAZ 4: AKILLI VE İNSAN ODAKLI PLATFORM**

*(Bu fazdaki görevler, ilk 3 faz tamamlandıktan sonra yeniden değerlendirilecektir.)*

| ID | Görev | Öncelik | Repo(lar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P4-T01**| **[Mevcut Görev]: UI:** `web-agent-ui` iskeletinin oluşturulması ve çağrı devri için altyapı hazırlığı | **Kritik**| `web-agent-ui` | `[ ] To Do` |
| **P4-T02**| **[Mevcut Görev]: Akış:** `agent-service`'den `web-agent-ui`'ye çağrı devri akışının tasarlanması | **Kritik**| `agent-service`, `web-agent-ui` | `[ ] To Do` |
| **P4-T03**| **[Mevcut Görev]: AI Zeka:** `knowledge-service` (RAG) iskeletinin oluşturulması ve `agent-service` entegrasyonu | **Yüksek**| `knowledge-service`, `agent-service` | `[ ] To Do` |
| **P4-T04**| **[Mevcut Görev]: Entegrasyon:** `connectors-service` için ilk konektörün (örn. Google Calendar) geliştirilmesi | Yüksek| `connectors-service` | `[ ] To Do` |
| **P4-T05**| **[Mevcut Görev]: DX:** `sentiric-cli`'ye "Geliştirici Sandbox" modunun eklenmesi | Orta| `cli` | `[ ] To Do` |
| **P4-T06**| **[Mevcut Görev]: UI/UX:** `dashboard-ui` üzerine "Low-Code Dialplan Tasarımcısı" v1.0 eklenmesi | Orta| `dashboard-ui` | `[ ] To Do` |