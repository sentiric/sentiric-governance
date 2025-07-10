# 🗺️ Sentiric: Ekosistem ve Repolar

Sentiric platformu, her biri belirli bir sorumluluğa sahip, bağımsız olarak geliştirilen ve yönetilen bir dizi depodan (repository) oluşur.

## 1. Yönetim

| Repo | Sorumluluk |
| :--- | :--- |
| **`sentiric-governance`** | Projenin anayasası. Vizyon, mimari, yol haritası ve standartları barındırır. **Bu repo.** |

## 2. Çekirdek Kütüphaneler (Platformun DNA'sı)

| Repo | Sorumluluk | Teknoloji |
| :--- | :--- | :--- |
| **`sentiric-core-interfaces`** | Tüm "Tak-Çıkar" bileşenlerin uyması gereken soyut arayüzleri (`BaseTask`, `BaseLLM` vb.) tanımlar. | Python |
| **`sentiric-task-framework`** | Belirli iş akışlarını (`RestaurantReservationTask` gibi) tanımlayan, `BaseTask`'tan türemiş somut görev sınıflarını içerir. | Python |

## 3. Adaptör Kütüphaneleri (Dış Dünya ile Konuşma)

| Repo | Sorumluluk | Teknoloji |
| :--- | :--- | :--- |
| **`sentiric-connectors`** | Harici **konuşma servisleri** (ASR, TTS, LLM) için adaptörleri barındırır. (örn: `GoogleGeminiAdapter`). | Python |
| **`sentiric-resources`** | Harici **iş mantığı sistemleri** (Veritabanı, Takvim, Ödeme) için adaptörleri barındırır. (örn: `GoogleCalendarAdapter`). | Python |

## 4. Platform Servisleri (Uygulama Katmanı)

| Repo | Sorumluluk | Teknoloji |
| :--- | :--- | :--- |
| **`sentiric-agent-worker`** | Her arama için Ajan sürecini başlatan, adaptörleri ve görevleri orkestre eden ana işçi servis. | Python, FastAPI |
| **`sentiric-telephony-gateway`** | Telefoni sağlayıcılarından gelen/giden ses akışını yöneten ağ geçidi. | Python, FastAPI, WebSockets |
| **`sentiric-api-server`** | Dashboard için RESTful API sunan, veritabanı işlemlerini ve kullanıcı yönetimini yürüten servis. | Python, FastAPI |
| **`sentiric-dashboard`** | Kullanıcıların aramaları, görevleri ve analizleri görüntülediği web tabanlı yönetim paneli. | React, Vite, TypeScript |
| **`sentiric-db-models`** | Tüm servisler tarafından paylaşılan veritabanı modellerini ve `Alembic` migrasyonlarını içerir. | Python, SQLAlchemy |


## 5. Opsiyonel "In-House" Motorlar (Gelecek Fazlar)

| Repo | Sorumluluk | Teknoloji |
| :--- | :--- | :--- |
| **`sentiric-voice-engine`** | Kendi ASR (Whisper tabanlı) ve TTS (HiFi-GAN tabanlı) motorlarımızı barındıran repo. | Python, PyTorch |

---
