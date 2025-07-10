# 📅 Randevu Rezervasyon Akışı

## 🎯 Kullanım Senaryosu
- **Kimler Kullanır?**: Müşteriler, Resepsiyon personeli
- **Ön Koşul**: Müşteri sistemde kayıtlı olmalı

## 🔄 Adım Adım Akış
```mermaid
sequenceDiagram
    participant Müşteri
    participant Sentiric
    Müşteri->>Sentiric: "Randevu almak istiyorum"
    Sentiric->>Müşteri: "Hangi hizmet için? (Dişçi/Estetik vb.)"
    Müşteri->>Sentiric: "Diş temizliği"
    Sentiric->>Müşteri: "Uygun tarihler: 15 Mart 10:00 veya 16 Mart 14:00"
```

## 💎 Özel Özellikler
- **Hızlı Komut**: "Yarın öğlen" → Otomatik saat önerisi
- **İptal**: SMS'teki linkle 1 tıkla iptal


---