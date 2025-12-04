# labpy7

Nama      : Nabila Fawwaz Nurliah

NIM       : 312510255

Kelas     : TI.25.A.2

MATKUL    : Pengantar Pemograman

Dosen     : Agung Nugroho, S.Kom., M.Kom.

Pertemuan : 12

# Program Daftar Nilai Mahasiswa (Menggunakan Class Python)

Repository ini berisi program sederhana untuk menampilkan daftar nilai mahasiswa dengan menggunakan konsep **OOP (Object-Oriented Programming)** di Python. Program ini dibuat sesuai instruksi tugas:

- Menggunakan class untuk menyimpan dan mengelola data mahasiswa.
- Memiliki method:
  - `tambah()` untuk menambah data mahasiswa
  - `tampilkan()` untuk menampilkan semua data
  - `hapus(nama)` untuk menghapus data berdasarkan nama
  - `ubah(nama)` untuk mengubah nilai mahasiswa berdasarkan nama
- Menyertakan **class diagram**, **flowchart**, dan **penjelasan program**.

---

## 📌 1. Deskripsi Program

Program ini merupakan aplikasi berbasis console untuk menyimpan, menampilkan, menghapus, dan mengubah data nilai mahasiswa.  
Data disimpan dalam bentuk list berisi dictionary (`{"nama": ..., "nilai": ...}`).

Program dibuat dengan pendekatan **OOP** agar lebih terstruktur, mudah dikembangkan, dan mudah dimengerti.

---

## 📌 2. Class Diagram

```
+---------------------------+
| DaftarNilaiMahasiswa |
+---------------------------+
| - data: list |
+---------------------------+
| + tambah() |
| + tampilkan() |
| + hapus(nama) |
| + ubah(nama) |
+---------------------------+
```

## 📌 3. Flowchart Program

```
          ┌───────────────┐
          │   Mulai       │
          └───────┬───────┘
                  │
          ┌───────▼────────┐
          │   Tampilkan    │
          │      Menu      │
          └───────┬────────┘
                  │
      ┌───────────┼─────────────────────┐
      │           │                     │
 ┌────▼───┐  ┌────▼────┐         ┌──────▼─────┐
 │Tambah  │  │Tampilkan│         │ Hapus Data │
 └────┬───┘  └────┬────┘         └──────┬─────┘
      │           │                     │
      └───────────┼────────────────────┘
                  │
           ┌──────▼──────┐
           │ Ubah Data   │
           └──────┬──────┘
                  │
          ┌───────▼────────┐
          │ Keluar?        │
          └───────┬────────┘
                  │
          ┌───────▼───────┐
          │ Selesai       │
          └───────────────┘
```

## 📌 4. Source Code (Program Utama)

```python
class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data = []

    def tambah(self):
        print("=== Tambah Data Mahasiswa ===")
        nama = input("Masukkan Nama       : ")
        nilai = float(input("Masukkan Nilai      : "))
        self.data.append({"nama": nama, "nilai": nilai})
        print("Data berhasil ditambahkan!\n")

    def tampilkan(self):
        print("=== Daftar Nilai Mahasiswa ===")
        if not self.data:
            print("Belum ada data.\n")
            return
        for i, mhs in enumerate(self.data, 1):
            print(f"{i}. {mhs['nama']} - Nilai: {mhs['nilai']}")
        print()

    def hapus(self, nama):
        print("=== Hapus Data ===")
        for mhs in self.data:
            if mhs['nama'].lower() == nama.lower():
                self.data.remove(mhs)
                print(f"Data '{nama}' berhasil dihapus!\n")
                return
        print(f"Data dengan nama '{nama}' tidak ditemukan.\n")

    def ubah(self, nama):
        print("=== Ubah Data ===")
        for mhs in self.data:
            if mhs['nama'].lower() == nama.lower():
                nilai_baru = float(input("Masukkan nilai baru: "))
                mhs['nilai'] = nilai_baru
                print(f"Data nilai '{nama}' berhasil diubah!\n")
                return
        print(f"Data dengan nama '{nama}' tidak ditemukan.\n")


if __name__ == "__main__":
    app = DaftarNilaiMahasiswa()

    while True:
        print("=== MENU ===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            app.tambah()
        elif pilihan == "2":
            app.tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama yang ingin dihapus: ")
            app.hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama yang ingin diubah: ")
            app.ubah(nama)
        elif pilihan == "5":
            print("Keluar program...")
            break
        else:
            print("Pilihan tidak valid!\n")
```

## 📌 5. Cara Menjalankan (Run Program)
 
  1. Clone repository:

      ```
      git clone <link-repository-kamu>
      ```   

  2. Masuk folder project:

     ```
     cd <nama-folder>
     ```

  3. Jalankan program:

     ```
     python main.py
     ```

## 📌 6. Penjelasan Fungsi

```
| Method        | Penjelasan                                          |
| ------------- | --------------------------------------------------- |
| `tambah()`    | Menerima input nama & nilai, lalu menyimpan ke list |
| `tampilkan()` | Menampilkan seluruh data mahasiswa                  |
| `hapus(nama)` | Menghapus data berdasarkan nama (case-insensitive)  |
| `ubah(nama)`  | Mengubah nilai mahasiswa berdasarkan nama           |
```

## 📌 7. Contoh Output Program

```
=== MENU ===
1. Tambah Data
2. Tampilkan Data
3. Hapus Data
4. Ubah Data
5. Keluar
Pilih menu: 1

=== Tambah Data Mahasiswa ===
Masukkan Nama : Bila
Masukkan Nilai : 100
Data berhasil ditambahkan!
```

## 📌 8. Commit & Push ke GitHub

```
git add .
git commit -m "Menambahkan program, diagram, flowchart, dan README"
git push origin main
```







