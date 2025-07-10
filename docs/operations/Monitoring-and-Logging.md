# 📊 Sentiric: İzleme ve Loglama Stratejisi

Bu doküman, platformun sağlığını, performansını ve davranışını anlamak için kullanılacak izleme (monitoring), loglama (logging) ve uyarı (alerting) mekanizmalarını tanımlar. Felsefemiz: **"Ölçemediğin şeyi iyileştiremezsin."**

## 1. Loglama

*   **Yapı (Structure):** Tüm loglar, makine tarafından kolayca ayrıştırılabilir olması için **JSON formatında** üretilecektir.
*   **İçerik:** Her log kaydı, minimumda şu bilgileri içerecektir: `timestamp`, `log_level`, `service_name`, `call_sid` (ilgiliyse), `trace_id` (ilgiliyse), `message` ve olaya özel diğer meta veriler.
*   **Toplama:** Tüm konteyner logları, `Loki` gibi merkezi bir log toplama sistemine `Promtail` aracılığıyla gönderilecektir.

## 2. Metrikler (Metrics)

*   **Tür:** Sistem, **Prometheus** formatında metrikler üretecektir.
*   **Toplanacak Ana Metrikler:**
    *   **İşletme Metrikleri (Business Metrics):**
        *   `calls_total`: Toplam arama sayısı.
        *   `tasks_executed_total{task="reservation", status="success"}`: Görev bazında başarı/hata sayıları.
        *   `average_call_duration_seconds`: Ortalama arama süresi.
    *   **Performans Metrikleri (Latency Metrics):**
        *   `asr_processing_duration_ms`: ASR işleminin süresi.
        *   `llm_ttft_duration_ms`: LLM'in ilk token'ı üretme süresi.
        *   `tts_processing_duration_ms`: TTS işleminin süresi.
        *   `end_to_end_turn_duration_ms`: Kullanıcı konuşması bittikten sonra sistemin cevap vermeye başladığı ana kadar geçen toplam süre.
    *   **Sistem Metrikleri (System Metrics):**
        *   CPU ve Bellek Kullanımı (servis bazında).
        *   API istek sayısı ve `4xx`/`5xx` hata oranları.

## 3. Görselleştirme ve Uyarı (Visualization & Alerting)

*   **Araç:** **Grafana** kullanılacaktır.
*   **Dashboard'lar:**
    *   **Genel Sistem Sağlığı:** Tüm servislerin durumunu, CPU/bellek kullanımını ve API hata oranlarını gösteren dashboard.
    *   **Performans Analizi:** Gecikme metriklerini (ASR, LLM, TTS) detaylı olarak gösteren, darboğazları tespit etmeyi sağlayan dashboard.
    *   **İş Akışı Analizi:** Hangi görevlerin ne kadar kullanıldığını, başarı oranlarını ve ortalama arama sürelerini gösteren dashboard.
*   **Uyarılar (Alerting):**
    *   `end_to_end_turn_duration_ms` metriği belirlenen bir eşiği (örn: 1000ms) aştığında.
    *   `tasks_executed_total` metriğindeki `status="failure"` oranı %5'i geçtiğinde.
    *   Herhangi bir servisin CPU kullanımı %90'ı geçtiğinde.

Bu yapı, proaktif bir şekilde sorunları tespit etmemizi ve platformun performansını sürekli olarak iyileştirmemizi sağlayacaktır.

---