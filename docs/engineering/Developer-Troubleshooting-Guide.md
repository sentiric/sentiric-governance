# 🩺 Sentiric: Sorun Giderme Rehberi (Yaşayan Belge)

Bu belge, geliştirme sırasında karşılaşılan yaygın sorunları, nedenlerini ve kanıtlanmış çözümlerini içerir. Bir sorunla karşılaştığınızda ilk başvuracağınız yer burası olmalıdır. Her yeni sorun ve çözümü buraya eklenecektir.

## Vaka: Telefoni Bağlantısı Kurulamıyor

*   **Semptom:** `sentiric-telephony-gateway` loglarında WebSocket bağlantı hatası veya Twilio konsolunda hata mesajları.
*   **Olası Nedenler:**
    1.  Geliştirme ortamındaki servisin (localhost) dış dünyadan erişilebilir olmaması.
    2.  Twilio Webhook URL'sinin yanlış yapılandırılması.
    3.  Firewall veya ağ sorunları.
*   **Çözüm Adımları:**
    1.  **ngrok Kontrolü:** `ngrok` veya benzeri bir tünel aracı kullanarak yerel `gateway` servisinizi genel bir URL ile dış dünyaya açın.
    2.  **Twilio Ayarları:** Twilio numaranızın "A CALL COMES IN" ayarındaki Webhook URL'sinin, ngrok tarafından verilen `wss://...` formatındaki doğru WebSocket URL'sini gösterdiğinden emin olun.
    3.  **Gateway Logları:** `sentiric-telephony-gateway` servisinin loglarını detaylı inceleyerek gelen bağlantı denemelerini ve olası hataları kontrol edin.

## Vaka: Konuşma Gecikmesi (Latency) Çok Yüksek

