import random

pesan_selamat_datang = "SELAMAT DATANG DI FILE PYTHONKU:D"
posisi_tikus = random.randint(1,5)

print("**********************************")
print(f"{pesan_selamat_datang}")
print("**********************************")

nama = input("Masukin nama kamu: ")

print(f'''
Halo {nama}! Coba kamu perhatikan lubang dibawah ini!

                |_| |_| |_| |_| |_|
''')
jawaban = int(input("Menurut kamu, lubang mana yang ada tikusnya? [1 / 2 / 3 / 4 / 5]:"))

if jawaban == posisi_tikus:
    print(f"BENER! Tikus ada di lubang nomor {posisi_tikus} dan pilihan kamu adalah {jawaban}")
else:
    print(f"SALAH! Tikus ada di lubang nomor {posisi_tikus} sedangkan pilihan kamu adalah {jawaban}")



