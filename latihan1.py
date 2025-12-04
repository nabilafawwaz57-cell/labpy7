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


# =============================
# Program Utama (Menu)
# =============================
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
