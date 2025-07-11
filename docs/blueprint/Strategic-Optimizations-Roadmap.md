# 🗺️ Sentiric: Stratejik Optimizasyon Yol Haritası (v3.2 Vizyonu)

Bu doküman, Sentiric platformunun mevcut sağlam temelinin (v3.0) üzerine inşa edilecek olan, gelecekteki yüksek performans, güvenlik ve verimlilik hedeflerini tanımlar. Bu, projemizin "Yıldız Haritası"dır ve teknolojik evrimimizi planlar.

Bu yol haritası, mevcut mimarinin bir alternatifi değil, onun **doğal bir sonraki adımıdır.** Her bir madde, platform olgunlaştıkça ve kurumsal gereksinimler arttıkça devreye alınacak modüler iyileştirmelerdir.

## 1. Güvenlik Katmanı Evrimi: Sıfır Güvenden Öteye

-   **Hedef:** Finans ve sağlık gibi regüle sektörlerin en katı gereksinimlerini karşılamak.
-   **Mevcut Durum (v3.0):** API Gateway arkasında JWT tabanlı yetkilendirme.
-   **Sonraki Adım (v3.2 Vizyonu):**
    -   **Dahili İletişimde mTLS:** Tüm servisler arası (Gateway, Worker, API vb.) iletişimin, karşılıklı olarak doğrulanmış sertifikalarla şifrelenmesi.
    -   **Gelişmiş Yetkilendirme:** JWT'lere ek olarak, her bir API çağrısının hassasiyetine göre daha granüler `scopes` ve `claims` ile yetkilendirme.

## 2. Performans ve Verimlilik Evrimi: Milisaniyelerin Önemi

-   **Hedef:** Çağrı başına maliyeti düşürmek, gecikmeyi (latency) minimize etmek ve ölçeklenebilirliği maksimize etmek.
-   **Mevcut Durum (v3.0):** Redis'te JSON olarak durum yönetimi.
-   **Sonraki Adım (v3.2 Vizyonu):**
    -   **Protobuf ile Serileştirme:** Redis'te tutulan `CallContext` gibi durum nesnelerinin, JSON yerine **Protocol Buffers (Protobuf)** ile serileştirilmesi.
    -   **Akıllı TTL Yönetimi:** Redis'teki her çağrı durumuna akıllı bir **TTL (Time-To-Live)** mekanizması eklenmesi.
    -   **Durum Checkpoint'leri:** Çok uzun süren diyaloglarda, çağrı durumunun periyodik olarak PostgreSQL'e kaydedilmesi.

## 3. Adaptör Yönetimi Evrimi: Güvenli ve Evrensel Genişletilebilirlik

-   **Hedef:** Üçüncü parti geliştiricilerin bile platforma güvenli ve yüksek performanslı adaptörler eklemesini sağlamak.
-   **Mevcut Durum (v3.0):** Python tabanlı adaptörlerin dinamik olarak yüklenmesi.
-   **Sonraki Adım (v3.2 Vizyonu):**
    -   **WebAssembly (Wasm) Runtime:** Tüm adaptörlerin, ana `AgentWorker` sürecinden tamamen izole edilmiş bir **WebAssembly sandbox** (`Wasmtime`) içinde çalıştırılması.
    -   **Faydaları:** Güvenlik, performans ve dil bağımsızlığı.

## 4. Gözlemlenebilirlik (Observability) Evrimi: Reaktiften Proaktife

-   **Hedef:** Sorunları ortaya çıkmadan önce tahmin etmek ve sistemin her bir parçasının performansını derinlemesine anlamak.
-   **Mevcut Durum (v3.0):** Yapılandırılmış loglama ve Prometheus/Grafana ile temel metrikler.
-   **Sonraki Adım (v3.2 Vizyonu):**
    -   **Dağıtık İzleme (Distributed Tracing):** **OpenTelemetry** standardının tüm servislere entegre edilmesi.
    -   **Akıllı Örnekleme (Sampling):** Üretim ortamında izleme verilerinin sadece belirli bir yüzdesinin örneklenmesi.

### Uygulama Fazları (Tahmini)

```mermaid
gantt
    title Stratejik Optimizasyon Uygulama Zaman Çizelgesi
    dateFormat  YYYY-Q
    axisFormat %Y-Q%
    
    section Gözlemlenebilirlik ve Güvenlik
    OpenTelemetry Entegrasyonu :crit, done, 2024-Q4, 1q
    mTLS Altyapısı          :crit, active, 2025-Q1, 1q

    section Performans
    Protobuf ve Redis Optimizasyonu :after mTLS Altyapısı, 2q

    section Adaptör Mimarisi
    Wasm Runtime PoC         :2025-Q2, 1q
    Adaptörlerin Wasm'a Port Edilmesi :after Wasm Runtime PoC, 3q
```
