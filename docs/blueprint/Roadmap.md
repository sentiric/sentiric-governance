# 🧭 Sentiric: Stratejik Yol Haritası (V3.0 - 23 Repo Desteğiyle)

Bu doküman, Sentiric platformunun geliştirme sürecini fazlara ayırarak, hedefleri ve her fazın çıktılarını net bir şekilde tanımlar.

## Faz 0: Kuruluş (Foundation) - Mevcut Faz

*   **Durum:** ✅ **Tamamlandı**
*   **Hedef:** Projenin kimliğini, vizyonunu, mimarisini ve standartlarını tanımlayan merkezi bir yönetim yapısı oluşturmak ve tüm temel bileşen repolarını fiziksel olarak yerleştirmek.
*   **Çıktı:** `sentiric-governance` reposunun bu versiyonu ve **GitHub organizasyonunda 23 adet ayrı mikroservis/kütüphane reposunun oluşturulması.** Bu, projenin fiziksel mimarisinin somutlaşmasıdır.

---

## Faz 1: Çekirdek Platform Sürümü 1.0 (Core Platform Release)

*   **Durum:** ⬜ **Sıradaki**
*   **Hedef:** Platformun "Tak-Çıkar" iskeletini inşa etmek ve tek bir görev (`GenericReservationTask`) ile uçtan uca, harici servisler kullanarak çalıştığını kanıtlamak. Gecikme (latency) metriklerini ölçmek ve temel mimariyi doğrulamak.
*   **Ana Adımlar:**
    1.  Tüm `sentiric-*` repolarının temel iskeletlerini oluşturmak (✅ Tamamlandı - GitHub repoları oluşturuldu!).
    2.  `sentiric-core-interfaces` içindeki soyut sınıfları tanımlamak.
    3.  `sentiric-connectors` içinde `GoogleGeminiAdapter` ve `TwilioAdapter`'ın ilk versiyonlarını yazmak.
    4.  `sentiric-task-framework` içinde basit bir `GenericReservationTask` oluşturmak.
    5.  `sentiric-agent-worker`'da bu bileşenleri bir araya getiren ana orkestrasyon döngüsünü yazmak.
    6.  **`sentiric-sip-gateway`'i FreeSWITCH ile entegre ederek doğrudan SIP/VoIP çağrılarını işleyebilme yeteneğini kazandırmak.**
    7.  Uçtan uca bir arama senaryosunu başarıyla tamamlamak ve gecikmeyi ölçmek.

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
    *   **`sentiric-sdk-python`** ve **`sentiric-sdk-javascript`** için ilk versiyonlar.

### Faz 3 - Zeka ve Optimizasyon

*   **Durum:** ⬜ **Planlandı**
*   **Hedef:** Platformun AI yeteneklerini derinleştirmek ve operasyonel verimliliği artırmak.
*   **Potansiyel Özellikler:**
    *   **"In-House" Motorların Entegrasyonu:** `sentiric-tts-api` ve `sentiric-stt-api` repolarını devreye alarak maliyetleri düşürme ve kontrolü artırma seçeneği.
    *   **Akıllı Yönlendirme:** Basit görevler için daha küçük/ucuz LLM'leri, karmaşık görevler için büyük LLM'leri kullanan "Model Kademelendirme" (Model Cascading).
    *   **Analitikler:** Dashboard'da arama süreleri, başarılı/başarısız görev oranları gibi metrikleri gösterme.

### Faz 4 - Çoklu Kanal (Omnichannel) Genişlemesi

*   **Durum:** ⬜ **Vizyon**
*   **Hedef:** Sentiric'in diyalog yeteneklerini sesin ötesine taşıyarak, metin tabanlı ve görsel kanalları da destekleyen bütünleşik bir platform haline getirmek.
*   **Potansiyel Özellikler:**
    *   **SMS/Mesajlaşma Entegrasyonu:** `sentiric-messaging-gateway`'i devreye alarak randevu hatırlatmaları, 2FA kodları, anketler, müşteri hizmetleri gibi işlevler için SMS/WhatsApp/Telegram gönderme/alma yeteneği.
    *   **Web Chat / Mobil SDK:** **`sentiric-web-agent-ui`** ve **`sentiric-embeddable-voice-widget`** repolarını kullanarak web sitelerine veya mobil uygulamalara (Flutter, React Native) entegre edilebilecek bir chat/sesli bileşen.
    *   **Video Agent Desteği:** SignalWire'a benzer şekilde, video görüşmelerine katılabilecek ve görsel verileri işleyebilecek AI agent'lar için altyapı hazırlığı.
    
---
*Bu yol haritası, projenin gelişimine ve alınan geri bildirimlere göre güncellenecek "yaşayan" bir belgedir.*

---