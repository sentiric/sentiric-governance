# ADR-003: Dağıtık İşlemlerde Veri Bütünlüğü İçin SAGA (Orchestration) Modelinin Benimsenmesi

*   **Durum:** Karar Verildi
*   **Tarih:** [Bugünün Tarihi]
*   **Karar Vericiler:** Proje Sahibi, AI Baş Mimar

## Bağlam

Sentiric platformu, doğası gereği dağıtık bir mikroservis mimarisine sahiptir. "Ödemeli randevu oluşturma" gibi bir iş akışı, birden fazla servisin (örn: `user-service`, `payment-service`, `connectors-service`) sıralı olarak çağrılmasını gerektirir. Geleneksel monolitik sistemlerdeki ACID (Atomicity, Consistency, Isolation, Durability) garantileri, bu dağıtık yapıda mevcut değildir.

Bu durum, kritik bir risk doğurur: Eğer iş akışının ortasındaki bir adım (örn: ödeme alma) başarısız olursa, önceki adımlar (örn: randevu oluşturma) geri alınmazsa sistemde veri tutarsızlığı oluşur. Bu, "zombi" randevulara veya tamamlanmamış kayıtlara yol açarak platformun güvenilirliğini zedeler.

## Karar

Bu sorunu çözmek ve platformun veri bütünlüğünü garanti altına almak için **SAGA (Orchestration) Modeli**'nin benimsenmesine karar verilmiştir.

1.  **Orkestratör (Orchestrator):** `sentiric-agent-service`, bu modelin merkezi beyni (orkestratörü) olarak görev yapacaktır. İş akışının hangi adımda olduğunu, hangi servisin çağrılacağını ve bir hata durumunda ne yapılacağını `agent-service` yönetecektir.
2.  **Kalıcı Durum Yönetimi:** Her bir dağıtık işlemin (SAGA) durumu, adımları ve sonuçları, PostgreSQL veritabanında oluşturulacak yeni bir `saga_transactions` tablosunda kalıcı olarak saklanacaktır. Bu, sistem çökse bile işlemin kaldığı yerden devam edebilmesini veya düzgün bir şekilde geri alınabilmesini sağlar.
3.  **Tazmin Edici İşlemler (Compensating Transactions):** Bir iş akışına katılan her servis, yürüttüğü her işlem için o işlemi "geri alacak" bir tazmin edici işlemi de API'si üzerinden sunmakla yükümlü olacaktır. (Örn: `createAppointment` için `cancelPendingAppointment`). Bir adım başarısız olduğunda, orkestratör önceki adımların tazmin edici işlemlerini tersten sırayla çağırarak sistemin tutarlı bir duruma dönmesini garanti eder.

## Sonuçlar ve Etkileri

*   **Pozitif:**
    *   **Artan Güvenilirlik:** Çok adımlı iş akışlarında bile veri bütünlüğü garanti altına alınır.
    *   **Hata Yönetimi:** Kısmi başarısızlıklar, tüm sistemi çökertmek yerine kontrollü bir şekilde yönetilir ve geri alınır.
    *   **İzlenebilirlik:** `saga_transactions` tablosu, her bir iş akışının tüm adımları için bir denetim izi (audit trail) sağlar, bu da hata ayıklamayı kolaylaştırır.
    *   **Net Sorumluluklar:** Orkestratör (`agent-service`) akışı yönetirken, katılımcı servisler sadece kendi iş mantıklarına odaklanır.

*   **Negatif:**
    *   **Artan Karmaşıklık:** Basit bir API çağrıları zincirine göre daha karmaşık bir mantık gerektirir. Her yeni işlem için bir de tazmin edici işlem tasarlanmalıdır.
    *   **Geliştirme Yükü:** Başlangıçtaki geliştirme süresini bir miktar artırır, ancak bu, uzun vadede potansiyel veri bozulmalarını ve karmaşık hata ayıklama süreçlerini önleyen değerli bir yatırımdır.