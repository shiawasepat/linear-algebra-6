from tambah import tambah

A = [2, 3]
B = [4, 6]

vek_A = input("Masukkan vektor A : ")
vek_B = input("Masukkan vektor B : ")

def menu_vektor():
    print("Operasi pada vektor 2D\n")
    print("1. Penjumlahan vektor")
    print("2. Pengurangan vektor")
    print("3. Dot Product")
    print("4. Panjang Vektor")
    print("5. Vektor Unit")
    pilihan = int(input("\nPilihan : "))
    return pilihan

# def user_input():
    
#     pilihan = menu_vektor()
#     if pilihan == 1:
#         penjumlahan(vek_A, vek_B)
#     elif pilihan == 2:
#         pengurangan(vek_A, vek_B)
#     elif pilihan == 3:
#         dot_product(vek_A, vek_B)
#     elif pilihan == 4:
#         panjang_vektor(vek_A)
#     elif pilihan == 5:
#         vektor_unit(vek_A)
#     else:
#         print("Pilihan Tidak Tersedia.")
