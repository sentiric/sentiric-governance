# 🏗️ Sentiric: Kapsamlı Mimari Dokümanı (Anayasa v4.1)

## 1. Mimari Vizyon ve Temel Prensipler

*   **"Tak-Çıkar Lego Seti" Felsefesi:** Platform, belirli teknolojilere (örn: Gemini, Twilio) "kaynak" yapılmamıştır. Her harici veya dahili servis (LLM, TTS, Takvim, STT), soyut bir arayüz (`BaseLLM`) arkasında çalışan somut bir **"Adaptör"** (`GeminiAdapter`) ile sisteme bağlanır. Bu, teknoloji yığınını (stack) gelecekte kolayca ve güvenle değiştirmemizi sağlar. Platform, şu anda **26 farklı mikroservis ve kütüphane reposundan** oluşan geniş bir Lego setidir.

*   **Asenkron ve Dayanıklı Mimari:** Sistem, telefon görüşmesinin gerçek zamanlı doğasına saygı duyar. Tüm kritik servisler, bir **Mesaj Kuyruğu (`RabbitMQ`)** üzerinden asenkron iletişim kurar. Bu, bir bileşenin yavaşlamasının veya çökmesinin, sistemin geri kalanını etkilemesini engeller ve platformu son derece dayanıklı hale getirir.

*   **İnsan Benzeri Akışkan Diyalog:** Amacımız, katı menü sunan bir IVR değil, `ChatGPT` gibi akışkan, bağlamı anlayan ve doğal bir diyalog kurabilen bir platform oluşturmaktır. Bu hedefe ulaşmak için, sadece metin değil, aynı zamanda konuşmanın tonunu, hızını ve duraklamalarını da yöneten **SSML (Speech Synthesis Markup Language)** kullanımı temel bir prensiptir.

## 2. Genel Mimari Şeması (Güncellenmiş v4.2 - 26 Repo Uyumlu)

Bu şema, sistemin 26 repoluk granüler yapısını, servisler arası etkileşimi ve merkezi altyapı bileşenlerini yansıtmaktadır. `sentiric-api-gateway-service`, tüm UI ve harici istemci istekleri için merkezi giriş noktasıdır. Gerçek zamanlı ses trafiği ise doğrudan `sentiric-sip-signaling-service` ve `sentiric-media-service` tarafından yönetilir.

```mermaid
graph TD
    subgraph "Dış Dünya & İstemciler"
        Kullanici("📞 Kullanıcı Telefonu")
        TelefoniSaglayici("☎️ Telefoni Sağlayıcısı (SIP Trunk)")
        DashboardUI("[[sentiric-dashboard-ui]]")
        WebAgentUI("[[sentiric-web-agent-ui]]")
        CLI("[[sentiric-cli]]")
    end

    subgraph "Sentiric Platformu (Bulut/On-Premise)"
        APIGateway("[[sentiric-api-gateway-service]]")
        SIPSignaling("[[sentiric-sip-signaling-service]]")
        MediaService("[[sentiric-media-service]]")
        AgentService("[[sentiric-agent-service]]")
        
        subgraph "Destekleyici Servisler"
            UserService("[[sentiric-user-service]]")
            DialplanService("[[sentiric-dialplan-service]]")
            KnowledgeService("[[sentiric-knowledge-service]]")
            Connectors("[[sentiric-connectors-service]]")
            CDRService("[[sentiric-cdr-service]]")
        end

        subgraph "Çekirdek Altyapı"
            MQ("🐇 RabbitMQ (Mesajlaşma & Olaylar)")
            DB("🗄️ PostgreSQL (Kalıcı Veri)")
            Cache("⚡ Redis (Anlık Durum & Önbellek)")
            VectorDB("🧠 Vector DB (Bilgi Bankası)")
        end
    end

    subgraph "Harici Servisler"
        AI_Services("🧠 Harici AI (LLM, STT, TTS)")
        ExternalSystems("💼 Harici İş Sistemleri (CRM, Takvim)")
    end

    %% Akışlar
    Kullanici -->|SIP/RTP Çağrı| TelefoniSaglayici
    TelefoniSaglayici -->|SIP (Sinyal)| SIPSignaling
    TelefoniSaglayici -->|RTP (Medya)| MediaService

    DashboardUI -->|REST API| APIGateway
    WebAgentUI -->|REST API| APIGateway
    CLI -->|REST API| APIGateway

    APIGateway -->|API Çağrıları| UserService
    APIGateway -->|API Çağrıları| DialplanService
    APIGateway -->|API Çağrıları| CDRService
    APIGateway -->|API Çağrıları| AgentService

    SIPSignaling -->|Kimlik Doğrulama| UserService
    SIPSignaling -->|Yönlendirme Kararı| DialplanService
    SIPSignaling -->|Medya Oturumu Yönet| MediaService
    SIPSignaling -->|CallStart/End Event| MQ
    
    MediaService -->|Audio Stream| AgentService
    
    AgentService -->|Diyalog Yönetimi| AI_Services
    AgentService -->|Bilgi Sorgulama| KnowledgeService
    AgentService -->|İş Sistemi Entegrasyonu| Connectors
    AgentService -->|Durum Oku/Yaz| Cache
    AgentService -->|Kalıcı Veri Yaz| DB
    
    KnowledgeService -->|Veri İndeksleme| VectorDB

    Connectors -->|API Çağrıları| ExternalSystems
    
    MQ -->|Olayları Tüketir| CDRService

```

