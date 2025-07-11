# 📚 Bilgi Alma Rehberi

## 🔍 Sık Sorulanlar
```mermaid
mindmap
  root((Bilgi Türleri))
    Çalışma_Saatleri
      "Hafta içi 09:00-18:00"
    Fiyatlandırma
      "Standart kontrol: 200₺"
    Lokasyon
      "Merkez Şube: Cumhuriyet Cd. No:15"
```

## 🎯 Örnek Akışlar
**Fiyat Sorgulama**  
> Müşteri: "Diş beyazlatma ücreti ne kadar?"  
> Sentiric: "Standart beyazlatma 1500₺, VIP paket 2500₺"  

**Çalışma Saatleri**  
> Müşteri: "Pazar açık mısınız?"  
> Sentiric: "Pazar kapalıyız, cumartesi 10:00-15:00 açığız"  

**Ulaşım Bilgisi**  
> Müşteri: "Adresinizi alabilir miyim?"  
> Sentiric: "Ana şubemiz: Levent Mah. Teknopark No:3. *SMS olarak gönderdim* 📍"

## 🧠 Bilgi Alma Mimarisi: RAG (Retrieval-Augmented Generation)

Sistem, "Çalışma saatleriniz nedir?" gibi soruları if-else bloklarıyla değil, modern bir AI mimarisiyle cevaplar. Bu, bilgi bankasının kolayca güncellenmesini ve sistemin sürekli öğrenmesini sağlar.

```mermaid
sequenceDiagram
    autonumber
    participant User as "Kullanıcı (Soruyu sorar)"
    participant Worker as "Agent Worker"
    participant VectorDB as "Vektör Veritabanı (Bilgi Hafızası)"
    participant LLM as "Büyük Dil Modeli (Akıl Yürütme)"

    User->>Worker: "Pazar günleri açık mısınız?"
    
    Worker->>VectorDB: "Pazar çalışma saatleri" (Anlamsal Arama Sorgusu)
    VectorDB-->>Worker: İlgili Bilgi Parçaları: <br>1. "Hafta içi: 09:00-18:00" <br>2. "Cumartesi: 10:00-15:00" <br>3. "Pazar günleri kapalıyız."
    
    Worker->>LLM: **Prompt:** <br> Context: [Yukarıdaki bilgi parçaları] <br> Soru: "Pazar günleri açık mısınız?" <br> Cevapla:
    LLM-->>Worker: "Pazar günleri kapalıyız, ancak Cumartesi günleri 10:00 ile 15:00 arasında hizmet vermekteyiz."
    
    Worker->>User: (TTS ile) "Pazar günleri kapalıyız, ancak Cumartesi..."
```
---