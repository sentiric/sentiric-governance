# 📦 Ön Rezervasyon Akışı

## 🎯 Kullanım Senaryosu
- **Kimler Kullanır?**: Yeni müşteriler, Grup rezervasyonları
- **Ön Koşul**: Minimum 24 saat önceden yapılmalı

## 🔄 Adım Adım Akış
```mermaid
flowchart TB
    A["Müşteri: 'Ön rezervasyon yaptırmak istiyorum'"] --> B[Sistem esnek tarih seçeneklerini sunar]
    B --> C{"Müşteri tarih seçer"}
    C -->|Onay| D[Rezervasyon kodu SMS ile gönderilir]
```

## ⚠️ Dikkat Edilecekler
- Kesin tarih 48 saat içinde belirlenmeli
- İptal ücretsiz


---