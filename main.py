from pengguna import Anggota, Pustakawan, Admin
from buku import Buku
from peminjaman import Peminjaman

def menu_login():
    print("=== Menu Masuk ===")
    email = input("Masukkan email: ")
    kata_sandi = input("Masukkan kata sandi: ")

    if email in database_pengguna:
        pengguna = database_pengguna[email]
        pengguna.masuk(kata_sandi) 
        if pengguna.status_masuk:
            if isinstance(pengguna, Anggota):
                menu_anggota(pengguna)
            elif isinstance(pengguna, Pustakawan):
                menu_pustakawan(pengguna)
            elif isinstance(pengguna, Admin):
                menu_admin(pengguna)
        else:
            print("Email atau kata sandi salah. Gagal masuk ke sistem.")
    else:
        print("Email atau kata sandi salah. Gagal masuk ke sistem.")


def menu_anggota(anggota):
    print("=== Menu Anggota ===")
    print("1. Pencarian Buku")
    print("2. Pinjam Buku")
    print("3. Kembalikan Buku")
    print("4. Lihat Riwayat Peminjaman")
    print("5. Lihat Buku yang Dipinjam")
    pilihan = input("Pilih opsi (1-5): ")

    if pilihan == "1":
        kata_kunci = input("Masukkan kata kunci untuk pencarian buku: ")
        anggota.pencarian_buku(kata_kunci)
    elif pilihan == "2":
        id_buku = input("Masukkan ID buku yang ingin dipinjam: ")
        anggota.pinjam_buku(id_buku)
    elif pilihan == "3":
        id_buku = input("Masukkan ID buku yang ingin dikembalikan: ")
        anggota.kembalikan_buku(id_buku)
    elif pilihan == "4":
        anggota.lihat_riwayat_peminjaman()
    elif pilihan == "5":
        anggota.lihat_buku_dipinjam()
    else:
        print("Pilihan tidak valid.")

def menu_pustakawan(pustakawan):
    print("=== Menu Pustakawan ===")
    print("1. Tambah Buku")
    print("2. Hapus Buku")
    print("3. Perbarui Detail Buku")
    print("4. Lihat Daftar Buku")
    pilihan = input("Pilih opsi (1-4): ")

    if pilihan == "1":
        id_buku = input("Masukkan ID buku: ")
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")
        subjek = input("Masukkan subjek buku: ")
        ISBN = input("Masukkan ISBN buku: ")
        buku_baru = Buku(id_buku, judul, penulis, subjek, ISBN)
        pustakawan.tambah_buku(buku_baru)
    elif pilihan == "2":
        id_buku = input("Masukkan ID buku yang ingin dihapus: ")
        pustakawan.hapus_buku(id_buku)
    elif pilihan == "3":
        id_buku = input("Masukkan ID buku yang ingin diperbarui: ")
        judul_baru = input("Masukkan judul baru: ")
        penulis_baru = input("Masukkan penulis baru: ")
        subjek_baru = input("Masukkan subjek baru: ")
        pustakawan.perbarui_detail_buku(id_buku, judul_baru, penulis_baru, subjek_baru)
    elif pilihan == "4":
        print("Daftar Buku:")
        for buku in pustakawan.daftar_buku:
            print(f"ID: {buku.id_buku}, Judul: {buku.judul}, Penulis: {buku.penulis}, Subjek: {buku.subjek}")
    else:
        print("Pilihan tidak valid.")

def menu_admin(admin):
    print("=== Menu Admin ===")
    print("1. Kelola Akun Pengguna")
    print("2. Generate Laporan")
    print("3. Awasi Operasi Sistem")
    pilihan = input("Pilih opsi (1-3): ")

    if pilihan == "1":
        admin.kelola_akun_pengguna()
    elif pilihan == "2":
        admin.generate_laporan()
    elif pilihan == "3":
        admin.awasi_operasi_sistem()
    else:
        print("Pilihan tidak valid.")

database_pengguna = {
    "anggota": Anggota("anggota", "anggota1"),
    "pustakawan": Pustakawan("pustakawan", "pustakawan1"),
    "admin": Admin("admin", "admin1")
}

if __name__ == "__main__":
    menu_login()
