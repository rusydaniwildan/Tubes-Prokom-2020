

from datetime import datetime, date
import math
import os
import sys
checkin, checkout = None, None
loop = True

def print_menu():
    print()
    print('\t','      HOTEL MELATI SOLO BARU ')
    print()
    print('\t','---------Selamat Datang----------')
    print()
    print('Jl.Solo baru No.900, kode pos 29112 No HP. 08232111')
    print('\t','      Solo baru Surakarta')
    print()
    print('\t',' Hotel bintang 3 dengan keunggulan: ')
    print('\t','           Nyaman')
    print('\t','            Aman')
    print('\t','           Bersih')
    print('\t','            Asri')
    print()
    print('======================================================')
    print('Pilih yang anda inginkan ?')
    print()
    print('1. CHECK IN')
    print('2. keluar program')
    print()

while loop:
    print_menu()
    pilihan = int(input('Masukan pilihan [1/2]: '))
    print()
    os.system('cls')
    if (pilihan == 1):
        print()
        print('\t','[ ISI BIODATA PENGINAP ]')
        print('--------------------------------')
        print()
        nama = input('Masukkan nama lengkap penginap : ').upper()
        nohp = input('Masukkan No HP penginap : +62 ')
        if len(nohp) != 4 and len (nohp) != 5: 
            os.system('cls')
            print('No Hp anda tidak terdaftar')
            continue
        ktp = input ('Apakah anda memiliki kartu identitas ktp/sim (y/n) : ')
        if ktp == 'n':
            sys.exit('\nError : Anda harus memuliki kartu identitas untuk MENGINAP')        
        elif ktp == 'y':
            kk = input('Masukkan No identitas kartu : ')
            tl = input("Masukkan Tempat lahir anda : ").upper()
            tt = input ('Masukkan tanggal lahir anda : ')
            print()
            os.system('cls')
        else:
            os.system('cls')
            input('\nError : Anda harus memilih antara (y/n)')
            continue
    elif (pilihan == 2):
        exit()
    else:
        print('Pilihan yang anda masukkan salah, silahkan coba lagi')
        continue







