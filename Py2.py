# Kata-kata yang dianggap spam
kata_spam = {"promo", "diskon", "hadiah"}

# Isi email
email = "Dapatkan hadiah dan diskon besar hari ini"

# Mengubah email menjadi huruf kecil lalu dipisahkan
kata_email = set(email.lower().split())

# Mengecek apakah ada kata spam
if kata_spam.intersection(kata_email):
    print("Email terdeteksi sebagai SPAM")
else:
    print("Email bukan spam")
