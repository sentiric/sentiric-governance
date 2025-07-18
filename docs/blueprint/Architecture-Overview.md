# 🏗️ Sentiric: Kapsamlı Mimari Dokümanı (Anayasa v5.0)

## 1. Mimari Vizyon ve Temel Prensipler

Bu bölüm, Sentiric platformunun temelini oluşturan, değiştirilemez mühendislik ilkelerini tanımlar.

### 1.1. Tak-Çıkar Modüler Mimarisi (Lego Felsefesi)

Platform, belirli bir teknolojiye bağımlı değildir. Her işlev, soyut bir arayüz arkasında çalışan değiştirilebilir bir "Adaptör" ile sisteme bağlanır. Bu, teknoloji bağımsızlığı sağlar.

```mermaid
flowchart TB
    subgraph Adaptör Katmanı
        direction LR
        A(BaseLLM) --> B[GeminiAdapter]
        A --> C[GPT4Adapter]
        A --> D[...]
        E(BaseSTT) --> F[DeepgramAdapter]
        E --> G[WhisperAdapter]
        E --> H[...]
    end
    
    subgraph Çekirdek Sistem
        Agent("[[sentiric-agent-service]]") -->|Soyut Bağımlılık| A
        Agent -->|Soyut Bağımlılık| E
    end
```

### 1.2. Asenkron ve Dayanıklı İletişim

Tüm kritik servisler arası iletişim, `RabbitMQ` mesaj kuyruğu üzerinden asenkron olarak gerçekleşir. Bu, sistemin bir bütün olarak dayanıklılığını ve ölçeklenebilirliğini garanti eder.

| Bileşen / Olay Türü  | Örnek Kuyruk Adı       | Hedeflenen TPS | Maks. Gecikme |
|----------------------|------------------------|----------------|---------------|
| SIP Sinyalleşmesi    | `events.call.lifecycle`| 1000+          | < 50ms        |
| Medya Akış Parçaları | `streams.audio.raw`    | 500+           | < 150ms       |
| AI İstekleri         | `requests.ai.priority` | 2000+          | < 100ms       |

### 1.3. İnsan Benzeri Diyalog Sanatı (SSML)

Amacımız, robotik bir sesten ziyade, duyguyu ve tonlamayı yansıtan doğal bir diyalog deneyimi sunmaktır. Bu nedenle LLM'den SSML (Speech Synthesis Markup Language) formatında yanıtlar üretmesini bekleriz.

```python
# Örnek: Duyguya göre SSML üreten bir yardımcı sınıf
class SSMLGenerator:
    def generate_emotional_response(self, text: str, emotion: str = "neutral") -> str:
        """Duygu durumuna göre konuşma hızını ve tonunu ayarlar."""
        prosody = {
            "happy": {'rate': 'fast', 'pitch': 'high'},
            "sad": {'rate': 'slow', 'pitch': 'low'},
            "neutral": {'rate': 'medium', 'pitch': 'medium'}
        }
        selected_prosody = prosody.get(emotion, prosody["neutral"])
        
        return f"""
<speak>
    <prosody rate="{selected_prosody['rate']}" pitch="{selected_prosody['pitch']}">
        {text}
    </prosody>
</speak>
"""
```

## 2. Genel Mimari Şeması (Doğrulanmış v5.0)

Bu şema, bizim **`RabbitMQ` merkezli, 26 repoluk granüler ve asenkron mimarimizi** yansıtmaktadır. Bu yapı, platformun ölçeklenebilirlik ve dayanıklılık hedefleri için esastır.

