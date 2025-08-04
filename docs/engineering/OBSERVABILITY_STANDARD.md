# 👁️ Sentiric Gözlemlenebilirlik Standardı (Observability Standard)

**Belge Durumu:** AKTİF VE BAĞLAYICI
**Sorumlu Görev:** `OBS-01`

Bu doküman, Sentiric ekosistemindeki tüm servislerin, platformun sağlığını, performansını ve davranışını anlamak için uyması gereken **zorunlu** loglama, metrik ve izleme standartlarını tanımlar.

## Felsefe: Gözlemlenebilirliğin Üç Sacayağı

Stratejimiz, modern dağıtık sistemlerde endüstri standardı haline gelmiş olan "Üç Sacayağı" modeline dayanır:

1.  **Yapılandırılmış Loglama (Structured Logging):** *"Ne oldu?"* sorusuna ayrıntılı cevap verir.
2.  **Metrikler (Metrics):** *"(Ne sıklıkta / Ne kadar) oldu?"* sorusuna sayısal cevap verir.
3.  **Dağıtık İzleme (Distributed Tracing):** *"(Nerede / Neden yavaş) oldu?"* sorusuna yolculuk analiziyle cevap verir.

Bu üç unsur, birbirinden ayrı değil, birbirini tamamlayan bir bütündür. `trace_id` gibi ortak tanımlayıcılar aracılığıyla loglardan metrik dashboards'larına, oradan da spesifik bir isteğin detaylı izine sorunsuzca geçiş yapabilmeliyiz.

---

### **Sacayağı 1: Yapılandırılmış ve Ortama Duyarlı Loglama**

Tüm servisler, loglarını bulundukları ortama göre uyarlamalıdır.

*   **Geliştirme Ortamı (`ENV=development`):** Loglar, geliştiricinin kolayca okuyabilmesi için **renkli, insan odaklı konsol formatında** olmalıdır.
*   **Üretim Ortamı (`ENV=production`):** Loglar, merkezi sistemler tarafından işlenebilmesi için **JSON formatında** olmalıdır.

#### **Standart Log Alanları**

Her log mesajı, hangi dilde veya serviste olursa olsun, **zorunlu olarak** aşağıdaki alanları içermelidir:

| Alan Adı     | Açıklama                                                                | Örnek Değer                  |
|--------------|-------------------------------------------------------------------------|------------------------------|
| `timestamp`  | Olayın gerçekleştiği zaman (UTC, ISO 8601 / RFC3339).                     | `2025-08-05T10:20:30.123Z`   |
| `level`      | Log seviyesi (`debug`, `info`, `warn`, `error`).                        | `error`                      |
| `service`    | Logu üreten servisin adı.                                               | `agent-service`              |
| `message`    | İnsan tarafından okunabilir log mesajı.                                 | `Kullanıcı doğrulanamadı.`   |
| `trace_id`   | İsteğin tüm yolculuğunu takip eden benzersiz ID. (Varsa)                 | `abc-123-def-456`            |
| `call_id`    | İlgili SIP çağrısının benzersiz ID'si. (Varsa)                          | `asdf123@1.2.3.4`            |

#### **Teknoloji ve Kütüphane Standartları**

*   **Go Servisleri:** `rs/zerolog`
*   **Rust Servisleri:** `tracing` ve `tracing-subscriber` (`json` formatlayıcı ile)
*   **Python Servisleri:** `structlog`

---

### **Sacayağı 2: Metrikler ile Sistem Sağlığı**

*   **Standart:** Tüm servisler, **Prometheus** formatında bir `/metrics` HTTP endpoint'i sunmalıdır.
*   **Toplama:** `sentiric-infrastructure`, Prometheus ve Grafana servislerini içerecektir.
*   **Temel Metrikler:**
    *   **RED Metrikleri (Rate, Errors, Duration):** Tüm gRPC/HTTP endpoint'leri için istek sayısı, hata oranı ve gecikme süresi histogramları.
    *   **İş Mantığı Metrikleri:** `sentiric_calls_started_total`, `sentiric_tasks_completed_total{task="<task_name>", status="<success/failure>"}`.
    *   **Sistem Metrikleri:** Go runtime metrikleri, CPU/Bellek kullanımı.

---

### **Sacayağı 3: Dağıtık İzleme (Distributed Tracing)**

*   **Standart:** **OpenTelemetry** standardı benimsenecektir.
*   **Uygulama:**
    1.  Ağ geçitleri (`sip-gateway`, `api-gateway`) platforma giren her istek için bir **`trace_id`** oluşturur.
    2.  Bu `trace_id`, sonraki tüm gRPC (metadata ile) ve HTTP (header ile) çağrılarına eklenerek **bağlam yayılımı (context propagation)** sağlanır.
    3.  Her servis, kendi içindeki önemli işlemleri ("DB sorgusu", "LLM çağrısı" vb.) birer **"span"** olarak işaretler.
*   **Toplama:** `sentiric-infrastructure`, **Jaeger** veya **Grafana Tempo** gibi bir tracing backend'i içerecektir.