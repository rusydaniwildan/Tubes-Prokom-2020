import csv

def kamarHotel():
    while True:
        DATA_FILE_NAME = 'listharga.csv'

    with open (DATA_FILE_NAME) as csvfile:
        readCSV = csv.reader(csvfile, delimiter= ',')
        listharga = list(readCSV)
        line_count = 0

        for row in readCSV:
            if line_count == 0:
                print(f'Nama kolom : {row}')
                line_count += 1
            else:
                print(row)
                line_count += 1

        print(f'Total {line_count} baris')
    print(listharga)
