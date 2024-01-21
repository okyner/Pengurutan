def bubble_sort(data):
    size = len(data)
    for i in range(size):
        for j in range(0, size - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

def write_file(filename, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write("%s\n" % item)

def read_file(filename):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f.readlines()]

def tampil_menu():
    print("Menu:")
    print("1. Input Angka")
    print("2. Tampil Hasil Pengurutan")
    print("3. Selesai")

while True:
    tampil_menu()
    pilihan = int(input("Masukkan pilihan [1/2/3]: "))
    if pilihan == 1:
        jumlah_angka = int(input("Masukkan jumlah angka yang akan diinput: "))
        data = []
        for i in range(jumlah_angka):
            data.append(int(input("Angka %d: " % (i + 1))))
        bubble_sort(data)
        write_file("data_angka.txt", data)
    elif pilihan == 2:
        data = read_file("data_angka.txt")
        print("Hasil pengurutan:")
        for i in range(len(data)):
            print("%d. %d" % (i + 1, data[i]))
    elif pilihan == 3:
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")