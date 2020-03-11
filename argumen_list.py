# belajar argument list 

#def jumlahkan(satu, dua, tiga, empat):
#    total = satu + dua + tiga + empat
#    print(f"total {[satu, dua, tiga, empat]} = {total}")

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"total {list_angka} = {total}")

jumlahkan(10, 10, 10, 10,10,200,10)     