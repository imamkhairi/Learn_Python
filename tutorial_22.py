# for loop


friends = ["Jim", "Caren", "Kevin"]

#deklarasi for, setelah for itu bebas nama nya
for letter in "Imam Khairi":
    print(letter)

for friend in friends:
    print(friend)

# range(10) -> 0 ~ 9.  range(2,5) -> 2 ~ 4
for index in range(3, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First iteration")
    else: 
        print("Not first")