*   **Semptom:** Siz konuştuktan sonra sistemin cevap vermesi 2-3 saniyeden uzun sürüyor.
*   **Olası Nedenler:**
    1.  **ASR Gecikmesi:** Sesin metne çevrilmesi yavaş.
    2.  **LLM Gecikmesi:** LLM'in cevap üretmesi (ilk token'ı üretme süresi - Time to First Token) yavaş.
    3.  **TTS Gecikmesi:** Üretilen metnin sese çevrilmesi yavaş.
    4.  **Ağ Gecikmesi:** Servisler arasındaki (özellikle harici API'lere) gidiş-dönüş süresi yüksek.
*   **Çözüm Adımları:**
    1.  **Metrik Toplama:** `sentiric-agent-worker` içinde, her bir adımın (ASR, LLM, TTS) ne kadar sürdüğünü ölçen ve loglayan bir zamanlama mekanizması kurun. (`MONITORING_AND_LOGGING.md`'ye bakın).
    2.  **Darboğaz Tespiti:** Logları analiz ederek en çok zaman harcayan adımı tespit edin.
    3.  **Optimizasyon:**
        *   **ASR/TTS için:** Daha hızlı bir model veya "streaming" destekli bir API (örn: Deepgram) deneyin.
        *   **LLM için:** Daha küçük bir model (örn: Llama 3 8B yerine Phi-3-mini) veya daha hızlı bir sağlayıcı (örn: Groq) deneyin. Sunucu konumunuza en yakın API endpoint'ini kullanın.

## Vaka: Mermaid Şeması Oluşturma/Görüntüleme Hataları (Parse Error)

*   **Semptom:** `.md` dosyalarındaki Mermaid şemaları GitHub'da veya yerel editörde (VS Code) düzgün görüntülenmiyor. "Parse error on line X" gibi bir hata mesajı görünüyor.
*   **Olası Nedenler:**
    1.  **En Yaygın Neden: Node ID Tutarsızlığı:** Bir düğüm (node) şemanın başında `APIGateway` gibi bir ID ile tanımlanmış, ancak daha sonra `APIGatewa` veya `api-gateway` gibi farklı bir ID ile ona bağlanılmaya çalışılmış olabilir. ID'ler büyük/küçük harfe duyarlıdır ve birebir aynı olmalıdır.
    2.  **Geçersiz Karakterler:** Tırnak (`"`) içine alınmamış node ID'lerinde boşluk, `-`, `.` gibi özel karakterlerin kullanılması.
    3.  **Sözdizimi Hataları:** Eksik veya fazla parantezler, tırnak işaretleri, `-->` gibi okların yanlış yazılması.
*   **Çözüm Adımları:**
    1.  **Hata Satırını İnceleyin:** Hata mesajındaki satır numarasını ve belirtilen karakteri (`got 'PS'` gibi) kontrol edin. Bu, sorunun nerede olduğunu anlamak için ilk ipucudur.
    2.  **Node ID'lerini Kontrol Edin:** Hatalı şemadaki **tüm** node ID'lerini gözden geçirin. Tanımlandıkları yer ile kullanıldıkları yerlerin birebir aynı olduğundan emin olun.
    3.  **Tırnak ve Parantezleri Kontrol Edin:** Özellikle `subgraph` bloklarının veya karmaşık node metinlerinin (`"Metin içeren Node"`) tırnaklarının doğru kapatıldığından emin olun.
    4.  **Online Editör Kullanın:** Şemayı kopyalayıp **[Mermaid Live Editor](https://mermaid.live)** gibi bir online araca yapıştırın. Bu araçlar, hataları anında gösterir ve şemayı canlı olarak düzelterek denemenizi sağlar. Bu, en hızlı hata ayıklama yöntemidir.

## Vaka: Servis Docker'da Sürekli Yeniden Başlıyor (`Restarting`)

*   **Semptom:** `docker ps` çıktısında bir veya daha fazla servis `Restarting` durumunda görünüyor.
*   **Olası Nedenler ve Çözümler:**
    1.  **Konfigürasyon Eksikliği:**
        *   **Teşhis:** `docker logs <container_adı>` komutunda `ZORUNLU ORTAM DEĞİŞKENİ EKSİK` veya `kritik ortam değişkenleri eksik` gibi bir hata mesajı görülür.
        *   **Çözüm:** `sentiric-infrastructure/docker-compose.yml` dosyasını kontrol edin. İlgili servisin `env_file: [".env.generated"]` satırını içerdiğinden emin olun. `sentiric-config/environments/common.env` ve `.../development.env` dosyalarında gerekli değişkenlerin tanımlı olduğunu doğrulayın.
    2.  **Bağımlı Servis Henüz Hazır Değil ("Race Condition"):**
        *   **Teşhis:** Loglarda `connection refused` veya `no such host` gibi hatalar görülür. Servis, bağlanmaya çalıştığı veritabanı veya başka bir servis henüz tam olarak başlamadan devreye girmeye çalışıyordur.
        *   **Çözüm:** `docker-compose.yml` dosyasında, servisin `depends_on` bölümüne `condition: service_healthy` (eğer healthcheck varsa) veya `condition: service_started` ekleyin.

## Vaka: Rust Servislerinde "Sessiz Çöküş" (`Exited with code 0`)

*   **Semptom:** Bir Rust servisi (`sip-gateway` gibi) `Restarting (0)` durumunda. `docker logs` komutu **hiçbir çıktı vermiyor**. `docker exec` ile konteynere girip binary'yi manuel çalıştırdığınızda, hata vermeden anında komut satırına geri dönüyor.
*   **Teşhis ve Kök Neden Analizi:**
    *   Bu durum, programın bir hata (`panic`) vermeden, normal bir şekilde çalışıp hemen bittiği anlamına gelir.
    *   **Olasılık 1 (En Yaygın):** `main` fonksiyonu `Result<()>` döndürüyor ve başlangıç aşamasındaki bir hata (örn: konfigürasyon okuma, porta bağlanma) yakalanıp `Err` olarak döndürülüyor. Bu, programın "başarıyla" ama istenmeyen bir şekilde sonlanmasına neden olur.
    *   **Olasılık 2 (`dotenvy` Problemi):** `dotenvy::dotenv().ok()` komutu, Docker'ın interaktif olmayan ortamında dosya sistemi erişimiyle ilgili beklenmedik bir soruna yol açarak programın sessizce çökmesine neden olabilir.
    *   **Olasılık 3 (Minimal İmaj Sorunu):** `FROM scratch` gibi aşırı minimal bir temel imaj kullanmak, programın çalışmak için ihtiyaç duyduğu temel sistem dosyalarını (`/etc/localtime` vb.) bulamamasına ve log basamadan çökmesine neden olabilir.
*   **Kanıtlanmış Çözüm Adımları:**
    1.  **`main` Fonksiyonunu Sağlamlaştırın:** `main` fonksiyonunun `Result` döndürmediğinden, sonsuz bir `loop` içinde çalıştığından veya bir `panic` durumu dışında asla bitmeyeceğinden emin olun. Başlangıçtaki kritik hataları (`env::var`, `UdpSocket::bind` vb.) `expect()` veya `match` ile yakalayıp anlamlı bir hata mesajıyla programı `process::exit(1)` ile sonlandırın.
    2.  **`dotenvy`'yi Docker'da Devre Dışı Bırakın:** Konfigürasyonunuzu `docker-compose` üzerinden enjekte ediyorsanız, Rust kodunuzun içinde `.env` dosyası okumaya çalışmayın.
    3.  **Temel İmaj Olarak `alpine` Kullanın:** Final imajınız için `FROM scratch` yerine, temel sistem dosyalarını içeren `FROM alpine:latest` kullanın ve `ca-certificates` gibi gerekli paketleri ekleyin.

## Vaka: Docker Build Sırasında `go mod download: unknown revision` Hatası

*   **Semptom:** `make up` komutu, bir Go servisini derlerken `unknown revision vX.Y.Z` hatası veriyor.
*   **Neden:** `go.mod` dosyasında belirtilen `sentiric-contracts` versiyonuna ait `git tag` (`vX.Y.Z`), yerel makinenizde oluşturulmuş ancak `git push --tags` veya `git push origin vX.Y.Z` komutuyla GitHub'a gönderilmemiş. Docker build işlemi, bağımlılıkları doğrudan GitHub'dan çektiği için etiketi bulamıyor.
*   **Çözüm:** `sentiric-contracts` reposunda, ilgili etiketi `git push origin <tag_adı>` komutuyla GitHub'a gönderin.

## Vaka: Docker Build Sırasında `apk add: Permission denied` Hatası

*   **Semptom:** Go servislerinin `Dockerfile`'ı, `apk add` komutunu çalıştırırken paket depolarına erişemiyor.
*   **Neden:** Alpine Linux'un paket depolarıyla ilgili geçici bir ağ sorunu veya Docker'ın WSL'deki ağ yapılandırmasıyla ilgili bir çakışma olabilir.
*   **Çözüm:** `builder` aşaması için `golang:1.24-alpine` yerine daha stabil olan `golang:1.24-bullseye` (Debian tabanlı) imajını kullanın ve paketleri `apt-get` ile kurun. Bu, derleme ortamını standartlaştırır ve bu tür ağ sorunlarına karşı daha dayanıklıdır.