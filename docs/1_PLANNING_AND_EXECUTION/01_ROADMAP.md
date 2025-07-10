# 🧭 Sentiric: Stratejik Yol Haritası

Bu doküman, Sentiric platformunun geliştirme sürecini fazlara ayırarak, hedefleri ve her fazın çıktılarını net bir şekilde tanımlar.

## Faz 0: Kuruluş (Foundation) - Mevcut Faz

*   **Durum:** ✅ **Tamamlandı**
*   **Hedef:** Projenin kimliğini, vizyonunu, mimarisini ve standartlarını tanımlayan merkezi bir yönetim yapısı oluşturmak.
*   **Çıktı:** `sentiric-governance` reposunun bu versiyonu.

---

## Faz 1: Çekirdek Platform Sürümü 1.0 (Core Platform Release)

*   **Durum:** ⬜ **Sıradaki**
*   **Hedef:** Platformun "Tak-Çıkar" iskeletini inşa etmek ve tek bir görev (`GenericReservationTask`) ile uçtan uca, harici servisler kullanarak çalıştığını kanıtlamak. Gecikme (latency) metriklerini ölçmek ve temel mimariyi doğrulamak.
*   **Ana Adımlar:**
    1.  Tüm `sentiric-*` repolarının temel iskeletlerini oluşturmak.
    2.  `sentiric-core-interfaces` içindeki soyut sınıfları tanımlamak.
    3.  `sentiric-connectors` içinde `GoogleGeminiAdapter` ve `TwilioAdapter`'ın ilk versiyonlarını yazmak.
    4.  `sentiric-task-framework` içinde basit bir `GenericReservationTask` oluşturmak.
    5.  `sentiric-agent-worker`'da bu bileşenleri bir araya getiren ana orkestrasyon döngüsünü yazmak.
    6.  Uçtan uca bir arama senaryosunu başarıyla tamamlamak ve gecikmeyi ölçmek.

---

## Gelecek Fazlar

### Faz 2 - Platformlaşma ve Geliştirici Deneyimi (DX)

*   **Durum:** ⬜ **Planlandı**
*   **Hedef:** Geliştiricilerin kendi "Görev" ve "Kaynak Adaptörlerini" kolayca oluşturup platforma eklemesini sağlamak. `Dashboard` üzerinden self-servis yapılandırma sunmak.
*   **Potansiyel Özellikler:**
    *   `sentiric-cli` komut satırı aracı (`create-task`, `add-adapter`).
    *   Detaylı geliştirici dokümantasyonu ve API referansı.
    *   Dashboard'da görev ve reçete (recipe) yönetim arayüzü.

### Faz 3 - Zeka ve Optimizasyon

*   **Durum:** ⬜ **Planlandı**
*   **Hedef:** Platformun AI yeteneklerini derinleştirmek ve operasyonel verimliliği artırmak.
*   **Potansiyel Özellikler:**
    *   **"In-House" Motorların Entegrasyonu:** `sentiric-voice-engine`'i devreye alarak maliyetleri düşürme ve kontrolü artırma seçeneği.
    *   **Akıllı Yönlendirme:** Basit görevler için daha küçük/ucuz LLM'leri, karmaşık görevler için büyük LLM'leri kullanan "Model Kademelendirme" (Model Cascading).
    *   **Analitikler:** Dashboard'da arama süreleri, başarılı/başarısız görev oranları gibi metrikleri gösterme.

---
*Bu yol haritası, projenin gelişimine ve alınan geri bildirimlere göre güncellenecek "yaşayan" bir belgedir.*

---
