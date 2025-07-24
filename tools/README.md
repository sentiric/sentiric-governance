# Snapshot Aracı

Bu dizin, ekosisteminin tamamının anlık görüntülerini (snapshot) almak ve yönetmek için kullanılan `snapshot_tool.py` aracını içerir.

## Genel Bakış

`snapshot_tool.py`, tüm AzuraForge "kardeş repo"larını tarayarak, projenin o anki durumunu tek bir metin dosyasına paketleyen güçlü bir komut satırı aracıdır. Bu dosya, projenin kod tabanını paylaşmak, analiz etmek, AI modellerine girdi olarak sunmak veya yedeklemek için idealdir.

Araç iki ana komut üzerine kuruludur:
*   `collect`: Proje dosyalarını tarar ve tek bir snapshot dosyası oluşturur.
*   `restore`: Bir snapshot dosyasından proje yapısını geri yükler.

---

## Kurulum ve Konum

Araç, projenin `sentric-governance` reposu içinde yer alır ve herhangi bir ek bağımlılık gerektirmez. Komutları çalıştırırken `sentric-governance` dizininde olmanız tavsiye edilir.

---

## Kullanım Örnekleri

Aşağıdaki tüm örneklerde, proje yapınızın şu şekilde olduğu varsayılmıştır:

```
/path/to/your/workspace/  <-- Projenin ana çalışma alanı
├── sentric-governance/
│   └── tools/
│       └── snapshot_tool.py
├── api/
├── core/
└── ...diğer repolar
```

Tüm komutlar, terminalde `/path/to/your/workspace/sentric-governance/` dizinindeyken çalıştırılmalıdır.

### 1. Temel Snapshot Oluşturma (Tavsiye Edilen Yöntem)

Bu komut, projenin ana çalışma alanını (`../`) tarar ve varsayılan ayarlarla (`.py`, `.js`, `.md` vb. dahil, `__pycache__`, `node_modules` vb. hariç) bir snapshot oluşturur.

```bash
# .../sentric-governance/ dizinindeyken:
python tools/snapshot_tool.py collect ../sentric.txt --base-dir ../
```
*   **Sonuç:** `.../sentric-governance/project_snapshot.txt` dosyası oluşturulur.

### 2. Gelişmiş Snapshot Oluşturma (Özel Kurallar)

Sadece belirli dizinleri veya dosya uzantılarını dahil etmek ve özel dışlama kuralları eklemek için:

```bash
# Sadece `api` ve `core` repolarını, sadece `.py` ve `.md` dosyalarını al
python tools/snapshot_tool.py collect api_core_snapshot.txt --base-dir ../ \
    --include-dir ../api \
    --include-dir ../core \
    --include-ext .py \
    --include-ext .md \
    --exclude-pattern tests
```

### 3. Yorumları Temizleyerek Snapshot Alma

Kod dosyalarındaki yorum satırlarını kaldırarak daha temiz ve daha küçük bir snapshot oluşturmak için `--clean-comments` bayrağını kullanın. Bu, AI modellerine girdi hazırlarken faydalıdır.

```bash
# Yorumsuz bir snapshot oluştur
python tools/snapshot_tool.py collect clean_snapshot.txt --base-dir ../ --clean-comments
```

### 4. Snapshot'tan Geri Yükleme

Oluşturulmuş bir `project_snapshot.txt` dosyasından tüm projeyi geri yüklemek için:

```bash
# 1. Geri yüklenecek snapshot dosyasının .../sentric-governance/ içinde olduğundan emin olun.
# 2. .../sentric-governance/ dizinindeyken aşağıdaki komutu çalıştırın.

# Bu komut, dosyaları bir üst dizine (ana çalışma alanına) geri yükleyecektir.
python tools/snapshot_tool.py restore project_snapshot.txt --target-dir ../
```

Mevcut dosyaların üzerine yazmak isterseniz `--overwrite` bayrağını ekleyin:

```bash
python tools/snapshot_tool.py restore project_snapshot.txt --target-dir ../ --overwrite
```

### 5. "Ne Dahil Edilecek?" Kontrolü (Dry Run)

Snapshot oluşturmadan önce hangi dosyaların dahil edileceğini listelemek için (dosya yazma işlemi yapmaz):

```bash
# Bu komut, snapshot_tool.py'nin --dry-run argümanını desteklediğini varsayar.
python tools/snapshot_tool.py collect test.txt --base-dir ../ --dry-run
```

---

## Aracın Yetenekleri

*   **`collect` komutu:**
    *   Var olmayan dizinler için uyarı gösterir.
    *   İşlem sonunda toplam kaç dosyanın dahil edildiğini raporlar.
    *   Tüm dosya içeriğini tam olarak korur (veya `--clean-comments` ile yorumları temizler).
    *   Kardeş repo yapısıyla tam uyumlu çalışır.

*   **`restore` komutu:**
    *   Geri yüklenen her dosya için detaylı ilerleme bilgisi gösterir.
    *   İşlem sonunda geri yüklenen/atlanan dosyaların bir özetini sunar.
    *   Gerekli dizin yapısını otomatik olarak oluşturur.

**Unutmayın:** Aracın varsayılan ayarları, en yaygın geliştirme dosyalarını dahil edip, derleme çıktılarını, bağımlılık klasörlerini ve geçici dosyaları hariç tutacak şekilde yapılandırılmıştır. Çoğu durumda, **"Temel Snapshot Oluşturma"** bölümündeki komut yeterli olacaktır.