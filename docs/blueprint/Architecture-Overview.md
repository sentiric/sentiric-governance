# 🏗️ Sentiric: Kapsamlı Mimari Dokümanı (Mevcut Anayasa v3.0)

## 1. Mimari Vizyon ve Temel Prensipler
**"Tak-Çıkar Lego Seti" & "Gerçek Zamanlı AI Diyaloğu" Felsefesi:**
- **Asenkron ve Dayanıklı:** Sistem, telefon görüşmesinin gerçek zamanlı doğasına saygı duyar. Bileşenler, **RabbitMQ** gibi bir mesaj kuyruğu üzerinden asenkron iletişim kurarak birbirlerinin yavaşlamasından veya çökmesinden etkilenmez.
- **Teknoloji Bağımsız:** Her işlev (LLM, TTS, Takvim), soyut bir arayüz (`BaseLLM`) arkasında çalışan somut bir adaptör (`GeminiAdapter`) ile sisteme bağlanır. Bu, teknoloji yığınını (stack) kolayca değiştirmemizi sağlar.
- **Akışkan Diyalog Odaklı:** Amacımız, katı menüler sunan bir IVR değil, `ChatGPT` veya `Gemini` gibi akışkan, bağlam farkındalığına sahip ve insan benzeri diyaloglar kurabilen bir platform oluşturmaktır.

## 2. Genel Mimari Şeması (Uygulanabilir ve Düzeltilmiş Versiyon)

Bu şema, sistemin dayanıklılığını ve ölçeklenebilirliğini artıran Mesaj Kuyruğu (RabbitMQ) ve merkezi durum/konfigürasyon yönetimi (Redis) gibi kritik ve **bugün uygulamaya başlayacağımız** bileşenleri içermektedir.

```mermaid
graph TD
    subgraph Dış Sistemler
        Kullanici("📞 Kullanıcı Telefonu")
        Telefoni("☎️ Telefoni Sağlayıcısı (Twilio, vb.)")
        AI("🧠 Harici AI Servisleri (Gemini, Whisper)")
        ExternalSystems("💼 Harici İş Sistemleri (Takvim, CRM)")
        VectorDB("📚 Vektör Veritabanı")
    end

    subgraph Sentiric Platformu
        Gateway("[[sentiric-telephony-gateway]]")
        Worker("[[sentiric-agent-worker]]")
        API("[[sentiric-api-server]]")
        Indexer("[[sentiric-knowledge-indexer]]")
        Dashboard("[[sentiric-dashboard]]")

        subgraph Çekirdek Altyapı
            MQ("🐇 RabbitMQ (Mesaj Kuyruğu)")
            DB("🗄️ PostgreSQL (SQLModel)")
            Cache("⚡ Redis (Durum ve Önbellek)")
        end
    end

    %% Akışlar
    Kullanici -->|Arama| Telefoni
    Telefoni -->|WebSocket Ses| Gateway
    Gateway -->|NewCallEvent| MQ
    MQ -->|İşi Tüketir| Worker
    
    Worker -->|Durum Oku/Yaz| Cache
    Worker -->|API Çağrıları| AI
    Worker -->|Entegrasyon| ExternalSystems
    Worker -->|Anlamsal Arama| VectorDB
    Worker -->|Veri Saklama| DB
    Worker -->|Ses Çalma Komutu| MQ
    MQ -->|Komutu Tüketir| Gateway
    Gateway -->|Ses Akışı| Telefoni
    
    Indexer -->|Vektör Yazar| VectorDB
    Dashboard -->|REST API| API
    API -->|Veri Erişimi| DB
```

## 3. Genişletilmiş ve Detaylı Lego Mimarisi (Arayüz & Adaptörler)

Bu diyagram, platformun "Tak-Çıkar" felsefesinin kalbini gösterir. `AgentWorker`, somut implementasyonlardan değil, soyut arayüzlerden (interfaces) haberdardır.

```mermaid
classDiagram
    class BaseLLM {
        <<interface>>
        +generateText(prompt: str, context: dict): str
    }
    class BaseSTT {
        <<interface>>
        +transcribe(audio: bytes): str
    }
    class BaseTTS {
        <<interface>>
        +synthesize(text: str): bytes
    }
    class BaseTask {
        <<interface>>
        +execute(context: object): object
    }
    class BaseCalendar {
        <<interface>>
        +checkAvailability(slot: object): bool
    }

    class GeminiAdapter {
      +generateText(prompt, context)
    }
    class WhisperAdapter {
      +transcribe(audio)
    }
    class ElevenLabsAdapter {
      +synthesize(text)
    }
    class GoogleCalendarAdapter {
      +checkAvailability(slot)
    }
    class ReservationTask {
      +execute(context)
    }
    
    class AgentWorker {
        -llm_adapter: BaseLLM
        -stt_adapter: BaseSTT
        -tts_adapter: BaseTTS
        -active_task: BaseTask
        +handle_message_from_queue()
    }

    BaseLLM <|-- GeminiAdapter
    BaseSTT <|-- WhisperAdapter
    BaseTTS <|-- ElevenLabsAdapter
    BaseTask <|-- ReservationTask
    BaseCalendar <|-- GoogleCalendarAdapter
    
    AgentWorker o--> BaseLLM
    AgentWorker o--> BaseSTT
    AgentWorker o--> BaseTTS
    AgentWorker o--> BaseTask
    ReservationTask o--> BaseCalendar
```

