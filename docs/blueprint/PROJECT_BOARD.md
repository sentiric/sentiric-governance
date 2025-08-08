### **Sentiric Platformu: Bütünleşik Eylem Planı (v4.1)**

Bu belge, stratejik yol haritasını, taktiksel görev panosunu ve teknik iyileştirme önerilerini tek bir yerde birleştiren, projenin ana eylem planıdır.

#### **Geliştirme Manifestosu: Her Servis İçin Altın Kurallar**

*Her yeni servis oluşturulduğunda veya mevcut bir servis güncellendiğinde aşağıdaki prensiplere uyulmalıdır:*

1.  **Gözlemlenebilirlik Temeldir:** Servis, `OBSERVABILITY_STANDARD.md`'ye uygun olarak ortama duyarlı (Console/JSON) yapılandırılmış loglama, Prometheus metrikleri ve `trace_id` yayma yeteneklerine sahip olmalıdır.
2.  **Güvenlik Varsayılandır:** Servisler arası iletişim **mTLS** ile şifrelenmeli, tüm harici API'ler yetkilendirilmelidir. Sırlar (secrets) asla kodda yer almamalıdır.
3.  **Üretime Hazır Tasarım:** Servis, `healthcheck` endpoint'lerine sahip olmalı, "Graceful Shutdown" mekanizmasını implemente etmeli ve Kubernetes gibi ortamlarda çalışabilecek şekilde tasarlanmalıdır.
4.  **Test Edilebilirlik Zorunluluktur:** Kritik iş mantıkları, CI/CD pipeline'ında çalıştırılan **birim testleri (unit tests)** ile kapsanmalıdır.
5.  **Dokümantasyon Canlıdır:** Servisin `README.md` dosyası, sorumluluklarını, API'lerini ve nasıl çalıştırılacağını net bir şekilde açıklamalıdır. `governance`'daki ana dokümanlarla tutarlı olmalıdır.
6.  **İşlem Bütünlüğü:** Her commit, tam ve eksiksiz bir işlevi (kod, test, dokümantasyon) temsil etmeli ve başarılı bir şekilde test edildikten sonra yapılmalıdır.

#### **Nasıl Okunmalı?**

*   **[Görev]:** Mevcut görev panosundan gelen, kapsamı netleştirilmiş görev.
*   **[Yeni Görev 🚀]:** Son analizlerde tespit edilen ve projenin kalitesini, ölçeklenebilirliğini veya vizyonunu ileriye taşımak için eklenen yeni, kritik görev.
*   **Durum:** `[ ✔️ ] Done`, `[ ⏳ ] WIP (Devam Ediyor)`, `[ ⬜ ] To Do`

---

### **FAZ 1: GÜVENLİ VE DAYANIKLI OMURGA**

**Hedef:** Platformun temel iskeletini, çoklu sunucu ortamlarında güvenli, dayanıklı, gözlemlenebilir ve test edilebilir bir şekilde çalışacak hale getirmek. Bu, üzerine inşa edilecek tüm servislerin sağlam zeminidir.

