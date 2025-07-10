# 🎭 Kullanıcı Rolleri ve Perspektifleri

Bu doküman, Sentiric platformuyla etkileşime giren farklı kullanıcı rollerinin ihtiyaçlarını, beklentilerini ve onlar için önemli olan komutları özetler.

---
## 1. Müşteri (Son Kullanıcı) Perspektifi
Müşteriler, hızlı ve etkili bir şekilde sorunlarını çözmek isterler. Diyalog doğal ve akıcı olmalıdır.

#### Sık Kullanılan Komutlar
- "Randevu almak istiyorum"
- "Fatura durumumu sorgulayabilir miyim?"
- "Rezervasyonumu iptal etmek istiyorum"
- "Çalışma saatleriniz nedir?"

#### Yardım Alma
- Herhangi bir adımda "operatör" veya "gerçek kişi" demek, canlı bir temsilciye bağlanma sürecini başlatmalıdır.
- "Yardım" komutu, mevcut görevle ilgili ipuçları sunmalıdır.

---
## 2. Operatör (Çalışan) Perspektifi
Operatörler, sistemin bir çağrıyı kendilerine ne zaman ve nasıl devrettiğini bilmelidir. Çağrıları yönetmek için kısayollara ihtiyaç duyarlar.

#### Çağrı Yönetim Komutları (Sistem İçi)
| Tuş Kombinasyonu / Komut | İşlev                                |
|--------------------------|--------------------------------------|
| `*1`                     | Çağrıyı acil durum olarak işaretle   |
| `*2`                     | Bir süpervizörü görüşmeye dahil et |
| "Sessize al"             | Müşteriyi duymadan arka planda işlem yap |

#### Acil Durum Prosedürleri
- **Tıbbi Acil Durum:** Sistem, "kalp krizi", "ambulans" gibi anahtar kelimeleri algıladığında çağrıyı otomatik olarak önceliklendirip operatöre "Tıbbi Acil Durum" uyarısıyla devretmelidir.
- **Teknik Arıza:** Sistem yanıt veremediğinde, çağrı otomatik olarak bir operatöre yönlendirilmeli ve arka planda bir hata kaydı oluşturulmalıdır.

---
## 3. Yönetici (Executive) Perspektifi
Yöneticiler, platformun genel performansı ve iş metrikleri ile ilgilenirler. Bu veriler, `sentiric-dashboard` üzerinde görselleştirilmelidir.

#### Takip Edilecek Kritik Göstergeler (KPIs)
- **Çağrı Başına Maliyet (Cost Per Call):** `(Toplam Altyapı Maliyeti + API Giderleri) / Toplam Çağrı Sayısı`
- **Otomasyon Oranı (Automation Rate):** `(Operatöre Aktarılmayan Çağrı Sayısı / Toplam Çağrı Sayısı) * 100`
- **Ortalama Çağrı Çözüm Süresi (Average Handle Time):** Otomatik tamamlanan çağrıların ortalama süresi.
- **Müşteri Memnuniyeti (CSAT):** Çağrı sonrası SMS ile gönderilen anketlerden gelen puanların ortalaması.
- **En Çok Yürütülen Görevler (Top Tasks):** `Randevu Alma`, `Bilgi Sorgulama` gibi görevlerin kullanım sıklığı.