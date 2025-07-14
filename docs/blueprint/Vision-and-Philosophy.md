# 📜 Vizyon ve Felsefe: "The Sentiric Way" (Revize Edilmiş v2.0)

## 1. Proje Manifestosu

Geleneksel sesli asistanlar ve IVR sistemleri, kullanıcıyı katı menülere hapseden, sinir bozucu deneyimler sunar. **Sentiric, bu paradigmayı kökünden değiştirir.** Amacımız, `ChatGPT` veya `Google Gemini` ile konuşur gibi doğal ve akışkan bir deneyimi, gerçek dünya iş süreçlerine entegre etmektir. Sistem, kullanıcının kurallarına uymak yerine, kullanıcının niyetini anlar, konuşmanın akışına adapte olur ve karmaşık görevleri tamamlamak için arka plandaki iş sistemleriyle akıllıca etkileşime girer.

**Vizyonumuz:** Geliştiricilerin, herhangi bir iş sürecini, **gerçek zamanlı, akışkan ve insan benzeri bir sesli diyalog** aracılığıyla otomatize edebileceği bir platform yaratmak.


**Hedef Kitlemiz:**
*   **Geliştiriciler ve Startup'lar:** Karmaşık altyapılarla uğraşmadan, kendi ürünlerine hızlıca sesli etkileşim yetenekleri eklemek isteyenler.
*   **KOBİ'ler ve Kurumsal Departmanlar:** Müşteri hizmetleri, rezervasyon, sipariş takibi gibi süreçlerini, pahalı ve esnek olmayan kurumsal çözümlere alternatif olarak otomatize etmek isteyenler.

## 2. Temel Felsefe: "Tak-Çıkar Lego Seti"

Sentiric, monolitik bir "her şeyi kendimiz yaparız" veya esnek olmayan bir "her şeyi dışarıdan alırız" yaklaşımını reddeder. Felsefemiz, bu iki dünyanın en iyi yanlarını birleştiren hibrit bir modeldir.

**"The Sentiric Way" dört temel prensibe dayanır:**

1.  **Soyutla ve Fethet (Abstract and Conquer):**
    Platform, belirli bir teknolojiyle (örn: Google Gemini, Twilio) doğrudan konuşmaz. Bunun yerine, `BaseASR`, `BaseTTS`, `BaseLLM` gibi iyi tanımlanmış **arayüzlerle (interfaces)** konuşur. Bu arayüzlerin arkasında hangi somut teknolojinin olduğu, platformun geri kalanı için bir detaydır. Bu, bize mutlak bir teknoloji bağımsızlığı sağlar.

2.  **Adaptör Tabanlı Mimari (Adapter-Centric Architecture):**
    Her harici servis (Google, Twilio, Stripe) veya dahili motor (kendi ASR motorumuz), bu soyut arayüzleri uygulayan bir **"Adaptör"** aracılığıyla sisteme bağlanır. Bir teknolojiyi değiştirmek, projenin tamamını yeniden yazmak değil, sadece yeni bir adaptör takmaktır.

3.  **Varsayılan Olarak Harici, Stratejik Olarak Dahili (External by Default, Internal by Strategy):**
    Pazara giriş hızını maksimize etmek için, başlangıçta her işlev için sınıfının en iyisi (ve mümkünse ücretsiz katmanı olan) harici servisleri kullanırız. Ancak mimarimiz, maliyet, kontrol veya performans nedenleriyle bu parçaları gelecekte kendi **"in-house"** çözümlerimizle değiştirme lüksünü bize her zaman tanır.

4.  **Görev Odaklı Orkestrasyon (Task-Oriented Orchestration):**
    Platformun zekası, sadece konuşmayı yönetmek değil, aynı zamanda **"Görevleri" (Tasks)** yürütmektir. `RestaurantReservationTask` gibi her görev, belirli bir iş akışını tanımlar. Ana orkestratör, kullanıcının niyetine göre doğru görevi seçer, çalıştırır ve görevin adımlarını yönetir. Bu görevler ve akışlar, koddan bağımsız **YAML "Reçete" dosyaları** ile tanımlanarak platformu sonsuz derecede genişletilebilir kılar.

## 3. İnsan Benzeri Diyalog Sanatı: SSML'in Rolü

Sentiric'in "akışkan diyalog" hedefi, sadece doğru kelimeleri bulmakla sınırlı değildir. Konuşmanın ritmi, tonu ve doğallığı da aynı derecede önemlidir. Bu nedenle mimarimiz, **SSML (Speech Synthesis Markup Language)** kullanımını temel bir prensip olarak benimser.

LLM'den sadece metin değil, aynı zamanda konuşmanın nasıl seslendirileceğini de (`<break time="400ms"/>` gibi duraklamalar, `<prosody>` ile tonlama) içeren SSML tabanlı yanıtlar üretmesini isteriz. Bu, robotik bir sesten, nefes alan, duraklayan ve vurgu yapan, insana çok daha yakın bir diyalog deneyimine geçmemizi sağlar.
Bu felsefe, Sentiric'i hem bugün hızlıca değer yaratabilen hem de gelecekteki her türlü teknolojik ve stratejik değişikliğe karşı dayanıklı, esnek bir platform haline getirir.

---
