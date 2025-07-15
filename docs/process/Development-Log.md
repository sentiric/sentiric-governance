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
### **2024-07-23: Faz 1 Adım 1 - MVP'de Çoklu Parametre Çıkarımı ve Akışkan Diyalog**

*   **Karar:** `sentiric-mvp-v1` prototipine, kullanıcının tek bir cümlede birden fazla bilgi vermesi durumunda bu bilgileri eş zamanlı olarak algılama ve işleme yeteneği (Çoklu Parametre Çıkarımı) entegre edilmiştir. Bu, sistemin diyalog akıcılığını ve doğal dil anlama kabiliyetini önemli ölçüde artırmıştır.
*   **Gerekçe:**
    *   **Akışkan Diyalog:** Kullanıcıların daha doğal konuşma alışkanlıklarına uyum sağlayarak, sistemin birden fazla soruyu tek seferde yanıtlaması, diyalogdaki tur sayısını azaltmış ve kullanıcı deneyimini iyileştirmiştir. Bu, "Gerçek Zamanlı AI Diyaloğu" felsefesinin somut bir çıktısıdır.
    *   **Verimlilik:** Gerekli tüm parametrelerin daha erken aşamalarda toplanması, form doldurma sürecini hızlandırmış ve sistemin görevleri daha verimli tamamlamasına olanak tanımıştır.
    *   **LLM Kullanımı Optimizasyonu:** LLM'e tek bir taleple birden fazla bilgi çıkarma görevi verilerek, her bilgi için ayrı bir LLM çağrısı yapma ihtiyacı azaltılmıştır (bilişsel yük).
*   **Sonuç:** `sentiric-mvp-v1` artık hem tekil (soru-cevap) hem de çoklu (tek cümlede birden çok bilgi) parametre girişlerini başarılı bir şekilde işleyebilen, daha insana yakın bir diyalog deneyimi sunmaktadır. Bu gelişme, platformun "Konuşan İşlem Platformu" vizyonuna önemli bir katkı sağlamıştır.
---
### **2024-07-23: Faz 1 Adım 1 - MVP'de Modüler Mimari, TTS Sağlık Kontrolü ve Mini-Dashboard**

*   **Karar:** `sentiric-mvp-v1` prototipi, ana `sentiric-governance` reposunda tanımlanan kurumsal düzeydeki mimari prensipleri (modülerlik, gözlemlenebilirlik, hata yönetimi) ve ürün vizyonunu (operasyonel dashboard) daha fazla yansıtacak şekilde kapsamlı bir iyileştirmeden geçirilmiştir.
*   **Gerekçe:**
    *   **Mimari Bütünlük:** `worker.js`'in sorumlulukları `CallContextManager` ve `DialogOrchestrator` gibi ayrı modüllere taşınarak, kod organizasyonu ve "Tak-Çıkar Lego Seti" felsefesine uygunluk büyük ölçüde artırılmıştır. Bu, gelecekteki ölçeklenebilirlik ve Python'daki ana projeye aktarım için sağlam bir temel oluşturur.
    *   **Dayanıklılık ve Gözlemlenebilirlik:** Sentiric Voice Engine (Coqui-TTS) sunucusuna eklenen sağlık kontrolü endpoint'i sayesinde, sistem TTS servisinin durumunu proaktif olarak izleyebilmekte ve sağlıksız durumlarda sesli yanıt denemek yerine metin tabanlı geri bildirim sağlayarak hatalı davranışı engellemektedir. Bu, `docs/operations/Monitoring-and-Logging.md`'deki hedeflerle uyumludur.
    *   **Operasyonel Farkındalık:** Kullanıcı arayüzüne eklenen "Aktif Oturum Bilgisi" paneli ve "TTS Durumu" göstergesi, platformun iç işleyişine dair anlık görünürlük sağlayarak `docs/product/User-Persona-Guides.md`'deki Yönetici/Operatör perspektifinin temelini atmıştır.
    *   **Kullanıcı Deneyimi:** Oturum yönetimi iyileştirilerek, bir görev tamamlandıktan sonra oturumun tamamen sıfırlanması yerine senaryo bağlamının sıfırlanması sağlanmış, böylece kullanıcıların aynı oturumda farklı görevlere geçiş yapması kolaylaştırılmıştır. UI'daki çeşitli `TypeError` ve `SyntaxError` hataları da giderilmiştir.
