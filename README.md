# 🛡️ Keylogger Edukatif — Python

> ⚠️ **PERINGATAN**  
> Proyek ini dibuat hanya untuk **tujuan pembelajaran & riset keamanan siber**. Penggunaan pada perangkat atau sistem tanpa izin tertulis adalah **ilegal** dan dapat dikenai sanksi hukum. Jalankan hanya pada **lingkungan lab uji** atau komputer pribadi.

![Badge Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Badge License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Badge Status](https://img.shields.io/badge/Status-Educational-orange?style=for-the-badge)
![Badge Ethical](https://img.shields.io/badge/Usage-Ethical%20Only-red?style=for-the-badge)

---

## 📚 Daftar Isi

- [📖 Tentang Proyek](#-tentang-proyek)
- [✨ Fitur](#-fitur)
- [🧰 Teknologi](#-teknologi)
- [📂 Struktur Proyek](#-struktur-proyek)
- [🚀 Instalasi & Penggunaan](#-instalasi--penggunaan)
- [⚖️ Etika & Legalitas](#️-etika--legalitas)
- [📜 Lisensi](#-lisensi)
- [👤 Pembuat](#-pembuat)

---

## 📖 Tentang Proyek

Proyek ini adalah contoh implementasi **keylogger dasar berbasis Python** yang digunakan untuk:
- Demonstrasi teknik perekaman input keyboard.  
- Latihan deteksi aktivitas keylogging.  
- Pengujian sistem keamanan lokal.

Script ini akan mencatat setiap penekanan tombol secara real-time dan mengirimkan log ke alamat email yang telah dikonfigurasi — fitur ini dimaksudkan sebagai simulasi skenario serangan untuk keperluan pelatihan.

> 🧠 Tujuannya bukan untuk eksploitasi, melainkan untuk **memahami cara kerja ancaman** agar dapat membuat sistem pertahanan yang lebih kuat.

---

## ✨ Fitur

- ⌨️ **Key Logging Real-time** — Mencatat input keyboard lengkap dengan timestamp.  
- 📨 **Pengiriman Log via Email (SMTP)** — Log otomatis dikirim secara periodik.  
- 🕒 **Timer Otomatis** — Interval pengiriman log dapat disesuaikan.  
- 🔒 **Konfigurasi Gmail App Password** untuk autentikasi aman.  
- 🧪 Dirancang untuk digunakan di **lab uji / sandbox**.

---

## 🧰 Teknologi

| Komponen         | Deskripsi                                                                 |
|------------------|----------------------------------------------------------------------------|
| Python 3.x       | Bahasa utama yang digunakan                                               |
| `keyboard`       | Merekam event penekanan tombol                                           |
| `smtplib`       | Mengirim email log melalui SMTP Gmail                                    |
| `email.mime`    | Format pesan email (MIMEText & MIMEMultipart)                             |
| `threading.Timer` | Menjadwalkan pengiriman log secara berkala                              |
| `datetime`      | Mencatat waktu setiap keystroke                                          |

---

## 📂 Struktur Proyek

```
keylogger-edu/
├── keylogger.py        # Script utama edukatif
└── README.md           # Dokumentasi proyek
```

---

## 🚀 Instalasi & Penggunaan

> ⚠️ Gunakan hanya pada sistem pribadi atau lab uji virtual (VM).

1. **Clone Repositori**
   ```bash
   git clone https://github.com/giska-15/keylogger.git
   cd keylogger
   ```

2. **Instal Dependensi**
   ```bash
   pip install keyboard
   ```

3. **Konfigurasi Email**  
   - Aktifkan 2FA pada akun Gmail.  
   - Buat *App Password* dan salin ke variabel `EMAIL_PASS` di `keylogger.py`.  
   - Sesuaikan alamat penerima.

4. **Jalankan Program**
   ```bash
   python3 keylogger.py
   ```

5. **Monitor Hasil Log**  
   Log akan dikirim secara berkala ke alamat email yang telah ditentukan.

---

## ⚖️ Etika & Legalitas

Keylogger termasuk perangkat lunak sensitif. Penggunaannya diatur oleh hukum siber di banyak negara.

✅ **Legal jika digunakan untuk:**
- Penetration testing dengan izin tertulis.  
- Riset keamanan siber di lab pribadi.  
- Pendidikan / pelatihan etis.

❌ **Ilegal jika digunakan untuk:**
- Memata-matai pengguna lain tanpa persetujuan.  
- Mencuri data pribadi atau kredensial.  
- Aktivitas hacking tanpa izin.

> ❗ Pelanggaran dapat berakibat pada tuntutan pidana dan perdata.

---

## 📜 Lisensi

Lisensi: **MIT License**  
Proyek ini hanya untuk keperluan pembelajaran & penelitian keamanan siber. Penulis tidak bertanggung jawab atas penyalahgunaan di luar konteks edukatif.

---

## 👤 Pembuat

**Giska Aura Muhamad Prasetyo**  
🔸 Security Enthusiast • Python Developer  
🌐 [GitHub](https://github.com/giska-15) | 💼 [LinkedIn](https://www.linkedin.com/in/giska-aura-muhamad-prasetyo-a90459319?utm_source=share_via&utm_content=profile&utm_medium=member_android)

---

> “Menguasai teknik ofensif adalah kunci untuk membangun pertahanan yang kuat.” 🧠
