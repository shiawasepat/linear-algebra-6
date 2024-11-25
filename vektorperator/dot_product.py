#dot product vector
def dot_product(vek_A, vek_B):
    if len(vek_A) != len(vek_B):
        raise ValueError("Ukuran vetor harus sama")
    print("")
    return sum(vek_A * vek_B for vek_A, vek_B in zip(vek_A, vek_B))
