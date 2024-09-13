import sys

data = {
  1 : {
      'Nama' : 'Nasi Goreng',
      'Harga' : 12000,
      'Stok' : 10,
      'Terjual' : 0
  },
  2 : {
      'Nama' : 'Mie Ayam',
      'Harga' : 7000,
      'Stok' : 10,
      'Terjual' : 0
  },
  3 : {
      'Nama' : 'Nasi Kuning',
      'Harga' : 10000,
      'Stok' : 10,
      'Terjual' : 0
  },
  4 : {
      'Nama' : 'Mie Campur',
      'Harga' : 10000,
      'Stok' : 10,
      'Terjual' : 0
  },
}

data_filter = {
    1 : "Nasi",
    2 : "Mie"
  }

def pilihanKembali():
  pilihan = input("Apakah ingin kembali ke menu utama? (y/n): ")
  while True:
    if pilihan.lower() == "y":
      main()
    elif pilihan.lower() == "n":
      sys.exit()
    else:
      print("Masukkan pilihan yang sesuai")

def showData():
  if data:
    print("No\t| Nama \t\t\t|Harga \t\t|Stok \t\t|Terjual")
    for key, value in data.items():
      print(f"{key}\t| {value.get('Nama')}\t\t\t| {value.get('Harga')}\t\t| {value.get('Stok')}\t\t| {value.get('Terjual')}")
  else:
    print("Data Kosong")
    
def inputData():
  def cariAngkaTerbesar(data):
    if data:
      return max(data.keys()) + 1
    else:
      return 1

  nama = input("Masukkan Nama: ")
  harga = int(input("Masukkan Harga: "))
  stok = int(input("Masukkan Stok: "))
  # terjual = int(input("Masukkan Terjual: "))

  data_baru = cariAngkaTerbesar(data)

  data[data_baru] = {
      'Nama' : nama, 
      'Harga' : harga,
      'Stok' : stok,
      "Terjual" : 0,
  }
  
  pilihanKembali()
  
def cari_nama_key(data, nama):
    hasil = []
    for key, value in data.items():
        if value.get('Nama').lower() == nama.lower():
            hasil.append((key, value))
    return hasil  
  
def cari_key(data, kunci):
    for key in data.items():
        if key  == kunci:
            return key
    return None 

def ubahData():
  showData()
  
  cari_nomor = int(input("Masukkan Nomor yang ingin dihapus: "))

  nama = input("Masukkan Nama: ")
  harga = int(input("Masukkan Harga: "))
  stok = int(input("Masukkan Stok: "))
  
  data[cari_nomor]['Nama'] = nama
  data[cari_nomor]['Harga'] = harga
  data[cari_nomor]['Stok'] = stok
  data[cari_nomor]['Terjual'] = 0
  
def hapusData():
  showData()
  
  cari_nama = int(input("Masukkan nama yang ingin dihapus: "))

  data.pop(cari_nama)
  
def cariData(data):
  cari_nama = input("Masukkan nama yang ingin dicari: ")
  print("No\t| Nama \t\t\t|Harga \t\t|Stok \t\t|Terjual")
  nilai_cari = False
  for key, item in data.items():
    if cari_nama.lower() in item['Nama'].lower():
      print(f"{key}\t| {item['Nama']}\t\t| {item['Harga']}\t\t| {item['Stok']}\t\t| {item['Terjual']}")
      nilai_cari = True
  
  if not nilai_cari:
    print("Data Tidak Ditemukan")
    
  pilihan = input("Apakah ingin mencari data lagi? (y/n): ")
  while True:
    if pilihan.lower() == "y":
      cariData(data)
    elif pilihan.lower() == "n":
      pilihanKembali()
    else:
      print("Masukkan pilihan yang sesuai")

def filterData(data,data_filter):
  if data_filter:
    print("Pilih filter sesuai dengan nomor dibawah ini:")
    print("No\t| Nama")
    for key, value in data_filter.items():
      print(f"{key}\t| {value}")
    
  cari_filter = int(input("Masukkan pilhan nomor yang ingin dicari: "))
  value_filter = data_filter[cari_filter]
  print(value_filter)

  nilai_cari = False
  for key, item in data.items():
    if value_filter.lower() in item['Nama'].lower():
      print(f"{key}\t| {item['Nama']}\t\t| {item['Harga']}\t\t| {item['Stok']}\t\t| {item['Terjual']}")
      nilai_cari = True
    
  if not nilai_cari:
      print("Data Tidak Ditemukan")
  
  pilihan = input("Apakah ingin mencari data lagi? (y/n): ")
  while True:
    if pilihan.lower() == "y":
      filterData(data, data_filter)
    elif pilihan.lower() == "n":
      pilihanKembali()
    else:
      print("Masukkan pilihan yang sesuai")
  
def menu(): 
  print("===== Menu =====")
  print("1. Tampilkan Semua Data")
  print("2. Tambah Data")
  print("3. Ubah Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("6. Filter Data")
  print("0. Keluar")
  
  pilih = int(input("Pilih: "))
  if pilih == 1:
    showData()
    pilihanKembali()
  elif pilih == 2:
    inputData()
  elif pilih == 3:
    ubahData()
  elif pilih == 4:
    hapusData()
  elif pilih == 5:
    cariData(data)
  elif pilih == 6:
    filterData(data, data_filter)
  elif pilih == 0:
    sys.exit()
  else:
    print("Pilihan Tidak Tersedia")

def main():
  menu()
      
main()