## 4. Detaylı Arama Akışı (Sequence Diagram)

```mermaid
sequenceDiagram
    autonumber
    participant K as Kullanıcı
    participant T as Telefoni
    participant G as Gateway
    participant MQ as RabbitMQ
    participant W as Worker
    participant AI as AI Servisleri
    participant DB as Veritabanı

    K->>T: Arama başlatır
    T->>G: WebSocket bağlantısı açar
    G->>MQ: publish(NewCallEvent)
    
    MQ-->>W: consume(NewCallEvent)
    W->>AI: generateWelcomeMessage()
    AI-->>W: "Merhaba, nasıl yardımcı olabilirim?"
    W->>AI: synthesize(text)
    AI-->>W: welcome_audio.wav
    W->>MQ: publish(PlayAudioCommand)
    MQ-->>G: consume(PlayAudioCommand)
    G-->>T: Ses akışı
    T-->>K: Karşılama mesajı

    loop Etkileşim Döngüsü
        K->>T: Sesli yanıt ("Randevu almak istiyorum")
        T->>G: Ses paketleri
        G->>MQ: publish(AudioChunk)
        
        MQ-->>W: consume(AudioChunk)
        W->>AI: transcribe(audio)
        AI-->>W: "Randevu almak istiyorum"
        W->>DB: saveInteraction(transcript)
        
        W->>W: Görev Yönlendirme
        W->>AI: generateNextPrompt()
        AI-->>W: "Elbette, hangi tarih için?"
        W->>AI: synthesize(prompt)
        AI-->>W: prompt_audio.wav
        W->>MQ: publish(PlayAudioCommand)
        MQ-->>G: consume(PlayAudioCommand)
        G-->>T: Ses yanıtı
        T-->>K: "Elbette, hangi tarih için?"
    end
```

```mermaid
sequenceDiagram
    autonumber
    participant K as Kullanıcı
    participant T as Telefoni
    participant G as Gateway
    participant MQ as RabbitMQ
    participant W as Worker
    participant AI as AI Servisleri
    participant DB as Veritabanı

    ...
    
    W->>W: Görev Yönlendirme
    W->>AI: **generateNextPromptAsSSML()**
    AI-->>W: **SSML Yanıtı:** <speak>Elbette, <break time="300ms"/> hangi tarih için?</speak>
    W->>AI: synthesizeSSML(ssml_text)
    AI-->>W: prompt_audio.wav
    W->>MQ: publish(PlayAudioCommand)
    MQ-->>G: consume(PlayAudioCommand)
    G-->>T: Ses yanıtı
    T-->>K: "Elbette, (duraksama) hangi tarih için?"
```

## 5. Konfigürasyon Yönetimi (Güvenli ve Esnek)

Konfigürasyon, sır içermeyen davranışsal parametreleri tanımlar. Sırlar, ortam değişkenleri ile yönetilir.

**Örnek Konfigürasyon (`config/tenant_acme.yaml`):**
```yaml
# ACME Şirketi'ne özel konfigürasyon
telephony:
  adapter: "TwilioAdapter"
  params:
    account_sid_ref: "TWILIO_ACCOUNT_SID"

ai:
  stt_adapter: "WhisperAdapter"
  llm_adapter: "GeminiAdapter"
  tts_adapter: "ElevenLabsAdapter"

tasks:
  enabled:
    - "ReservationTask"
    - "InformationRequestTask"
```

## 6. Bileşen Detayları ve Sürüm Yönetimi

| Bileşen                  | Sorumlu Repo                   | Açıklama                                       |
|--------------------------|--------------------------------|------------------------------------------------|
| telephony-gateway        | `sentiric-telephony-gateway`   | Telefoni sağlayıcıları ile WebSocket bağlantısı kurar. |
| agent-worker             | `sentiric-agent-worker`        | Diyalog mantığını yürütür, görevleri orkestre eder. |
| api-server               | `sentiric-api-server`          | Dashboard için REST API sunar.                 |
| knowledge-indexer        | `sentiric-knowledge-indexer`   | Bilgi bankasını vektör veritabanına indeksler. |
| core-interfaces          | `sentiric-core-interfaces`     | Tüm adaptörlerin uyması gereken soyut sınıflar.  |
---
