# belajar tipe data dictionary

customer = {"name":"algifari", "age":30, "address":"subang"}


name = customer["name"]
age = customer["age"]
address = customer["address"]

# menambahkan data baru dan mengubah
customer["hobby"] = "basket"
customer["name"] = "rizki algifari"

# menghapus data
del customer["address"]

#for key in customer:
#    value = customer[key]
#    print(f"{key}:{value}")


# cara lain = simple
for key, value in customer.items():
    print(f"{key}:{value}")