*   **Sonuç:** `sentiric-mvp-v1` artık sadece temel bir prototip olmaktan çıkmış, gerçek bir "Konuşan İşlem Platformu"nun temel özelliklerini (modüler mimari, akıllı diyalog, sağlam hata yönetimi ve operasyonel görünürlük) sergileyen, son derece yetenekli ve etkileyici bir Minimal Değerli Ürün (MVP) haline gelmiştir. Faz 1'deki hedeflere büyük ölçüde ulaşılmıştır.
---
### **2024-07-24: Stratejik Yeniden Hizalanma ve Mimari Netleştirme (v4.0)**

*   **Karar:** Pazar ve rakip analizi (SignalWire vb.) sonucunda projenin vizyonu, sadece bir "Konuşan İşlem Platformu" olmaktan çıkarak, farklı endüstriler için özelleştirilmiş çözümler sunan bir **"Dikey Entegrasyon Platformu ve Geliştirici Ekosistemi"** olarak genişletilmiştir. Bu karar, projenin benzersiz hibrit (bulut/yerel) yapısını bir rekabet avantajı olarak konumlandırmayı hedefler.
*   **Karar:** Platformun insan benzeri diyalog yeteneğini artırmak için **SSML (Speech Synthesis Markup Language)** kullanımı, mimarinin temel bir prensibi olarak benimsenmiştir. `agent-worker`'ın LLM'den SSML tabanlı yanıtlar üretmesi ve TTS servislerinin bu formatı işlemesi standartlaştırılmıştır.
*   **Karar:** Platformun esnek iş akışı yapılandırması, **YAML tabanlı "Reçeteler" (Recipes)** olarak adlandırılmış ve bu konseptin dokümantasyonda daha belirgin hale getirilmesine karar verilmiştir.
*   **Karar:** Mevcut Node.js MVP'si ile nihai Python üretim mimarisi arasındaki farkları ve geçiş stratejisini netleştirmek için `MVP-to-Production-Bridge.md` dokümanı oluşturulmuştur.
*   **Gerekçe:** Bu kapsamlı güncelleme, projenin başlangıç aşamasındaki stratejik belirsizlikleri ortadan kaldırmak, tüm paydaşlar için tek ve net bir doğruluk kaynağı oluşturmak ve projenin hem teknik hem de ticari olarak sağlam bir temel üzerinde ilerlemesini sağlamak için yapılmıştır. Bu, teorik plandan, pazar farkındalığına sahip, uygulanabilir bir mühendislik ve ürün yol haritasına geçişi temsil eder.
---
# **İNANILMAZ! BAŞARDIK!** 🚀

Evet! Oldu! Gözlerimle görüyorum, `https://sentiric.azmisahin.com` adresinde kilit işareti var, arayüz çalışıyor, "Merhaba." mesajına cevap vermiş ve konsolda hiçbir kırmızı hata yok!

**"Durum Değişikliği: idle -> listening"**
**"SpeechRecognition başladı."**
**"Durum Değişikliği: listening -> thinking"**
**"SpeechRecognition durdu."**
**"Durum Değişikliği: thinking -> speaking"**
**"Durum Değişikliği: speaking -> listening"**
**"SpeechRecognition başladı."**

Bu loglar, sistemin bizim yazdığımız **Durum Makinesi mantığıyla kusursuz bir şekilde çalıştığını,** mikrofonu kapatıp açtığını ve diyalog akışını doğru yönettiğini gösteriyor. **"Kendi kendine konuşma" sorunu da tamamen çözüldü.**

---

### **2024-07-24: MVP'nin Bulutta Canlıya Alınması ve Kritik Sorun Giderme Süreci**

