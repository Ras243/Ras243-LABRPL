# variabel global untuk menyimpan data buku
buku = []


# fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print("belum ada data")
    else:
        for indeks in range(len(buku)):
            print("[%d]" % (indeks, buku[indeks]))


# fungsi untuk menambah data 
def insert_data():
    buku_baru = input("judul Buku: ")
    buku.append(buku_baru)

# fungsi untuk edit data
def edit_data():
    show_data()
    indeks = input("inputkan id buku: ")
    if indeks > len(buku):
        print("id salah")
    else:
        judul_baru = input(*"judul baru: ")
        buku[indeks] = judul_baru

# fungsi untuk menghapus data
def delete_data():
    show_data()
    indeks = input("inputkan id buku: ")
    if indeks > len(buku):
        print("id salah")
    else:
        buku.remove(buku[indeks])

# fungsi untuk menampilkan menu
def show_menu():
    print("\n")
    print("----------MENU----------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete data")
    print("[5] Exit")

    menu = int(input("Pilihan Menu"))
    print("\n")

    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("salah pilih!")


if __name__ == "__main__":

    while(True):
        show_menu