# if statement

is_male = True
is_tall = True

# cara nulis if
# kasih "or" atau "and" untuk menggabungkan 
# "not" akan menegeate (membalikan) nilai booleannya
# elif -> else if
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall): 
    print("Youre a short male")
elif not(is_male) and is_tall: 
    print("Youre not a male but tall")
else:
    print("You are not male and not tall")