# try / except


# cara deklarasi try / except
# ketika ada error akan eksekusi di except
# except bisa ditentukan untuk menangkap error apa contoh : "ZeroDivisionError"
# error yang dispesifikasikan dapat disimpan dalam bentuk variabel pakai "as"
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
