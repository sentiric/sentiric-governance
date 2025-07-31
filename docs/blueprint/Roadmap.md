# 🧭 Sentiric: Stratejik Yol Haritası (v12.0 "Bütünleşik Genesis")

Bu yol haritası, Sentiric "İletişim İşletim Sistemi" vizyonunu hayata geçiren, iteratif ve sonuç odaklı geliştirme planıdır. Her faz, platforma somut ve test edilebilir yeni bir değer katmanı ekler.

## **FAZ 1: "GÜVENLİ VE DAĞITIK OMURGA"**

*   **Hedef:** Platformun temel iskeletini, çoklu sunucu (multi-cloud, hybrid) ortamlarında güvenli, dayanıklı ve gözlemlenebilir bir şekilde çalışacak hale getirmek. Bu, gelecekteki tüm servislerin üzerine inşa edileceği **sağlam zemindir.**
*   **Kabul Kriteri:** Bir test script'i (`sentiric-cli`) ile `user-service`'e gRPC üzerinden `GetUser` isteği atıldığında, isteğin `api-gateway`'den geçerek `user-service`'e ulaştığı, logların doğru formatta basıldığı ve tüm iletişimin mTLS ile şifrelendiği kanıtlanmalıdır.

---

## **FAZ 2: "FONKSİYONEL İSKELET"**

*   **Hedef:** Omurga üzerine, bir telefon çağrısını baştan sona yönetebilen temel servisleri (iskeleti) yerleştirmek. Bu faz sonunda, sistem bir çağrıyı alabilir, hangi plana göre hareket edeceğine karar verebilir, bir medya kanalı açabilir ve temel bir kayıt oluşturabilir.
*   **Kabul Kriteri:** `sentiric-cli`'den başlatılan bir test çağrısı, `sip-gateway` -> `sip-signaling` -> `dialplan` -> `media` servislerini başarıyla tetiklemeli, RabbitMQ'ya `call.started` olayı düşmeli ve `cdr-service` bunu veritabanına temel bir kayıt olarak işlemelidir. Henüz sesli yanıt yoktur.

---

## **FAZ 3: "CANLANAN PLATFORM"**

*   **Hedef:** İskelete "beyin" ve "ses" ekleyerek platformu canlandırmak. Bu faz sonunda, sistem arayanla ilk anlamlı sesli diyaloğu kurabilir ve bu etkileşim bir yönetici tarafından izlenebilir.
*   **Kabul Kriteri:** Gerçek bir telefonla arama yapıldığında, sistem "Merhaba, Sentiric'e hoş geldiniz" anonsunu çalmalı, kullanıcının cevabını metne çevirmeli ve bu etkileşim `dashboard-ui`'da canlı olarak görülebilmelidir.

---

## **FAZ 4: "AKILLI VE İNSAN ODAKLI PLATFORM"**

*   **Hedef:** Platformu, karmaşık görevleri yürütebilen, bilgi bankasından faydalanabilen ve gerektiğinde görevi sorunsuz bir şekilde insan temsilciye devredebilen, tam teşekküllü bir AI orkestratörüne dönüştürmek.
*   **Kabul Kriteri:** Bir kullanıcı, "yarın için randevu almak istiyorum" dediğinde, sistem RAG ile bilgi alıp, Durum Makinesi ile adımları takip ederek randevuyu oluşturabilmeli veya "operatöre bağlan" dediğinde çağrıyı `web-agent-ui`'ye düşürebilmelidir.

---

## **FAZ 5: "EKOSİSTEMİN DOĞUŞU"**

*   **Hedef:** Sentiric'i sadece bir sesli platform olmaktan çıkarıp, metin tabanlı kanalları da destekleyen ve üçüncü parti geliştiricilerin katkıda bulunabileceği bir ekosisteme dönüştürmek.
*   **Kabul Kriteri:** Bir web sitesine `embeddable-voice-widget-sdk` entegre edilebilmeli, WhatsApp'tan gelen bir mesaja `messaging-gateway-service` aracılığıyla yanıt verilebilmeli ve SAGA paterni ile yapılan çok adımlı bir işlemin veri bütünlüğü garanti edilebilmelidir.

---
