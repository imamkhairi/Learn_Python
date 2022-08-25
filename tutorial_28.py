# reading file

# nama_variabel = open(...)
# open("nama file", "mode")
# mode -> "r", "w", "a", "r+" -> read and write
employee_file = open("employees.txt", "r")

# .readable() -> mengembalikan true ketika file bisa diread
#print(employee_file.readable())

# .read() -> read isi dari file yang ditunjuk variabel
#print(employee_file.read())

# .readline() -> read baris dimana kursor sekarang
# setelah read kursor pindah ke baris selanjutnya
# print(employee_file.readline())
# print(employee_file.readline())

# .readlines() -> read seluruh line dan memindahkannya ke list
# jadi ini bisa diakses per index gitu
# print(employee_file.readlines())
for employee in employee_file.readlines():
    print(employee)

# untuk close file
employee_file.close()