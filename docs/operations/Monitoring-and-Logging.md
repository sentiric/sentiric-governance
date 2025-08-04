# 📊 Sentiric: Gözlemlenebilirlik Stratejisi

Bu doküman, platformun sağlığını, performansını ve davranışını anlamak için kullandığımız stratejinin üst düzey bir özetini sunar. Felsefemiz: **"Ölçemediğin şeyi iyileştiremezsin."**

## Gözlemlenebilirlik Standardı

Platformumuzdaki tüm servisler, `sentiric-governance` reposunda tanımlanan **[Sentiric Gözlemlenebilirlik Standardı](./../engineering/OBSERVABILITY_STANDARD.md)** belgesine uymak zorundadır.

Bu standart, gözlemlenebilirliğin üç temel sacayağını detaylandırır:

1.  **Yapılandırılmış Loglama:** Geliştirme ortamında insan tarafından okunabilir, üretim ortamında ise makine tarafından işlenebilir (JSON) loglama.
2.  **Metrikler:** Prometheus formatında toplanan ve Grafana ile görselleştirilen sistem, uygulama ve iş metrikleri.
3.  **Dağıtık İzleme (Distributed Tracing):** OpenTelemetry standardını kullanarak bir isteğin platform içindeki tüm yolculuğunu takip etme.

Bu üç bileşen, platformun hem geliştirme hem de operasyon aşamalarında proaktif bir şekilde izlenmesini, sorunların hızla tespit edilmesini ve performansın sürekli olarak iyileştirilmesini sağlar.

Teknik detaylar, zorunlu log alanları ve standartlaştırılmış kütüphaneler için lütfen ana standart belgesine başvurun.