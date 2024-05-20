barang = []
def tambah_data ():
    nama_barang = str(input("masukan nama barang : "))
    jumlah = int(input("masukan stok barang : "))

    barang_baru = {f"nama": nama_barang, "jml" : jumlah }
    barang.append(barang_baru)
    print("Data Berhasil Ditambahkan")

def edit_data():
    index = int(input("Masukkan index data yang akan diubah: "))
    if index >= len(barang):
        print("Index tidak valid")
        return

    barang[index]["nama"] = input("Masukkan nama barang baru: ")
    barang[index]["jml"] = int(input("Masukkan stok barang baru: "))
    print("Data berhasil diubah")


def hapus_data():
    hapus = int(input("hapus data index ke : "))
    barang.pop(hapus)
    print("Data Berhasil Dihapus")

def tampil_data():
    print ("-------- Daftar Data --------")
    for i in barang:
        print(f"{i['nama']} : {i['jml']}")

def cari_data():
    cari = input("Cari nama barang: ")
    found = False
    for i in barang:
        if i['nama'].lower() == cari.lower():
            print('-', i['nama'], i['jml'])
            found = True
    if not found:
        print("Data tidak ditemukan")

def jumlah_data():
    print("jumlah data tersimpan",len(barang),"barang")