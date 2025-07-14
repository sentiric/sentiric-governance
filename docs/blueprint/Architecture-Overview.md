# 🏗️ Sentiric: Kapsamlı Mimari Dokümanı (Anayasa v4.0)

## 1. Mimari Vizyon ve Temel Prensipler

*   **"Tak-Çıkar Lego Seti" Felsefesi:** Platform, belirli teknolojilere (örn: Gemini, Twilio) "kaynak" yapılmamıştır. Her harici veya dahili servis (LLM, TTS, Takvim, STT), soyut bir arayüz (`BaseLLM`) arkasında çalışan somut bir **"Adaptör"** (`GeminiAdapter`) ile sisteme bağlanır. Bu, teknoloji yığınını (stack) gelecekte kolayca ve güvenle değiştirmemizi sağlar.

*   **Asenkron ve Dayanıklı Mimari:** Sistem, telefon görüşmesinin gerçek zamanlı doğasına saygı duyar. Tüm kritik servisler, bir **Mesaj Kuyruğu (`RabbitMQ`)** üzerinden asenkron iletişim kurar. Bu, bir bileşenin yavaşlamasının veya çökmesinin, sistemin geri kalanını etkilemesini engeller ve platformu son derece dayanıklı hale getirir.

*   **İnsan Benzeri Akışkan Diyalog:** Amacımız, katı menüler sunan bir IVR değil, `ChatGPT` gibi akışkan, bağlamı anlayan ve doğal bir diyalog kurabilen bir platform oluşturmaktır. Bu hedefe ulaşmak için, sadece metin değil, aynı zamanda konuşmanın tonunu, hızını ve duraklamalarını da yöneten **SSML (Speech Synthesis Markup Language)** kullanımı temel bir prensiptir.

## 2. Genel Mimari Şeması

Bu şema, sistemin dayanıklılığını ve ölçeklenebilirliğini artıran Mesaj Kuyruğu (RabbitMQ) ve merkezi durum/konfigürasyon yönetimi (Redis) gibi kritik bileşenleri içermektedir.

```mermaid
graph TD
    subgraph "Dış Dünya & Servisler"
        Kullanici("📞 Kullanıcı Telefonu")
        Telefoni("☎️ Telefoni Sağlayıcısı (VoIP/SIP Gateway)")
        AI("🧠 Harici AI Servisleri (LLM, STT, RAG)")
        ExternalSystems("💼 Harici İş Sistemleri (Takvim, CRM)")
    end

    subgraph "Sentiric Platformu (Google Cloud veya On-Premise)"
        Gateway("[[sentiric-telephony-gateway]]")
        Worker("[[sentiric-agent-worker]]")
        API("[[sentiric-api-server]]")
        Indexer("[[sentiric-knowledge-indexer]]")
        Dashboard("[[sentiric-dashboard]]")

        subgraph "Çekirdek Altyapı"
            MQ("🐇 RabbitMQ (Mesaj Kuyruğu)")
            DB("🗄️ PostgreSQL (SQLModel)")
            Cache("⚡ Redis (Anlık Durum & Önbellek)")
        end
    end

    %% Akışlar
    Kullanici -->|Arama| Telefoni
    Telefoni -->|Canlı Ses Akışı WSS-UDP| Gateway
    Gateway -->|NewCallEvent| MQ
    MQ -->|İşi Tüketir| Worker
    
    Worker -->|Durum Oku/Yaz| Cache
    Worker -->|Akıllı Yönlendirme| AI
    Worker -->|Entegrasyon Çağrıları| ExternalSystems
    Worker -->|Veri Saklama| DB
    Worker -->|Ses Çalma Komutu SSML| MQ
    MQ -->|Komutu Tüketir| Gateway
    Gateway -->|Sesi Sentezle & Oynat| Telefoni
    
    Indexer -->|Veriyi Vektörleştir| AI
    Dashboard -->|REST API| API
    API -->|Veri Erişimi| DB & Cache
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

    class GeminiAdapter { +generateText() }
    class DeepgramAdapter { +transcribe() }
    class SentiricTTSAdapter { +synthesize() }
    class ReservationTask { +execute() }

    class ServiceRouter {
      <<utility>>
      +get_best_service(type: str): object
    }
    
    class AgentWorker {
        -stt_router: ServiceRouter
        -llm_router: ServiceRouter
        -tts_router: ServiceRouter
        +handle_message()
    }

    BaseLLM <|-- GeminiAdapter
    BaseSTT <|-- DeepgramAdapter
    BaseTTS <|-- SentiricTTSAdapter
    BaseTask <|-- ReservationTask
    
    AgentWorker o--> ServiceRouter
```

