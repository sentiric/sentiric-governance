# 🗺️ Sentiric: Ekosistem ve Repolar (V3.0 - 26 Repo Desteğiyle)

Sentiric platformu, her biri belirli bir sorumluluğa sahip, bağımsız olarak geliştirilen ve yönetilen toplam **26 adet depodan (repository)** oluşur. Bu modüler yapı, projenin "Tak-Çıkar Lego Seti" felsefesini somutlaştırır, ölçeklenebilirliği artırır, sorumlulukları netleştirir ve karmaşık bir sistemin yönetimini kolaylaştırır. Her repo, kendi başına çalışabilen bir birimi temsil eder ve birbiriyle yalnızca API'ler (HTTP/REST veya gRPC) veya Mesaj Kuyrukları aracılığıyla iletişim kurar.

Bu liste, Sentiric ekosistemindeki her bir reponun rolünü, önerilen teknoloji yığınını ve temel sorumluluklarını tanımlar.

---

## **A. Çekirdek İletişim ve AI Servisleri**
*(Platformun kalbi ve beyni; gerçek zamanlı insan-makine etkileşimi ve zekasını yöneten temel servisler.)*

| Kategori | Repo Adı                     | Temel Sorumluluklar                                                                                                                                                                                            | Önerilen Dil(ler)      |
| :------- | :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **İletişim** | `sentiric-sip-signaling-service` | SIP çağrı sinyalleşmesini (kurulum, yönetim, sonlandırma) orkestre eder, SIP mesajlarını işler, TLS destekler ve diğer servislerin API'lerini tüketerek çağrı akışını sağlar. CDR olaylarını yayınlar.             | Node.js → Go / Rust                |
|          | `sentiric-media-service`     | Gerçek zamanlı ses/görüntü (RTP/SRTP) akışlarını yönetir, proxy'ler, şifreler/deşifreler ve medya bazlı etkileşimleri (anons, IVR) sağlar.                                                                             | Go → Go / Rust / C++       |
| **Yapay Zeka** | `sentiric-tts-service`       | Metin girdilerini doğal insan sesine dönüştüren yapay zeka servisidir (Text-to-Speech).                                                                                                                     | Python → Python + C++ Engine                 |
|          | `sentiric-stt-service`       | Ses girdilerini metne dönüştüren yapay zeka servisidir (Speech-to-Text).                                                                                                                                                    | Python → Python + C++ Engine                 |
|          | `sentiric-knowledge-service` | Sentiric'in AI ajanları için yapılandırılmış, indekslenmiş ve sorgulanabilir bir bilgi tabanı oluşturan servistir. Dış kaynaklardan veri çeker ve indeksler.                                                 | Python, Java           |
|          | `sentiric-agent-service`     | Sentiric'in akıllı "ajan" işlevini üstlenen, diyalog akışlarını yöneten, AI servislerini koordine eden ve yanıt üreten temel mantık servisidir.                                                                   | Python, Node.js        |

## **B. Veri ve Kalıcılık Servisleri**
*(Platformun kullanıcı, yapılandırma ve çağrı detay verilerini yöneten servisler.)*

| Kategori | Repo Adı                  | Temel Sorumluluklar                                                                                                                                                                                            | Önerilen Dil(ler)      |
| :------- | :------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Veri Yönetimi** | `sentiric-user-service`     | Kullanıcı hesaplarını, kimlik bilgilerini ve aktif SIP kayıtlarını güvenli ve kalıcı bir şekilde yöneten servistir. SIP Digest Authentication'ı gerçekleştirir.                                             | Node.js, Go            |
|          | `sentiric-dialplan-service` | Gelen çağrı hedeflerine göre dinamik olarak en uygun yönlendirme kararını sağlayan servistir. Arama planı kurallarını saklar ve sunar.                                                                              | Node.js, Go            |
|          | `sentiric-cdr-service`      | Tüm çağrı detaylarını ve yaşam döngüsü olaylarını toplar, işler ve kalıcı olarak depolar (Call Detail Record). Raporlama ve analiz için veriyi hazırlar.                                                        | Node.js, Python, Go    |

## **C. Ağ Geçitleri ve Dış Entegrasyon Servisleri**
*(Platformun dış dünya ile ve farklı protokollerle güvenli ve uyumlu iletişim kurmasını sağlayan katman.)*

| Kategori | Repo Adı                           | Temel Sorumluluklar                                                                                                                                                                                            | Önerilen Dil(ler)            |
| :------- | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------- |
| **Geçitler** | `sentiric-messaging-gateway-service` | Sentiric'i WhatsApp, Telegram, SMS gibi çeşitli harici mesajlaşma kanallarıyla entegre eden servistir. Mesaj formatlarını normalize eder.                                                               | Node.js, Go, Python          |
|          | `sentiric-sip-gateway-service`     | Sentiric'in iç SIP ağı ile dış SIP ağları veya servis sağlayıcıları arasında aracı görevi gören servistir (SIP Trunking). Dış SIP trafiğini çevirir ve yönlendirir.                                     | Node.js, Go                  |
|          | `sentiric-telephony-gateway-service` | Sentiric'i geleneksel telefon şebekesi (PSTN), TDM veya diğer legacy telekomünikasyon sistemleriyle entegre eden servistir. Telekom protokollerini dahili formatlara çevirir.                           | Go, C++                      |
| **Entegrasyon** | `sentiric-connectors-service`      | Harici iş sistemleri (CRM, ERP, Help Desk) ile entegrasyon için spesifik API adaptörleri veya mikroservisleri barındıran genel bir connector servisidir.                                           | Python, Node.js, Java        |

