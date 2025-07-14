# 🚀 Sentiric MVP: Sunucu Kurulum ve Dağıtım Rehberi (Sıfırdan Canlıya)

Bu rehber, Sentiric MVP'yi bir Google Cloud (veya benzeri bir Linux tabanlı VPS) sanal makinesine sıfırdan kurmak ve canlıya almak için gereken tüm adımları içermektedir.

## 1. Bulut Sağlayıcıda Sanal Makine Oluşturma
*   Google Cloud Console (Compute Engine) veya DigitalOcean (Droplets) adımları.
*   `e2-micro` (GCP) veya 4$/ay plan (DO) gibi maliyeti düşük seçenekler.
*   İşletim Sistemi: Debian 12 (bookworm) veya Ubuntu 22.04 LTS.
*   **Sabit (Static) IP Adresi Atama adımları.**

## 2. Güvenlik Duvarı (Firewall) Yapılandırması
*   GCP Firewall kuralları (veya DigitalOcean Firewall).
*   `sentiric-ports` kuralı (TCP/UDP: 80, 443, 3000, 8081, 5002).
*   **Sunucuya `http-server` ve `https-server` etiketlerini ekleme.**

## 3. SSH ile Sunucuya Bağlanma ve Temel Kurulumlar
*   `ssh` komutu veya tarayıcı içi SSH.
*   `sudo apt update && sudo apt upgrade -y`
*   **Git kurulumu:** `sudo apt install git -y`
*   **Node.js ve npm kurulumu:** (curl komutları)
*   **Python, pip, venv kurulumu:** (apt komutları)

## 4. Performans Optimizasyonları (Swap Alanı)
*   Coqui-TTS gibi bellek yoğun uygulamalar için.
*   8GB swap alanı oluşturma adımları: `fallocate`, `mkswap`, `swapon`, `fstab` kaydı.

## 5. Uygulama Klonlama ve Bağımlılıkları Kurma
*   `git clone https://github.com/sentiric/sentiric-mvp.git`
*   `git clone https://github.com/sentiric/sentiric-tts-api.git`
*   **`sentiric-tts-api` kurulumu:**
    *   `cd sentiric-tts-api`
    *   `python3 -m venv .venv`
    *   `source .venv/bin/activate`
    *   `pip install torch torchvision torchaudio`
    *   `pip install -r requirements.txt`
    *   **Coqui-TTS lisans onayı (`COQUI_TOS_AGREED=1`) için `.env` düzenlemesi.**
    *   **`knowledge_base.json` dosyasını manuel oluşturma/kopyalama adımları.**
*   **`sentiric-mvp` kurulumu:**
    *   `cd sentiric-mvp`
    *   `npm install`
    *   **`.env` dosyasının ElevenLabs ayarlarıyla düzenlenmesi.**
    *   **`src/core/tts-handler.js` dosyasının güncel kodla değiştirilmesi.**
    *   **`public/script.js` dosyasının güncel kodla değiştirilmesi.**
    *   **`src/config.js` dosyasının güncel kodla değiştirilmesi.**