| ID | Görev | Öncelik | Repo(lar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P1-T01**| **[Görev]: Altyapı:** Profil Tabanlı Dağıtım Stratejisi Oluşturma | **Kritik** | `infrastructure` | `[ ✔️ ] Done` |
| **P1-T02**| **[Görev]: Altyapı:** Dayanıklı Başlatma için `healthcheck` ve `depends_on` entegrasyonu | **Kritik** | `infrastructure` | `[ ✔️ ] Done` |
| **P1-T03**| **[Görev]: Güvenlik:** Tüm gRPC İletişimini mTLS ile Güvenli Hale Getirme | **Kritik** | Tüm gRPC servisleri | `[ ✔️ ] Done` |
| **P1-T04**| **[Yeni Görev 🚀]: Mimari:** RabbitMQ Mimarisi'ni "Fanout Exchange" Modelin'e Geçirme | **Kritik**| `sip-signaling`, `agent-service`, `cdr-service` | `[ ⬜ ] To Do` |
| **P1-T05**| **[Yeni Görev 🚀]: Test:** Kritik İş Mantığı için Birim Testi (Unit Test) Altyapısını Kurma | **Kritik**| `dialplan-service`, `agent-service`, Tümü | `[ ⬜ ] To Do` |
| **P1-T06**| **[Yeni Görev 🚀]: DevOps:** Tüm CI/CD pipeline'larına Test (`go test`) ve Linting (`golangci-lint`) adımlarını eklemek. | **Kritik**| Tümü | `[ ⬜ ] To Do` |
| **P1-T07**| **[Yeni Görev 🚀]: Kod Kalitesi:** Monolitik `main.go` dosyalarını `internal` paket yapısıyla modüler hale getirme | **Yüksek**| `user-service`, `dialplan-service` | `[ ⬜ ] To Do` |
| **P1-T08**| **[Görev]: API:** `api-gateway-service` iskeletini oluşturma ve mTLS ile güvenli hale getirme | Yüksek | `api-gateway-service` | `[ ⬜ ] To Do`|
| **P1-T09**| **[Görev]: Test:** `cli` üzerinden `api-gateway` aracılığıyla `user-service`'e ulaşan ilk uçtan uca testi yazma | Yüksek | `cli`, `api-gateway-service`, `user-service` | `[ ⬜ ] To Do` |
| **P1-T10**| **[Yeni Görev 🚀]: Kod Kalitesi:** Ortam değişkenleri ve Dockerfile'lar için standardizasyon sağlama | Orta | Tümü, `infrastructure`, `governance` | `[ ⬜ ] To Do` |

---

### **FAZ 1.5: GÖZLEMLENEBİLİRLİK OMURGASI**

**Hedef:** Platformun her bir parçasını izlenebilir, ölçülebilir ve hataların kolayca ayıklanabilir hale getirmek. Bu, projenin hem geliştirme hızını hem de üretim kararlılığını artıracak temel bir yatırımdır.

| ID | Görev | Öncelik | Repo(lar) | Durum |
|:---|:---|:---|:---|:---|
| **OBS-01** | **[Görev]:** `OBSERVABILITY_STANDARD.md` dokümanını oluşturmak ve ana dokümanları güncellemek. | **Kritik** | `governance` | `[ ✔️ ] Done` |
| **OBS-02** | **[Görev]:** Tüm servislerde standart ve ortama duyarlı (JSON/Console) loglamayı implemente etmek. | **Kritik** | Tümü | `[ ⏳ ] WIP` |
| **OBS-03** | **[Yeni Görev 🚀]:** Altyapıya Prometheus ve Grafana eklemek. | **Yüksek** | `infrastructure` | `[ ⬜ ] To Do` |
| **OBS-04** | **[Yeni Görev 🚀]:** Tüm servislere Prometheus `/metrics` endpoint'ini ve temel RED metriklerini eklemek. | **Yüksek** | Tümü | `[ ⬜ ] To Do` |
| **OBS-05** | **[Yeni Görev 🚀]:** Ağ geçitlerinde (`sip-gateway`, `api-gateway`) `trace_id` oluşturma ve yayma mekanizmasını implemente etmek. | **Yüksek** | `sip-gateway`, `api-gateway` | `[ ⬜ ] To Do` |
| **OBS-06** | **[Yeni Görev 🚀]:** Diğer tüm servislerde gelen `trace_id`'yi yakalama ve yayma (context propagation) işlemini implemente etmek. | **Yüksek** | Tümü | `[ ⬜ ] To Do` |
| **OBS-07** | **[Yeni Görev 🚀]:** Altyapıya Jaeger/Tempo (tracing backend) eklemek. | **Orta** | `infrastructure` | `[ ⬜ ] To Do` |

---

### **FAZ 2: FONKSİYONEL İSKELET**

**Hedef:** Omurga üzerine, bir telefon çağrısını baştan sona yönetebilen ve yeni yeteneklerin eklenebileceği temel servisleri (iskeleti) yerleştirmek.

| ID | Görev | Öncelik | Repo(lar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P2-T01**| **[Görev]: Veritabanı:** `init.sql` ile "Genesis Bloğu" (tüm tablolar) mantığını tamamlama| **Kritik**| `infrastructure` | `[ ✔️ ] Done` |
| **P2-T02**| **[Görev]: Çekirdek:** `dialplan-service` ve `user-service`'in veritabanından okuma/yazma yetenekleri | **Kritik**| `dialplan-service`, `user-service` | `[ ✔️ ] Done` |
| **P2-T03**| **[Görev]: Telekom:** `sip-signaling` ve `media-service`'in temel çağrı kurma ve port yönetimi yetenekleri | **Yüksek**| `sip-signaling-service`, `media-service` | `[ ✔️ ] Done` |
| **P2-T04**| **[Görev]: Olaylaşma:** `sip-signaling`'in `call.started/ended` olaylarını RabbitMQ'ya atması | Yüksek | `sip-signaling-service` | `[ ✔️ ] Done` |
| **P2-T05**| **[Görev]: Raporlama:** `cdr-service`'in olayları dinleyip DB'ye temel kayıtları atması | Yüksek | `cdr-service` | `[ ⬜ ] To Do` |
| **P2-T06**| **[Görev]: Test:** `cli` ile tam bir çağrı akışını (INVITE -> BYE) simüle edip DB'de CDR kaydını doğrulama | Yüksek | `cli`, `cdr-service` | `[ ⬜ ] To Do` |
| **P2-T07**| **[Yeni Görev 🚀]: Çekirdek:** `sentiric-task-service` iskeletini (Celery/Redis) oluşturma | **Yüksek** | `task-service`, `infrastructure` | `[ ⬜ ] To Do` |
| **P2-T08**| **[Yeni Görev 🚀]: Entegrasyon:** `sentiric-messaging-gateway-service` iskeletini oluşturma | **Orta** | `messaging-gateway-service`, `infrastructure` | `[ ⬜ ] To Do` |
| **P2-T09**| **[Yeni Görev 🚀]: Veri Bütünlüğü:** `saga_transactions` tablosunu `init.sql`'e ekle | **Yüksek** | `infrastructure` | `[ ⬜ ] To Do` |
| **P2-T10**| **[Yeni Görev 🚀]: Veri Bütünlüğü:** `agent-service`'de `SagaManager` modülünün iskeletini oluştur | **Yüksek** | `agent-service` | `[ ⬜ ] To Do` |
| **P2-T11**| **[Yeni Görev 🚀]: Veri Bütünlüğü:** Katılımcı servislerde temel işlem/tazmin endpoint'lerini tanımla | **Orta** | `user-service`, `connectors-service` | `[ ⬜ ] To Do` |
| **P2-T12**| **[Yeni Görev 🚀]: Veri Bütünlüğü:** `cli` ile ilk SAGA akışını tetikleyen bir prototip test yaz | **Orta** | `cli`, `agent-service` | `[ ⬜ ] To Do` |

---

### **FAZ 3: CANLANAN PLATFORM**

**Hedef:** İskelete "beyin" ve "ses" ekleyerek platformu, arayanla anlamlı bir diyalog kurabilen akıllı bir sisteme dönüştürmek.

| ID | Görev | Öncelik | Repo(lar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P3-T01**| **[Yeni Görev 🚀]: AI Çekirdek:** `agent-service`'de Redis tabanlı Durum Makinesi (State Machine) implementasyonu | **Kritik**| `agent-service`, `infrastructure` | `[ ⬜ ] To Do` |
| **P3-T02**| **[Görev]: AI Çekirdek:** `llm-service`'in `agent-service` ile entegrasyonu | **Kritik**| `llm-service`, `agent-service` | `[ ✔️ ] Done` |
| **P3-T03**| **[Görev]: Akış:** `agent-service`'in `dialplan` kararına göre `media-service`'e `PlayAudio` komutu göndermesi | **Yüksek**| `agent-service`, `media-service` | `[ ✔️ ] Done` |
| **P3-T04**| **[Görev]: AI Duyular:** `tts-service` ve `stt-service` iskeletlerinin oluşturulması ve entegrasyonu
| **P3-T05**| **[Görev]: UI:** `dashboard-ui`'nin `api-gateway` üzerinden `cdr-service` verilerini göstermesi | Yüksek | `dashboard-ui`, `api-gateway-service` | `[ ⬜ ] To Do` |
| **P3-T06**| **[Görev]: Test:** Gerçek bir telefonla arama yapıp sistemin ilk anonsunu duyma (Uçtan Uca Test) | Yüksek | Tümü | `[ ✔️ ] Done` |

---

### **FAZ 4: AKILLI VE GENİŞLETİLEBİLİR PLATFORM**

*(Bu fazdaki görevler, ilk 3 faz tamamlandıktan sonra yeniden değerlendirilecektir.)*

| ID | Görev | Öncelik | Repo(lar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P4-T01**| **[Görev]: UI:** `web-agent-ui` iskeletinin oluşturulması ve çağrı devri için altyapı hazırlığı | **Kritik**| `web-agent-ui` | `[ ⬜ ] To Do` |
| **P4-T02**| **[Görev]: AI Zeka:** `knowledge-service` (RAG) iskeletinin oluşturulması ve `agent-service` entegrasyonu | **Yüksek**| `knowledge-service`, `agent-service` | `[ ⬜ ] To Do` |
| **P4-T03**| **[Görev]: Entegrasyon:** `connectors-service` için ilk konektörün (örn. Google Calendar) geliştirilmesi | Yüksek| `connectors-service` | `[ ⬜ ] To Do` |
| **P4-T04**| **[Yeni Görev 🚀]: Vizyon:** `sentiric-marketplace-service` iskeletini oluşturma | **Orta** | `marketplace-service`, `infrastructure` | `[ ⬜ ] To Do` |
| **P4-T05**| **[Görev]: UI/UX:** `dashboard-ui` üzerine "Low-Code Dialplan Tasarımcısı" v1.0 eklenmesi | Orta| `dashboard-ui` | `[ ⬜ ] To Do` |
```