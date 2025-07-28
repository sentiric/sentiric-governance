# 🏛️ Sentiric: Platform Anayasası ve Bütünleşik Ekosistem Mimarisi (v9.0 "Genesis")

**Belge Sürümü:** 3.0
**Son Güncelleme:** 28 Temmuz 2025
**Durum:** **AKTİF VE BAĞLAYICI**

## **İçindekiler**

1.  [Yönetici Özeti: "İletişim İşletim Sistemi" Vizyonu](#1-yönetici-özeti-iletişim-işletim-sistemi-vizyonu)
2.  ["Genesis Bloğu" Mimarisi: Temel Felsefemiz](#2-genesis-bloğu-mimarisi-temel-felsefemiz)
3.  [Ekosistemin Bütünleşik Mimarisi (26 Repo)](<#3-ekosistemin-bütünleşik-mimarisi-26-repo>)
4.  [Servislerin Nihai Rolleri ve Etki Analizi](#4-servislerin-nihai-rolleri-ve-etki-analizi)
5.  [Uçtan Uca Senaryo: "Misafir Arayan" Yaşam Döngüsü](#5-uçtan-uca-senaryo-misafir-arayan-yaşam-döngüsü)
6.  [Teknik Derinlik: Güvenlik, Performans ve Veri Tutarlılığı](#6-teknik-derinlik-güvenlik-performans-ve-veri-tutarlılığı)

---

### 1. Yönetici Özeti: "İletişim İşletim Sistemi" Vizyonu

Sentiric, bir ürün değil, bir **ekosistemdir**. Geleneksel PBX sistemlerinin kararlılığını, modern VoIP'nin esnekliğini, yapay zekanın anlama ve konuşma yeteneğini ve iş akışı otomasyon platformlarının gücünü tek bir çatı altında birleştiren, **yeni nesil bir İletişim İşletim Sistemi (Communication OS)** inşa ediyoruz.

**Misyonumuz:** Her türlü insan-makine etkileşimini (ses, metin, video) akıllı, otomatize edilebilir ve geliştiriciler tarafından sonsuz şekilde genişletilebilir bir platforma dönüştürmek.

**Temel Değer Önerimiz:** Müşterilerimize "kiralık" bir çözüm sunmak yerine, onlara kendi iletişim geleceklerinin **tapusunu** veriyoruz. Platform, hem bulutta bir hizmet (SaaS) olarak hem de müşterinin kendi sunucularında (On-Premise) çalışarak mutlak veri egemenliği ve esneklik sağlar.

---

### 2. "Genesis Bloğu" Mimarisi: Temel Felsefemiz

Platformumuzun kalbinde, tüm kararları koddan ayıran ve her şeyi dinamik, veritabanı tabanlı kurallarla yöneten dört temel prensip yatar:

1.  **Sıfır Hard-Code:** Hiçbir telefon numarası, anons metni veya iş kuralı kodun içinde yer almaz. Her şey bir UI aracılığıyla yönetilebilir.
2.  **Tek Sorumluluk Prensibi:** Her mikroservis sadece tek bir işi mükemmel bir şekilde yapar. `sip-signaling` sadece sinyali taşır, `dialplan-service` sadece karar verir, `agent-service` sadece uygular.
3.  **Kendi Kendini Başlatma (Self-Bootstrapping):** Sistem, boş bir veritabanıyla bile, çalışması için gereken temel "sistem" ve "misafir" kurallarını otomatik olarak oluşturur. Tak ve çalıştır.
4.  **Genişletilebilirlik:** Yeni bir iletişim kanalı (WhatsApp) veya yeni bir iş akışı eklemek, kodun çekirdeğini değiştirmeyi değil, veritabanına yeni "eylem" (action) ve "yönlendirme" (route) kuralları eklemeyi gerektirir.

---

### 3. Ekosistemin Bütünleşik Mimarisi (26 Repo)

```mermaid
graph TD
    subgraph "🌍 Dış Dünya & Kanallar"
        A1("☎️ Telefon (PSTN/SIP)")
        A2("📱 Mesajlaşma (WhatsApp, etc.)")
        A3("🌐 Web & Mobil (WebRTC, SDK)")
        A4("💼 Harici Sistemler (CRM, ERP)")
    end

    subgraph "🚀 Sentiric Platform Çekirdeği"
        subgraph "🔌 1. Ağ Geçitleri (Edge Layer)"
            style EdgeLayer fill:#e7f5ff,stroke:#228be6
            B1("[[sentiric-sip-gateway-service]] <br> **Güvenlik & NAT**")
            B2("[[sentiric-sip-signaling-service]] <br> **Sinyal Orkestrasyonu**")
            B3("[[sentiric-media-service]] <br> **Ses Akışı (RTP/SRTP)**")
            B4("[[sentiric-messaging-gateway-service]] <br> **Metin Mesajları**")
        end

        subgraph "🧠 2. Zeka ve Karar Katmanı (Brain Layer)"
             style BrainLayer fill:#ebfbee,stroke:#40c057
            C1("[[sentiric-dialplan-service]] <br> **Stratejik Karar Merkezi**")
            C2("[[sentiric-agent-service]] <br> **Eylem Orkestratörü**")
        end

        subgraph "🛠️ 3. Destekleyici Çekirdek Servisler (Core Services)"
            style CoreServices fill:#fff4e6,stroke:#fd7e14
            D1("[[sentiric-user-service]] <br> **Kimlik Yönetimi**")
            D2("[[sentiric-knowledge-service]] <br> **Bilgi Bankası (RAG)**")
            D3("[[sentiric-connectors-service]] <br> **Harici Entegrasyonlar**")
            D4("[[sentiric-cdr-service]] <br> **Çağrı Kayıtları**")
            D5("[[sentiric-task-service]] <br> **Asenkron Görevler**")
        end

        subgraph "🤖 4. AI Motorları (AI Engines)"
            style AIEngines fill:#ffebee,stroke:#e53935
            E1("[[sentiric-stt-service]] <br> **Konuşma -> Metin**")
            E2("[[sentiric-tts-service]] <br> **Metin -> Konuşma**")
        end
    end

    subgraph "🏗️ 5. Yönetim, Altyapı ve Geliştirici Ekosistemi"
        style Infra fill:#f8f9fa,stroke:#6c757d
        F1("🐇 RabbitMQ")
        F2("🗄️ PostgreSQL")
        F3("[[sentiric-infrastructure]] <br> **Docker Compose / IaC**")
        F4("[[sentiric-contracts]] <br> **API Sözleşmeleri (.proto)**")
        F5("[[sentiric-dashboard-ui]] <br> **Yönetim Paneli**")
        F6("[[sentiric-cli]] <br> **Geliştirici Aracı**")
        F7("[[sentiric-api-gateway-service]] <br> **UI/CLI Erişim Noktası**")
    end

    %% --- Akışlar ---
    A1 --> B1 --> B2
    A2 --> B4
    B2 -- "ResolveDialplan" --> C1
    C1 -- "Veritabanından Kuralları Oku" --> F2
    C1 -- "Kullanıcıyı Doğrula" --> D1
    C1 -- "Kararı İlet" --> B2
    B2 -- "Olay (call.started)" --> F1
    F1 -- "Olayı Tüket" --> C2
    C2 -- "Eylemleri Uygula" --> B3 & D2 & D3 & E1 & E2
    D4 -- "Tüm Olayları Dinle" --> F1
    F5 & F6 --> F7 --> C1 & D1 & D4
```

---

### 4. Servislerin Nihai Rolleri ve Etki Analizi

"Genesis Bloğu" mimarisiyle bazı servislerin rolleri daha da netleşti ve güçlendi:

| Repo Adı | **Nihai Rolü** | Stratejik Gerekçe |
| :--- | :--- | :--- |
| **`dialplan-service`** | **Stratejik Karar Merkezi.** "Bu çağrıya ne yapılmalı?" sorusunun tek yetkili cevabını verir. | İş mantığını tek bir yerde toplamak, diğer servisleri basitleştirmek. |
| **`sip-signaling-service`**| **Yüksek Hızlı Postacı.** Sadece gelen isteği `dialplan-service`'e sorar ve gelen cevabı `agent-service`'e iletir. | Performansı maksimize etmek ve sorumluluğu azaltmak. |
| **`agent-service`** | **Dinamik Eylem Orkestratörü.** `dialplan-service`'ten gelen komutları (`PLAY_ANNOUNCEMENT` vb.) harfiyen uygular. | Platformu kod değişikliği olmadan, UI üzerinden yönetilebilir kılmak. |
| **`user-service`** | **Kimlik ve Varlık Yönetimi.** Sadece kullanıcılar, agent'lar, yöneticiler gibi varlıkların CRUD operasyonlarından sorumlu. | Tek Sorumluluk Prensibi. |

Diğer 22 reponun rolleri, `Ecosystem-Repos.md` belgesinde tanımlandığı gibi geçerliliğini korumaktadır.

---

### 5. Uçtan Uca Senaryo: "Misafir Arayan" Yaşam Döngüsü

Bu yeni mimarinin gücünü en iyi anlatan senaryo:

1.  **İlk Temas:** Sistemin hiç tanımadığı bir numara, platforma ait bir numarayı arar.
2.  **Karar:** `sip-signaling`, bu bilgiyi `dialplan-service`'e sorar. `dialplan-service`, arayan numarayı veritabanında bulamaz ve **`DP_GUEST_ENTRY`** (Misafir Giriş Planı) planını geri döner.
3.  **Eylem:** `agent-service` bu planı alır. `PROCESS_GUEST_CALL` eylemini görür.
4.  **Orkestrasyon:**
    *   Misafir karşılama anonsunu çalar.
    *   `user-service`'i çağırarak bu yeni numarayı veritabanına "misafir" olarak kaydeder.
    *   Varsayılan AI konuşma akışını başlatır.
5.  **Sonuç:** Çağrı bittiğinde, bu "misafir" artık sistem için tanınan bir kullanıcıdır. Bir sonraki aramasında, `dialplan-service` onu tanıyacak ve kiracıya özel karşılama planını uygulayacaktır. Sistem, **kendi kendine öğrenmiş ve büyümüştür.**

---

### 6. Teknik Derinlik: Güvenlik, Performans ve Veri Tutarlılığı

Bu mimari, en başından itibaren kurumsal düzeyde gereksinimleri karşılamak üzere tasarlanmıştır:

*   **Güvenlik:**
    *   **Uçtan Uca Şifreleme:** `media-service`, SRTP/ZRTP protokollerini destekleyerek sesli iletişimin gizliliğini garanti altına alacaktır.
    *   **AI Güvenliği:** STT/TTS servisleri, ses deepfake'leri gibi `adversarial` saldırılara karşı, ses filigranı (audio watermarking) gibi tekniklerle güçlendirilecektir.
*   **Performans:**
    *   **Gerçek Zamanlı AI:** `agent-service` ile AI motorları (STT/TTS/LLM) arasındaki tüm iletişim, gecikmeyi minimize etmek için **streaming (akış) API'leri** üzerine kurulacaktır. Kullanıcı konuşurken transkripsiyon başlayacak, LLM yanıt üretmeye başlar başlamaz TTS sesi sentezlemeye başlayacaktır.
*   **Veri Tutarlılığı:**
    *   **Dağıtık İşlemler:** Birden fazla servisi ilgilendiren karmaşık iş akışları (örn: ödeme al ve rezervasyon yap), veri tutarlılığını garanti altına almak için gelecekte **SAGA pattern**'i ile yönetilecektir.

Bu anayasa, Sentiric platformunun bugünkü inşa sürecine rehberlik eden ve yarının zorluklarına hazır olmasını sağlayan yaşayan bir belgedir.