## **D. Yönetim, Geliştirici ve Kullanıcı Arayüzleri**
*(Kullanıcıların ve yöneticilerin platformla etkileşim kurmasını sağlayan araçlar ve arayüzler.)*

| Kategori | Repo Adı                           | Temel Sorumluluklar                                                                                                                                                                                            | Önerilen Dil(ler)              |
| :------- | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------- |
| **Yönetim UI** | `sentiric-dashboard-ui`            | Sistem yöneticileri ve iş analistleri için platformun genel durumunu izleme, kullanıcı/dialplan yönetimi ve raporlama sağlayan merkezi bir web arayüzüdür.                                                | JavaScript/TypeScript (React)  |
| **Kullanıcı UI** | `sentiric-web-agent-ui`            | Müşteri hizmetleri temsilcileri veya diğer son kullanıcılar için tarayıcı tabanlı bir "ajan" arayüzüdür. Sesli ve metinli etkileşimleri yönetir.                                                         | JavaScript/TypeScript (React)  |
|          | `sentiric-embeddable-voice-widget-sdk` | Web sitelerine veya mobil uygulamalara kolayca entegre edilebilen, Sentiric'in sesli etkileşim yeteneklerini sunan bir JavaScript widget'ı/SDK'sıdır.                                                         | JavaScript/TypeScript          |
| **Geliştirici Araçları** | `sentiric-cli`                     | Geliştiriciler ve yöneticiler için Sentiric platformunu komut satırından yönetme ve otomatize etme aracıdır.                                                                                         | Python, Go                     |

## **E. Yardımcı ve Çerçeve Repoları**
*(Platformun genel işleyişini destekleyen ve geliştirme süreçlerini kolaylaştıran bileşenler.)*

| Kategori | Repo Adı                   | Temel Sorumluluklar                                                                                                                                                                                            | Önerilen Dil(ler)                |
| :------- | :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------- |
| **Yardımcı Servisler** | `sentiric-api-gateway-service` | Tüm Sentiric mikroservisleri için tek ve birleşik bir API Gateway ve/veya Backend-for-Frontend (BFF) katmanı. Güvenlik, yönlendirme gibi çapraz kesen konuları yönetir.                                  | Node.js, Go                      |
|          | `sentiric-task-service`    | Uzun süreli, asenkron veya zamanlanmış görevleri (batch işlemleri, AI modeli eğitimi) yöneten ve yürüten bir servistir.                                                                                        | Python, Node.js                  |
| **Paylaşımlı Kaynaklar** | `sentiric-core-interfaces`   | Tüm mikroservisler arasında paylaşılan temel API sözleşmeleri (gRPC protos, OpenAPI specs), fundamental data structures, and universal constants. (Çalışan bir servis değildir, bir kütüphanedir).     | Dilden bağımsız (Proto/YAML)     |
|          | `sentiric-db-models`       | Birden fazla servis tarafından paylaşılan veritabanı şemalarını ve ORM modellerini barındırır. (Çalışan bir servis değildir, bir kütüphanedir).                                                                   | SQL, Python, Node.js             |
|          | `sentiric-assets`          | Statik varlıkları (medya dosyaları, UI bileşenleri, resimler, ikonlar) depolar. (Çalışan bir servis değildir, bir depolama reposudur).                                                                         | N/A (Veri içerir)                |
| **SDK'lar** | `sentiric-sip-client-sdk`    | Sentiric SIP Server'a bağlanan, SIP iletişimini (softphone, mobil, WebRTC) sağlayan bir istemci SDK'sıdır.                                                                                                   | JavaScript, Swift, Kotlin, C#    |
|          | `sentiric-api-sdk-python`  | Python geliştiricilerinin Sentiric API'lerine kolayca erişmesi ve platformla entegre olması için bir SDK'dır.                                                                                                 | Python                           |
|          | `sentiric-api-sdk-javascript` | JavaScript geliştiricilerinin Sentiric API'lerine kolayca erişmesi ve web uygulamalarına entegre olması için bir SDK'dır.                                                                                  | JavaScript, TypeScript           |

## **F. Yönetim ve Altyapı Desteği**
*(Platformun genel yönetimini ve dağıtımını sağlayan repolar.)*

| Kategori | Repo Adı                     | Temel Sorumluluklar                                                                                                                                                                                            | Önerilen Dil(ler)      |
| :------- | :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Yönetim** | `sentiric-governance`        | Projenin anayasası; vizyon, mimari, yol haritası, standartlar, süreçler ve paylaşılan geliştirici araçları (`snapshot_tool.py`) ve dokümantasyonlarını barındırır. **(Bu repo)**                           | Markdown, Python, Shell |
| **Altyapı** | `sentiric-infrastructure`    | Platformun bulut veya on-prem dağıtımı için gerekli tüm altyapı kaynaklarını "Kod Olarak Altyapı" (IaC) prensibiyle yöneten repo. Kubernetes manifestleri, Helm chart'ları içerir.                            | Terraform, K8s YAML, Shell |
| **Ekosistem** | `sentiric-marketplace-service` | Üçüncü parti geliştiricilerin kendi görev ve adaptörlerini Sentiric kullanıcılarına sunabileceği gelecekteki pazar yeri platformudur.                                                                    | Node.js, JavaScript    |