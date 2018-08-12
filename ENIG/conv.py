## This is just used to change a string of characters into a list of numbers for the rotors to use

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
i = 0
z = list()
while i != len(text):
    z.append(ord(text[i]))
    print(z)
    i+=1
