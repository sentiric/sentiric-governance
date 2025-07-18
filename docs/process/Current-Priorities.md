# 🚀 Sentiric: Anlık Öncelikler ve Sonraki Adımlar

Bu belge, projenin "şimdi" neye odaklandığını gösteren yaşayan bir dokümandır. **Proje Sahibi** tarafından düzenli olarak güncellenir ve **AI Mimar** için bir sonraki görevin ne olduğunu belirtir.

## 🎯 Mevcut Odak: Faz 1 - Çekirdek Platform Kurulumu

*   **Açıklama:** Projenin canlıya alınabilmesi için gereken temel altyapının ve çekirdek iletişim servislerinin kurulması. Bu, platformun dış dünyadan (telefon hattı/SIP) gelen bir çağrıyı alıp işleyebilmesinin ilk adımıdır.
*   **Durum:** ⬜ **Sıradaki**

## ⚡ Sıradaki Görev (Up Next)

*   **Görev Adı:** Faz 1 Adım A - Temel Altyapı ve Dış Bağlantı Hazırlığı
*   **Açıklama:** `Roadmap.md`'de tanımlanan "Faz 1 - A. Temel Altyapı ve Dış Bağlantı" bölümündeki ilk adımları tamamlamak. Bu, projenin somut olarak çalışır hale gelmesi için atılacak ilk adımdır.
*   **Kabul Kriterleri:**
    - [ ] **Altyapı Hazırlığı:** `sentiric-infrastructure` reposu kullanılarak, temel bulut kaynaklarının (Kubernetes cluster, veritabanı, ağ kuralları vb.) Terraform veya eşdeğer bir IaC aracı ile oluşturulması.
    - [ ] **API Gateway Dağıtımı:** `sentiric-api-gateway-service`'in derlenip, hazırlanan altyapıya dağıtılması. Bu, diğer tüm servisler için merkezi erişim noktası olacaktır.
    - [ ] **SIP Servislerinin Dağıtımı:** `sentiric-sip-signaling-service` ve `sentiric-media-service`'in derlenip, hazırlanan altyapıya dağıtılması.
    - [ ] **Temel Yönlendirme Servislerinin Dağıtımı:** `sentiric-user-service` ve `sentiric-dialplan-service`'in derlenip, altyapıya dağıtılması.
    - [ ] **Doğrulama:** Dışarıdan yapılan bir SIP çağrısının, `sentiric-api-gateway`'den geçerek `sentiric-sip-signaling-service` tarafından alınıp, temel bir yanıtla (örn: "servis aktif") karşılanabildiğinin test edilmesi.

## 📚 Gelecek Planı (Backlog)

*   **Görev:** Faz 1 Adım B - Çekirdek İş Akışı ve İlk Görev (`GenericReservationTask`).
*   **Görev:** `sentiric-core-interfaces` içindeki soyut sınıfları ve API sözleşmelerini tanımlamak.
*   **Görev:** `sentiric-agent-service`'in ilk versiyonunu dağıtmak.
*   ...