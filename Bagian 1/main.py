import random

pesan_selamat_datang = "SELAMAT DATANG DI FILE PYTHONKU:D"
posisi_tikus = random.randint(1,5)

print("**********************************")
print(f"{pesan_selamat_datang}")
print("**********************************")

nama = input("Masukin nama kamu: ")

bentuk_lubang = "|_|"
lubang_kosong = [bentuk_lubang] * 5
lubang_berbentuk = lubang_kosong.copy()

lubang_berbentuk[posisi_tikus - 1] = "|0_0|"

print(f'''
Halo {nama}! Coba kamu perhatikan lubang dibawah ini!
                {lubang_kosong}
''')
jawaban = int(input("Menurut kamu, lubang mana yang ada tikusnya? [1 / 2 / 3 / 4 / 5]:"))

konfirmasi = input(f"{nama} kamu menjawab gua no: {jawaban}, apa kamu yakin? [y/n]")

if konfirmasi == "n":
    exit()
elif konfirmasi == "y":
    if jawaban == posisi_tikus:
        print(f'''{lubang_berbentuk} \n BENER! Tikus ada di lubang nomor {posisi_tikus} dan pilihan kamu adalah {jawaban}''')
    else:
        print(f'''{lubang_berbentuk} \n SALAH! Tikus ada di lubang nomor {posisi_tikus} sedangkan pilihan kamu adalah {jawaban}''')
else:
    print("Yang kamu ketik gak ada di pilihan!")
    exit()