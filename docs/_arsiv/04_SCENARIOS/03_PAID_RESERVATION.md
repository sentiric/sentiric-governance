# 💳 Ödemeli Rezervasyon Akışı

## 🎯 Kullanım Senaryosu
- **Kimler Kullanır?**: Premium hizmetler, Etkinlik rezervasyonları
- **Ön Koşul**: Ön ödeme gerektiren hizmetler

## 🔄 Adım Adım Akış
1. **Ön Bilgilendirme**:
   - Sistem otomatik olarak ücret bilgisini paylaşır
   - "50₲ depozito alınacaktır"

2. **Ödeme Süreci**:
   ```mermaid
   journey
       title Ödeme Akışı
       section Müşteri
         SMS alır: 5: Müşteri
         Ödeme yapar: 4: Müşteri
       section Sistem
         Onay gönderir: 5: Sistem
   ```


---