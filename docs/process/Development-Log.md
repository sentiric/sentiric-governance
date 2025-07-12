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
### **2024-07-23: Faz 1 Adım 1 - MVP Diyalog Akışı ve Anlama İyileştirmeleri**

*   **Karar:** `sentiric-mvp-v1` prototipinin diyalog akışı ve kullanıcı girdilerini anlama yeteneği, LLM prompt'larının sıkılaştırılması, parametre doğrulama mekanizmalarının eklenmesi ve anlayamama durumlarının kullanıcı dostu bir şekilde yönetilmesiyle önemli ölçüde iyileştirilmiştir.
*   **Gerekçe:**
    *   **Kullanıcı Deneyimi:** LLM'in anlamsız değerler döndürmesi ve diyalogda takılı kalma sorunları giderilerek, kullanıcıların sistemle daha doğal ve akıcı bir şekilde etkileşime girmesi sağlanmıştır. "Anlayamadım" geri bildirimi ve tekrar deneme hakkı, platformun dayanıklılığını artırmıştır.
    *   **LLM Kontrolü:** LLM'den beklenen JSON formatının ve içeriksel değerin (örn. `null` döndürme talimatı, sayısal değerler) daha katı bir şekilde talep edilmesi, modellerin güvenilirliğini artırmıştır.
    *   **Veri Bütünlüğü:** Çıkarılan parametrelerin basit kurallarla (örn. konum için kelime sayısı, sayısal alanlar için sayısal doğrulama) doğrulanması, veritabanına yanlış veya anlamsız verilerin kaydedilmesini engellemiştir.
    *   **Hata Dayanıklılığı:** Kod tabanındaki `TypeError` gibi kritik hatalar giderilerek sistemin kararlılığı sağlanmış, genel hata yakalama mekanizması iyileştirilmiştir.
*   **Sonuç:** `sentiric-mvp-v1` artık "otel rezervasyonu" görevini çok daha güvenilir, hatasız ve kullanıcı dostu bir şekilde tamamlayabilen, pratik bir konuşma AI'sı haline gelmiştir. Bu gelişme, projenin "Konuşan İşlem Platformu" vizyonunun somut bir kanıtıdır.
---

### **2024-07-23: Faz 1 Adım 1 - MVP'de Bilgi Talebi (RAG) ve Gelişmiş Diyalog**

*   **Karar:** `sentiric-mvp-v1` prototipinde temel bir RAG (Retrieval-Augmented Generation) yeteneği ve daha gelişmiş diyalog akışı entegre edilmiştir. Bu, sistemin sadece belirli formları doldurmakla kalmayıp, statik bir bilgi bankasından genel soruları da yanıtlayabilmesini sağlamıştır.
*   **Gerekçe:**
    *   **Ürün Vizyonunun Genişletilmesi:** "Konuşan İşlem Platformu" vizyonunun temel bileşenlerinden olan bilgi erişimi (RAG) özelliğinin MVP'de somutlaştırılması, projenin kapsamını ve değer önerisini artırmıştır.
    *   **Geliştirilmiş Anlama:** LLM prompt'larının daha da sıkılaştırılması (özellikle `null` değer döndürme talimatı ve sayısal değerler için özel prompt'lar), Ollama'nın yanıt kalitesini ve parametre çıkarma doğruluğunu önemli ölçüde artırmıştır. LLM'den kaynaklanan halüsinasyonlar ve hatalı bilgi atamaları minimize edilmiştir.
    *   **Daha Akıcı Diyalog:** `worker` mantığındaki iyileştirmeler sayesinde, kullanıcı girişlerinin daha akıllıca işlenmesi, geçersiz veya eksik girdilerde daha nazik geri bildirimler verilmesi ve senaryolar arası dinamik geçişler (örn. otel rezervasyonundan bilgi talebine) sağlanmıştır.
    *   **Kararlılık:** LLM'den sayısal değer döndüğünde ortaya çıkan `TypeError` gibi kritik hatalar giderilerek sistemin genel kararlılığı artırılmıştır.
*   **Sonuç:** `sentiric-mvp-v1` artık hem görev odaklı (otel rezervasyonu gibi) hem de bilgi odaklı (çalışma saatleri sorma gibi) diyalogları başarılı bir şekilde yürütebilen, daha akıllı, esnek ve güvenilir bir prototip haline gelmiştir. Bu, projenin bir sonraki fazları için sağlam bir temel oluşturmaktadır.
---