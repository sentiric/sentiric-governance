# 📖 Sentiric: Geliştirme Günlüğü

Bu belge, projenin gelişim hikayesini, alınan önemli kararları ve bu kararların arkasındaki "neden"leri kaydeder. Ters kronolojik sıra ile tutulur.


---
### **2024-07-17: Faz 0 - Kuruluş**

*   **Karar:** Projenin adı **"Sentiric"** olarak belirlendi ve `sentiric` GitHub organizasyonu kuruldu.
*   **Gerekçe:** "Sentient" (farkında) ve "Fabric" (doku) kelimelerinden ilhamla, platformun bağlam farkındalığını ve akıcı diyalog örme yeteneğini yansıtan, benzersiz ve akılda kalıcı bir isim seçildi. Önceki önerilerin (`Sonus`, `FluentAI` vb.) GitHub'da alınmış olması, tamamen özgün bir kelime türetme stratejisine yönelmemize neden oldu.
*   **Karar:** Projenin merkezi yönetim reposu olarak `sentiric-governance` oluşturuldu ve projenin anayasası niteliğindeki tüm temel dokümanlar (vizyon, mimari, uçtan uca akış, yol haritası, standartlar, süreçler) bu repoya eklendi.
*   **Gerekçe:** Koda başlamadan önce projenin tüm paydaşları için "tek bir doğruluk kaynağı" oluşturmak, gelecekteki teknik borcu ve stratejik sapmaları en aza indirecektir. Bu, `AzuraForge` ve `VocalForge` projelerinden alınan en önemli derslerden biridir. Uçtan uca akış dokümanının eklenmesi, mimari şemaların somut bir senaryo üzerinden nasıl hayata geçeceğini netleştirmiştir.
*   **Sonuç:** Proje, sağlam bir dokümantasyon temeli ve net bir vizyonla resmi olarak "Kuruluş Fazı"nı tamamlamıştır. Bir sonraki adım, `ROADMAP.md`'de belirtildiği gibi Faz 1'e geçmektir.

---

### **2024-07-18: Faz 0 - Anayasanın Zırhlandırılması**

*   **Karar:** Projenin temel `governance` dokümanları, farklı mühendislik perspektiflerinden (Backend, DevOps, Güvenlik) geçirilen titiz bir inceleme sonucunda detaylandırıldı ve güçlendirildi. `Core-Data-Structures.md` adında yeni bir doküman oluşturuldu ve `API-Design-Guide.md`, `Monitoring-and-Logging.md` gibi kritik belgeler önemli ölçüde güncellendi.
*   **Gerekçe:** Koda başlamadan önce, servisler arası kontratları (`TaskResult`, `CallContext`), operasyonel protokolleri (Distributed Tracing) ve güvenlik mekanizmalarını (JWT Scopes) net bir şekilde tanımlamak, gelecekteki teknik borcu ve entegrasyon sorunlarını en aza indirmek için hayati önem taşımaktadır. Bu, projenin teorik plandan, uygulanabilir bir mühendislik planına geçişini sağlamıştır.
*   **Karar:** Proje Sahibi ve AI Mimar arasındaki işbirliği modeli, "Stratejik Gözden Geçirme ve Eylem Döngüsü" adı altında standartlaştırılarak `AI-Collaboration-Guide.md`'ye eklendi.
*   **Gerekçe:** Projenin kendisi kadar, geliştirme sürecinin de disiplinli, tutarlı ve belgelenmiş olmasını sağlamak.
*   **Sonuç:** `sentiric-governance` reposu, tüm ekip için referans alınabilecek, detaylandırılmış ve sağlam bir temel haline getirilmiştir. Proje, Faz 1'e geçiş için tamamen hazırdır.


*   **Karar:** Projenin temel mimarisi, gelen geri bildirimler doğrultusunda hız, dayanıklılık, güvenlik ve ürünleştirme odağında "zırhlandırıldı". Asenkron iletişim için RabbitMQ, veri modellemesi için SQLModel, diyalog akışı için Durum Makinesi ve bilgi bankası için RAG gibi temel teknolojiler ve desenler standart olarak kabul edildi.
*   **Gerekçe:** Koda başlamadan önce bu temel mühendislik kararlarını netleştirmek ve belgelemek, gelecekteki teknik borcu önleyecek, geliştirme sürecini hızlandıracak ve projenin en başından itibaren ticari bir ürün olma potansiyelini destekleyecektir. Bu, teorik plandan, uygulanabilir ve sağlam bir mühendislik planına geçişin son adımıdır.

