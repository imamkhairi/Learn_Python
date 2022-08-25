# Writing to Files

# appending file
# employee_file = open("employees.txt", "a")

# write a file
# kalau write dan file nya dari awal gk ada, maka akan bikin file baru
employee_file = open("employees.txt", "w")
# print(employee_file.read())
employee_file.write("\nKelly - Costumer Service")
employee_file.close()