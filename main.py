from vektorperator.penjumlahan_vektor import penjumlahan
from vektorperator.pengurangan_vektor import pengurangan
from vektorperator.dot_product import dot_product
from vektorperator.panjang_vektor import panjang_vektor
from vektorperator.vektor_unit import vektor_unit

import time
import os

os.system("cls")
def user_input():
    while True:
        print("Operasi pada vektor 2D")
        print("1. Penjumlahan vektor")
        print("2. Pengurangan vektor")
        print("3. Dot Product")
        print("4. Panjang Vektor")
        print("5. Vektor Unit")
        print("6. Keluar")

        pilihan = input("Masukkan nomor 1-6: ")

        if pilihan == "6":
            os.system("cls")
            print("Mengeluarkan anda")
            time.sleep(2)
            break

        #Input vektor dari pengguna
        try:
            os.system("cls")
            vek_A = list(map(int, input("Masukkan vektor A (dalam format x,y): ").split(',')))
            vek_B = list(map(int, input("Masukkan vektor B (dalam format x,y): ").split(',')))
        except ValueError:
            print("Input tidak valid, silakan masukkan vektor dalam format x,y.")
            continue

        if pilihan == "1":
            print("\nHasil Penjumlahan:", penjumlahan(vek_A, vek_B))
        elif pilihan == "2":
            print("\nHasil Pengurangan:", pengurangan(vek_A, vek_B))
        elif pilihan == "3":
            print("\nHasil Dot Product:", dot_product(vek_A, vek_B))
        elif pilihan == "4":
            print("\nPanjang Vektor A:", panjang_vektor(vek_A))
            print("\nPanjang Vektor B:", panjang_vektor(vek_B))
        elif pilihan == "5":
            print("\nVektor Unit A:", vektor_unit(vek_A))
            print("\nVektor Unit B:", vektor_unit(vek_B))
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.\n")

user_input()
