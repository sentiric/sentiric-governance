# 🩺 Sentiric: Sorun Giderme Rehberi (Yaşayan Belge)

Bu belge, geliştirme sırasında karşılaşılan yaygın sorunları, nedenlerini ve kanıtlanmış çözümlerini içerir. Bir sorunla karşılaştığınızda ilk başvuracağınız yer burası olmalıdır. Her yeni sorun ve çözümü buraya eklenecektir.

## Vaka 1: Telefoni Bağlantısı Kurulamıyor

*   **Semptom:** `sentiric-telephony-gateway` loglarında WebSocket bağlantı hatası veya Twilio konsolunda hata mesajları.
*   **Olası Nedenler:**
    1.  Geliştirme ortamındaki servisin (localhost) dış dünyadan erişilebilir olmaması.
    2.  Twilio Webhook URL'sinin yanlış yapılandırılması.
    3.  Firewall veya ağ sorunları.
*   **Çözüm Adımları:**
    1.  **ngrok Kontrolü:** `ngrok` veya benzeri bir tünel aracı kullanarak yerel `gateway` servisinizi genel bir URL ile dış dünyaya açın.
    2.  **Twilio Ayarları:** Twilio numaranızın "A CALL COMES IN" ayarındaki Webhook URL'sinin, ngrok tarafından verilen `wss://...` formatındaki doğru WebSocket URL'sini gösterdiğinden emin olun.
    3.  **Gateway Logları:** `sentiric-telephony-gateway` servisinin loglarını detaylı inceleyerek gelen bağlantı denemelerini ve olası hataları kontrol edin.

## Vaka 2: Konuşma Gecikmesi (Latency) Çok Yüksek

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

## Vaka 3: Mermaid Şeması Oluşturma/Görüntüleme Hataları (Parse Error)

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