## 3. Genişletilmiş Lego Mimarisi (Arayüz & Adaptörler)

Bu diyagram, platformun "Tak-Çıkar" felsefesinin kalbini gösterir. `AgentWorker`, somut implementasyonlardan değil, soyut arayüzlerden (interfaces) haberdardır.

```mermaid
classDiagram
    direction LR

    class BaseLLM { <<interface>> +generateText() }
    class BaseSTT { <<interface>> +transcribe() }
    class BaseTTS { <<interface>> +synthesize() }
    class BaseTask { <<interface>> +execute() }
    class BaseResourceAdapter { <<interface>> +call() }

    class GeminiAdapter { +generateText() }
    class DeepgramAdapter { +transcribe() }
    class SentiricTTSAdapter { +synthesize() }
    class ReservationTask { +execute() }
    class GoogleCalendarAdapter { +call() }

    class ServiceRouter {
      <<utility>>
      +get_best_service(type: str): object
    }
    
    class AgentWorker {
        -stt_router: ServiceRouter
        -llm_router: ServiceRouter
        -tts_router: ServiceRouter
        -task_router: ServiceRouter
        -resource_router: ServiceRouter
        +handle_message()
    }

    BaseLLM <|-- GeminiAdapter
    BaseSTT <|-- DeepgramAdapter
    BaseTTS <|-- SentiricTTSAdapter
    BaseTask <|-- ReservationTask
    BaseResourceAdapter <|-- GoogleCalendarAdapter
    
    AgentWorker o--> ServiceRouter
```

## 4. Detaylı ve Akıllı Arama Akışı (SSML ve Yönlendirme ile)

Bu akış, sistemin sadece bir dizi komutu değil, aynı zamanda akıllı yönlendirme ve doğal konuşma üretme yeteneklerini de nasıl kullandığını gösterir.

```mermaid
sequenceDiagram
    autonumber
    participant K as Kullanıcı
    participant TS as Telefoni Sağlayıcısı
    participant SG as "Sentiric SIP Gateway"
    participant TG as "Sentiric Telephony Gateway"
    participant MQ as RabbitMQ
    participant W as "Agent Worker"
    participant SR as "Akıllı Yönlendirici"
    participant AI as "AI Servisleri"
    participant EX as "Harici Sistemler"

    K->>TS: Arama başlatır (+90 212 454 85 90)
    TS->>SG: SIP/RTP ses akışı
    SG->>TG: WebSocket/UDP ses akışı başlatır
    TG->>MQ: publish(NewCallEvent)
    
    MQ-->>W: consume(NewCallEvent)
    W->>SR: En iyi LLM'i ve TTS'i bul
    SR-->>W: GeminiAdapter ve SentiricTTSAdapter'ı ver
    
    W->>AI: (Gemini) Kişiselleştirilmiş karşılama metni (SSML formatında) üret
    AI-->>W: "<speak>Merhaba Ahmet Bey, <break time='400ms'/> size nasıl yardımcı olabilirim?</speak>"
    
    W->>AI: (SentiricTTS) Bu SSML'i sese çevir
    AI-->>W: welcome_audio.wav
    
    W->>MQ: publish(PlayAudioCommand, audio_data)
    MQ-->>TG: consume(PlayAudioCommand)
    TG->>SG: Sesi WebSocket ile gönder
    SG-->>TS: Sesi RTP ile kullanıcıya oynat
    TS-->>K: (Doğal duraklamalı karşılama sesi)

    loop Etkileşim Döngüsü
        K->>TS: Sesli yanıt ("Randevu almak istiyorum")
        TS->>SG: Ses paketleri
        SG->>TG: Ses paketleri
        TG->>MQ: publish(AudioChunk)
        
        MQ-->>W: consume(AudioChunk)
        W->>SR: En iyi STT servisini bul (hız öncelikli)
        SR-->>W: DeepgramAdapter'ı ver
        W->>AI: (Deepgram) Sesi metne çevir
        AI-->>W: "Randevu almak istiyorum"
        
        W->>W: Görev Yönlendirme (ReservationTask seçilir)
        
        W->>SR: En iyi LLM'i bul (doğruluk öncelikli)
        SR-->>W: GeminiAdapter'ı ver
        W->>AI: (Gemini) Sonraki soruyu SSML olarak üret
        AI-->>W: "<speak>Elbette, hangi tarih için?</speak>"
        
        W->>AI: (SentiricTTS) Bu SSML'i sese çevir
        AI-->>W: prompt_audio.wav
        
        W->>MQ: publish(PlayAudioCommand, audio_data)
        MQ-->>TG: consume(PlayAudioCommand)
        TG->>SG: Sesi WebSocket ile gönder
        SG-->>TS: Sesli yanıt
        TS-->>K: "Elbette, hangi tarih için?"
    end
```

