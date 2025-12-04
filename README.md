# Mini Pipeline CI/CD - Tugas Kelompok 🚀

Repository ini dibuat untuk memenuhi tugas mata kuliah [Nama Mata Kuliah] mengenai implementasi **Continuous Integration / Continuous Delivery (CI/CD)** sederhana.

Proyek ini mendemonstrasikan otomatisasi pengujian kode menggunakan **GitHub Actions**.

## 👥 Anggota Kelompok

1. **Nazwa Alyssa Fauzia** - [NIM]
2. **Camelia Nurazizah** - [NIM]
3. **Siti Maefaulan** - [NIM]

---

## 📋 Deskripsi Proyek

Kami merancang simulasi pipeline pengujian untuk aplikasi kalkulator Python sederhana. Setiap kali ada kode baru yang di-*push* ke repository, sistem akan secara otomatis:

1. Menyiapkan lingkungan (Environment) Ubuntu & Python.
2. Menjalankan Unit Test (`test_app.py`).
3. Membuat laporan hasil tes (Log/Artifact).

## 🛠️ Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python 3.9
* **Testing Framework:** Unittest (Built-in Python)
* **CI Tool:** GitHub Actions
* **VCS:** Git & GitHub

---

## 📂 Struktur Repository

```text
my-mini-pipeline/
├── .github/workflows/
│   └── ci-test.yml    # Konfigurasi Pipeline (YAML)
├── app.py             # Kode Aplikasi Utama
├── test_app.py        # Script Pengujian Otomatis
└── README.md          # Dokumentasi Proyek
```
