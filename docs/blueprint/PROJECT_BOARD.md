# 🎯 Sentiric Platformu: Stratejik Proje Panosu (v5.0)

Bu doküman, Sentiric platformunun üst düzey stratejik hedeflerini, bu hedeflerden sorumlu ana bileşenleri ve detaylı görev listelerinin bulunduğu yerleri gösteren **merkezi yönetim kuruludur**. Bu pano, projenin genel ilerleyişini ve fazlar arası geçişleri takip etmek için kullanılır.

Teknik detaylar ve görev listeleri, her bir reponun kendi `TASKS.md` dosyasında yaşar.

#### **Durum Göstergeleri**
*   `[ ✔️ ] Tamamlandı`
*   `[ ⏳ ] Devam Ediyor`
*   `[ ⬜ ] Planlandı`

---

## **FAZ 1: GÜVENLİ VE DAYANIKLI OMURGA**

**Hedef:** Platformun temel iskeletini, çoklu sunucu ortamlarında güvenli, dayanıklı, gözlemlenebilir ve test edilebilir bir şekilde çalışacak hale getirmek.

| ID | Stratejik Hedef | Sorumlu Repo(lar) | Detaylı Görevler (Yerel Yasalar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P1-T01**| Profil Tabanlı Dağıtım Stratejisi | `infrastructure` | `sentiric-infrastructure/TASKS.md` | `[ ✔️ ] Tamamlandı` |
| **P1-T02**| Dayanıklı Başlatma (Healthchecks) | `infrastructure`, Tümü | `sentiric-infrastructure/TASKS.md` | `[ ✔️ ] Tamamlandı` |
| **P1-T03**| Tüm gRPC İletişimini mTLS ile Güvenli Hale Getirme | Tümü (Go/Rust) | `sentiric-governance/docs/security/...` | `[ ✔️ ] Tamamlandı` |
| **P1-T04**| RabbitMQ Mimarisi'ni Fanout Exchange'e Geçirme | `sip-signaling`, `agent`, `cdr` | `(ilgili TASKS.md dosyaları)` | `[ ✔️ ] Tamamlandı` |
| **P1-T05**| Kritik İş Mantığı için Birim Testi Altyapısı Kurma | **Tüm Servisler** | `sentiric-governance/docs/engineering/Testing-Strategy.md` | `[ ⬜ ] Planlandı` |
| **P1-T06**| CI/CD Pipeline'larına Test ve Linting Adımları Ekleme | Tümü | `(ilgili TASKS.md dosyaları)` | `[ ⬜ ] Planlandı` |
| **P1-T07**| Monolitik `main.go` dosyalarını Modüler Hale Getirme | `user`, `dialplan`, `cdr` | `(ilgili TASKS.md dosyaları)` | `[ ✔️ ] Tamamlandı` |
| **P1-T08**| `api-gateway-service` İskeletini Oluşturma | `api-gateway-service` | `sentiric-api-gateway-service/TASKS.md` | `[ ✔️ ] Tamamlandı` |
| **P1-T09**| İlk Uçtan Uca Yönetim API Testini Yazma | `cli`, `api-gateway`, `user` | `sentiric-cli/TASKS.md` | `[ ⬜ ] Planlandı` |
| **P1-T10**| Konfigürasyon ve Dockerfile Standardizasyonu | Tümü | `sentiric-governance/docs/engineering/Coding-Standards.md` | `[ ✔️ ] Tamamlandı` |

---

## **FAZ 1.5: GÖZLEMLENEBİLİRLİK OMURGASI**

**Hedef:** Platformun her bir parçasını izlenebilir, ölçülebilir ve hataların kolayca ayıklanabilir hale getirmek.

| ID | Stratejik Hedef | Sorumlu Repo(lar) | Detaylı Görevler (Yerel Yasalar) | Durum |
|:---|:---|:---|:---|:---|
| **OBS-01** | Gözlemlenebilirlik Standardı Dokümantasyonu | `governance` | `docs/engineering/OBSERVABILITY_STANDARD.md` | `[ ✔️ ] Tamamlandı` |
| **OBS-02** | Tüm Servislerde Standart ve Ortama Duyarlı Loglama | **Tüm Servisler** | `(ilgili README.md dosyaları)` | `[ ✔️ ] Tamamlandı` |
| **OBS-03** | Altyapıya Prometheus ve Grafana Ekleme | `infrastructure` | `sentiric-infrastructure/TASKS.md` | `[ ⬜ ] Planlandı` |
| **OBS-04** | Tüm Servislere Prometheus `/metrics` Endpoint'i Ekleme| **Tüm Servisler** | `(ilgili TASKS.md dosyaları)` | `[ ✔️ ] Tamamlandı` |
| **OBS-05** | Ağ Geçitlerinde `trace_id` Oluşturma ve Yayma | `sip-gateway`, `api-gateway` | `(ilgili TASKS.md dosyaları)` | `[ ✔️ ] Tamamlandı` |
| **OBS-06** | `trace_id`'yi Diğer Tüm Servislerde Yakalama ve Yayma| **Tüm Servisler** | `(ilgili TASKS.md dosyaları)` | `[ ✔️ ] Tamamlandı` |
| **OBS-07** | Altyapıya Jaeger/Tempo (Tracing Backend) Ekleme | `infrastructure` | `sentiric-infrastructure/TASKS.md` | `[ ⬜ ] Planlandı` |

---

## **FAZ 2: FONKSİYONEL İSKELET**

**Hedef:** Omurga üzerine, bir telefon çağrısını baştan sona yönetebilen ve yeni yeteneklerin eklenebileceği temel servisleri (iskeleti) yerleştirmek.

| ID | Stratejik Hedef | Sorumlu Repo(lar) | Detaylı Görevler (Yerel Yasalar) | Durum |
|:---|:---|:---|:---|:---|
| **P2-T01** | "Genesis Bloğu" Veritabanı Mantığını Tamamlama | `config`, `infrastructure` | `sentiric-config/README.md` | `[ ✔️ ] Tamamlandı` |
| **P2-T02** | `dialplan` ve `user` servislerinin DB'den Okuma/Yazma Yetenekleri | `dialplan-service`, `user-service`| `(ilgili TASKS.md dosyaları)` | `[ ✔️ ] Tamamlandı` |
| **P2-T03** | `sip-signaling` ve `media` servislerinin Çağrı Kurma/Port Yönetimi Yetenekleri | `sip-signaling`, `media-service` | `(ilgili TASKS.md dosyaları)` | `[ ✔️ ] Tamamlandı` |
| **P2-T04** | `sip-signaling`'in `call.started/ended` Olaylarını Yayınlaması | `sip-signaling` | `sentiric-sip-signaling-service/TASKS.md`| `[ ✔️ ] Tamamlandı` |
| **P2-T05** | `cdr-service`'in Olayları Dinleyip DB'ye Kaydetmesi | `cdr-service` | `sentiric-cdr-service/TASKS.md` | `[ ✔️ ] Tamamlandı` |
| **P2-T06** | `cli` ile Tam Çağrı Akışını Simüle Edip DB'de CDR Doğrulama | `cli`, `cdr-service` | `sentiric-cli/TASKS.md` | `[ ⬜ ] Planlandı` |
| **P2-T07** | `task-service` İskeletini Oluşturma | `task-service`, `infrastructure` | `sentiric-task-service/TASKS.md` | `[ ✔️ ] Tamamlandı` |
| **P2-T08** | SAGA Pattern Veri Bütünlüğü Altyapısını Kurma | `config`, `agent-service`, Tümü | `sentiric-agent-service/TASKS.md` | `[ ⬜ ] Planlandı` |

---

## **FAZ 3: CANLANAN PLATFORM**

**Hedef:** İskelete "beyin" ve "ses" ekleyerek platformu, arayanla anlamlı bir diyalog kurabilen akıllı bir sisteme dönüştürmek.

| ID | Stratejik Hedef | Sorumlu Repo(lar) | Detaylı Görevler (Yerel Yasalar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P3-T01**| Akıllı Ses Orkestrasyon Mimarisine Geçiş | `tts-gateway`, `edge-tts`, `coqui-tts` | `sentiric-tts-gateway-service/TASKS.md`| `[ ⬜ ] Planlandı` |
| **P3-T02**| `agent-service`'de Redis Tabanlı Durum Makinesi (State Machine) | `agent-service`, `infrastructure` | `sentiric-agent-service/TASKS.md` | `[ ⬜ ] Planlandı` |
| **P3-T03**| Tam Diyalog Döngüsü (STT -> LLM -> TTS) | `agent`, `stt`, `llm`, `tts-gateway` | `(ilgili TASKS.md dosyaları)` | `[ ⬜ ] Planlandı` |
| **P3-T04**| `dashboard-ui`'nin API Gateway Üzerinden Canlı Veri Göstermesi | `dashboard-ui`, `api-gateway` | `sentiric-dashboard-ui/TASKS.md` | `[ ⬜ ] Planlandı` |

---

## **FAZ 4: AKILLI VE GENİŞLETİLEBİLİR PLATFORM**

**Hedef:** Platformu, karmaşık görevleri yürütebilen, bilgi bankasından faydalanabilen ve gerektiğinde görevi sorunsuz bir şekilde insan temsilciye devredebilen, tam teşekküllü bir AI orkestratörüne dönüştürmek.

| ID | Stratejik Hedef | Sorumlu Repo(lar) | Detaylı Görevler (Yerel Yasalar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P4-T01**| `web-agent-ui` İskeletini Oluşturma ve Çağrı Devri | `web-agent-ui` | `sentiric-web-agent-ui/TASKS.md` | `[ ✔️ ] Tamamlandı` |
| **P4-T02**| RAG Yeteneği (`knowledge-service`) | `knowledge-service`, `agent`, `llm` | `sentiric-knowledge-service/TASKS.md`| `[ ✔️ ] Tamamlandı` |
| **P4-T03**| İlk Gerçek Konektörün Geliştirilmesi (örn. Google Calendar) | `connectors-service` | `sentiric-connectors-service/TASKS.md`| `[ ⬜ ] Planlandı` |
| **P4-T04**| Low-Code Dialplan Tasarımcısı v1.0 | `dashboard-ui` | `sentiric-dashboard-ui/TASKS.md` | `[ ⬜ ] Planlandı` |

---