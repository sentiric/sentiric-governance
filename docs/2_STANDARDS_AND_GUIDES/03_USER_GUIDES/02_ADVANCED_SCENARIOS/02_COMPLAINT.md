# 📢 Şikayet Yönetimi

## 🔄 İşlem Akışı
```mermaid
flowchart TB
    A[Şikayet Algılandı] --> B{"Şikayet Türü?"}
    B -->|Ürün| C[Ürün ekibine yönlendir]
    B -->|Hizmet| D[Müdür onayına gönder]
    B -->|Acil| E[Anlık müdahale ekibini uyar]
```

## ✨ Örnek Çözümler
**Senaryo 1 - Basit Şikayet**  
> Müşteri: "Randevuma geç kaldılar!"  
> Sentiric: "Üzgünüz, 50₺ indirim kuponu gönderdim. Kabul eder misiniz?"  

**Senaryo 2 - Karmaşık Şikayet**  
> Müşteri: "Yanlış tedavi uygulandı!"  
> Sentiric: "Hukuk ekibimiz 15 dakika içinde sizi arayacak. *Dosya no: SHK-2024-456*"
```

---