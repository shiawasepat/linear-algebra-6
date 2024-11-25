# unit vektor
import math #module matematica

def vektor_unit(v): #(v) =  vektor 
    #panjang = magnitudo
    panjang = math.sqrt((sum([i**2 for i in v])))
    vektor_unit = [i/panjang for i in v] #normalisasi
    vektor_unit = [round(i,2) for i in vektor_unit] #normalisasi
    return vektor_unit