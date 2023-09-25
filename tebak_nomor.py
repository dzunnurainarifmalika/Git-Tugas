import random

# Fungsi untuk memulai permainan
def guess_the_number():
    # Memilih angka acak antara 1 dan 100
    target_number = random.randint(1, 100)
    attempts = 0

    print("Selamat datang di Permainan Tebak Angka by pandu anugrah")
    print("Saya telah memilih angka antara 1 dan 100. Coba tebak!")

    while True:
        try:
            guess = int(input("Masukkan tebakan Anda: "))
            attempts += 1

            if guess < target_number:
                print("Tebakan Anda terlalu kecil. Coba lagi.")
            elif guess > target_number:
                print("Tebakan Anda terlalu besar. Coba lagi.")
            else:
                print(f"Selamat! Anda menebak angka {target_number} dengan benar dalam {attempts} percobaan.")
                break
        except ValueError:
            print("Masukkan harus berupa angka.")

if __name__ == "__main__":
    guess_the_number()