*   **Karar:** `sentiric-mvp` prototipinin Google Cloud'daki `e2-micro` sanal makine üzerinde canlıya alınmasına ve `sentiric.azmisahin.com` alan adı üzerinden HTTPS (Cloudflare proxy'li) erişimine açılmasına karar verildi. Bu, projenin "Canlı Prototip" ve "Pragmatik Başlangıç" felsefesinin somutlaştırılmasıdır.

*   **Yaşanan Temel Sorunlar ve Çözümleri:**
    1.  **"Killed" Hataları (RAM Yetersizliği):**
        *   **Belirti:** `pip install torch` ve `python app.py` komutlarının RAM yetersizliğinden dolayı `Killed` hatası vermesi.
        *   **Çözüm:** Sunucu üzerinde 8GB'lık bir swap alanı oluşturularak toplam bellek kapasitesi artırıldı. Bu, `e2-micro` üzerindeki büyük Python modellerinin (Coqui-TTS) yüklenmesini sağladı.
    2.  **Disk Alanı Yetersizliği:**
        *   **Belirti:** `pip install` sırasında "No space left on device" hatası.
        *   **Çözüm:** Google Cloud konsolundan sanal diskin boyutu 10GB'tan 30GB'a çıkarıldı. İşletim sistemi bu yeni alanı otomatik olarak tanıdı.
    3.  **Coqui-TTS Lisans Onayı (`OSError: [Errno 9] Bad file descriptor`):**
        *   **Belirti:** `nohup` ile başlatıldığında Coqui-TTS'in lisans onayını interaktif olarak bekleyip hata vermesi.
        *   **Çözüm:** `COQUI_TOS_AGREED=1` ve `COQUI_COOKIE_XTTS_AGREED=1` ortam değişkenleri `nohup` komutunun doğrudan başında verilerek, kütüphanenin lisansı otomatik olarak kabul etmesi sağlandı.
    4.  **TTS Servis Yönlendirme Mantığı Hatası:**
        *   **Belirti:** Yerel TTS (Coqui) çalışmasına rağmen, `sentiric-mvp`'nin ElevenLabs'e geçmeye çalışması (`config.js` ve `tts-handler.js` mantık hatası).
        *   **Çözüm:** `tts-handler.js` ve `config.js` dosyalarındaki mantık düzeltilerek, öncelikli olarak yerel TTS'in denenmesi, zaman aşımı veya hata durumunda ElevenLabs'e geçilmesi sağlandı.
    5.  **Ağ Katmanı Erişim Sorunları (Cloudflare 52x Hataları):**
        *   **Belirti:** `http://IP/` adresinin çalışmaması, Cloudflare'den 521/522 hataları alınması.
        *   **Çözüm:**
            *   Nginx sunucusunun konfigürasyonu basitleştirildi (`listen 80; proxy_pass http://localhost:3000;`).
            *   Google Cloud'da sunucuya `http-server` ve `https-server` ağ etiketleri eklendi.
            *   Cloudflare'den Origin Sertifikası (`cloudflare.crt`, `cloudflare.key`) oluşturuldu ve Nginx'e kuruldu.
            *   Nginx, `listen 443 ssl;` ile HTTPS trafiğini dinleyecek şekilde yapılandırıldı.
            *   Cloudflare SSL/TLS modu "Full (Strict)" olarak ayarlandı.
    6.  **"Kendi Kendine Konuşma" ve `SpeechRecognition` Hataları:**
        *   **Belirti:** Sistem kendi sesini mikrofondan tekrar duyup yanıt vermeye çalışması (`audio feedback loop`), `InvalidStateError` ve `no-speech` hataları.
        *   **Çözüm:** `public/script.js` dosyasındaki istemci tarafı JavaScript kodu, `SpeechRecognition` motorunu ses çalarken **aktif olarak durduracak** ve ses bitince **güvenli bir gecikmeyle** yeniden başlatacak şekilde "Durum Makinesi" mantığıyla yeniden yazıldı.

*   **Sonuç:** `sentiric-mvp` prototipi, `https://sentiric.azmisahin.com` adresi üzerinden, yerel TTS sunucusu ve ElevenLabs fallback mekanizması ile, stabil ve akıcı bir diyalog deneyimi sunarak **başarıyla canlıya alınmıştır.** Bu zorlu süreç, projenin dayanıklılığını ve hata giderme yeteneğini kanıtlamıştır.

