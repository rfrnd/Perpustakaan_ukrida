class Buku:
    def __init__(self, id_buku, judul, penulis, subjek, ISBN, ketersediaan=True):
        self.id_buku = id_buku
        self.judul = judul
        self.penulis = penulis
        self.subjek = subjek
        self.ISBN = ISBN
        self.ketersediaan = ketersediaan

    @staticmethod
    def cari_judul_buku(daftar_buku, judul):
        hasil_pencarian = []
        for buku in daftar_buku:
            if judul.lower() in buku.judul.lower():
                hasil_pencarian.append(buku)
        return hasil_pencarian

    @staticmethod
    def cari_penulis_buku(daftar_buku, penulis):
        hasil_pencarian = []
        for buku in daftar_buku:
            if penulis.lower() in buku.penulis.lower():
                hasil_pencarian.append(buku)
        return hasil_pencarian

    @staticmethod
    def cari_subjek_buku(daftar_buku, subjek):
        hasil_pencarian = []
        for buku in daftar_buku:
            if subjek.lower() in buku.subjek.lower():
                hasil_pencarian.append(buku)
        return hasil_pencarian