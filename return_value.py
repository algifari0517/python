# belajar method return value

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
#    print(f"total {list_angka} = {total}")
#   return total
    return (list_angka, total)
list_angka, total = jumlahkan(10, 10, 10, 10,10,200,10)     


# mengambil data total

# print(total)
print(f"total {list_angka} = {total}")
print(f"total {list_angka} = {total}")
print(f"total {list_angka} = {total}")
print(f"total {list_angka} = {total}")
print(f"total {list_angka} = {total}")
print(f"total {list_angka} = {total}")
print(f"total {list_angka} = {total}")
print(f"total {list_angka} = {total}")
print(f"total {list_angka} = {total}")
print(f"total {list_angka} = {total}")
print(f"total {list_angka} = {total}")