## 4. Detaylı ve Akıllı Arama Akışı (SSML ve Yönlendirme ile)

Bu akış, sistemin sadece bir dizi komutu değil, aynı zamanda akıllı yönlendirme ve doğal konuşma üretme yeteneklerini de nasıl kullandığını gösterir.

```mermaid
sequenceDiagram
    autonumber
    participant K as Kullanıcı
    participant T as Telefoni
    participant G as Gateway
    participant MQ as RabbitMQ
    participant W as "Agent Worker"
    participant R as "Akıllı Yönlendirici"
    participant AI as "AI Servisleri"

    K->>T: Arama başlatır
    T->>G: WebSocket/UDP ses akışı başlatır
    G->>MQ: publish(NewCallEvent)
    
    MQ-->>W: consume(NewCallEvent)
    W->>R: En iyi LLM'i ve TTS'i bul
    R-->>W: GeminiAdapter ve SentiricTTSAdapter'ı ver
    
    W->>AI: (Gemini) Kişiselleştirilmiş karşılama metni (SSML formatında) üret
    AI-->>W: "<speak>Merhaba Ahmet Bey, <break time='400ms'/> size nasıl yardımcı olabilirim?</speak>"
    
    W->>AI: (SentiricTTS) Bu SSML'i sese çevir
    AI-->>W: welcome_audio.wav
    
    W->>MQ: publish(PlayAudioCommand, audio_data)
    MQ-->>G: consume(PlayAudioCommand)
    G-->>T: Sesi kullanıcıya oynat
    T-->>K: (Doğal duraklamalı karşılama sesi)

    loop Etkileşim Döngüsü
        K->>T: Sesli yanıt ("Randevu almak istiyorum")
        T->>G: Ses paketleri
        G->>MQ: publish(AudioChunk)
        
        MQ-->>W: consume(AudioChunk)
        W->>R: En iyi STT servisini bul (hız öncelikli)
        R-->>W: DeepgramAdapter'ı ver
        W->>AI: (Deepgram) Sesi metne çevir
        AI-->>W: "Randevu almak istiyorum"
        
        W->>W: Görev Yönlendirme (ReservationTask seçilir)
        
        W->>R: En iyi LLM'i bul (doğruluk öncelikli)
        R-->>W: GeminiAdapter'ı ver
        W->>AI: (Gemini) Sonraki soruyu SSML olarak üret
        AI-->>W: "<speak>Elbette, hangi tarih için?</speak>"
        
        W->>AI: (SentiricTTS) Bu SSML'i sese çevir
        AI-->>W: prompt_audio.wav
        
        W->>MQ: publish(PlayAudioCommand, audio_data)
        MQ-->>G: consume(PlayAudioCommand)
        G-->>T: Sesli yanıt
        T-->>K: "Elbette, hangi tarih için?"
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

| Bileşen | Sorumlu Repo | Açıklama |
| :--- | :--- | :--- |
| **telephony-gateway** | `sentiric-telephony-gateway` | Telefoni sağlayıcıları ile WebSocket/UDP ses akışını yönetir. |
| **agent-worker** | `sentiric-agent-worker` | Diyalog mantığını yürütür, Akıllı Yönlendiriciyi kullanır, görevleri orkestre eder. |
| **api-server** | `sentiric-api-server` | Dashboard için REST API sunar ve veritabanı işlemlerini yönetir. |
| **knowledge-indexer** | `sentiric-knowledge-indexer` | Bilgi bankasını RAG mimarisi için vektör veritabanına indeksler. |
| **core-interfaces** | `sentiric-core-interfaces` | Tüm adaptörlerin uyması gereken soyut Python sınıflarını (`BaseLLM` vb.) barındırır. |