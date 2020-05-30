#
#
#
#
#
#




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
    print()
    print('\t','ISI TIPE KAMAR SESUAI DENGAN PILIHAN PENGINAP')
    print('======================================================')
    print()
    print('1. Regular')
    print('2. Deluxe')
    print('3. Suite')
    print('4. President suite')

    tipe = int(input('Masukkan Tipe kamar yang anda pilih : '))
    os.system('cls')
    if (tipe == 1):
        kamar = 'Regular'
        tarif = ['150.000','175.000','200.000','225.000','250.000','275.000','300.000']
        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn? ")
            print('(NOTES: MAKSIMAL MENGINAP 7 HARI)')
            try:
                checkin = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")

        while checkout is None:
            tanggal = input("Masukkan tanggal CheckOut? ")

            try:
                checkout = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")
        waktuMenginap = checkout - checkin
        waktu =(waktuMenginap.days)
        if (waktu==1):
            tarif2=tarif[0]
        elif (waktu==2):
            tarif2=tarif[1]
        elif (waktu==3):
            tarif2=tarif[2]
        elif (waktu==4):
            tarif2=tarif[3]
        elif (waktu==5):
            tarif2=tarif[4]
        elif (waktu==6):
            tarif2=tarif[5]
        elif (waktu==7):
            tarif2=tarif[6]
        else:
            try:
                pass
            except NameError:
                print()            
            sys.exit('\nError : Maksimal hanya menginap 7 hari')
    elif (tipe == 2):
        kamar = 'Deluxe'
        tarif = ['155.000','185.000','205.000','235.000','275.000','285.000','310.000']
        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn? ")
            print('(NOTES: MAKSIMAL MENGINAP 7 HARI)')
            try:
                checkin = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")

        while checkout is None:
            tanggal = input("Masukkan tanggal CheckOut? ")

            try:
                checkout = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")
        waktuMenginap = checkout - checkin
        waktu =(waktuMenginap.days)
        if (waktu==1):
            tarif2=tarif[0]
        elif (waktu==2):
            tarif2=tarif[1]
        elif (waktu==3):
            tarif2=tarif[2]
        elif (waktu==4):
            tarif2=tarif[3]
        elif (waktu==5):
            tarif2=tarif[4]
        elif (waktu==6):
            tarif2=tarif[5]
        elif (waktu==7):
            tarif2=tarif[6]
        else:
            os.system('cls')   
            print('Waktu yang andah isi salah')
            continue

    elif (tipe == 3):
        kamar = 'Suite'
        tarif = ['185.000','285.000','305.000','435.000','575.000','885.000','910.000']
        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn? ")
            print('(NOTES: MAKSIMAL MENGINAP 7 HARI)')
            try:
                checkin = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")
            while checkout is None:
                tanggal = input("Masukkan tanggal CheckOut? ")
            try:
                checkout = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")
        waktuMenginap = checkout - checkin
        waktu =(waktuMenginap.days)
        if (waktu==1):
            tarif2=tarif[0]
        elif (waktu==2):
            tarif2=tarif[1]
        elif (waktu==3):
            tarif2=tarif[2]
        elif (waktu==4):
            tarif2=tarif[3]
        elif (waktu==5):
            tarif2=tarif[4]
        elif (waktu==6):
            tarif2=tarif[5]
        elif (waktu==7):
            tarif2=tarif[6]
        else:
            os.system('cls')   
            print('Waktu yang andah isi salah')
            continue

    elif (tipe == 4):
        kamar = 'President suite'
        tarif = ['355.000','485.000','505.000','635.000','775.000','885.000','990.000']
        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn? ")
            print('(NOTES: MAKSIMAL MENGINAP 7 HARI)')
            try:
                checkin = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")

        while checkout is None:
            tanggal = input("Masukkan tanggal CheckOut? ")

            try:
                checkout = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")
        waktuMenginap = checkout - checkin
        waktu =(waktuMenginap.days)
        if (waktu==1):
            tarif2=tarif[0]
        elif (waktu==2):
            tarif2=tarif[1]
        elif (waktu==3):
            tarif2=tarif[2]
        elif (waktu==4):
            tarif2=tarif[3]
        elif (waktu==5):
            tarif2=tarif[4]
        elif (waktu==6):
            tarif2=tarif[5]
        elif (waktu==7):
            tarif2=tarif[6]
        else:
            os.system('cls')   
            print('Waktu yang andah isi salah')
            continue

    else:
        print('Pilihan yang anda pilih salah, silahkan coba lagi')
        continue
        
        break
    
    print()
    print()
    print('\t','KWITANSI PEMBAYARAN RESERVASI HOTEL')
    print('---------------------------------------------')
    print()
    print('\t','Nama : '+ str(nama))
    print()
    print('\t','No HP : (+62)'+ str(nohp))
    print()
    print('\t','No identitas : '+ str(kk))
    print()
    print('\t','TTL : '+ str(tl) + ','+ str(tt))
    print()
    print('\t','Tipe kamar : '+ str(kamar))
    print()
    print('\t','Waktu : '+ str(waktu)+ ' Malam')
    print()
    print('\t','Biaya : '+ 'Rp.' + str(tarif2)+',00-')
    print()
    print('\t','Bayar dengan uang pas')
    print()
    print()
    print('Terimakasih atas kepercayaan yang anda berikan kepada kami, semoga anda senang')
    print()
    print('Mohon maaf apabilan pelayanan kami kurang maksimal.')
    print()
    print('=======================================================')

    def pengecekanUlang():
        print('Silahkan cek data diatas terlebih dahulu')
        pilih = input("Apakah data tersebut sudah sesuai? [y/n]: ")
        if pilih == 'y':
            print()
        else:
            os.system('cls')
            print('Silahkan Ulang dari awal, Pastikan Data yang anda isi BENAR')
            sys.exit()

    pengecekanUlang()

    while loop: 
        print("[SILAHKAN MELAKUKAN PEMBAYARAN]")
        print()
        print("Pilih metode pembayaran yang akan Anda lakukan:")
        print('1. Cash')
        print('2. Debit Card') 
        
        pilih = input("Pilih yang anda inginkan (1/2):  ")
        if pilih == "1":
            cash = int(input('Uang dari penginap: Rp. '))
            tarif3 = int(input('Biaya hotel: Rp.'))
            kurang = str(tarif3 - cash)
            kembali = str(cash - tarif3)
            if (cash > tarif3):
                print ('Jumlah kembalian adalah :'+ 'Rp.' + str(kembali)+',00-')
                print("""
            Terima kasih telah melakukan reservasi di hotel kami
            Selamat menikmati penginapan yang nyaman
            Semoga hari Anda menyenangkan:)
            """)
            
            else:
                print ('Maaf uang anda kurang sebesar :'+ 'Rp.' + str(kurang)+',00-')
                os.sys('cls')
                print('Pastikan uang anda cukup')
                continue


        else:
            saldo = input('Apakah saldo mencukupi? [y/n]: ')
            if saldo == 'y':
                print("""
                Terima kasih telah melakukan reservasi di hotel kami
                Selamat menikmati penginapan yang nyaman
                Semoga hari Anda menyenangkan:)
                """)
            else :
                print ("""
                Mohon maaf sisa saldo Anda tidak mencukupi untuk melakukan reservasi ini.
                Silahkan gunakan debit card lain atau menggunakan metode pembayaran lain
                """)
                ubah = input ('Ingin mengubah metode pembayaran atau mengganti debit card? [y/n]: ')
                if ubah == 'y':
                    change = input('Ubah metode pembayaran menjadi cash? [y/n]: ')
                    if change == 'y':
                        os.sys('cls')
                        continue
                    else :
                        ganti = input ('Ingin mengganti debit card? [y/n]: ')
                        if ganti == 'y':
                            saldo = input('Apakah saldo mencukupi? [y/n]: ')
                            if saldo == 'y':
                                print("""
                                Terima kasih telah melakukan reservasi di hotel kami
                                Selamat menikmati penginapan yang nyaman
                                Semoga hari Anda menyenangkan:)
                                """)
                            else:
                                os.sys('cls')
                                print('Gunakan pembayaran Cash saja')
                        else :
                            os.sys('cls')
                else :
                    
                    sys.exit()
                    
        ulang =''
        while ulang!= 'y' and ulang!= 't':
            ulang = input('Apakah anda ingin memesan kamar lagi [Y/T] : ')
            if ulang == 'y':
                os.system('cls')
                print ('Silahkan pilih lagi')
            elif ulang =='t':
                print('Terimakasih telah melakukan reservasi di Hotel kami :)')
                exit()


exit()
   




