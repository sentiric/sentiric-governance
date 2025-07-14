# 🌉 Sentiric: MVP'den Üretim Mimarisine Geçiş Köprüsü

Bu doküman, mevcut **Node.js tabanlı MVP** ile nihai **Python tabanlı Üretim Mimarisi** arasındaki temel farkları, bu farkların nedenlerini ve geçiş stratejisini açıklamaktadır.

## 1. Felsefe: "Canlı Laboratuvar"

MVP projemiz, bir kenara atılacak bir "kullan-at" prototip değildir. O, bizim **"canlı laboratuvarımızdır"**. Yeni fikirleri (çoklu parametre çıkarma, RAG, diyalog akışı vb.) hızla test ettiğimiz, somutlaştırdığımız ve potansiyel müşterilere "İşte bunu yapabiliyoruz!" dediğimiz çevik geliştirme alanımızdır.

Üretim projesi geliştikçe, MVP'deki test edilmiş ve onaylanmış mantık blokları, Python'daki daha sağlam, ölçeklenebilir ve kurumsal karşılıklarına aktarılacaktır.

## 2. Temel Teknolojik Farklılıklar

| Bileşen | MVP Yaklaşımı (Hız ve Prototipleme) | Üretim Mimarisi (Ölçeklenebilirlik ve Dayanıklılık) | Neden Farklı? |
| :--- | :--- | :--- | :--- |
| **Konuşma-Metin (STT)** | Tarayıcının kendi `SpeechRecognition` API'si. | Sunucu tarafında çalışan harici STT servislerine (Deepgram, Whisper vb.) bağlanan **adaptörler**. | **Kontrol & Kalite:** Sunucu tarafı STT, gürültü filtreleme, farklı dillere destek ve daha yüksek doğruluk oranı gibi konularda tam kontrol sağlar. |
| **Çekirdek Mantık (Worker)** | Tek bir `worker.js` dosyası ve modüller. | `sentiric-agent-worker` (Python/FastAPI) mikroservisi. | **Ölçeklenebilirlik:** Python, AI kütüphaneleri ve ağır işlem yükleri için daha olgun bir ekosisteme sahiptir. Mikroservis yapısı, worker'ın bağımsız olarak ölçeklenmesini sağlar. |
| **İletişim** | Direkt WebSocket bağlantıları (Gateway <-> Worker). | **RabbitMQ** mesaj kuyruğu üzerinden asenkron iletişim. | **Dayanıklılık:** Mesaj kuyruğu, servislerden biri çöktüğünde bile sistemin geri kalanının çalışmaya devam etmesini ve mesajların kaybolmamasını garanti eder. |
| **Yapılandırma** | `.env` dosyası ve kod içi mantık. | **YAML tabanlı "Reçete" dosyaları** ile diyalog akışlarını, görevleri ve adaptörleri koddan bağımsız olarak tanımlama. | **Esneklik:** Teknik olmayan kullanıcılar bile YAML dosyalarını düzenleyerek sistemin davranışını değiştirebilir. Yeni görevler eklemek kod değişikliği gerektirmez. |
| **Veritabanı** | Basit bir `veritabani.json` dosyası. | **PostgreSQL** (kalıcı veriler için) ve **Redis** (anlık durum için). | **Performans ve Güvenilirlik:** JSON dosyası çok kullanıcılı ortamlar için uygun değildir. SQL ve Redis, kurumsal düzeyde veri yönetimi ve hız sunar. |

## 3. Geçiş Stratejisi

MVP, geliştirme sürecimiz boyunca canlı kalacaktır. Ana Python projesinde bir özellik (`sentiric-agent-worker`'da SSML desteği gibi) geliştirildiğinde, MVP'deki karşılığı da bu yeni standardı kullanacak şekilde güncellenebilir veya zamanla tamamen kaldırılarak yerini ana projeye bırakabilir. Bu, sürekli bir geri bildirim ve entegrasyon döngüsü yaratır.