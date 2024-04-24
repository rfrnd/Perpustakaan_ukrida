from abc import ABC, abstractmethod

class Pengguna:
    def __init__(self, email, kata_sandi):
        self.email = email
        self.__kata_sandi = kata_sandi
        self.status_masuk = False

    def masuk(self, kata_sandi):
        if kata_sandi == self.__kata_sandi:
            self.status_masuk = True
            print("Berhasil masuk ke sistem.")
        else:
            self.status_masuk = False
            print("Kata sandi salah. Gagal masuk ke sistem.")
            
    def keluar(self):
        self.masuk = False
        print("Keluar dari sistem.")

    def ubah_kata_sandi(self, kata_sandi_lama, kata_sandi_baru):
        if kata_sandi_lama == self.__kata_sandi:
            self.__kata_sandi = kata_sandi_baru
            print("Kata sandi berhasil diubah.")
        else:
            print("Kata sandi lama salah. Gagal mengubah kata sandi.")

class Anggota(Pengguna):
    def __init__(self, email, kata_sandi):
        super().__init__(email, kata_sandi)
        self.buku_dipinjam = []
        self.riwayat_peminjaman = []

    def pencarian_buku(self, kata_kunci):
        print("Melakukan pencarian buku dengan kata kunci:", kata_kunci)

    def pinjam_buku(self, id_buku):
        print("Meminjam buku dengan ID:", id_buku)

    def kembalikan_buku(self, id_buku):
        print("Mengembalikan buku dengan ID:", id_buku)

    def lihat_riwayat_peminjaman(self):
        print("Melihat riwayat peminjaman anggota.")

    def lihat_buku_dipinjam(self):
        print("Melihat daftar buku yang sedang dipinjam.")

class Pustakawan(Pengguna):
    def __init__(self, email, kata_sandi):
        super().__init__(email, kata_sandi)
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print("Buku baru berhasil ditambahkan ke katalog.")

    def hapus_buku(self, id_buku):
        for buku in self.daftar_buku:
            if buku.id == id_buku:
                self.daftar_buku.remove(buku)
                print("Buku dengan ID", id_buku, "telah dihapus dari katalog.")
                return
        print("Buku dengan ID", id_buku, "tidak ditemukan dalam katalog.")

    def perbarui_detail_buku(self, id_buku, judul_baru, penulis_baru, subjek_baru):
        for buku in self.daftar_buku:
            if buku.id == id_buku:
                buku.judul = judul_baru
                buku.penulis = penulis_baru
                buku.subjek = subjek_baru
                print("Detail buku dengan ID", id_buku, "telah diperbarui.")
                return
        print("Buku dengan ID", id_buku, "tidak ditemukan dalam katalog.")

class Admin(Pengguna):
    def __init__(self, email, kata_sandi):
        super().__init__(email, kata_sandi)
        self.id_admin = email

    def kelola_akun_pengguna(self):
        print("Menu Kelola Akun Pengguna")
        print("1. Tambah akun pengguna")
        print("2. Hapus akun pengguna")
        print("3. Perbarui informasi akun pengguna")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            self.tambah_akun_pengguna()
        elif pilihan == "2":
            self.hapus_akun_pengguna()
        elif pilihan == "3":
            self.perbarui_informasi_akun_pengguna()
        else:
            print("Pilihan tidak valid.")

    def tambah_akun_pengguna(self):
        print("Tambah akun pengguna")
        pass

    def hapus_akun_pengguna(self):
        print("Hapus akun pengguna")
        pass

    def perbarui_informasi_akun_pengguna(self):
        print("Perbarui informasi akun pengguna")
        pass

    def generate_laporan(self):
        print("Menu Generate Laporan")
        print("1. Laporan peminjaman buku")
        print("2. Laporan pengembalian buku")
        print("3. Laporan inventaris buku")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            self.laporan_peminjaman_buku()
        elif pilihan == "2":
            self.laporan_pengembalian_buku()
        elif pilihan == "3":
            self.laporan_inventaris_buku()
        else:
            print("Pilihan tidak valid.")

    def laporan_peminjaman_buku(self):
        print("Laporan peminjaman buku")
        pass

    def laporan_pengembalian_buku(self):
        print("Laporan pengembalian buku")
        pass

    def laporan_inventaris_buku(self):
        print("Laporan inventaris buku")
        pass

    def awasi_operasi_sistem(self):
        print("Menu Awasi Operasi Sistem")
        print("1. Awasi aktivitas pengguna")
        print("2. Awasi kinerja sistem")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            self.awasi_aktivitas_pengguna()
        elif pilihan == "2":
            self.awasi_kinerja_sistem()
        else:
            print("Pilihan tidak valid.")

    def awasi_aktivitas_pengguna(self):
        print("Awasi aktivitas pengguna")
        pass

    def awasi_kinerja_sistem(self):
        print("Awasi kinerja sistem")
        pass
