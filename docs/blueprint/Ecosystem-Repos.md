# 🗺️ Sentiric: Ekosistem ve Repolar (v5.0 - Nihai ve Bütünleşik Sürüm)

Sentiric platformu, her biri belirli bir sorumluluğa sahip, bağımsız olarak geliştirilen ve yönetilen toplam **26 adet depodan (repository)** oluşur. Bu modüler yapı, projenin "Tak-Çıkar Lego Seti" felsefesini somutlaştırır ve karmaşık bir sistemin yönetimini kolaylaştırır. Her repo, birbiriyle yalnızca standartlaştırılmış API'ler (**gRPC**) veya mesaj kuyrukları (**RabbitMQ**) aracılığıyla iletişim kurar.

Bu liste, Sentiric ekosistemindeki her bir reponun nihai rolünü, kararlaştırılan teknolojisini ve temel sorumluluklarını tanımlar.

---

## **A. Çekirdek İletişim ve AI Servisleri**
*(Platformun kalbi ve beyni; gerçek zamanlı insan-makine etkileşimi ve zekasını yöneten temel servisler.)*

| Kategori | Repo Adı | **Nihai Teknoloji** | Temel Sorumluluklar |
| :--- | :--- | :--- | :--- |
| **İletişim** | `sentiric-sip-signaling-service` | **Rust** | SIP sinyalleşmesini orkestre eder, proxy sorunlarını çözer. Diğer çekirdek servisleri **gRPC** ile anlık olarak çağırır ve `call.started` olayını **RabbitMQ**'ya yayınlar. |
| | `sentiric-media-service` | **Rust** | Gerçek zamanlı ses/görüntü (RTP/SRTP) akışlarını yönetir. **gRPC** ile port ayırır, harici komutlarla (REST/API) medya oynatır. |
| **Yapay Zeka**| `sentiric-agent-service` | **Python (FastAPI)**| **Platformun asıl beyni.** `RabbitMQ`'dan gelen olayları dinler, diyalog akışını yönetir, AI motorlarını (STT/LLM/TTS) orkestra eder ve görevleri yürütür. |
| | `sentiric-tts-service` | **Python** | Metin girdilerini doğal insan sesine dönüştürür (Text-to-Speech). |
| | `sentiric-stt-service` | **Python** | Ses girdilerini metne dönüştürür (Speech-to-Text). |
| | `sentiric-knowledge-service`| **Python** | AI ajanları için RAG mimarisiyle yapılandırılmış, sorgulanabilir bir bilgi tabanı sunar. |

## **B. Veri ve Kalıcılık Servisleri (gRPC Tabanlı)**
*(Platformun kullanıcı, yapılandırma ve çağrı detay verilerini yöneten ve **gRPC** ile hizmet veren uzman servisler.)*

| Kategori | Repo Adı | **Nihai Teknoloji** | Temel Sorumluluklar |
| :--- | :--- | :--- | :--- |
| **Veri Yönetimi**| `sentiric-user-service` | **Go** | Kullanıcı hesaplarını, kimlik bilgilerini ve yetkileri yöneten **gRPC** servisidir. |
| | `sentiric-dialplan-service`| **Go** | Gelen çağrı hedeflerine göre yönlendirme kararı sağlayan **gRPC** servisidir. |
| | `sentiric-cdr-service` | **Go/Python** | `RabbitMQ`'dan gelen tüm çağrı yaşam döngüsü olaylarını dinler ve veritabanına kalıcı olarak kaydeder (Call Detail Record). |

## **C. Ağ Geçitleri ve Dış Entegrasyon Servisleri**
*(Platformun dış dünya ile ve farklı protokollerle güvenli iletişim kurmasını sağlayan katman.)*

| Kategori | Repo Adı | **Nihai Teknoloji** | Temel Sorumluluklar |
| :--- | :--- | :--- | :--- |
| **Geçitler** | `sentiric-messaging-gateway-service` | **Node.js** | Sentiric'i WhatsApp, Telegram gibi harici mesajlaşma kanallarıyla entegre eder ve olayları `RabbitMQ`'ya atar. |
| | `sentiric-sip-gateway-service` | **Go/Rust** | Sentiric'in iç SIP ağı ile dış SIP ağları (SIP Trunking) arasında aracı görevi görür. `sip-signaling`'e yönlendirme yapar. |
| | `sentiric-telephony-gateway-service` | **Go/C++** | Sentiric'i geleneksel telefon şebekesi (PSTN, TDM) ile entegre eder. Telekom protokollerini SIP'e çevirir. |
| **Entegrasyon**| `sentiric-connectors-service` | **Python** | Harici iş sistemleri (CRM, ERP, Takvim) ile entegrasyon için spesifik API adaptörlerini barındırır. `agent-service` tarafından çağrılır. |

## **D. Yönetim, Geliştirici ve Kullanıcı Arayüzleri**
*(Kullanıcıların ve yöneticilerin platformla etkileşim kurmasını sağlayan araçlar ve arayüzler.)*