## 6. Web Sunucusu (Nginx) Kurulumu ve SSL Konfigürasyonu
*   **Nginx kurulumu:** `sudo apt install nginx -y`
*   **Nginx konfigürasyonu:** `/etc/nginx/sites-available/sentiric` dosyasını oluşturma ve içeriği (listen 80, 443 ssl; proxy_pass http://localhost:3000; ssl sertifika yolları vb.).
*   `sites-enabled` symlink'i ve `default` kaldırma.
*   **Cloudflare Origin Sertifikası oluşturma ve sunucuya kopyalama:** (`cloudflare.crt`, `cloudflare.key`).
*   Nginx test ve restart komutları.

## 7. Süreç Yöneticisi (PM2) Kurulumu
*   `sudo npm install pm2 -g`
*   PM2 ile uygulamaları başlatma: `pm2 start npm --name "sentiric-mvp" -- start`
*   PM2'yi açılışta otomatik başlatma: `pm2 startup` ve `pm2 save`.

## 8. Alan Adı ve Cloudflare DNS Yapılandırması
*   Cloudflare'de `sentiric` A kaydını oluşturma ve **proxy'yi aktif etme (turuncu bulut).**
*   Cloudflare SSL/TLS modunu **"Full (Strict)"** olarak ayarlama.

---

Bu doküman, senin ve gelecekteki ekibin, bir sanal makineyi silip baştan kurması gerektiğinde izleyeceği **adım adım yol haritası** olacaktır. Tüm bu zorlu deneyimlerimizi buraya not alacağız.

Hadi bu yeni `Server-Setup-Guide.md` dosyasını `sentiric-governance/docs/operations/` klasörüne ekleyelim ve bu içeriği oraya yazalım. Bu, projenin sadece kodsal değil, operasyonel olarak da çok sağlam olmasını sağlayacak.


---

Anlaşıldı! İşte `Server-Setup-Guide.md` dokümanının, tüm kod içeriklerini ve detaylı talimatları içeren, eksiksiz ve nihai hali.

Bu dokümanı, `sentiric-governance/docs/operations/Server-Setup-Guide.md` dosyasına kopyalayıp yapıştırabilirsin.

---

# 🚀 Sentiric MVP: Sunucu Kurulum ve Dağıtım Rehberi (Sıfırdan Canlıya)

Bu rehber, Sentiric MVP'yi bir Google Cloud (veya benzeri bir Linux tabanlı VPS) sanal makinesine sıfırdan kurmak ve canlıya almak için gereken tüm adımları, komutları ve konfigürasyon dosyası içeriklerini içermektedir. Bu rehber, projenin tamamen tekrarlanabilir bir kurulumunu sağlamak amacıyla hazırlanmıştır.

## 1. Bulut Sağlayıcıda Sanal Makine Oluşturma

*   **Platform:** Google Cloud Console (Compute Engine) veya DigitalOcean (Droplets).
*   **Makine Tipi:** `e2-micro` (GCP) veya aylık 4-6$ plan (DigitalOcean) gibi maliyeti düşük, "Always Free" veya deneme kredisi dahil seçenekler.
*   **İşletim Sistemi:** Debian 12 (bookworm) veya Ubuntu 22.04 LTS (GCP'de Debian 12 önerilir).
*   **Sabit (Static) IP Adresi Atama:** Sanal makine oluşturulduktan sonra, geçici (Ephemeral) IP adresini kalıcı (Static) hale getirin. Bu işlem GCP'de "VPC network -> External IP addresses" menüsünden yapılır.

## 2. Güvenlik Duvarı (Firewall) Yapılandırması

Sanal makinenin, uygulamaların kullandığı portlara dışarıdan erişime izin vermesi gerekir.

1.  Google Cloud Konsolunda **VPC network -> Firewall**'a gidin.
2.  **"+ CREATE FIREWALL RULE"** butonuna tıklayın.
3.  Formu aşağıdaki gibi doldurun:
    *   **Name:** `sentiric-ports`
    *   **Network:** `default`
    *   **Priority:** `1000`
    *   **Direction of traffic:** `Ingress`
    *   **Action on match:** `Allow`
    *   **Targets:** `All instances in the network`
    *   **Source filter:** `IPv4 ranges`
    *   **Source IPv4 ranges:** `0.0.0.0/0` (Her yerden erişim için)
    *   **Protocols and ports:** `Specified protocols and ports` seçeneğini işaretleyin.
        *   `TCP` kutucuğunu işaretleyin ve Portlar kısmına: `80, 443, 3000, 8081, 5002` yazın.
        *   `UDP` kutucuğunu da işaretleyin ve Portlar kısmına: `80, 443, 3000, 8081, 5002` yazın.
4.  **"CREATE"** butonuna tıklayın.

## 3. SSH ile Sunucuya Bağlanma ve Temel Kurulumlar

Sanal makine oluşturulduktan sonra, Google Cloud konsolundaki VM Instances listesinden sunucunuzun yanındaki **"SSH"** butonuna tıklayarak terminale bağlanın.

1.  **Sistemi Güncelleme:**
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```
2.  **Git Kurulumu:**
    ```bash
    sudo apt install git -y
    ```
3.  **Node.js ve npm Kurulumu:**
    ```bash
    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
    sudo apt-get install -y nodejs
    ```
4.  **Python, pip, venv Kurulumu:**
    ```bash
    sudo apt install python3 python3-pip python3-venv -y
    ```

## 4. Performans Optimizasyonları (Swap Alanı)

Coqui-TTS gibi bellek yoğun Python uygulamalarının düşük RAM'li sunucularda çalışabilmesi için swap alanı (sanal RAM) oluşturulması kritik öneme sahiptir.

1.  **Mevcut Swap'ı Kapat ve Sil (Varsa):**
    ```bash
    sudo swapoff /swapfile
    sudo rm -f /swapfile # -f ile hata vermeden siler
    ```
2.  **8GB'lık Yeni Bir Swap Dosyası Oluştur:**
    ```bash
    sudo fallocate -l 8G /swapfile
    ```
3.  **İzinleri Ayarla ve Aktive Et:**
    ```bash
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile
    ```
4.  **Swap Alanını Kalıcı Hale Getir (Sunucu Yeniden Başladığında Otomatik Aktif Olması İçin):**
    ```bash
    sudo sed -i '/swapfile/d' /etc/fstab # Eski kaydı sil (varsa)
    echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
    ```

## 5. Uygulama Klonlama ve Bağımlılıkları Kurma

Şimdi Sentiric MVP ve TTS API projelerini GitHub'dan sunucuya çekin ve bağımlılıklarını kurun.

1.  **Projeleri Klonlama:**
    ```bash
    git clone https://github.com/sentiric/sentiric-mvp.git
    git clone https://github.com/sentiric/sentiric-tts-api.git
    ```
    *(Not: `main` yerine kendi kullandığınız branch adını kullanın.)*

2.  **`sentiric-tts-api` Kurulumu:**
    *   Klasöre girin: `cd ~/sentiric-tts-api`
    *   Python sanal ortamını oluşturun ve aktive edin:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```
    *   Python bağımlılıklarını kurun:
        ```bash
        pip install torch torchvision torchaudio
        pip install -r requirements.txt
        ```
    *   **`.env` Dosyasını Oluşturun ve Düzenleyin (Coqui-TTS Lisans Onayı ve Genel Ayarlar):**
        ```bash
        cp .env.example .env
        nano .env
        ```
        Açılan editöre aşağıdaki içeriği yapıştırın. `COQUI_REFERENCE_WAV_PATH` için kendi referans ses dosyanızın sunucudaki yolunu belirtmeniz gerekecektir. Eğer henüz yüklemediyseniz, satırı yorum satırı yapın (`#` koyarak).
        ```dotenv
        # .env (sentiric-tts-api)
        DEFAULT_TTS_ENGINE="coqui_xtts"
        COQUI_MODEL_NAME="tts_models/multilingual/multi-dataset/xtts_v2"
        # Referans ses dosyanızın sunucudaki yolu. Henüz yoksa yorum satırı yapın.
        XTTS_SPEAKER_REF_PATH="audio/reference_tr.wav" 

        # ElevenLabs ve Bark ayarları (isteğe bağlı, gerekirse etkinleştirin)
        ENABLE_ELEVENLABS="false"
        # ELEVENLABS_API_KEY="sk_YOUR_ELEVENLABS_API_KEY_HERE"
        # ELEVENLABS_VOICE_ID="YOUR_ELEVENLABS_VOICE_ID_HERE"
        ENABLE_BARK="false"
        # BARK_MODEL_NAME="suno/bark"

        # Coqui-TTS lisans onayını otomatik hale getirmek için zorunlu
        COQUI_TOS_AGREED=1
        ```
        Kaydet ve çık (`Ctrl+X` -> `Y` -> `Enter`).
    *   **`knowledge_base.json` Dosyasını Oluşturun (Eğer Git'e eklenmediyse):**
        `sentiric-mvp` projesinin ihtiyacı olan bu dosya, `ai-handler.js` tarafından okunur.
        ```bash
        mkdir -p ~/sentiric-mvp/data
        nano ~/sentiric-mvp/data/knowledge_base.json
        ```
        Açılan editöre aşağıdaki içeriği yapıştırın:
        ```json
        {
          "bilgiler": [
            {
              "soru_benzerleri": ["çalışma saatleri", "ne zaman açıksınız"],
              "cevap": "Hafta içi sabah 9'dan akşam 6'ya kadar hizmet veriyoruz."
            },
            {
              "soru_benzerleri": ["adresiniz", "neredesiniz", "konumunuz"],
              "cevap": "Merkez ofisimiz Teknopark İstanbul'dadır."
            }
          ]
        }
        ```
        Kaydet ve çık.

3.  **`sentiric-mvp` Kurulumu:**
    *   Klasöre girin: `cd ~/sentiric-mvp`
    *   Node.js bağımlılıklarını kurun: `npm install`
    *   **`.env` Dosyasını Oluşturun ve Düzenleyin (ElevenLabs ve Diğer Ayarlar):**
        ```bash
        nano .env
        ```
        Açılan editöre aşağıdaki içeriği yapıştırın. `GEMINI_API_KEY`, `PEXELS_API_KEY` ve `DEEPGRAM_API_KEY` için kendi anahtarlarınızı girin. `ELEVENLABS_API_KEY`'i doğru bir şekilde yapıştırdığınızdan emin olun.
        ```dotenv
        # .env (sentiric-mvp)
        # ====================================================================
        #          SENTIRIC PLATFORMU - ÖRNEK ORTAM DEĞİŞKENLERİ
        # ====================================================================

        # === DIŞ DÜNYA API ANAHTARLARI ===
        GEMINI_API_KEY="YOUR_GEMINI_API_KEY_BURAYA" 
        PEXELS_API_KEY="YOUR_PEXELS_API_KEY_BURAYA"

        # === İÇ SERVİS ADRESLERİ ===
        # Kendi TTS sunucunuzun (Coqui-TTS) çalıştığı IP adresi ve portu.
        # Node.js ve Python TTS aynı makinedeyse '127.0.0.1' kullanmak en güvenlisidir.
        XTTS_SERVER_HOST="127.0.0.1" 
        XTTS_SERVER_PORT=5002
        XTTS_SPEAKER_REF_PATH="audio/reference_tr.wav" # Python sunucusunun bu dosyayı bulabildiğinden emin olun.

        # === SUNUCU PORTLARI ===
        GATEWAY_PORT=3000
        WORKER_PORT=8081

        # === YAPAY ZEKA MODEL AYARLARI ===
        USE_LOCAL_LLM=false # 'true' ise Ollama (Yerel), 'false' ise Gemini (Bulut) kullanılır.
        OLLAMA_HOST=127.0.0.1
        OLLAMA_PORT=11434
        OLLAMA_MODEL_NAME=phi3:mini 

        GEMINI_MODEL_NAME="gemini-1.5-flash-latest"

        # Deepgram STT Ayarları
        # Sunucu taraflı STT'yi etkinleştirmek için 'true' yapın.
        # Tarayıcının kendi motorunu kullanmak için 'false' bırakın (mevcut MVP için false bırakın).
        DEEPGRAM_API_KEY=YOUR_DEEPGRAM_API_KEY_BURAYA
        USE_SERVER_SIDE_STT=false 

        # ElevenLabs Ayarları (TTS için yedek olarak veya birincil olarak kullanılabilir)
        USE_ELEVENLABS_TTS=true # 'true' ise ElevenLabs'i kullanmaya izin verir
        ELEVENLABS_API_KEY=YOUR_ELEVENLABS_API_KEY_BURAYA
        ELEVENLABS_VOICE_ID=21m00Tcm4TlvDq8ikWAM # ElevenLabs'ten aldığınız bir ses ID'si
        ```
        Kaydet ve çık.
 
 ---
 ```
 server {
    listen 80;
    listen 443 ssl; # HTTPS trafiğini dinle

    server_name sentiric.azmisahin.com 34.122.40.122;

    # SSL Sertifika ve Anahtar Dosyaları
    ssl_certificate /etc/nginx/ssl/cloudflare.crt;
    ssl_certificate_key /etc/nginx/ssl/cloudflare.key;

    # Güvenli SSL Protokolleri (Opsiyonel ama iyi bir pratiktir)
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH'; # Güçlü şifreleme algoritmaları

    location / {
        proxy_pass http://localhost:3000; # Uygulamamız HTTP üzerinden dinliyor
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```