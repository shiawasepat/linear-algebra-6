import math
from vektorperator.dot_product import dot_product
from vektorperator.panjang_vektor import panjang_vektor

def sudut_antara_vektor(vek_A, vek_B):
    """
    Menghitung sudut antara dua vektor dalam derajat.
    """
    dot = dot_product(vek_A, vek_B)
    magnitude_A = panjang_vektor(vek_A)
    magnitude_B = panjang_vektor(vek_B)

    if magnitude_A == 0 or magnitude_B == 0:
        return "Sudut tidak terdefinisi (salah satu vektor adalah nol)."

    cos_theta = dot / (magnitude_A * magnitude_B)
    cos_theta = max(-1, min(1, cos_theta))
    theta = math.acos(cos_theta)
    return math.degrees(theta)
