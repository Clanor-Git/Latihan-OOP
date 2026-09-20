from abc import ABC, abstractmethod

class KamarHotel(ABC):
    def __init__(self, nama_kamar, stok, harga_dasar):
        self.nama_kamar = nama_kamar
        self.__stok = 0
        self.__harga_dasar = harga_dasar
        
        self.tambah_stok(stok)

    def get_stok(self):
        return self.__stok

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama_kamar}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok = self.__stok + jumlah
            print(f"Berhasil menambahkan stok {self.nama_kamar}: {jumlah} unit.")

    def get_harga_dasar(self):
        return self.__harga_dasar

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah_malam):
        pass

class KamarDeluxe(KamarHotel):
    def __init__(self, nama_kamar, stok, harga_dasar, fasilitas):
        super().__init__(nama_kamar, stok, harga_dasar)
        self.fasilitas = fasilitas

    def hitung_harga_total(self, jumlah_malam):
        pajak = 0.10 * self.get_harga_dasar()
        harga_per_malam = self.get_harga_dasar() + pajak
        return harga_per_malam * jumlah_malam

    def tampilkan_detail(self):
        pajak = int(0.10 * self.get_harga_dasar())
        harga_dasar = int(self.get_harga_dasar())
        print(f"[DELUXE] {self.nama_kamar} | Fasilitas: {self.fasilitas}")
        print(f"Harga Dasar/Malam: Rp {harga_dasar:,}".replace(",", ".") + f" | Pajak(10%): Rp {pajak:,}".replace(",", "."))


class KamarStandard(KamarHotel):
    def __init__(self, nama_kamar, stok, harga_dasar, kapasitas):
        super().__init__(nama_kamar, stok, harga_dasar)
        self.kapasitas = kapasitas

    def hitung_harga_total(self, jumlah_malam):
        pajak = 0.05 * self.get_harga_dasar()
        harga_per_malam = self.get_harga_dasar() + pajak
        return harga_per_malam * jumlah_malam

    def tampilkan_detail(self):
        pajak = int(0.05 * self.get_harga_dasar())
        harga_dasar = int(self.get_harga_dasar())
        print(f"[STANDARD] {self.nama_kamar} | Kapasitas: {self.kapasitas}")
        print(f"Harga Dasar/Malam: Rp {harga_dasar:,}".replace(",", ".") + f" | Pajak(5%): Rp {pajak:,}".replace(",", "."))



def proses_transaksi(daftar_pesanan):
    print("\n--- STRUK PEMESANAN ---")
    total_tagihan = 0
    nomor = 1

    for item in daftar_pesanan:
        kamar = item[0]  
        malam = item[1]  

        subtotal = int(kamar.hitung_harga_total(malam))
        total_tagihan = total_tagihan + subtotal

        print(f"{nomor}. ", end="")
        kamar.tampilkan_detail()
        print(f"Menginap: {malam} malam | Subtotal: Rp {subtotal:,}".replace(",", "."))
        print()
        
        nomor = nomor + 1

    print("-----------------------------------")
    print(f"TOTAL TAGIHAN: Rp {total_tagihan:,}".replace(",", "."))
    print("-----------------------------------")



print("--- SETUP DATA KAMAR ---")


deluxe1 = KamarDeluxe("Kamar Deluxe Sea View", 10, 1500000, "Private Pool")


standard1 = KamarStandard("Kamar Standard Superior", 0, 500000, "2 Orang")
standard1.tambah_stok(-5) 
standard1.tambah_stok(20) 

# c) Daftar pesanan (Tuple sederhana: [objek_kamar, lama_menginap])
pesanan_tamu = [
    [deluxe1, 2],   
    [standard1, 1]   
]

# d) Cetak struk pembayaran
proses_transaksi(pesanan_tamu)