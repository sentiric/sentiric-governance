# 🗺️ Sentiric: Ekosistem ve Repolar (v5.2 - Kapsamlı Revizyon)

Sentiric platformu, her biri belirli bir sorumluluğa sahip, bağımsız olarak geliştirilen ve yönetilen toplam **28 adet depodan (repository)** oluşur. Bu modüler yapı, projenin "Tak-Çıkar Lego Seti" felsefesini somutlaştırır ve karmaşık bir sistemin yönetimini kolaylaştırır. Her repo, birbiriyle yalnızca standartlaştırılmış API'ler (**gRPC**) veya mesaj kuyrukları (**RabbitMQ**) aracılığıyla iletişim kurar.

Bu liste, Sentiric ekosistemindeki her bir reponun nihai rolünü, **doğrulanmış teknolojisini** ve temel sorumluluklarını tanımlayan, projenin tek ve güncel referans kaynağıdır.

---

## **A. Çekirdek İletişim ve AI Servisleri**
*(Platformun kalbi ve beyni; gerçek zamanlı insan-makine etkileşimi ve zekasını yöneten temel servisler.)*

| Kategori | Repo Adı | **Doğrulanmış Teknoloji** | Temel Sorumluluklar |
| :--- | :--- | :--- | :--- |
| **İletişim** | `sentiric-sip-signaling-service` | **Rust** | Gelen SIP sinyallerini alır, `dialplan-service`'e danışarak çağrıyı orkestre eder ve `call.started` olayını RabbitMQ'ya yayınlar. |
| | `sentiric-media-service` | **Rust** | Yüksek performanslı, gerçek zamanlı ses (RTP/SRTP) akışlarını yönetir. Dinamik port tahsisi ve anons/medya dosyası çalma işlemlerinden sorumludur. |
| **Orkestrasyon**| `sentiric-agent-service` | **Go**| **Platformun asenkron beyni.** RabbitMQ'dan gelen olayları dinler, `dialplan` kararlarını uygular ve diğer uzman servisleri (gRPC ve HTTP ile) yöneterek iş akışlarını hayata geçirir. |
| **Yapay Zeka**| `sentiric-llm-service` | **Python** | **AI Dil Modeli Ağ Geçidi.** `agent-service`'ten gelen metin üretme isteklerini alır ve bunları Google Gemini, OpenAI gibi harici LLM sağlayıcılarına soyutlayarak yönlendirir. |
| | `sentiric-tts-service` | **Python** | Verilen metin girdilerini (SSML desteğiyle) doğal insan sesine dönüştürür (Text-to-Speech). |
| | `sentiric-stt-service` | **Python** | Gelen ses akışlarını veya dosyalarını yüksek doğrulukla metne dönüştürür (Speech-to-Text). |
| | `sentiric-knowledge-service`| **Python** | AI ajanları için çok-kaynaklı (dosya, web, DB) ve çok-kiracılı (multi-tenant) bir RAG bilgi tabanı sunar. Vektör veritabanını (Qdrant) yönetir. |

## **B. Veri ve Kalıcılık Servisleri**
*(Platformun kullanıcı, yapılandırma ve çağrı detay verilerini yöneten ve gRPC ile hizmet veren uzman servisler.)*

| Kategori | Repo Adı | **Doğrulanmış Teknoloji** | Temel Sorumluluklar |
| :--- | :--- | :--- | :--- |
| **Veri Yönetimi**| `sentiric-user-service` | **Go** | Kullanıcı, arayan ve kiracı (tenant) hesaplarını, kimlik bilgilerini ve yetkilerini yöneten merkezi **gRPC** servisidir. |
| | `sentiric-dialplan-service`| **Go** | Veritabanındaki kurallara göre gelen çağrıların nereye yönlendirileceğine dair stratejik kararı veren merkezi **gRPC** servisidir. |
| | `sentiric-cdr-service` | **Go** | `RabbitMQ`'dan gelen tüm çağrı yaşam döngüsü olaylarını dinler ve analiz/raporlama için veritabanına kalıcı olarak kaydeder (Call Detail Record). |

## **C. Ağ Geçitleri ve Dış Entegrasyon Servisleri**
*(Platformun dış dünya ile ve farklı protokollerle güvenli iletişim kurmasını sağlayan katman.)*

| Kategori | Repo Adı | **Doğrulanmış Teknoloji** | Temel Sorumluluklar |
| :--- | :--- | :--- | :--- |
| **Geçitler** | `sentiric-messaging-gateway-service` | **Node.js** | Sentiric'i WhatsApp, Telegram gibi harici metin tabanlı mesajlaşma kanallarıyla entegre eder ve olayları `RabbitMQ`'ya atar. |
| | `sentiric-sip-gateway-service` | **Rust** | Platformun **zırhlı ön kapısı (SBC)**. Gelen ham SIP trafiğini süzer, güvenli hale getirir, NAT sorunlarını çözer ve `sip-signaling`'e yönlendirir. |
| | `sentiric-telephony-gateway-service` | **Go/C++** | Sentiric'i geleneksel telefon şebekesi (PSTN, TDM, PRI) ile entegre eder. Telekom protokollerini SIP'e çevirir. |
| **Entegrasyon**| `sentiric-connectors-service` | **Node.js/TypeScript** | Harici iş sistemleri (CRM, ERP, Takvim) ile entegrasyon için spesifik API adaptörlerini barındırır. `agent-service` tarafından çağrılır. |