---
### **2024-07-15: UI/UX Refaktör ve Otomatik Oynatma Engeli Çözümü**

*   **Karar:** Tarayıcılardaki otomatik ses oynatma politikası (`NotAllowedError`) nedeniyle oluşan ilk karşılama mesajı hatası ve UI'daki sorumluluk ayrımı sorunlarını gidermek amacıyla kapsamlı bir refaktör yapılmıştır. Ayrıca, hardcode edilmiş sunucu URL'leri ortam değişkenleri üzerinden yönetilecek şekilde düzeltilmiştir.
*   **Gerekçe:**
    *   **Otomatik Oynatma Engeli:** Tarayıcıların kullanıcı etkileşimi olmadan ses oynatmasını engelleyen güvenlik politikası (`NotAllowedError`), uygulamanın ilk açılışında Sentiric'in karşılama sesini çalmasını engelliyordu.
    *   **Sorumluluk Ayrımı:** Frontend (`public/script.js`) ve Backend (`src/services/worker.js`) arasında ilk karşılama mesajının kim tarafından gönderileceği ve UI'da nasıl gösterileceği konusunda bir karmaşa yaşanıyordu, bu da çift mesaj ve tutarsız UI davranışına yol açıyordu.
    *   **URL Yönetimi:** Sunucu adreslerinin (özellikle Dev Tunnels URL'lerinin) kod içine doğrudan yazılması (`gateway.js` ve `script.js`'te), projenin esneklik ve dağıtım prensiplerine aykırıydı.
*   **Uygulanan Çözümler:**
    1.  **`public/script.js`:**
        *   WebSocket bağlantısının (`connect()`) ve `session_init` mesajının gönderilmesinin, kullanıcının mikrofon orb düğmesine yaptığı **ilk tıklama olayına** bağlanması sağlandı. Bu, tarayıcının autoplay politikasını aşarak sesin çalınmasına izin vermiştir.
        *   UI'ın, ilk karşılama mesajı da dahil olmak üzere, tüm yapay zeka mesajlarını **sadece backend'den geldiğinde** göstermesi sağlanmıştır. Önceden hardcode edilmiş veya yinelenen mesaj ekleme mantığı kaldırılmıştır.
        *   WebSocket bağlantısı için sunucu adresinin `window.location.host` üzerinden dinamik olarak alınması sağlanmış, böylece frontend'in nerede çalıştığından bağımsız olması sağlanmıştır.
    2.  **`.env`:** Gateway servisinin dışarıdan erişilebilen WebSocket URL'i (`wss://...`) için `PUBLIC_GATEWAY_WSS_URL` adında yeni bir ortam değişkeni tanımlanmıştır.
    3.  **`src/config.js`:** Yeni `PUBLIC_GATEWAY_WSS_URL` ortam değişkenini okuyacak şekilde güncellenmiştir.
    4.  **`src/services/gateway.js`:** Twilio'ya TwiML yanıtında geri döneceği `<Stream>` URL'i olarak `config.publicGatewayWssUrl` değeri kullanılarak, URL yönetiminin merkezi ve yapılandırılabilir olması sağlanmıştır.
*   **Sonuç:** Bu refaktörle, tarayıcıda oluşan ses oynatma hatası giderilmiş, UI'daki çift mesaj ve karmaşa sorunları çözülmüş, frontend ve backend arasındaki sorumluluk ayrımı netleştirilmiş ve sunucu URL'lerinin hardcode edilmesi hatası ortadan kaldırılmıştır. Proje, daha sağlam, taşınabilir ve kullanıcı dostu bir yapıya kavuşmuştur. Bu, telefon araması testlerindeki ilerlememizi destekleyici niteliktedir.

---
### **2024-07-15: Kendi Kendini Duyma, UI/UX ve Otomatik Oynatma Hataları İçin Kapsamlı Düzeltmeler**

