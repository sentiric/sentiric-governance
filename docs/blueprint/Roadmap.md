# 🧭 Sentiric: Stratejik Yol Haritası (v9.0 "Genesis" Uyumlu)

Bu doküman, Sentiric platformunun geliştirme sürecini fazlara ayırarak, hedefleri ve her fazın çıktılarını net bir şekilde tanımlar. Bu, "Genesis Mimarisi" vizyonumuzu eyleme döken plandır.

---

## Faz 1: "Genesis Çekirdeği" - Dayanıklı MVP (Mevcut Odak)

*   **Durum:** ⬜ **Sıradaki**
*   **Hedef:** Platformun "Genesis Mimarisi"ni hayata geçirmek. Dış dünyadan gelen her türlü çağrıyı (kayıtlı, misafir, hatalı) anlayan, kararlı bir şekilde karşılayan ve temel bir sesli yanıt veren çekirdek sistemi oluşturmak.
*   **Ana Adımlar:**
    1.  **Veritabanı İnşası:** Kendi kendini başlatan (self-bootstrapping) `init.sql` ile veritabanı şemasını kurmak.
    2.  **Karar Merkezi'nin Geliştirilmesi:** `dialplan-service`'i, gelen aramalara göre dinamik olarak karar veren (misafir, kayıtlı, bakım modu) bir beyin haline getirmek.
    3.  **Çekirdek Servislerin Adaptasyonu:** `sip-signaling`, `agent-service` ve `user-service`'i yeni "Tek Sorumluluk" rollerine göre yeniden yapılandırmak.
    4.  **Güvenli Medya Akışı (SRTP):** `media-service`'e, ses akışlarını şifrelemek için SRTP desteğinin temellerini eklemek.
    5.  **Performans Odaklı AI Akışı (Streaming):** `agent-service`'in AI motorlarıyla olan iletişimini, gelecekteki "streaming" API'leri destekleyecek şekilde tasarlamak.

---

## Faz 2 - Platformlaşma ve Geliştirici Deneyimi (DX)

*   **Durum:** ⬜ **Planlandı**
*   **Hedef:** Geliştiricilerin kendi "Görev" ve "Kaynak Adaptörlerini" kolayca oluşturup platforma eklemesini sağlamak. `Dashboard` üzerinden "low-code" (az kodlu) yapılandırma sunmak.
*   **Potansiyel Özellikler:**
    *   **Low-Code IVR Tasarımcısı:** Yöneticilerin `dashboard-ui` üzerinden sürükle-bırak ile kendi arama akışlarını (dialplan) tasarlayabilmesi.
    *   **Geliştirici Sandbox:** `sentiric-cli`'ye, geliştiricilerin yazdıkları yeni "Task"ları platformun geri kalanını kurmadan, yerel olarak test edebilecekleri bir simülasyon ortamı eklenmesi.
    *   **Pazar Yeri (Marketplace) v1.0:** `sentiric-marketplace-service`'in ilk versiyonu ile, topluluk tarafından geliştirilen "Task" ve "Connector" paketlerinin listelenmesi.

---

## Faz 3 - Zeka, Optimizasyon ve Veri Bütünlüğü

*   **Durum:** ⬜ **Planlandı**
*   **Hedef:** Platformun AI yeteneklerini derinleştirmek, operasyonel verimliliği artırmak ve dağıtık sistemlerde veri bütünlüğünü garanti altına almak.
*   **Potansiyel Özellikler:**
    *   **Akıllı Yönlendirme:** Basit görevler için daha küçük/ucuz LLM'leri, karmaşık görevler için büyük LLM'leri kullanan "Model Kademelendirme" (Model Cascading).
    *   **Gelişmiş RAG:** `knowledge-service`'e, hibrit arama (keyword + vector) ve daha hafif embedding modelleri (örn: bge-small) entegrasyonu.
    *   **Dağıtık Transaction Yönetimi (SAGA Pattern):** Birden fazla servise yayılan işlemlerin (örn: ödeme al, CRM'e kaydet, takvime ekle) atomik olarak, veri tutarlılığı bozulmadan yapılmasını sağlamak.

---

## Faz 4 - Çoklu Kanal (Omnichannel) ve Küresel Ölçeklenme

*   **Durum:** ⬜ **Vizyon**
*   **Hedef:** Sentiric'in diyalog yeteneklerini sesin ötesine taşıyarak, metin tabanlı ve görsel kanalları da destekleyen bütünleşik bir platform haline getirmek.
*   **Potansiyel Özellikler:**
    *   **Mesajlaşma Entegrasyonu:** `sentiric-messaging-gateway-service`'i devreye alarak WhatsApp/Telegram gibi kanallardan gelen talepleri işleme.
    *   **Web & Mobil SDK:** `sentiric-embeddable-voice-widget-sdk` ve `sentiric-sip-client-sdk` ile web sitelerine ve mobil uygulamalara sesli/görüntülü iletişim yetenekleri ekleme.
    *   **Edge Computing:** Medya işlemlerini (transcoding, STT ön işleme) kullanıcılara daha yakın sunucularda (edge) WebAssembly (WASM) ile yaparak gecikmeyi daha da azaltmak.