## **D. Yönetim, Geliştirici ve Kullanıcı Arayüzleri**
*(Kullanıcıların ve yöneticilerin platformla etkileşim kurmasını sağlayan araçlar ve arayüzler.)*

| Kategori | Repo Adı | **Doğrulanmış Teknoloji** | Temel Sorumluluklar |
| :--- | :--- | :--- | :--- |
| **Yönetim UI** | `sentiric-dashboard-ui` | **Next.js (React/TS)** | Sistem yöneticileri için platformu izleme, yönetme (kullanıcı, dialplan vb.) ve raporlama arayüzü. `api-gateway` ile konuşur. |
| **Kullanıcı UI**| `sentiric-web-agent-ui` | **Next.js (React/TS)** | Müşteri hizmetleri temsilcileri için çağrıları devraldığı, müşteri bilgilerini gördüğü ve AI ile etkileşim kurduğu tarayıcı tabanlı arayüz. |
| | `sentiric-mobile` | **Flutter/Dart** | Ajanlar, süpervizörler ve müşteriler için tasarlanmış platformun mobil kokpiti. |
| **Geliştirici Araçları**| `sentiric-cli` | **Python** | Geliştiriciler ve yöneticiler için platformu komut satırından yönetme, test etme ve otomatize etme aracı. `api-gateway` ile konuşur. |

## **E. Yardımcı ve Çerçeve Repoları**
*(Platformun genel işleyişini destekleyen ve geliştirme süreçlerini kolaylaştıran bileşenler.)*

| Kategori | Repo Adı | **Doğrulanmış Teknoloji** | Temel Sorumluluklar |
| :--- | :--- | :--- | :--- |
| **Yardımcı Servisler**| `sentiric-api-gateway-service` | **Go** | Tüm harici UI ve CLI istemcileri için tek, birleşik ve güvenli bir API Gateway katmanı. `gRPC-Gateway` ile REST'e çevrim yapar. |
| | `sentiric-task-service` | **Python (Celery)** | Uzun süreli, asenkron veya zamanlanmış görevleri (rapor oluşturma, model eğitimi, toplu veri işleme) yönetir. Redis'i kullanır. |
| **Paylaşımlı Kaynaklar**| `sentiric-contracts` | **Protobuf / Multi-language**| **(Kritik)** Tüm mikroservisler arasında paylaşılan API sözleşmelerini (`.proto` dosyaları) barındırır ve CI/CD ile tüm dillere (Go, Rust, Python) kod üretir. |
| | `sentiric-db-models` | **SQL / ORM** | Birden fazla servis tarafından paylaşılan veritabanı şemalarını (`init.sql`) ve gelecekteki ORM modellerini barındırır. |
| | `sentiric-assets` | **Veri Dosyaları** | Anons sesleri, UI ikonları gibi platform genelindeki statik dosyaları depolar. |
| **SDK'lar** | `sentiric-sip-client-sdk` | **JS, Swift, Kotlin** | Web (WebRTC), mobil (iOS/Android) gibi istemcilerin platforma SIP üzerinden bağlanmasını sağlayan kütüphane. |
| | `sentiric-embeddable-voice-widget-sdk`| **JavaScript/TS**| Web sitelerine kolayca entegre edilebilen "bize sesle ulaşın" widget'ı. |

## **F. Yönetim ve Altyapı Desteği**
*(Platformun genel yönetimini ve dağıtımını sağlayan repolar.)*

| Kategori | Repo Adı | **Doğrulanmış Teknoloji** | Temel Sorumluluklar |
| :--- | :--- | :--- | :--- |
| **Yönetim** | `sentiric-governance` | **Markdown / Shell**| Projenin anayasası; vizyon, mimari, standartlar ve proje yönetim panosu. **(Bu repo)** |
| **Altyapı** | `sentiric-infrastructure` | **Docker Compose / Shell**| Platformun dağıtımı için gerekli tüm altyapı kaynaklarını "Kod Olarak Altyapı" (IaC) prensibiyle yönetir. |
| **Ekosistem**| `sentiric-marketplace-service`| **Node.js** | (Gelecek Vizyonu) Üçüncü parti geliştiricilerin kendi görev ve adaptörlerini sunabileceği pazar yeri. |

---

### **Önemli Değişiklikler ve Gözlemler**

*   **Teknoloji Doğrulaması:** Tablodaki teknoloji yığınları, her bir reponun kendi `go.mod`, `Cargo.toml`, `package.json` gibi dosyaları incelenerek doğrulanmış ve güncellenmiştir.
*   **Repo Sayısı:** `sentiric-mobile` reposu da dahil edilerek toplam **28 repo** listeye eklenmiştir.
*   **Sorumluluk Detayları:** Her bir servisin temel sorumluluğu, kendi `README.md` dosyasındaki açıklamalara göre daha net ve spesifik hale getirilmiştir. Örneğin, `sip-gateway`'in bir SBC rolü üstlendiği veya `knowledge-service`'in çok-kiracılı olduğu gibi kritik detaylar eklenmiştir.
*   **Tutarlılık:** Bu belge, artık projenin fiziksel yapısıyla ve beyan edilen vizyonuyla tam bir tutarlılık içindedir.

```