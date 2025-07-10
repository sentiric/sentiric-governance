# 💻 Sentiric: Kodlama Standartları

Bu doküman, Sentiric ekosistemindeki tüm kod tabanının tutarlı, okunabilir, sürdürülebilir ve yüksek kalitede kalmasını sağlamak için benimsediğimiz geliştirme standartlarını tanımlar.

## 1. Python Standartları

*   **Formatlama:** Tüm Python kodu, `black` formatlayıcısı ile formatlanmalıdır. Ayarlar `pyproject.toml` dosyasında belirtilecektir.
*   **Linting:** Tüm Python kodu, `Ruff` linter'ı ile denetlenmelidir. `Ruff`, `flake8`, `isort` ve birçok diğer popüler linter'ın yerini alan, son derece hızlı ve kapsamlı bir araçtır.
*   **Tip İpuçları (Type Hinting):** Tüm fonksiyon ve metot imzaları, `Python 3.10+` standartlarına uygun tip ipuçları içermelidir. Kod tabanı, `mypy --strict` modunda hatasız doğrulanabilmelidir.
*   **Dokümantasyon (Docstrings):** Tüm public modüller, sınıflar, fonksiyonlar ve metotlar, `Google Style` docstring formatına uygun dokümantasyon içermelidir.
*   **İsimlendirme:**
    *   Değişkenler ve fonksiyonlar: `snake_case` (örn: `calculate_total_price`).
    *   Sınıflar: `PascalCase` (örn: `RestaurantReservationTask`).
    *   Sabitler: `UPPER_SNAKE_CASE` (örn: `DEFAULT_TIMEOUT`).

## 2. TypeScript/React Standartları

*   **Formatlama:** Tüm `.ts`, `.tsx`, `.js`, `.jsx` kodları `Prettier` ile formatlanmalıdır.
*   **Linting:** `ESLint`, React ve TypeScript için önerilen kurallarla yapılandırılacaktır.
*   **Bileşen Yapısı:** Bileşenler, kendi klasörlerinde, stil dosyaları (`.module.css`) ve test dosyalarıyla birlikte bulunmalıdır. (örn: `/components/Button/index.tsx`, `/components/Button/Button.module.css`, `/components/Button/Button.test.tsx`).
*   **CSS:** Global stiller minimumda tutulacak, bileşenlere özel stiller için **CSS Modülleri** kullanılacaktır.

## 3. Genel Standartlar

*   **Commit Mesajları:** Tüm commit'ler **[Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)** standardına uymalıdır. Bu, otomatik versiyonlama ve `CHANGELOG` oluşturma için zorunludur.
*   **Branch İsimlendirme:**
    *   Yeni özellikler: `feat/kisa-ozellik-adi` (örn: `feat/add-google-calendar-adapter`)
    *   Hata düzeltmeleri: `fix/issue-numarasi` (örn: `fix/123-telephony-latency`)
    *   Refaktör: `refactor/iyilestirilecek-alan` (örn: `refactor/simplify-agent-loop`)

---
