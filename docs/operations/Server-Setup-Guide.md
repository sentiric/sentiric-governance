# 🚀 Sentiric Platformu: Sunucu Kurulum Rehberi (Sıfırdan Canlıya)

Bu rehber, Ubuntu 22.04+ veya Debian 12+ tabanlı temiz bir sanal sunucuyu, Sentiric platformunu çalıştırmaya hazır hale getirmek için gereken tüm adımları içerir. Bu adımlar, `e2-micro` gibi düşük kaynaklı ortamlarda karşılaşılan sorunları çözmek üzere optimize edilmiştir.

## Adım 1: Temel Sistem ve Güvenlik Duvarı

1.  **Sanal Sunucu Oluşturma:** Google Cloud, AWS, Azure veya DigitalOcean gibi bir sağlayıcıdan en az 2 vCPU ve 2 GB RAM'e sahip bir sanal makine oluşturun. (Not: `e2-micro` gibi daha düşük kaynaklı makineler test edilmiş ancak kararsız bulunmuştur. Önerilen minimum `e2-small` veya eşdeğeridir).
2.  **Statik IP Atama:** Sunucunuza kalıcı bir genel IP adresi atayın.
3.  **Güvenlik Duvarı (Firewall) Kuralları:** Gelen (Ingress) trafik için aşağıdaki portlara izin verin:
    *   **TCP:** `22` (SSH), `80` (HTTP), `443` (HTTPS), `5432` (PostgreSQL), `15672` (RabbitMQ UI), `50052-50054` (gRPC)
    *   **UDP:** `5060` (SIP), `10000-10300` (RTP - başlangıç için 301 port)

## Adım 2: Docker ve Gerekli Araçların Kurulumu (Resmi Yöntem)

Bu adımlar, sisteminize Docker'ın en güncel ve uyumlu sürümünü kurar.

```bash
# 1. Sistemin paket listesini güncelle
sudo apt-get update

# 2. Gerekli yardımcı programları kur
sudo apt-get install -y ca-certificates curl git

# 3. Docker'ın resmi GPG anahtarını ve deposunu ekle
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 4. Apt paket listesini yeni depoyla tekrar güncelle
sudo apt-get update

# 5. Docker motorunu, CLI'ı ve en önemlisi Compose eklentisini kur
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 6. Mevcut kullanıcıyı 'docker' grubuna ekle (logout/login gerekebilir)
sudo usermod -aG docker ${USER}
```

## Adım 3: Performans İçin Swap Alanı Oluşturma

Düşük RAM'li sunucularda bu adım kritik öneme sahiptir.
```bash
# 4GB'lık bir swap dosyası oluştur
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Swap alanını kalıcı hale getir
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

## Adım 4: Platform Kodunu Alma ve Dağıtma

1.  **`sentiric-infrastructure` Reposunu Klonla:**
    ```bash
    git clone https://github.com/sentiric/sentiric-infrastructure.git
    cd sentiric-infrastructure
    ```
2.  **Ortam Değişkenlerini Yapılandır:**
    ```bash
    cp .env.local.example .env
    nano .env
    # Dosya içindeki PUBLIC_IP'yi sunucunuzun IP'si ile değiştirin.
    # EXTERNAL_RTP_PORT_MAX değerini 10300 olarak ayarlayın (301 port).
    ```
3.  **Otomatik Dağıtım Script'ini Çalıştır:**
    ```bash
    # Script'i çalıştırılabilir yap
    chmod +x deploy.sh
    
    # Platformu başlat
    sudo ./deploy.sh
    ```
    Bu script, tüm altyapıyı sizin için kontrollü ve doğru bir şekilde ayağa kaldıracaktır.

Artık Sentiric platformunuz çalışmaya hazır!