*   **Karar:** Daha önce çözüldüğü düşünülen "kendi kendini duyma" (audio feedback loop) sorunu, tarayıcının otomatik ses oynatma politikası (`NotAllowedError`) ve UI'daki çift mesaj/tutarsızlık sorunları, köklü bir refaktörle nihai olarak giderilmiştir. Bu düzeltmeler, projenin en temel kullanıcı deneyimi sorunlarını çözmeyi hedeflemiştir.
*   **Gerekçe:**
    *   **Kendi Kendini Duyma (Regresyon):** `public/script.js`'deki `SpeechRecognition`'ın yaşam döngüsü ve `currentState` geçişlerindeki zamanlama hataları veya yanlış koşullar nedeniyle sistemin kendi sesini veya ortam sesini yanlışlıkla algılayıp diyalog akışını bozduğu tespit edilmiştir. Bu, önceki düzeltmelerde tam olarak giderilmediği veya yeni değişikliklerle tekrar ortaya çıktığı için acil bir öncelik haline gelmiştir.
    *   **Otomatik Oynatma ve Çift Mesaj:** Tarayıcıların kullanıcı etkileşimi olmadan otomatik ses çalma yasağı ve frontend ile backend arasında mesaj gönderim sorumluluklarının net olmaması, uygulamanın ilk açılışında görsel ve işitsel karmaşaya neden olmuştur.
    *   **TTS Zaman Aşımı:** Coqui-TTS gibi yerel modellerin ilk yüklemelerinde veya ağır yük altında kaldığı durumlarda yaşanan zaman aşımı hataları, diyalog akışını kesintiye uğratıyordu.
*   **Uygulanan Çözümler:**
    1.  **`public/script.js` (Kritik Alan):**
        *   `SpeechRecognition`'ın yaşam döngüsü tamamen `currentState`'e (idle, listening, thinking, speaking) bağlı hale getirilmiştir. Mikrofon, AI `speaking` veya `thinking` durumundayken **mutlaka** durdurulmakta, sadece `listening` durumunda başlatılmaktadır. Bu, kendi kendini duyma sorununa kesin bir çözüm getirmiştir.
        *   `connect()` fonksiyonu ve `session_init` mesajının gönderimi, tarayıcıyla ilk kullanıcı etkileşimi (mikrofon orb düğmesine tıklama) anına taşınmıştır. Bu, tarayıcının autoplay kuralını aşarak sesin ilk açılışta çalmasını sağlamıştır.
        *   Tüm AI yanıt mesajları (ilk karşılama dahil) **sadece backend'den geldiğinde** `addMessage` ile UI'a eklenmekte, frontend'in kendi kendine mesaj üretme veya yinelenen mesajlar ekleme mantığı tamamen kaldırılmıştır.
    2.  **`src/core/tts-handler.js`:** `synthesizeWithLocalXTTS` fonksiyonundaki `timeout` süresi, ilk model yüklemeleri ve işlem gecikmeleri için yeterli zaman tanımak amacıyla 7 saniyeden 20 saniyeye çıkarılmıştır.
    3.  **URL Yönetimi:** `PUBLIC_GATEWAY_WSS_URL` ortam değişkeni kullanımı, hardcode edilmiş URL'lerin yerine geçerek projenin dağıtım esnekliğini ve mimari tutarlılığını artırmıştır.
*   **Sonuç:** Bu kapsamlı düzeltmelerle, Sentiric MVP'nin temel kullanıcı deneyimi sorunları (kendi kendini duyma, otomatik oynatma hatası, çift mesaj) giderilmiş, diyalog akışı çok daha tutarlı ve güvenilir hale gelmiştir. Proje artık, zorlu diyalog senaryolarını test etmek için sağlam bir temele sahiptir.
---
### **2024-07-16: Diyalog Akışı ve LLM Tutarlılığı İçin Kapsamlı Geliştirmeler (MVP V2.0 - Finalize)**

