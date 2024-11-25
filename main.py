from vektorperator.penjumlahan_vektor import penjumlahan
from vektorperator.pengurangan_vektor import pengurangan
from vektorperator.dot_product import dot_product
from vektorperator.panjang_vektor import panjang_vektor
from vektorperator.vektor_unit import vektor_unit

vek_A = input("Masukkan vektor A : ")
vek_B = input("Masukkan vektor B : ")

def user_input():
    while True:
        print("\nOperasi pada vektor 2D")
        print("1. Penjumlahan vektor")
        print("2. Pengurangan vektor")
        print("3. Dot Product")
        print("4. Panjang Vektor")
        print("5. Vektor Unit")
        print("6. Keluar")

        pilihan = input("Masukkan nomor 1-6: ")

        if pilihan == "6":
            print("Program selesai.")
            break

        #Input vektor dari pengguna
        try:
            vek_A = list(map(int, input("Masukkan vektor A (dalam format x,y): ").split(',')))
            vek_B = list(map(int, input("Masukkan vektor B (dalam format x,y): ").split(',')))
        except ValueError:
            print("Input tidak valid, silakan masukkan vektor dalam format x,y.")
            continue

        if pilihan == "1":
            print("Hasil Penjumlahan:", penjumlahan(vek_A, vek_B))
        elif pilihan == "2":
            print("Hasil Pengurangan:", pengurangan(vek_A, vek_B))
        elif pilihan == "3":
            print("Hasil Dot Product:", dot_product(vek_A, vek_B))
        elif pilihan == "4":
            print("Panjang Vektor A:", panjang_vektor(vek_A))
            print("Panjang Vektor B:", panjang_vektor(vek_B))
        elif pilihan == "5":
            print("Vektor Unit A:", vektor_unit(vek_A))
            print("Vektor Unit B:", vektor_unit(vek_B))
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

user_input()
