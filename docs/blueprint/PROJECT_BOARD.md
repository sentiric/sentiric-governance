# 📋 Sentiric: Merkezi Görev Panosu (v2.1)

Bu belge, `Roadmap.md`'deki stratejik hedeflere ulaşmak için gereken tüm taktiksel görevleri içerir. Görevler öncelik sırasına göre listelenmiştir ve bu liste yaşayan bir belgedir.

**Durumlar:** `[ ] To Do`, `[ WIP ] In Progress`, `[ ✔️ ] Done`

## **FAZ 1: GÜVENLİ VE DAĞITIK OMURGA**

| ID | Görev | Öncelik | Repo(lar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P1-T01**| **Altyapı:** Profil Tabanlı Dağıtım Stratejisi Oluşturma (`telekom`, `app`, `data` profilleri) | **Kritik** | `infrastructure` | `[ ] To Do` |
| **P1-T02**| **Altyapı:** Dayanıklı Başlatma için `healthcheck` ve `depends_on` entegrasyonu | **Kritik** | `infrastructure` | `[ ] To Do` |
| **P1-T03**| **Güvenlik:** Tüm gRPC İletişimini mTLS ile Güvenli Hale Getirme | **Kritik** | Tüm gRPC servisleri | `[ ] To Do` |
| **P1-T04**| **DevOps:** Ortama Duyarlı (Console/JSON) Loglama Yapısını Tüm Servislere Uygulama| **Yüksek** | Tüm servisler | `[ ] To Do` |
| **P1-T05**| **API:** `api-gateway-service` iskeletini oluşturma ve mTLS ile güvenli hale getirme| Yüksek | `api-gateway-service` | `[ ] To Do`|
| **P1-T06**| **Test:** `cli` üzerinden `api-gateway` aracılığıyla `user-service`'e ulaşan ilk uçtan uca testi yazma| Yüksek | `cli`, `api-gateway-service`, `user-service` | `[ ] To Do` |
| **P1-T07**| **Kod Kalitesi:** Go servislerinde versiyon tutarlılığını sağlama | Orta | Go Servisleri | `[ ] To Do` |
| **P1-T08**| **Kod Kalitesi:** Ortam değişkeni isimlendirmesini standartlaştırma | Orta | `infrastructure`, Tüm servisler | `[ ] To Do` |
| **P1-T09**| **DevOps:** Tüm CI/CD pipeline'larına Docker build cache ekleme | Orta | Tüm servisler | `[ ] To Do` |

## **FAZ 2: FONKSİYONEL İSKELET**

| ID | Görev | Öncelik | Repo(lar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P2-T01**| **Veritabanı:** `init.sql` ile "Genesis Bloğu" (tüm tablolar) mantığını tamamlama| **Kritik**| `infrastructure` | `[ ] To Do` |
| **P2-T02**| **Çekirdek:** `dialplan-service`'in DB'den okuyarak dinamik karar verme yeteneği | **Kritik**| `dialplan-service` | `[ ] To Do` |
| **P2-T03**| **Çekirdek:** `user-service`'in DB'den `GetUser` ve `CreateUser` yetenekleri | **Kritik**| `user-service` | `[ ] To Do` |
| **P2-T04**| **Telekom:** `sip-signaling`'in `dialplan`, `user`, `media` servislerini orkestre etmesi | **Yüksek**| `sip-signaling-service` | `[ ] To Do` |
| **P2-T05**| **Telekom:** `media-service`'in `Allocate/ReleasePort` ve temel SRTP hazırlıklarını tamamlaması | **Yüksek**| `media-service` | `[ ] To Do` |
| **P2-T06**| **Olaylaşma:** `sip-signaling`'in `call.started` ve `call.ended` olaylarını RabbitMQ'ya atması| Yüksek| `sip-signaling-service`| `[ ] To Do` |
| **P2-T07**| **Raporlama:** `cdr-service`'in bu olayları dinleyip DB'ye temel kayıtları atması | Yüksek| `cdr-service` | `[ ] To Do` |
| **P2-T08**| **Test:** `cli` ile tam bir çağrı akışını (INVITE -> BYE) simüle edip DB'de CDR kaydını doğrulama | Yüksek| `cli`, `cdr-service` | `[ ] To Do` |

## **FAZ 3: CANLANAN PLATFORM**

| ID | Görev | Öncelik | Repo(lar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P3-T01**| **AI Çekirdek:** `agent-service`'de temel Durum Makinesi (Redis ile) implementasyonu| **Kritik**| `agent-service` | `[ ] To Do` |
| **P3-T02**| **AI Çekirdek:** `llm-service`'in `agent-service` ile entegrasyonu | **Kritik**| `llm-service`, `agent-service` | `[ ] To Do` |
| **P3-T03**| **AI Duyular:** `tts-service` ve `stt-service` iskeletlerinin oluşturulması ve entegrasyonu | **Yüksek**| `tts-service`, `stt-service`, `agent-service` | `[ ] To Do` |
| **P3-T04**| **Akış:** `agent-service`'in `dialplan` kararına göre `media-service`'e `PlayAudio` komutu göndermesi | **Yüksek**| `agent-service`, `media-service` | `[ ] To Do` |
| **P3-T05**| **UI:** `dashboard-ui`'nin `api-gateway` üzerinden `cdr-service` verilerini göstermesi | Yüksek| `dashboard-ui`, `api-gateway-service` | `[ ] To Do` |
| **P3-T06**| **Test:** Gerçek bir telefonla arama yapıp sistemin ilk anonsunu duyma (Uçtan Uca Test) | Yüksek| Tümü | `[ ] To Do` |
| **P3-T07**| **AI Akışı:** `agent-service`'in gelecekteki "streaming" API'leri destekleyecek şekilde tasarlanması| Orta | `agent-service` | `[ ] To Do` |

## **FAZ 4: AKILLI VE İNSAN ODAKLI PLATFORM**

| ID | Görev | Öncelik | Repo(lar) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **P4-T01**| **UI:** `web-agent-ui` iskeletinin oluşturulması ve çağrı devri için altyapı hazırlığı | **Kritik**| `web-agent-ui` | `[ ] To Do` |
| **P4-T02**| **Akış:** `agent-service`'den `web-agent-ui`'ye çağrı devri akışının tasarlanması | **Kritik**| `agent-service`, `web-agent-ui` | `[ ] To Do` |
| **P4-T03**| **AI Zeka:** `knowledge-service` (RAG) iskeletinin oluşturulması ve `agent-service` entegrasyonu | **Yüksek**| `knowledge-service`, `agent-service` | `[ ] To Do` |
| **P4-T04**| **Entegrasyon:** `connectors-service` için ilk konektörün (örn. Google Calendar) geliştirilmesi | Yüksek| `connectors-service` | `[ ] To Do` |
| **P4-T05**| **DX:** `sentiric-cli`'ye "Geliştirici Sandbox" modunun eklenmesi | Orta| `cli` | `[ ] To Do` |
| **P4-T06**| **UI/UX:** `dashboard-ui` üzerine "Low-Code Dialplan Tasarımcısı" v1.0 eklenmesi | Orta| `dashboard-ui` | `[ ] To Do` |

---
