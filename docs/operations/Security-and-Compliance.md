# 🛡️ Sentiric: Güvenlik ve Uyumluluk Politikası

Bu doküman, Sentiric platformunun ve işlediği verilerin güvenliğini sağlamak için benimsediğimiz politika ve teknik önlemleri tanımlar. Güvenlik, bir özellik değil, platformun temel bir gereksinimidir.

## 1. Temel Güvenlik Prensipleri

1.  **En Az Ayrıcalık (Least Privilege):** Her servis ve kullanıcı, sadece işini yapmak için kesinlikle gerekli olan kaynaklara ve verilere erişim yetkisine sahiptir.
2.  **Derinlemesine Savunma (Defense in Depth):** Tek bir güvenlik katmanına güvenmek yerine, ağ, uygulama, veri ve operasyonel seviyelerde çok katmanlı güvenlik önlemleri uygulanır.
3.  **Sıfır Güven (Zero Trust):** Ağ içindeki hiçbir servis veya kullanıcıya varsayılan olarak güvenilmez. Tüm erişim istekleri kimlik doğrulaması ve yetkilendirme süreçlerinden geçer.
4.  **Güvenli Tasarım (Secure by Design):** Güvenlik, geliştirme sürecinin en başında mimariye dahil edilir, sonradan eklenen bir yama olarak görülmez.

## 2. Veri Güvenliği ve Gizliliği

*   **Hassas Veri Maskeleme (PII Redaction):**
    *   **Politika:** Kredi kartı numarası, T.C. kimlik numarası gibi Kişisel Tanımlayıcı Bilgiler (PII) **asla** veritabanlarına veya loglara kaydedilmez.
    *   **Uygulama:** `sentiric-agent-worker` servisi, ASR'dan gelen metin üzerinde, LLM'e göndermeden önce PII tespiti ve maskeleme (`[TCKN_REDACTED]`) yapacak bir katmana sahip olacaktır.
*   **Veritabanı Şifrelemesi:** Tüm veritabanları, hem bekleme durumunda (at-rest) hem de aktarım sırasında (in-transit) şifrelenecektir.
*   **API Güvenliği:** Tüm API endpoint'leri, `JWT` tabanlı kimlik doğrulama ve rol bazlı yetkilendirme (RBAC) ile korunacaktır.
*   **Sır Yönetimi (Secret Management):** Tüm şifreler, API anahtarları ve sertifikalar, koddan tamamen ayrı olarak, `HashiCorp Vault` veya bulut sağlayıcısının (AWS/GCP/Azure) sunduğu sır yönetim servisleri aracılığıyla yönetilecektir.

## 3. Uyumluluk (Compliance)

*   **GDPR (Genel Veri Koruma Yönetmeliği):** Platform, kullanıcıların verilerini silme ("unutulma hakkı") ve verilerine erişme taleplerini karşılayacak şekilde tasarlanacaktır.
*   **PCI-DSS (Ödeme Kartı Sektörü Veri Güvenliği Standardı):**
    *   **Politika:** Platform, **asla** ham kredi kartı bilgilerini işlemeyecek, iletmeyecek veya saklamayacaktır.
    *   **Uygulama:** Ödeme işlemleri, Stripe gibi PCI-DSS uyumlu bir sağlayıcıya yönlendirilen **güvenli ödeme linkleri** aracılığıyla gerçekleştirilecektir. Bu, uyumluluk yükümüzü önemli ölçüde azaltır.

## 4. Güvenlik Denetimleri

*   **Bağımlılık Taraması:** `Dependabot` veya `Snyk` gibi araçlar, kullanılan kütüphanelerdeki bilinen güvenlik açıklarını tespit etmek için tüm repolarda düzenli olarak çalıştırılacaktır.
*   **Kod Analizi:** Statik Kod Analizi (SAST) araçları, CI/CD pipeline'larına entegre edilerek potansiyel güvenlik açıkları (SQL Injection, XSS vb.) tespit edilecektir.

---