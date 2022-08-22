# dictionaries
# pasangan key dan value

# cara bikin dictionary
monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}


# akses dictionary, bukan menggunakan index tapi "key"
#print(monthConversion["Jan"])

print(monthConversion.get("Luv", "Not a valid key"))
# Kalau pakei .get() itu akan membantu ketika key yang dimasukkan itu tidak ada
# parameter ke 2 akan menjadi default value ketika key nya tidak ada