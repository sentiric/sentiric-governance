# 🛡️ Sentiric: Güvenlik ve Uyumluluk Politikası (v3.0 "Genesis" Uyumlu)

Bu doküman, Sentiric platformunun ve işlediği verilerin güvenliğini sağlamak için benimsediğimiz politika ve teknik önlemleri tanımlar. Güvenlik, bir özellik değil, platformun temel bir gereksinimidir.

## 1. Temel Güvenlik Prensipleri

1.  **En Az Ayrıcalık (Least Privilege):** Her servis ve kullanıcı, sadece işini yapmak için kesinlikle gerekli olan kaynaklara ve verilere erişim yetkisine sahiptir.
2.  **Derinlemesine Savunma (Defense in Depth):** Tek bir güvenlik katmanına güvenmek yerine, ağ, uygulama, veri ve operasyonel seviyelerde çok katmanlı güvenlik önlemleri uygulanır.
3.  **Sıfır Güven (Zero Trust):** Ağ içindeki hiçbir servis veya kullanıcıya varsayılan olarak güvenilmez. Tüm erişim istekleri kimlik doğrulaması ve yetkilendirme süreçlerinden geçer.
4.  **Güvenli Tasarım (Secure by Design):** Güvenlik, geliştirme sürecinin en başında mimariye dahil edilir, sonradan eklenen bir yama olarak görülmez.

## 2. İletişim Güvenliği

*   **Sinyal Şifrelemesi (TLS/WSS):** `sip-gateway` ve `api-gateway` gibi dış dünyaya açık tüm servisler, standart olarak TLS şifrelemesini zorunlu kılar.
*   **Medya Şifrelemesi (SRTP/ZRTP):**
    *   **Politika:** Tüm sesli (ve gelecekteki görüntülü) iletişim, dinlemeye (eavesdropping) karşı korunmalıdır.
    *   **Uygulama:** `sentiric-media-service`, **SRTP (Secure Real-time Transport Protocol)** ve anahtar değişimi için **ZRTP** veya **DTLS-SRTP** protokollerini destekleyecektir. Bu, çağrının başından sonuna kadar medyanın uçtan uca şifrelenmesini sağlar. Bu, Faz 1 geliştirme hedeflerinin bir parçasıdır.
*   **Servisler Arası Güvenlik (mTLS):** Uzun vadeli yol haritamız, tüm iç mikroservis iletişimini karşılıklı TLS (mTLS) ile şifreleyerek Sıfır Güven ağ modelini tam olarak uygulamayı hedefler.

## 3. Veri Güvenliği ve Gizliliği

*   **Hassas Veri Maskeleme (PII Redaction):** Kredi kartı numarası, T.C. kimlik numarası gibi Kişisel Tanımlayıcı Bilgiler (PII) **asla** veritabanlarına veya loglara kaydedilmez. `agent-service`, bu verileri AI motorlarına göndermeden önce maskeleyecektir.
*   **Veritabanı Şifrelemesi:** Tüm veritabanları, hem bekleme durumunda (at-rest) hem de aktarım sırasında (in-transit) şifrelenecektir.
*   **API Güvenliği:** Tüm API endpoint'leri, `JWT` tabanlı kimlik doğrulama ve rol bazlı yetkilendirme (RBAC) ile korunacaktır.
*   **Sır Yönetimi (Secret Management):** Tüm şifreler ve API anahtarları, koddan ayrı olarak, `GitHub Secrets` (CI/CD için) ve üretim ortamında `HashiCorp Vault` veya eşdeğeri bir servis aracılığıyla yönetilecektir.

## 4. Yapay Zeka Güvenliği

*   **Yetkisiz Model Erişimi:** Tüm dahili AI servisleri (`stt-service`, `tts-service`), sadece platform içinden gelen isteklere yanıt verecek şekilde ağ politikaları ile korunacaktır.
*   **Adversarial Saldırılar:** Platform, ses deepfake'leri veya kötü niyetli prompt enjeksiyonları gibi saldırılara karşı, ses filigranı (audio watermarking) ve girdi doğrulama katmanları ile güçlendirilecektir. Bu, uzun vadeli araştırma ve geliştirme hedeflerimiz arasındadır.

## 5. Uyumluluk (Compliance)

*   **GDPR (Genel Veri Koruma Yönetmeliği):** Platform, kullanıcıların verilerini silme ("unutulma hakkı") ve verilerine erişme taleplerini karşılayacak şekilde tasarlanacaktır.
*   **PCI-DSS (Ödeme Kartı Sektörü Veri Güvenliği Standardı):** Platform, ham kredi kartı bilgilerini **asla** işlemeyecek, iletmeyecek veya saklamayacaktır. Ödeme işlemleri, Stripe gibi PCI-DSS uyumlu harici sağlayıcılara yönlendirilecektir.