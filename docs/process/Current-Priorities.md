# 🚀 Sentiric: Anlık Öncelikler ve Sonraki Adımlar

Bu belge, projenin "şimdi" neye odaklandığını gösteren yaşayan bir dokümandır ve **AI Mimar** için bir sonraki görevin ne olduğunu belirtir.

## 🎯 Mevcut Odak: Milestone 1 - Arama Sinyalinin Alınması

*   **Açıklama:** Projemizin ilk fonksiyonel parçasını inşa etmek. Amacımız, dış dünyadan gelen bir SIP çağrısını alıp, temel bir yanıtla karşılayabilen `sentiric-sip-signaling-service`'i ayağa kaldırmak.
*   **Referans Belge:** `docs/blueprint/Build-Strategy.md`
*   **Durum:** ⬜ **Sıradaki**

## ⚡ Sıradaki Görev (Up Next)

*   **Görev Adı:** `sentiric-sip-signaling-service` İskeletinin Oluşturulması
*   **Açıklama:** `Build-Strategy.md` belgesindeki **Milestone 1**'i tamamlamak üzere, `sentiric-sip-signaling-service`'in ilk, temel versiyonunu oluşturmak ve mevcut `Docker Compose` altyapısına entegre etmek.
*   **Kabul Kriterleri:**
    - [ ] `sentiric-sip-signaling-service` için temel bir Node.js proje iskeleti oluşturuldu.
    - [ ] Servis, gelen SIP `INVITE` isteklerini dinleyebiliyor ve konsola log basabiliyor.
    - [ ] Servis, gelen çağrıya `200 OK` yanıtı dönebiliyor.
    - [ ] Servis için bir `Dockerfile` oluşturuldu.
    - [ ] `sentiric-infrastructure` reposundaki `docker-compose.yml`'ye `sip-signaling-service` eklendi ve `5060/udp` portu map edildi.
    - [ ] Tüm altyapı (`docker compose up -d`) çalıştırıldığında, `sip-signaling-service`'in de başarılı bir şekilde başladığı `docker compose ps` ile doğrulanabiliyor.
```
