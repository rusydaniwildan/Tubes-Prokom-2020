import os

import datetime

lama_hari=0

def waktuinap():
    x=datetime.datetime.now()

def print_menu():
    print(1* "-")
    print()
    print('\t','     HOTEL MELATI SOLO BARU ')
    print()
    print('\t','---------Selamat Datang----------')
    print()
    print('Jl.Solo baru No.900, kode pos 29112 No HP. 0001122')
    print('\t','      Solo baru Surakarta')
    print()
    print('\t',' Hotel bintang 3 dengan keunggulan: ')
    print('\t','           Nyaman')
    print('\t','            Aman')
    print('\t','           Bersih')
    print('\t','            Asri')
    print()
    print(50* "-")
    print('Pilih yang anda inginkan ?')
    print()
    print('1. CHECK IN')
    print('2. keluar program')
    print()
    print('Jenis kamar hotel?')
    print()
    print('1. Reguler')
    print('2. Deluxe')
    print('3. Suite')
    print()
    
    tanggalmasuk = int(input("Masukkan TANGGAL (1-31):"))
    bulanmasuk = int(input("Masukkan BULAN (1-12):"))
    tahunmasuk = int(input("Masukkan TAHUN (2020-2050):"))
    
    keluar = datetime.datetime.now()
    masuk = datetime.datetime(tahunmasuk, bulanmasuk, tanggalmasuk)
    lama = keluar - masuk
    
    


print_menu()
pilihan = input("Pilih yang anda inginkan:  ")
    
    
jenis = input("Jenis kamar hotel? ")
if jenis == "1":
    bed = input("Queen atau Twin? ")
    if bed == "Queen":
        from random import randint
        for _ in range(450):
            harga = randint(400, 450)
        print("Tarif",harga,".000 rupiah")
    if bed == "Twin":
        from random import randint
        for _ in range(460):
            harga = randint(420, 460)
        print("Tarif",harga,".000 rupiah")
        
elif jenis == "2":
    bed = input("Queen atau Twin? ")
    if bed == "Queen":
        from random import randint
        for _ in range(700):
            harga = randint(650, 700)
        print("Tarif",harga,".000 rupiah")
    if bed == "Twin":
        from random import randint
        for _ in range(720):
            harga = randint(680, 720)
            print("Tarif",harga,".000 rupiah")
        
else:
    bed = input("Queen atau Twin? ")
    if bed == "Queen":
        from random import randint
        for _ in range(960):
            harga = randint(900, 960)
            print("Tarif",harga,".000 rupiah")
    if bed == "Twin":
        from random import randint
        for _ in range(980):
            harga = randint(920, 980)
            print("Tarif",harga,".000 rupiah")
