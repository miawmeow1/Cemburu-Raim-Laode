# Cemburu - Raim Laode (Animated Lyrics)

Project sederhana menggunakan **Python** dan **Threading** untuk menampilkan animasi lirik lagu *"Cemburu"* karya **Raim Laode** secara berjalan (*typing / karaoke style*) di terminal.

## 🎵 Tentang Lagu
Lagu **"Cemburu"** karya **Raim Laode** menceritakan tentang perasaan dilema dan galau seseorang yang merasa cemburu melihat orang yang disukainya bersanding atau bergandengan tangan dengan orang lain. Namun, ia menyadari bahwa ia tidak berhak melarang atau menuntut apa pun karena mereka tidak memiliki hubungan resmi (*"kau bukan milikku"*).

> *"Aku cemburu melihat kau bersamanya"*  
> *"Aku cemburu tanganmu digenggam dia"*  
> *"Tapi ku tak tahu mengapa aku cemburu"*  
> *"Kau bukan milikku, kau bukan milikku"*  
> — **Raim Laode**

*Catatan: Untuk menikmati lirik lengkapnya secara resmi, Anda dapat mencarinya melalui pencarian Google.*

---

## 🛠️ Fitur Kode
- **Multi-threading:** Menggunakan modul `threading.Thread` untuk mengatur *timing* (delay) penampilan setiap baris lirik.
- **Thread Lock:** Memanfaatkan `threading.Lock()` agar teks dicetak secara urut tanpa tumpang tindih di terminal.
- **Efek Animasi Teks:** Menggunakan `sys.stdout` dan `time.sleep()` untuk menciptakan efek ketikan per karakter.

---

## 🚀 Cara Menjalankan

### 1. Prasyarat
Pastikan Python sudah terinstal di komputer Anda. Cek dengan perintah:
```bash
python --version