---

### **2024-07-20: Faz 0 - Revizyon ve Bütünleştirme**
*   **Karar:** Proje anayasası, Proje Sahibi'nden gelen kritik geri bildirimler doğrultusunda kapsamlı bir revizyondan geçirildi. Önceki "zırhlandırma" çabasında kaybolan değerli detaylar (Lego Mimarisi, detaylı akışlar) yeni mimariyle (RabbitMQ, SQLModel) bütünleştirilerek geri getirildi.
*   **Gerekçe:** AI Mimar'ın ilk zırhlandırma denemesi, teknik optimizasyona odaklanırken projenin temel vizyonunu (gerçek zamanlı AI diyaloğu) ve dokümantasyon bütünlüğünü kısmen gözden kaçırmıştı. Bu revizyon, teknik sağlamlık ile vizyoner netliği tek bir tutarlı belgede birleştirmek için yapıldı. Hatalı `mermaid` şemaları düzeltildi, eksik bölümler eklendi ve MVP tanımı, projenin ruhuna uygun olarak yeniden şekillendirildi.
*   **Karar:** `sentiric-knowledge-indexer`'ın başlangıçtan itibaren ayrı bir repo olarak yönetilmesine karar verildi.
*   **Gerekçe:** RAG (Retrieval-Augmented Generation) mimarisinin projedeki stratejik önemini ve modüler yapıyı en başından itibaren vurgulamak.
*   **Sonuç:** Proje anayasası, tüm paydaşların üzerinde anlaştığı, hem teknik olarak detaylı hem de vizyoner olarak net, sağlam ve bütünleşik bir yapıya kavuşturulmuştur. Proje, vizyonuna sadık bir MVP geliştirmek için hazırdır.
---

---
### **2024-07-23: Faz 1 Adım 1 - MVP'de Lego Mimarisi Uygulaması**

*   **Karar:** `sentiric-mvp-v1` prototipinde, projenin temel `Tak-Çıkar Lego Seti` ve `Varsayılan Olarak Harici, Stratejik Olarak Dahili` mimari felsefelerini somutlaştırmak amacıyla LLM ve TTS bileşenleri için adaptör tabanlı bir yapıya geçilmiştir. Piper TTS adaptörü, Coqui-TTS tabanlı özelleştirilmiş `Sentiric Voice Engine Adapter` olarak yeniden adlandırılarak, projenin kendi "in-house" ses motoru vizyonunun MVP'de somutlaştırılması sağlanmıştır.
*   **Gerekçe:**
    *   **Vizyonun Kanıtı:** Ana mimarideki temel prensiplerin (teknoloji bağımsızlığı, adaptör tabanlılık) en küçük prototip seviyesinde bile uygulanabilir ve çalışır durumda olduğunu göstermek.
    *   **Esneklik:** LLM seçiminin (yerel Ollama veya harici Gemini) `.env` üzerinden dinamik hale getirilmesi, geliştiricilere farklı AI modelleriyle hızlıca deneme yapma imkanı sunar.
    *   **Stratejik Uyum:** Kendi Coqui-TTS çatallanmasının "Sentiric Voice Engine" olarak isimlendirilmesi, `Roadmap.md`'deki Faz 3 hedefleriyle uyumu pekiştirir ve projenin "kendi motorunu entegre etme" yeteneğini şimdiden sergiler.
    *   **Hızlı Geri Bildirim:** Bu tür temel mimari kararların MVP aşamasında denenmesi, ilerideki daha büyük entegrasyonlar için değerli öğrenimler sağlar ve potansiyel sorunları erken aşamada tespit eder.
*   **Sonuç:** `sentiric-mvp-v1` artık `sentiric-governance`'daki mimari vizyonu yansıtan, dinamik olarak yapılandırılabilir LLM ve TTS adaptörlerine sahip, daha "akıllı" bir prototip haline gelmiştir. Bu, projenin sadece teoride değil, pratikte de sağlam temeller üzerinde ilerlediğini kanıtlamıştır.
---