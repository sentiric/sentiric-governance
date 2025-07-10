# 🆘 Acil Durum Protokolü

## 🚑 Kritik Adımlar
1. Müşteri "acil" veya "yardım" kelimesini kullanır
2. Sistem otomatik olarak:
   ```mermaid
   graph TD
       A[Acil çağrı] --> B{Konum bilgisi var mı?}
       B -->|Evet| C[En yakın hastane bilgisi]
       B -->|Hayır| D[Genel acil numaraları]
   ```
3. Eş zamanlı olarak:
   - Yetkili personele uyarı gider
   - Otomatik konum paylaşımı istenir

## 📞 Örnek Diyalog
> Müşteri: "*Kalp krizi geçiriyorum!*"  
> Sentiric: "ACİL DURUM! En yakın hastane: MedicalPark Bahçelievler. 112'yi aradım. Konumunuzu paylaşabilir misiniz? 🚑"  
> *Sistem otomatik olarak 112'yi arar ve konum bilgisini iletir*

---