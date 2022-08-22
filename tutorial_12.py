# List function

lucky_number = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

# friends.extend(lucky_number)
# .extend(list) -> append sebuah list ke list

friends.append("Creed")
# .append(data) -> append satu data ke list

friends.insert(1, "Kelly")
# .insert(index, data) -> memasukkan data ke list pada index yang diinginkan,
# sisanya akan dipush ke kanan

# friends.remove("jim")
# .remove(data) -> menghapus data dari list

# friends.clear()
# .clear() -> menhapus semua isi list

friends.pop()
# .pop() -> pop (mengeluarkan) sebuah data dari dalam list

print(friends.index("Oscar"))
# sama kyk untuk strings .index -> mendapatkan index dari suatu data

print(friends.count("Jim"))
# .count(data) -> menghitung berapa jumlah data itu dalam suatu list

# friends.sort()
# .sort() -> untuk sorting data di list
# harus tipe data sama (gk bisa digabung strings dan int)

lucky_number.reverse()
# membalikkan urutan dari list

friends2 = friends.copy()
# friends2 akan memiliki semua isi dari friend

print(friends)

print(lucky_number)