```mermaid
graph TD
    subgraph "Dış Dünya & İstemciler"
        Kullanici("📞 Kullanıcı Telefonu")
        TelefoniSaglayici("☎️ Telefoni Sağlayıcısı (SIP Trunk v1.2)")
        DashboardUI("[[sentiric-dashboard-ui]]")
        WebAgentUI("[[sentiric-web-agent-ui]]")
        CLI("[[sentiric-cli]]")
    end

    subgraph "Sentiric Platformu (Bulut/On-Premise)"
        APIGateway("[[sentiric-api-gateway-service]]")
        SIPSignaling("[[sentiric-sip-signaling-service v1.0]]")
        MediaService("[[sentiric-media-service v1.0]]")
        AgentService("[[sentiric-agent-service v1.0]]")
        
        subgraph "Destekleyici Servisler"
            UserService("[[sentiric-user-service]]")
            DialplanService("[[sentiric-dialplan-service]]")
            KnowledgeService("[[sentiric-knowledge-service]]")
            Connectors("[[sentiric-connectors-service]]")
            CDRService("[[sentiric-cdr-service]]")
        end

        subgraph "Çekirdek Altyapı"
            MQ("🐇 RabbitMQ\n<size=8>Cluster Mode</size>")
            DB("🗄️ PostgreSQL\n<size=8>TimescaleDB</size>")
            Cache("⚡ Redis\n<size=8>Sentinel</size>")
            VectorDB("🧠 Vector DB")
        end
    end

    subgraph "Harici Servisler"
        AI_Services("🧠 Harici AI (LLM, STT, TTS)")
        ExternalSystems("💼 Harici İş Sistemleri (CRM, Takvim)")
    end

    %% Akışlar
    Kullanici -->|SIP/RTP| TelefoniSaglayici
    TelefoniSaglayici -->|SIP:5060/TLS| SIPSignaling
    TelefoniSaglayici -->|RTP:10000-20000| MediaService

    DashboardUI & WebAgentUI & CLI -->|REST/GraphQL| APIGateway

    APIGateway -->|gRPC/REST| UserService
    APIGateway -->|gRPC/REST| DialplanService
    APIGateway -->|gRPC/REST| CDRService
    APIGateway -->|gRPC/REST| AgentService

    SIPSignaling -->|API Çağrısı| UserService
    SIPSignaling -->|API Çağrısı| DialplanService
    SIPSignaling -->|API Çağrısı| MediaService
    SIPSignaling -->|Olay Yayınla| MQ
    
    MediaService -->|Olay Yayınla| MQ
    MediaService -.->|İşlenmiş Ses Akışı| AgentService
    
    AgentService -->|API Çağrısı| AI_Services
    AgentService -->|API Çağrısı| KnowledgeService
    AgentService -->|API Çağrısı| Connectors
    AgentService -->|Durum Oku/Yaz| Cache
    AgentService -->|Kalıcı Veri Yaz| DB
    
    KnowledgeService -->|Veri İndeksle| VectorDB
    Connectors -->|API Çağrısı| ExternalSystems
    
    MQ -->|Olayları Tüketir| CDRService
    MQ -->|İşleri Tüketir| AgentService
```

## 3. Adaptör Mimarisi Sınıf Diyagramı

Bu diyagram, platformun "Tak-Çıkar" felsefesinin kod seviyesindeki yansımasıdır.

```mermaid
classDiagram
    class BaseLLM {
        <<interface>>
        +generate(prompt: str, config: dict) -> str
        +get_usage_metrics() -> dict
    }
    
    class GeminiAdapter {
        -api_key: str
        -model: str = "gemini-1.5-pro"
        +generate(prompt: str, config: dict) -> str
        +get_usage_metrics() -> dict
    }
    
    class GPT4Adapter {
        -endpoint: str = "https://api.openai.com/v1"
        +generate(prompt: str, config: dict) -> str
        +get_usage_metrics() -> dict
    }
    
    BaseLLM <|-- GeminiAdapter
    BaseLLM <|-- GPT4Adapter
    
    note for BaseLLM "Tüm adaptörlerin uygulaması gereken temel kontrat.\n• Thread-safe olmalı\n• Yeniden deneme (retry) mekanizması içermeli"
```

## 4. Gelişmiş Çağrı Akışı Sıralı Diyagramı

