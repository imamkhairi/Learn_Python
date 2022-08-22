# building translator

def translate(phrase):
    translation = ""
    for letter in phrase:
        # if juga bisa pake in
        if letter.lower() in "aiueo":
            if letter.isupper():
                # menggabungkan string bisa gini
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))