*   **Karar:** Daha önceki testlerde gözlemlenen diyalog akışı bağlam kaybı (görev ortasında bilgi/genel sohbet sonrası senaryo sıfırlama), LLM yanıt kalitesi ve tarih/kişi sayısı algılama hataları, yapılan köklü refaktörler ve LLM prompt iyileştirmeleriyle büyük ölçüde giderilmiştir. Sistem artık insan benzeri akışkan diyalog kurma hedefinde önemli bir aşama kaydetmiştir.
*   **Gerekçe:**
    *   **Bağlam Kaybı (Çalışma Saatleri Regresyonu):** `dialog_orchestrator.js` içindeki `INFORMATION_REQUEST` ve `GENERAL_CHAT` intent tiplerinde görev ortasında `session.reset = true;` bayrağının koşulsuz ayarlanması, aktif görev bağlamının kaybolmasına neden oluyordu. Bu durum, LLM prompt'undaki bağlam koruma kurallarının uygulanmamasına yol açıyordu.
    *   **Tarih/Kişi Sayısı Algılama Hataları:** LLM'in göreceli tarih ifadelerini `YYYY-MM-DD` formatına çevirmekte zorlanması ve `sanitizeLlmOutput`'un hatalı tarih formatlarını zorla yorumlamaya çalışması, yanlış rezervasyon tarihlerine neden oluyordu. Kişi sayısı algılamada da karmaşık ifadelerde tutarsızlıklar vardı.
    *   **LLM Yanıt Kalitesi:** Genel sohbet ve otel dışı konulara verilen yanıtlar hala yeterince doğal veya net değildi.
*   **Uygulanan Çözümler:**
    1.  **`src/dialog_flow/dialog_orchestrator.js`:**
        *   `INFORMATION_REQUEST` ve `GENERAL_CHAT` intent'leri, aktif bir görev (`session.scenarioId`) varken tetiklendiğinde `session.reset = true;` bayrağını ayarlamayacak şekilde revize edilmiştir. Bu, sistemin görev ortasında bilgi sorgulama veya genel sohbet yapıldıktan sonra **rezervasyon görevine sorunsuz bir şekilde geri dönmesini** sağlamıştır. Bu, projenin en büyük diyalog akışı başarısıdır.
        *   `handleTask` fonksiyonu içinde rezervasyon onay mesajında `checkin_date`'in `toLocaleDateString('tr-TR', options)` ile **gün, ay, yıl ve gün adı formatında okunması** sağlanarak kullanıcı deneyimi iyileştirilmiştir.
    2.  **`src/core/ai-handler.js`:**
        *   `sanitizeLlmOutput` fonksiyonu, `checkin_date` için `YYYY-MM-DD` formatı dışında gelen değerleri doğrudan `null` olarak işaretleyecek şekilde basitleştirilmiştir. Bu, LLM'i daha disiplinli formatlar döndürmeye zorlayacak ve hatalı tarihlerle rezervasyon yapılmasını engelleyecektir.
        *   `people_count` için kelime karşılıkları listesi (`bir`, `iki` vb.) genişletilmiştir.
    3.  **`src/prompts/ai_system_prompt.md`:**
        *   Görevin ortasında bilgi/genel sohbet yapıldıktan sonra **"REZERVASYON BAĞLAMINI KESİNLİKLE UNUTMAMA"** ve **"DEVAM ETMEYİ BEKLEME"** kuralı daha güçlü bir şekilde vurgulanmıştır.
        *   Kapsam dışı sorular için (örn. "Dünyanın en yüksek dağı?"), LLM'in **"KESİNLİKLE nazikçe ve doğrudan reddetmesi"** ve ardından otel konularına yönlendirmesi kuralı daha netleştirilmiştir.
        *   Rezervasyon onay mesajında `checkin_date`'in insan dostu formatta (`GG Ay YYYY`) belirtilmesi gerektiği eklenmiştir.
*   **Sonuç:** Sentiric MVP, artık çok daha akışkan, bağlam farkındalığına sahip ve insan benzeri bir diyalog kurabilmektedir. Görev akışındaki kritik bağlam kayıpları giderilmiş, LLM yanıt tutarlılığı artırılmış ve tarih/kişi sayısı algılama hassasiyeti yükseltilmiştir. Bu, projenin Faz 1 hedeflerine ulaşmasında büyük bir adımdır.
---