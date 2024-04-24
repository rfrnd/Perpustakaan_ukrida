import datetime

class Peminjaman:
    def __init__(self, id_peminjaman, id_buku, id_anggota, tanggal_peminjaman):
        self.id_peminjaman = id_peminjaman
        self.id_buku = id_buku
        self.id_anggota = id_anggota
        self.tanggal_peminjaman = tanggal_peminjaman
        self.tanggal_jatuh_tempo = tanggal_peminjaman + datetime.timedelta(days=7)

    def hitung_denda(self):
        tanggal_kembali = datetime.datetime.now()
        if tanggal_kembali > self.tanggal_jatuh_tempo:
            selisih_hari = (tanggal_kembali - self.tanggal_jatuh_tempo).days
            denda = selisih_hari * 1000 
            return denda
        else:
            return 0
