class Paket:
    
    __tarif_dasar = 10000
    
    def __init__(self,id_paket, berat, tujuan, status):
        self.__id_paket = id_paket
        self.__berat = berat
        self.__tujuan = tujuan
        self.__status = status
    
    def update_status(self, new_status):
        self.__status = new_status
        return self.__status
    
    def get_status(self):
        return self.__status
    
    def get_berat(self):
        return self.__berat
    
    def hitung_total_biaya(self):
        return Paket.__tarif_dasar * self.__berat
    
    def get_detail_data_paket(self):
        print(f"ID Paket: {self.__id_paket}")
        print(f"Berat: {self.__berat}")
        print(f"Tujuan: {self.__tujuan}")
        print(f"Status Terkirim: {self.__status}")

class ArmadaMotor(Paket):
    def hitung_total_biaya(self):
        return super().hitung_total_biaya()
    
    def get_detail_data_paket(self):
        super().get_detail_data_paket()
        print(f"Total Biaya: {self.hitung_total_biaya()}")
        print("=" * 40)
       

class ArmadaTruk(Paket):
    def __init__(self, id_paket, berat, tujuan, status, biaya_bongkar_muat):
        super().__init__(id_paket, berat,tujuan, status)
        self.__biaya_bongkar_muat = biaya_bongkar_muat
    
    def hitung_total_biaya(self):
        return super().hitung_total_biaya() + self.__biaya_bongkar_muat
    
    def get_detail_data_paket(self):
        super().get_detail_data_paket()
        print(f"Total Biaya: {self.hitung_total_biaya()}")
        print("=" * 40)

class ArmadaPesawat(Paket):
    def __init__ (self, id_paket, berat, tujuan, status, biaya_asuransi_udara):
        super().__init__(id_paket, berat, tujuan, status)
        self.__biaya_asuransi_udara = biaya_asuransi_udara
    
    def hitung_total_biaya(self):
        return super().hitung_total_biaya() + self.__biaya_asuransi_udara
    
    def get_detail_data_paket(self):
        super().get_detail_data_paket()
        print(f"Total Biaya: {self.hitung_total_biaya()}")
        print("=" * 40)

class ArmadaKapal(Paket):
    def __init__(self, id_paket, berat, tujuan, status, biaya_asuransi_tenggelam):
        super().__init__(id_paket, berat, tujuan, status)
        self.__biaya_asuransi_tenggelam = biaya_asuransi_tenggelam
    
    def hitung_total_biaya(self):
        return super().hitung_total_biaya() + self.__biaya_asuransi_tenggelam
    
    def get_detail_data_paket(self):
        super().get_detail_data_paket()
        print(f"Total Biaya: {self.hitung_total_biaya()}")
        print("=" * 40)

data_paket = [
    ArmadaMotor(1, 0.6, "Kota Bandung", "Belum Terkirim"),
    ArmadaTruk(2, 2.5, "Kota Jakarta", "Terkirim", 5000),
    ArmadaPesawat(3, 1.0, "Kota Batam", "Terkirim", 1000),
    ArmadaKapal(4, 75.4, "Kota Pontianak", "Terkirim", 1000000)
]

for paket in data_paket:
    paket.get_detail_data_paket()
