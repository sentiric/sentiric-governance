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

## 4. Dağıtık İzleme (Distributed Tracing)

Loglama "ne olduğunu", metrikler "ne kadar olduğunu" söylerken, dağıtık izleme **"nerede ve neden yavaş olduğunu"** söyler. Bu, mikroservis mimarimiz için kritik öneme sahiptir.

*   **Standart:** **OpenTelemetry** standardını benimseyeceğiz.
*   **Uygulama:**
    1.  `sentiric-telephony-gateway`, bir çağrı aldığında benzersiz bir **`trace_id`** oluşturur.
    2.  Bu `trace_id`, isteğin geçtiği tüm servisler (`agent-worker`, `api-server`, vb.) ve hatta harici API çağrıları (HTTP header'ları aracılığıyla) boyunca taşınır.
    3.  Her servis, kendi içindeki ana işlemler (span'ler) için (örn: `asr_processing`, `llm_call`) başlangıç ve bitiş zamanlarını bu `trace_id` ile ilişkilendirerek kaydeder.
*   **Toplama ve Görselleştirme:**
    *   Tüm servislerden gelen izleme verileri (traces), **Grafana Tempo** veya **Jaeger** gibi bir arka uca gönderilecektir.
    *   Grafana üzerinden, tek bir `trace_id` ile bir çağrının tüm yaşam döngüsünü, hangi serviste ne kadar zaman harcadığını gösteren bir "şelale grafiği" (waterfall chart) görüntüleyebileceğiz. Bu, performans darboğazlarını tespit etmek için en güçlü aracımız olacaktır.

---
