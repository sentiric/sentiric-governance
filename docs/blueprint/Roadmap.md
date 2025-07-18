# 🧭 Sentiric: Stratejik Yol Haritası (V3.0 - 26 Repo Desteğiyle)

Bu doküman, Sentiric platformunun geliştirme sürecini fazlara ayırarak, hedefleri ve her fazın çıktılarını net bir şekilde tanımlar.

## Faz 0: Kuruluş (Foundation) - Mevcut Faz

*   **Durum:** ✅ **Tamamlandı**
*   **Hedef:** Projenin kimliğini, vizyonunu, mimarisini ve standartlarını tanımlayan merkezi bir yönetim yapısı oluşturmak ve tüm temel bileşen repolarını fiziksel olarak yerleştirmek.
*   **Çıktı:** `sentiric-governance` reposunun bu versiyonu ve **GitHub organizasyonunda 26 adet ayrı mikroservis/kütüphane reposunun oluşturulması.** Bu, projenin fiziksel mimarisinin somutlaşmasıdır.

---

## Faz 1: Çekirdek Platform Sürümü 1.0 (Core Platform Release)

*   **Durum:** ⬜ **Sıradaki**
*   **Hedef:** Platformun "Tak-Çıkar" iskeletini inşa etmek, dış dünyadan (telefon hattı) gelen akışı alıp işleyebildiğini kanıtlamak ve tek bir görev (`GenericReservationTask`) ile uçtan uca çalıştığını göstermek. Gecikme (latency) metriklerini ölçmek ve temel mimariyi doğrulamak.
*   **Ana Adımlar:**

    ### A. Temel Altyapı ve Dış Bağlantı (PSTN/SIP Trunk Entegrasyonu)
    *(Amacımız: `212 454 85 90` numaralı hatta gelen çağrıyı `34.122.40.122` sunucumuza düşürmek.)*

    1.  **`sentiric-infrastructure` ile Ortam Hazırlığı:**
        *   `34.122.40.122` IP adresine sahip sunucunuzu (veya Kubernetes cluster'ınızı) `sentiric-infrastructure` repodaki IaC (Infrastructure as Code) tanımları ile yapılandırın.
        *   Operatörünüzden gelecek SIP ve RTP trafiği için gerekli firewall kurallarını (genellikle SIP için UDP 5060, RTP için UDP 10000-20000) tanımlayın ve uygulayın.
        *   **Çıktı:** Sentiric servislerinin deploy edileceği temel altyapı hazır.

    2.  **`sentiric-api-gateway-service`'i Devreye Alma:**
        *   Tüm mikroservisler için tek ve birleşik bir API Gateway ve/veya Backend-for-Frontend (BFF) katmanı olarak `sentiric-api-gateway-service`'i deploy edin. Bu, iç ve dış API trafiğinin güvenli ve yönetilebilir bir şekilde yönlendirilmesini sağlayacaktır.
        *   **Çıktı:** Sentiric servislerine güvenli ve merkezi erişim noktası oluşturuldu.

    3.  **`sentiric-sip-gateway-service` ile Operatör Entegrasyonu:**
        *   Operatörünüzün sağladığı SIP trunk (veya PSTN) bilgilerini kullanarak `sentiric-sip-gateway-service`'i yapılandırın ve deploy edin.
        *   Bu servisi, FreeSWITCH gibi bir SIP proxy/PBX ile entegre ederek dış SIP ağından gelen çağrıları Sentiric'in iç SIP sinyalleşme servisine yönlendirin.
        *   Operatörünüzden `212 454 85 90` numarasını `34.122.40.122` IP adresinize yönlendirmelerini sağlayın.
        *   **Çıktı:** Dışarıdan yapılan telefon çağrıları sunucunuzdaki `sentiric-sip-gateway-service`'e ulaşabiliyor.

    4.  **`sentiric-sip-signaling-service` ve `sentiric-media-service` ile Çekirdek İletişim:**
        *   `sentiric-sip-signaling-service`'i deploy ederek SIP çağrı sinyalleşmesini (kurulum, yönetim, sonlandırma) orkestre etmesini sağlayın.
        *   `sentiric-media-service`'i deploy ederek gerçek zamanlı ses (RTP/SRTP) akışlarını yönetmesini, proxy'lemesini ve medya bazlı etkileşimlere (anons) olanak sağlamasını temin edin.
        *   **Çıktı:** Sentiric iç ağında temel SIP çağrıları kurulabiliyor ve medya akışı yönetilebiliyor.

    5.  **`sentiric-user-service` ve `sentiric-dialplan-service` ile Temel Yönlendirme:**
        *   `sentiric-user-service`'i deploy ederek Sentiric'in dahili SIP kullanıcılarını (örneğin bir test agent'ı veya IVR uç noktası) yönetmesini sağlayın.
        *   `sentiric-dialplan-service`'i deploy edin ve `212 454 85 90` numarasına gelen çağrıları geçici olarak basit bir "test" uygulamasına veya bir "meşgul" sinyaline yönlendiren temel bir kural tanımlayın.
        *   **Çıktı:** Telefon numaranıza gelen çağrılar Sentiric tarafından karşılanabiliyor ve basitçe yönlendirilebiliyor (örn. test anonsu çalabiliyor).

    ### B. Çekirdek İş Akışı ve İlk Görev (GenericReservationTask)
    *(Amacımız: Gelen çağrıyı AI servisleri ile işleyerek belirlenmiş bir görevi tamamlamak.)*

    6.  **`sentiric-core-interfaces` içindeki Soyut Sınıfları ve API Sözleşmelerini Tanımlama:**
        *   Gerekli gRPC protos veya OpenAPI spec'lerini bu repoda tanımlayarak servisler arası iletişimin standartlarını belirleyin.
        *   **Çıktı:** Servisler arası iletişim için ortak sözleşmeler mevcut.

    7.  **`sentiric-agent-service` ile Ana Orkestrasyon Mantığı:**
        *   `sentiric-agent-service`'i deploy edin. Bu servis, diyalog akışlarını yönetecek ve diğer AI servislerini koordine edecek Sentiric'in ana mantık katmanıdır.
        *   **Çıktı:** AI ajan mantığı için temel orkestrasyon servisi hazır.

    8.  **`sentiric-stt-service` (Speech-to-Text) ve `sentiric-tts-service` (Text-to-Speech) Entegrasyonu:**
        *   `sentiric-stt-service`'i deploy ederek sesli girdileri metne çevirme yeteneği kazandırın.
        *   `sentiric-tts-service`'i deploy ederek metin girdilerini doğal insan sesine dönüştürme yeteneği kazandırın.
        *   **Çıktı:** Sesli etkileşimler için temel AI (STT/TTS) servisleri entegre ve çalışır durumda.

    9.  **`sentiric-connectors-service` ile Harici Entegrasyonlar (Google Gemini / Twilio):**
        *   `sentiric-connectors-service`'i deploy edin ve `GoogleGeminiAdapter` ile `TwilioAdapter`'ın ilk versiyonlarını yazarak harici AI (LLM) ve SMS/mesajlaşma servisleriyle entegrasyon yeteneğini sağlayın (eğer `GenericReservationTask` için gerekiyorsa).
        *   **Çıktı:** Harici sistemlerle entegrasyon için temel adaptörler mevcut.

    10. **`sentiric-task-service` (eski `sentiric-task-framework` ve `sentiric-agent-worker` yerine) ile `GenericReservationTask` Oluşturma:**
        *   `sentiric-task-service`'i deploy edin. Bu servis, uzun süreli ve asenkron görevleri yönetecektir.
        *   Bu servis içinde, `sentiric-agent-service`'i kullanarak `GenericReservationTask`'ın ilk versiyonunu yazın. Bu görev, kullanıcıdan randevu bilgisi alıp, bunu onaylayarak basit bir uçtan uca akış sağlar.
        *   **Çıktı:** Platform, gelen bir çağrıyı (sesli) işleyip belirli bir görevi (randevu alma) tamamlayabiliyor.

    ### C. Gözlemleme ve İzleme (Basic Monitoring)

    11. **Uçtan Uca Senaryo Tamamlama ve Gecikme Ölçümü:**
        *   `212 454 85 90` numarasına yapılan bir çağrının, `GenericReservationTask` aracılığıyla başarıyla işlendiğini ve tamamlandığını test edin.
        *   Çağrı kurulumundan görevin tamamlanmasına kadar geçen süreyi (latency) ölçün.
        *   **Çıktı:** Platformun temel işlevselliği doğrulanmış ve performans metrikleri için bir başlangıç noktası belirlenmiş.

    12. **`sentiric-cdr-service` ile Çağrı Detay Kayıtları:**
        *   `sentiric-cdr-service`'i deploy ederek platformdaki tüm çağrı detaylarını ve yaşam döngüsü olaylarını toplamaya başlayın.
        *   **Çıktı:** Temel çağrı kayıtları toplanıyor, bu da sorun giderme ve temel raporlama için ilk adımı oluşturuyor.

---

## Gelecek Fazlar

### Faz 2 - Platformlaşma ve Geliştirici Deneyimi (DX)

*   **Durum:** ⬜ **Planlandı**
*   **Hedef:** Geliştiricilerin kendi "Görev" ve "Kaynak Adaptörlerini" kolayca oluşturup platforma eklemesini sağlamak. `Dashboard` üzerinden self-servis yapılandırma sunmak.
*   **Potansiyel Özellikler:**
    *   **`sentiric-cli`** komut satırı aracı (`create-task`, `add-adapter`).
    *   Detaylı geliştirici dokümantasyonu ve API referansı.
    *   Dashboard'da görev ve **Reçete (Recipe)** yönetim arayüzü.
    *   **İlk Endüstri Dikey Çözümü:** Seçilecek bir endüstri (Sağlık, Emlak vb.) için önceden paketlenmiş "Reçete" ve görev seti geliştirilmesi.
    *   **`sentiric-api-sdk-python`** ve **`sentiric-api-sdk-javascript`** için ilk versiyonlar.
    *   **`sentiric-sip-client-sdk`:** Sentiric SIP Server'a bağlanan, SIP iletişimini (softphone, mobil, WebRTC) sağlayan istemci SDK'sının geliştirilmesi ve yayınlanması.

### Faz 3 - Zeka ve Optimizasyon

*   **Durum:** ⬜ **Planlandı**
*   **Hedef:** Platformun AI yeteneklerini derinleştirmek ve operasyonel verimliliği artırmak.
*   **Potansiyel Özellikler:**
    *   **"In-House" Motorların Entegrasyonu:** `sentiric-tts-service` ve `sentiric-stt-service` repolarını devreye alarak maliyetleri düşürme ve kontrolü artırma seçeneği (eğer başlangıçta dış servisler kullanıldıysa).
    *   **Akıllı Yönlendirme:** Basit görevler için daha küçük/ucuz LLM'leri, karmaşık görevler için büyük LLM'leri kullanan "Model Kademelendirme" (Model Cascading).
    *   **Analitikler:** Dashboard'da arama süreleri, başarılı/başarısız görev oranları gibi metrikleri gösterme.
    *   **`sentiric-knowledge-service`:** AI ajanları için yapılandırılmış bilgi tabanı entegrasyonu.

### Faz 4 - Çoklu Kanal (Omnichannel) Genişlemesi

*   **Durum:** ⬜ **Vizyon**
*   **Hedef:** Sentiric'in diyalog yeteneklerini sesin ötesine taşıyarak, metin tabanlı ve görsel kanalları da destekleyen bütünleşik bir platform haline getirmek.
*   **Potansiyel Özellikler:**
    *   **SMS/Mesajlaşma Entegrasyonu:** `sentiric-messaging-gateway-service`'i devreye alarak randevu hatırlatmaları, 2FA kodları, anketler, müşteri hizmetleri gibi işlevler için SMS/WhatsApp/Telegram gönderme/alma yeteneği.
    *   **Web Chat / Mobil SDK:** **`sentiric-web-agent-ui`** ve **`sentiric-embeddable-voice-widget-sdk`** repolarını kullanarak web sitelerine veya mobil uygulamalara (Flutter, React Native) entegre edilebilecek bir chat/sesli bileşen.
    *   **Video Agent Desteği:** SignalWire'a benzer şekilde, video görüşmelerine katılabilecek ve görsel verileri işleyebilecek AI agent'lar için altyapı hazırlığı.
    *   **`sentiric-marketplace-service`:** Üçüncü parti geliştiricilerin kendi görev ve adaptörlerini Sentiric kullanıcılarına sunabileceği gelecekteki pazar yeri platformunun geliştirilmesi ve devreye alınması.
    
---
*Bu yol haritası, projenin gelişimine ve alınan geri bildirimlere göre güncellenecek "yaşayan" bir belgedir.*

---

**Önemli Değişiklikler ve Nedenleri:**

*   **Repo Sayısı Güncellendi:** Faz 0'daki repo sayısı 23'ten 26'ya güncellendi.
*   **Faz 1 Detaylandırıldı:**
    *   "Temel Altyapı ve Dış Bağlantı" (A) bölümü eklendi. Bu, operatörden gelen telefon hattını gerçekten platforma bağlama konusundaki ilk ve en önemli adımları içeriyor. `sentiric-infrastructure`, `sentiric-sip-gateway-service`, `sentiric-sip-signaling-service`, `sentiric-media-service`, `sentiric-user-service`, `sentiric-dialplan-service` gibi temel servislerin deployment ve konfigürasyonunu kapsar.
    *   Mevcut Faz 1'deki "6. `sentiric-sip-gateway`'i FreeSWITCH ile entegre ederek doğrudan SIP/VoIP çağrılarını işleyebilme yeteneğini kazandırmak" adımı, yeni "A.2" adımına dahil edildi ve daha genel bir ifadeyle ele alındı.
    *   "Çekirdek İş Akışı ve İlk Görev" (B) bölümü, AI servislerini (STT/TTS) ve ilk görevi (`GenericReservationTask`) devreye alma adımlarını daha net bir sıraya koydu.
    *   `sentiric-task-framework` ve `sentiric-agent-worker` yerine daha güncel ve mantıklı olan `sentiric-task-service` kullanıldı (bu, benim ilk verdiğim repo listesindeki yeni isme uygun).
    *   Yeni bir "C. Gözlemleme ve İzleme" bölümü eklenerek `sentiric-cdr-service`'in Faz 1'de devreye alınması gerektiği vurgulandı.
*   **Gelecek Fazlar Temizlendi/Uyumlu Hale Getirildi:** Faz 3'teki "In-House Motorların Entegrasyonu" kısmına parantez içinde "eğer başlangıçta dış servisler kullanıldıysa" notu eklendi, bu da esnekliği vurguluyor. `sentiric-knowledge-service` de Faz 3'e taşındı, çünkü bu zeka ve optimizasyonla daha ilgili. SDK isimleri güncellendi (`sentiric-sdk-python` -> `sentiric-api-sdk-python` vb.).

Bu güncellenmiş yol haritası, "nereden başlayacağınız" sorusuna çok daha somut bir yanıt veriyor ve Sentiric'in modüler yapısını en iyi şekilde kullanmanızı sağlıyor. İlk odak noktanız artık net: **Faz 1'in "A" bölümündeki adımları tamamlamak.**