## 5. Akış Tanımlama ve Servis Orkestrasyonu

Platformun esnekliği ve zekası, iş mantığının koddan ayrıştırılması ve servis çağrılarının dinamik olarak yönetilmesine dayanır.

### 5.1. Sentiric Reçeteleri (YAML)

Bir "Kiracı" (Tenant) için tüm diyalog akışı ve kullanılacak görevler, **"Reçete" (Recipe)** adını verdiğimiz basit YAML dosyaları ile tanımlanır. Bu, platformun davranışını kod değişikliği yapmadan özelleştirmeyi sağlar.

**Örnek `tenant_recipe.yaml`:**
```yaml
# ACME Şirketi'ne özel Reçete
recipe_name: "Standart Müşteri Hizmetleri Akışı"
version: 1.0

enabled_tasks:
  - "AppointmentReservationTask"
  - "InformationRequestTask"

task_routing:
  - intent: "randevu_al"
    task: "AppointmentReservationTask"
  - intent: "bilgi_iste"
    task: "InformationRequestTask"
```

### 5.2. Akıllı Servis Yönlendirme: Kademeli Fallback

Sentiric, tek bir servis endpoint'ine bağımlı kalmak yerine, her servis türü (TTS, STT, LLM) için ayrı bir **"Servis Reçetesi"** kullanır. Bu reçete, kullanılacak servislerin bir öncelik listesini, zaman aşımlarını ve stratejilerini içerir. Bu, platformun otonom olarak en iyi performans/maliyet dengesini bulmasını ve bir servisin çökmesi durumunda bile diyalogun kesintisiz devam etmesini garanti altına alır.

**Örnek `stt_recipe.yaml`:**
```yaml
# STT Servisleri için Yönlendirme Reçetesi
# Strateji: En hızlıdan başla, kalite için gerekirse yedeğe geç.

services:
  - name: "Deepgram_Streaming_API"
    adapter: "DeepgramAdapter"
    priority: 1
    timeout_ms: 1500
    enabled: true

  - name: "Google_Speech_API_Enhanced"
    adapter: "GoogleSTTAdapter"
    priority: 2
    timeout_ms: 3000
    enabled: true
    config:
      model: "telephony"

  - name: "Sentiric_Inhouse_Whisper"
    adapter: "WhisperAdapter"
    endpoint: "http://localhost:5003/api/stt"
    priority: 3
    timeout_ms: 5000
    enabled: false
```
`Agent-Worker` içerisindeki **Akıllı Yönlendirici (ServiceRouter)**, bir STT isteği geldiğinde bu listeyi okur ve `priority` sırasına göre, `timeout_ms` sürelerini göz önünde bulundurarak servisleri dener.

## 6. Bileşen Detayları ve Sorumlu Repolar

Sentiric ekosistemindeki tüm repoların detaylı listesi ve sorumlulukları için lütfen **[Sentiric Ekosistem ve Repolar Dokümanına](./Ecosystem-Repos.md)** başvurun.
