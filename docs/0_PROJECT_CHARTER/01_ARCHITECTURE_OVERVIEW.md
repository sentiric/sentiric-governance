# 🏗️ Sentiric: Kapsamlı Mimari Dokümanı

## 1. Mimari Vizyon ve Temel Prensipler
**"Tak-Çıkar Lego Seti" Felsefesi:**
- Her bileşen belirli bir sorumluluğa odaklanır
- Bileşenler arası iletişim kesinlikle arayüzler üzerinden yapılır
- Yeni adaptörler çalışma zamanında yüklenebilir
- Sistem konfigürasyonla davranış değiştirebilir

## 2. Tam Mimari Şeması (Geliştirilmiş Versiyon)

```mermaid
graph TD
    subgraph "Dış Sistemler"
        Kullanici[📞 Kullanıcı Telefonu]
        Telefoni[☎️ Telefoni Sağlayıcısı]
        AI[🧠 AI Servisleri]
        Calendar[📅 Takvim Sistemleri]
        CRM[👥 CRM Sistemleri]
    end

    subgraph "Sentiric Platformu"
        Gateway[[sentiric-telephony-gateway]]
        Worker[[sentiric-agent-worker]]
        API[[sentiric-api-server]]
        Dashboard[[sentiric-dashboard]]
        DB[(🗄️ PostgreSQL)]
        Cache[(⚡ Redis)]
        Config[⚙️ Config Manager]
    end

    Kullanici -->|Arama| Telefoni
    Telefoni -->|WebSocket| Gateway
    Gateway -->|Ses Akışı| Worker
    Worker -->|LLM API| AI
    Worker -->|Calendar API| Calendar
    Worker -->|CRM Entegrasyonu| CRM
    Worker -->|Veri İşleme| DB
    Worker -->|Önbellek| Cache
    Dashboard -->|REST| API
    API -->|Veri Erişimi| DB
    Config -->|Yapılandırma| Worker
    Config -->|Yapılandırma| Gateway
```

## 3. Genişletilmiş ve Detaylı Lego Mimarisi

```mermaid
classDiagram
    %% Arayüz Tanımları
    class BaseLLM {
        <<interface>>
        +generateText(prompt: str, context: dict): str
        +transcribe(audio: bytes): str
    }

    class BaseTask {
        <<interface>>
        +execute(context: dict): TaskResult
        +getNextPrompt(): str
    }

    class BaseAvailability {
        <<interface>>
        +checkAvailability(slot: TimeSlot): bool
        +reserveSlot(slot: TimeSlot): bool
    }

    class BaseCRM {
        <<interface>>
        +getCustomerInfo(phone: str): Customer
        +updateCustomerInfo(customer: Customer): bool
    }

    %% Adaptör Implementasyonları
    class GeminiAdapter {
        +generateText(prompt: str, context: dict): str
        +transcribe(audio: bytes): str
    }

    class GoogleCalendarAdapter {
        +checkAvailability(slot: TimeSlot): bool
        +reserveSlot(slot: TimeSlot): bool
    }

    class SalesforceAdapter {
        +getCustomerInfo(phone: str): Customer
        +updateCustomerInfo(customer: Customer): bool
    }

    %% Çekirdek Bileşenler
    class AgentWorker {
        -llmAdapter: BaseLLM
        -activeTask: BaseTask
        -crmAdapter: BaseCRM
        +handleCall()
        +switchTask()
        +saveContext()
    }

    %% İlişkiler
    BaseLLM <|-- GeminiAdapter
    BaseTask <|-- ReservationTask
    BaseTask <|-- InformationTask
    BaseAvailability <|-- GoogleCalendarAdapter
    BaseCRM <|-- SalesforceAdapter
    
    AgentWorker o--> BaseLLM
    AgentWorker o--> BaseTask
    AgentWorker o--> BaseCRM
    ReservationTask o--> BaseAvailability
```

**Anahtar Özellikler:**
1. **Dinamik Adaptör Yönetimi:**
```python
def load_adapter(adapter_type: str, adapter_class: str, config: dict):
    if adapter_type == "LLM":
        self.llm_adapter = import_class(adapter_class)(config)
    elif adapter_type == "CRM":
        self.crm_adapter = import_class(adapter_class)(config)
```

2. **Görev Yaşam Döngüsü:**
   - Görev bulucu (Task Finder) → Görev başlatma → Context yönetimi → Sonlandırma

## 4. Tam Arama Akışı (Detaylı Sequence Diagram)

