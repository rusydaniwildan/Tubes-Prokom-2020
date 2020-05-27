



import os

import datetime

lama_hari=0


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
    print()
    
print_menu()

 
def sistem():
    print('Pilih yang anda inginkan ?')
    print()
    print('1. CHECK IN')
    print('2. keluar program') 
    pilihan = input("Pilih yang anda inginkan (1/2):  ")
    if pilihan == "1":
        print("Dimohon mengisi tanggal")
    else :
        quit()
sistem()
    
    
def waktuinap(): 
    print('\t','Masukkan tanggal CHECK-IN')
    tanggalmasuk = int(input("Masukkan TANGGAL (1-31):"))
    bulanmasuk = int(input("Masukkan BULAN (1-12):"))
    tahunmasuk = int(input("Masukkan TAHUN (2020-2050):"))
    
    print('\t','Masukkan tanggal CHECK-OUT')
    tanggalkeluar = int(input("Masukkan TANGGAL (1-31):"))
    bulankeluar = int(input("Masukkan BULAN (1-12):"))
    tahunkeluar = int(input("Masukkan TAHUN (2020-2050):"))
    
    keluar = datetime.datetime(tahunkeluar, bulankeluar, tanggalkeluar)
    masuk = datetime.datetime(tahunmasuk, bulanmasuk, tanggalmasuk)
    lama = keluar - masuk
    print("Anda menginap selama", lama)
    
waktuinap()


def jumlahorang():
    Dewasa = input("Masukkan jumlah dewasa(0-5): ")
    Anak = input("Masukan jumlah anak(0-5) ")
    Bayi = input("Masukkan jumlah bayi(0-5) ")
    print("Jumlah penghuni kamar sebanyak", Dewasa, "dewasa, ", Anak, "anak, dan ", Bayi, "bayi")
jumlahorang()
    

def jenis():   
    print('Jenis kamar hotel?')
    print()
    print('1. Reguler')
    print('2. Deluxe')
    print('3. Suite')
    print()
        
    jenis = input("Jenis kamar hotel? ")
    if jenis == "1":
        bed = input("Queen atau Twin? ")
        if bed == "Queen":
            from random import randint
            for _ in range(1):
                harga = randint(400, 450)
                print("Tarif",harga,".000 rupiah")
        if bed == "Twin":
            from random import randint
            for _ in range(1):
                harga = randint(420, 460)
                print("Tarif",harga,".000 rupiah")
        
    elif jenis == "2":
        bed = input("Queen atau Twin? ")
        if bed == "Queen":
             from random import randint
             for _ in range(1):
                harga = randint(650, 700)
                print("Tarif",harga,".000 rupiah")
        if bed == "Twin":
            from random import randint
            for _ in range(1):
                harga = randint(680, 720)
                print("Tarif",harga,".000 rupiah")
        
    if jenis == "3":
        bed = input("Queen atau Twin? ")
        if bed == "Queen":
            from random import randint
            for _ in range(1):
                harga = randint(900, 960)
                print("Tarif",harga,".000 rupiah")
        if bed == "Twin":
            from random import randint
            for _ in range(1):
                harga = randint(920, 980)
                print("Tarif",harga,".000 rupiah")
jenis()

iterasi = True
print("WAJIB MEMPUNYAI IDENTITAS JIKA AKAN MELAKUKAN PEMBAYARAN!")

while iterasi == True:
    identitas = input("Apakah anda mempunyai identitas(KTP/Paspor/SIM)? (y/n)")
    if identitas =="y":
        iterasi = False
    else :
        iterasi = True
