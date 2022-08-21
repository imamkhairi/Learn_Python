# Using Strings

print("Imam \n\" \Khairi")
# \n untuk enter, \ bisa digunakan untuk chacacter unik gitu
# tapi juga bisa kalau mau print \ ya tinggal tulis \

phrase = "Imam Khairi"
print(phrase + " is cool")
# concatination (nyambungkan dua string gt) make +. Atau bisa dibilang append

print(phrase.upper())
# strings bisa dimodifikasi dengan menggunakan fungsi tambahin .(dot)

print(phrase.upper().isupper())
# true kalau semua uppercase
# fungsi2 ini juga bisa digabung dalam penggunaannya

print(len(phrase))
# len akan mendapatkan berapa banyak character yang ada di variabel / data yang diinginkan

print(phrase[0])
# akses index pada strings, sama lah ya mulai dari 0

print(phrase.index("Khai"))
# untuk mencari nilai index dari suatu nilai string / char
# kalau diaksih string akan dikembalikan dimana string ini awalnya mulai
# kalau dikasih sesuatu yang tidak ada di strings nya akan jadi error

print(phrase.replace("Imam", "Adine"))
# untuk replace string parameter1 -> data lama, parameter2 -> data baru 


# hal baru .index, .replace, len