```mermaid
sequenceDiagram
    autonumber
    participant K as Kullanıcı
    participant T as Telefoni
    participant G as Gateway
    participant W as Worker
    participant AI as AI Servisi
    participant TS as Görev Sistemi
    participant CRM as CRM
    participant DB as Veritabanı

    K->>T: Arama başlatır (0555 XXX XX XX)
    T->>G: WebSocket bağlantısı açar
    G->>W: NewCallEvent (call_id, metadata)
    
    %% Müşteri Tanıma
    W->>CRM: getCustomerInfo(phoneNumber)
    CRM-->>W: Customer (varsa) veya null
    
    %% Karşılama Mesajı
    W->>AI: generateWelcomeMessage(customer)
    AI-->>W: "Merhaba [isim], nasıl yardımcı olabilirim?"
    W->>G: playAudio(TTS_Response)
    G->>T: Ses akışı
    T->>K: Karşılama mesajı

    loop Etkileşim Döngüsü
        K->>T: Sesli yanıt ("Randevu almak istiyorum")
        T->>G: Ses paketleri
        G->>W: AudioChunk (raw)
        
        %% STT ve Niyet Analizi
        W->>AI: transcribeAudio(audio)
        AI-->>W: "Randevu almak istiyorum"
        W->>DB: saveInteraction(call_id, transcript)
        
        %% Görev Yönlendirme
        W->>TS: findTask(intent="appointment")
        TS-->>W: ReservationTask
        W->>W: task.execute(context)
        
        %% Takvim Kontrolü
        W->>AI: generateDatePrompt(available_slots)
        AI-->>W: "Hangi tarih uygun: 15 Mart 10:00 veya 16 Mart 14:00?"
        W->>G: playAudio(response)
        G->>T: Ses yanıtı
        T->>K: Soru iletimi
        
        %% Kullanıcı Yanıtı İşleme
        K->>T: "15 Mart uygun"
        T->>G: Ses verisi
        G->>W: AudioChunk
        W->>AI: transcribe(audio)
        AI-->>W: "15 Mart"
        W->>DB: saveResponse(call_id, "date_pref", "15 Mart")
        
        %% Onay ve Sonlandırma
        W->>AI: generateConfirmation()
        AI-->>W: "Randevunuz 15 Mart için ayarlandı"
        W->>G: playAudio(confirmation)
    end
    
    %% Post-call İşlemler
    W->>CRM: updateCustomer(call_data)
    W->>DB: finalizeCall(call_id)
    W->>G: terminateCall()
```

## 5. Bileşen Detayları ve Sürüm Yönetimi

| Bileşen                  | Sürüm  | Açıklama                          | Bağımlılıklar                 |
|--------------------------|--------|----------------------------------|-------------------------------|
| telephony-gateway        | v2.2.0 | Çoklu protokol desteği            | WebSocket, SIP, RTMP          |
| agent-worker            | v3.1.0 | Akıllı görev orkestrasyonu        | Python 3.10+, Redis           |
| api-server              | v1.5.2 | REST API ve yönetim arayüzü       | FastAPI, JWT Auth             |
| task-framework          | v2.3.0 | Standart görev kütüphanesi        | BaseInterfaces v1.4+          |
| llm-adapters            | v1.2.0 | Çoklu AI sağlayıcı desteği        | Gemini, Whisper, OpenAI       |

## 6. Konfigürasyon Yönetimi (Örnek)

```yaml
# config/production.yaml
telephony:
  active_adapter: "Twilio"
  params:
    account_sid: "ACXXXXXX"
    auth_token: "YYYYYY"

ai:
  primary: 
    adapter: "GeminiPro"
    params:
      api_key: "ZZZZZZ"
      model: "gemini-1.5"
  fallback: "OpenAI"

tasks:
  enabled:
    - "Reservation"
    - "Information"
    - "Complaint"
  
  reservation:
    calendar_adapter: "GoogleCalendar"
    min_advance_hours: 24
```

## 7. Hata Senaryoları ve Kurtarma Mekanizmaları

**Senaryo 1: AI Servis Kesintisi**
1. Worker primary AI'dan 3 saniye yanıt alamazsa
2. Otomatik olarak fallback adaptöre geçer
3. Olayı monitoring sistemine kaydeder
4. Sağlıklı adaptör dönünce otomatik geri geçer

**Senaryo 2: Telefoni Bağlantı Kopması**
1. Gateway 10 saniye içinde yeniden bağlanmaya çalışır
2. Başarısız olursa çağrıyı "failed_calls" tablosuna kaydeder
3. Yöneticiye otomatik bildirim gönderir

## 8. Genişletme Noktaları

**Yeni Adaptör Eklemek İçin:**
1. İlgili base interface'i implemente et
2. Adapter sınıfını oluştur
3. `adapters/` dizinine ekle
4. Config'de aktifleştir

**Örnek Adaptör Kodu:**
```python
class NewLLMAdapter(BaseLLM):
    def __init__(self, config):
        self.api_key = config['api_key']
    
    def generateText(self, prompt, context):
        # Özel implementasyon
        return response
```

Bu doküman, sistemin tüm kritik yönlerini kapsarken, hem geliştiriciler hem de sistem mimarları için kapsamlı bir rehber sunmaktadır.