| Kategori | Repo Adı | **Nihai Teknoloji** | Temel Sorumluluklar |
| :--- | :--- | :--- | :--- |
| **Yönetim UI** | `sentiric-dashboard-ui` | **React/TypeScript** | Sistem yöneticileri için platformu izleme, yönetme ve raporlama arayüzü. `api-gateway` ile konuşur. |
| **Kullanıcı UI**| `sentiric-web-agent-ui` | **React/TypeScript** | Müşteri hizmetleri temsilcileri için tarayıcı tabanlı "ajan" arayüzü. |
| | `sentiric-embeddable-voice-widget-sdk`| **JavaScript/TypeScript**| Web sitelerine kolayca entegre edilebilen sesli etkileşim widget'ı. |
| **Geliştirici Araçları**| `sentiric-cli` | **Python/Go** | Geliştiriciler ve yöneticiler için platformu komut satırından yönetme ve otomatize etme aracı. `api-gateway` ile konuşur. |

## **E. Yardımcı ve Çerçeve Repoları**
*(Platformun genel işleyişini destekleyen ve geliştirme süreçlerini kolaylaştıran bileşenler.)*

| Kategori | Repo Adı | **Nihai Teknoloji** | Temel Sorumluluklar |
| :--- | :--- | :--- | :--- |
| **Yardımcı Servisler**| `sentiric-api-gateway-service` | **Go/Node.js** | Tüm mikroservisler için tek ve birleşik bir API Gateway katmanı. Güvenlik, yönlendirme gibi çapraz kesen konuları yönetir. |
| | `sentiric-task-service` | **Python (Celery)** | Uzun süreli, asenkron veya zamanlanmış görevleri (rapor oluşturma, model eğitimi) yönetir. |
| **Paylaşımlı Kaynaklar**| `sentiric-core-interfaces` | **Protobuf / OpenAPI**| **(Kritik)** Tüm mikroservisler arasında paylaşılan API sözleşmelerini (`.proto` dosyaları vb.) barındırır. (Çalışan bir servis değildir). |
| | `sentiric-db-models` | **SQL / ORM** | Birden fazla servis tarafından paylaşılan veritabanı şemalarını ve ORM modellerini barındırır. (Çalışan bir servis değildir). |
| | `sentiric-assets` | **Veri Dosyaları** | Statik varlıkları (medya dosyaları, UI ikonları) depolar. (Çalışan bir servis değildir). |
| **SDK'lar** | `sentiric-sip-client-sdk` | **JS, Swift, Kotlin** | `sip-signaling-service`'e bağlanan istemci (softphone, mobil, WebRTC) SDK'sıdır. |
| | `sentiric-api-sdk-python` | **Python** | Python geliştiricilerinin `api-gateway`'e kolayca erişmesi için bir SDK'dır. |
| | `sentiric-api-sdk-javascript`| **JavaScript/TS** | JavaScript geliştiricilerinin `api-gateway`'e kolayca erişmesi için bir SDK'dır. |

## **F. Yönetim ve Altyapı Desteği**
*(Platformun genel yönetimini ve dağıtımını sağlayan repolar.)*

| Kategori | Repo Adı | **Nihai Teknoloji** | Temel Sorumluluklar |
| :--- | :--- | :--- | :--- |
| **Yönetim** | `sentiric-governance` | **Markdown / Shell**| Projenin anayasası; vizyon, mimari, standartlar. **(Bu repo)** |
| **Altyapı** | `sentiric-infrastructure` | **Docker Compose / K8s**| Platformun dağıtımı için gerekli tüm altyapı kaynaklarını "Kod Olarak Altyapı" (IaC) prensibiyle yönetir. |
| **Ekosistem**| `sentiric-marketplace-service`| **Node.js/JS** | (Gelecek Vizyonu) Üçüncü parti geliştiricilerin kendi görev ve adaptörlerini sunabileceği pazar yeri. |

---

### **Bu Versiyonun Öncekilerden Farkı Nedir?**

*   **Tam Kapsam:** Bu liste, projenin sadece şu anki ana odak noktasını değil, aynı zamanda SDK'lar, CLI, marketplace gibi tüm vizyoner bileşenlerini de içerir.
*   **Net Teknoloji Kararları:** "Önerilen Diller" yerine, `Centiric` deneyimi ve performans hedefleri doğrultusunda **kararlaştırılan nihai teknolojiler** (Rust, Go, Python) belirtilmiştir.
*   **`core` Reposunun Yokluğu:** Mimari kararlarımız doğrultusunda, merkezi `core` reposu kaldırılmış ve görevleri ilgili uzman servislere (`sip-signaling` ve `agent-service`) dağıtılmıştır.
*   **İletişim Protokolleri:** Her servisin temel iletişim yöntemleri (gRPC, RabbitMQ, REST) sorumluluklarına eklenerek mimari daha net hale getirilmiştir.

Bu doküman, artık tüm paydaşlar için projenin tam ve eksiksiz bir haritasını sunmaktadır.