```mermaid
sequenceDiagram
    box Mor Kullanıcı Tarafı
        participant K as Kullanıcı
        participant T as Telefon Cihazı
    end
    
    box Mavi Sentiric Platformu
        participant SG as SIP Signaling
        participant MS as Media Service
        participant MQ as RabbitMQ
        participant AS as Agent Service
    end
    
    K->>T: Arama Başlatır
    T->>SG: SIP INVITE (Hedef: 5060)
    SG->>MQ: publish(event: 'call.started')
    MQ->>AS: consume(event: 'call.started')
    
    AS->>AS: Müşteriyi Tanı & Bağlam Oluştur
    AS->>AS: Karşılama için SSML Üret
    AS->>MS: play_audio(ssml_data)
    
    MS->>T: RTP Akışı (Port: 10000-20000)
    T-->>K: Karşılama sesi oynatılır

    loop Diyalog Yönetimi
        K->>T: Sesli Yanıt ("Randevu...")
        T->>MS: RTP Paketleri
        MS->>AS: İşlenmiş Ses Akışı
        
        AS->>AS: STT ile Metne Çevir
        AS->>AS: Niyet Analizi & Görev Yönlendirme
        AS->>AS: Yanıt için SSML Üret
        
        AS->>MS: play_audio(ssml_response)
        MS->>T: RTP Akışı
        T-->>K: AI yanıtı oynatılır
    end
```

## 5. Güvenlik, Performans ve Operasyonlar

### 5.1. Güvenlik Mimarisi

Platform, "Derinlemesine Savunma" (Defense in Depth) prensibini benimser.

```mermaid
graph LR
    A[İstemci] -->|mTLS 1.3| B[API Gateway]
    B -->|JWT Auth| C[İç Servisler]
    C -->|Vault| D[Şifreleme Anahtarları]
    D --> E[Veritabanı]
    D --> F[Redis]
```

### 5.2. Performans Optimizasyon Stratejileri

Gecikme (latency), projenin en kritik metriğidir. Aşağıdaki stratejilerle yönetilecektir.

| Senaryo                     | Çözüm Stratejisi                 | Hedeflenen Kazanım |
|-----------------------------|----------------------------------|--------------------|
| Yüksek CPU'lu Medya İşleme  | WebAssembly (Wasm) DSP Filtreleri| %30-40 CPU Azalması|
| STT Gecikmesi (İlk Yanıt)   | Streaming STT & Ön İşlemeli Buffer| 200ms+ İyileşme    |
| LLM Maliyet ve Gecikmesi    | Akıllı Adaptif Model Yönlendirme | %35 Tasarruf       |

### 5.3. Akıllı Ölçeklendirme ve Dayanıklılık

Sistem, KEDA (Kubernetes Event-driven Autoscaling) gibi araçlarla kuyruk uzunluğuna ve CPU kullanımına göre otonom olarak ölçeklenecektir.

```python
# KEDA'ya ilham verecek otonom ölçeklendirme mantığı (Teorik)
async def auto_scale_logic():
    while True:
        # Prometheus'tan metrikleri al
        cpu_load = get_metric("cpu.agent_service.avg")
        queue_depth = get_metric("rabbitmq.requests_ai_priority.depth")
        
        if cpu_load > 0.8 and queue_depth > 1000:
            # Agent Service pod sayısını artır
            scale_up("agent-service", count=2)
        elif cpu_load < 0.3 and queue_depth < 50:
            # Agent Service pod sayısını azalt
            scale_down("agent-service", count=1)
        
        await asyncio.sleep(60)
```

### 5.4. Gelişmiş Hata Ayıklama (Debugging)

Üretim ortamındaki sorunları çözmek için, çağrı bazında dinamik olarak etkinleştirilebilen hata ayıklama özellikleri olacaktır.

```yaml
# Örnek: Belirli bir çağrı için debug yapılandırması (Redis'te tutulur)
# call_id: CA123456789
features:
  call_recording: true
  realtime_logs: 
    enabled: true
    level: DEBUG
  trace_injection:
    enabled: true
    sample_rate: 1.0 # Bu çağrıyı kesinlikle izle
```

## 6. Sonuç ve Doküman Yönetimi

Bu doküman, Sentiric platformunun yaşayan anayasasıdır ve **v5.0** olarak kabul edilmiştir. Tüm geliştirme faaliyetleri bu belgeye referansla yapılmalıdır. Bu belge, projenin `sentiric-governance` reposunda `docs/blueprint/Architecture-Overview.md` olarak yer alacaktır.
