# 📡 Sentiric: API Tasarım Rehberi

Bu rehber, Sentiric ekosistemi içindeki ve dış dünyaya açılan tüm API'lerin tasarımında tutarlılığı ve en iyi pratikleri sağlamak için oluşturulmuştur.

## 1. RESTful API Prensipleri (`sentiric-api-server`)

*   **Kaynak Odaklı URL'ler:** URL'ler, eylemleri değil, kaynakları temsil etmelidir.
    *   **İyi:** `/bookings`, `/bookings/123`, `/users/456/bookings`
    *   **Kötü:** `/getAllBookings`, `/createBooking`
*   **Doğru HTTP Metotları:**
    *   `GET`: Kaynakları okumak için (güvenli, idempotant).
    *   `POST`: Yeni bir kaynak oluşturmak için (idempotant değil).
    *   `PUT`: Bir kaynağı tamamen güncellemek için (idempotant).
    *   `PATCH`: Bir kaynağı kısmen güncellemek için (idempotant).
    *   `DELETE`: Bir kaynağı silmek için (idempotant).
*   **Sürümleme:** API, URL üzerinden sürümlenecektir. (örn: `/api/v1/...`).
*   **JSON Standardı:** Tüm istek ve yanıt gövdeleri (body) `application/json` formatında olmalıdır. Değişken isimleri `snake_case` kullanılacaktır.
*   **Standart Yanıt Yapısı:**
    *   **Başarılı (`2xx`):**
      ```json
      {
        "data": { ... } // veya [ ... ]
      }
      ```
    *   **Hatalı (`4xx`, `5xx`):**
      ```json
      {
        "error": {
          "code": "RESOURCE_NOT_FOUND",
          "message": "Booking with ID 123 not found.",
          "details": { ... } // Opsiyonel
        }
      }
      ```

## 2. WebSocket API Prensipleri (`sentiric-telephony-gateway`)

*   **Mesaj Formatı:** Tüm WebSocket mesajları JSON formatında olacaktır. Her mesaj, bir `event` türü ve bir `payload` içerecektir.
    ```json
    {
      "event": "media_stream_started",
      "payload": { "call_sid": "CA123..." }
    }
    ```
*   **Yön:** Gateway'e gönderilen ses verisi (client -> server) ve Gateway'den gönderilen ses verisi (server -> client) için olaylar net bir şekilde ayrılacaktır.
    *   **Client -> Server:** `{"event": "media", "payload": { "chunk": "base64-encoded-audio" }}`
    *   **Server -> Client:** `{"event": "media", "payload": { "chunk": "base64-encoded-audio" }}`

## 3. Olay (Event) Veri Yapısı (Dahili)

Platform içindeki `EventBus` üzerinden geçen tüm olayların payload'ları tutarlı bir yapıya sahip olmalıdır.

*   Her payload, olayın ne zaman ve nerede oluştuğunu belirten meta veriler içermelidir.
*   Mümkün olduğunca basit ve düz bir yapıda olmalıdır.

```json
{
  "timestamp_iso": "2024-07-16T10:30:00Z",
  "source_service": "sentiric-agent-worker",
  "call_sid": "CA123...",
  // ... olaya özel diğer veriler
  "task_result": { ... }
}
```

## 4. Standart Hata Yanıt Yapısı (Geliştirilmiş)

Tüm `4xx` ve `5xx` hataları, istemcinin hatayı programatik olarak işlemesini sağlayacak tutarlı bir yapı döndürmelidir.

```json
{
  "error": {
    "type": "VALIDATION_ERROR", // Genel hata kategorisi (örn: AUTHENTICATION_ERROR, NOT_FOUND)
    "code": "INVALID_PHONE_NUMBER", // Daha spesifik, makine tarafından okunabilir kod
    "message": "Provided phone number is not valid.", // İnsan tarafından okunabilir açıklama
    "details": [ // Opsiyonel, özellikle validasyon hataları için
      {
        "field": "phoneNumber",
        "issue": "Must be a 10-digit number."
      }
    ],
    "trace_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef" // Hatanın takibi için Trace ID
  }
}
---

## 5. Dahili TTS API Kontratı (SSML Desteği)

`agent-worker` ile `sentiric-tts-api` (veya harici TTS adaptörleri) arasındaki iletişim, doğal diyalog akışını sağlamak için **SSML**'i önceliklendirmelidir.

*   **İstek Formatı:** İstek, düz metin yerine SSML içeren bir JSON nesnesi olmalıdır.
*   **Örnek Payload (`agent-worker` -> TTS Servisi):**
    ```json
    {
      "format": "ssml",
      "text": "<speak>Randevunuz başarıyla oluşturuldu.<break time='500ms'/> Size başka bir konuda yardımcı olabilir miyim?</speak>",
      "language": "tr-TR",
      "speed": 1.0
    }
    ```
*   **Gerekçe:** Bu yapı, TTS motoruna sadece ne söyleyeceğini değil, nasıl söyleyeceğini de (duraklamalar, tonlama vb.) ileterek, çok daha insan benzeri ve kaliteli bir sesli yanıt üretilmesini sağlar.
