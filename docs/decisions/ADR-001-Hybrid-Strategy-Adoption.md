# ADR-001: Pragmatik Temel ve Vizyoner Yol Haritası Hibrit Stratejisinin Benimsenmesi

*   **Durum:** Karar Verildi
*   **Tarih:** 2024-07-21
*   **Karar Vericiler:** Proje Sahibi, AI Baş Mimar

## Bağlam

Projenin başlangıç (Faz 0) aşamasında, iki temel mimari ve strateji yaklaşımı ortaya çıkmıştır:

1.  **Pragmatik Temel (v3.0):** RabbitMQ, SQLModel, Docker Compose gibi yaygın, anlaşılır ve hızlı bir şekilde uygulanabilir teknolojilerle, projenin temel ruhunu (gerçek zamanlı AI diyaloğu) yakalayan, modüler ve sağlam bir başlangıç noktası.
2.  **Vizyoner Hedef (v3.2):** mTLS, WebAssembly (Wasm) adaptörleri, Protobuf serileştirmesi gibi kurumsal düzeyde güvenlik, performans ve ölçeklenebilirlik sunan, son teknoloji bir mimari.

Bu iki yaklaşım arasında bir seçim yapmak, projenin ya ilk adımlarında aşırı mühendislikle yavaşlamasına ya da uzun vadeli vizyonundan kopmasına neden olabilirdi.

## Karar

Projenin hem hızlı bir başlangıç yapabilmesi hem de uzun vadeli hedeflerine sadık kalabilmesi için bir **hibrit strateji** benimsenmesine karar verilmiştir:

1.  **Pragmatik Temel (v3.0) Anayasa Olarak Kabul Edilmiştir:** Projenin mevcut ve uygulanabilir mimarisi, `docs/blueprint/Architecture-Overview.md` dosyasında tanımlanan v3.0 versiyonudur. Geliştirme, bu temel üzerine inşa edilecektir.

2.  **Vizyoner Hedef (v3.2) Stratejik Yol Haritası Olarak Belgelenmiştir:** İleri düzey optimizasyonlar, `docs/blueprint/Strategic-Optimizations-Roadmap.md` adında ayrı bir dokümanda, projenin gelecekteki evrim planı olarak kaydedilecektir. Bu, bir "teknik borç" değil, bilinçli bir "teknik yatırım planıdır".

## Sonuçlar ve Etkileri

*   **Pozitif:**
    *   **Hızlı Başlangıç:** Ekip, aşırı karmaşık teknolojilerle boğuşmadan, projenin temel değerini (MVP) oluşturmaya hemen başlayabilir.
    *   **Netlik ve Odak:** Geliştiriciler şu an neyin inşa edileceğini, yöneticiler ve yatırımcılar ise gelecekte nelerin hedeflendiğini net bir şekilde görür.
    *   **Aşırı Mühendislikten Kaçınma:** Teknolojiler, gerçek ihtiyaçlar ortaya çıktıkça ve platform olgunlaştıkça, planlı bir şekilde eklenecektir.
    *   **Vizyonun Korunması:** Uzun vadeli hedefler kaybolmaz, aksine resmi bir yol haritası ile projenin bir parçası haline gelir.

*   **Negatif:**
    *   Bu yaklaşım, iki farklı ama birbiriyle ilişkili doküman setinin bakımını gerektirir. Mimari değiştikçe, hem anayasanın hem de yol haritasının güncel tutulması kritik olacaktır.

---

