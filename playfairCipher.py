keyWord = input("Enter a keyword for encryption: ").upper()
pT = input("Enter a plain text to encrypt: ")


lofK = []
for letter in keyWord:
    l = 'I' if letter == 'J' else letter
    if l not in lofK:
        lofK.append(l)

square = [
    "A", "B", "C", "D", "E",
    "F", "G", "H", "I", "K",
    "L", "M", "N", "O", "P",
    "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"
]

for i in lofK:
    if i in square:
        square.remove(i)
square = lofK + square


spacelessPT = [l.upper() for l in pT if l.isalpha()]
spacelessPT = ['I' if l == 'J' else l for l in spacelessPT]

doubles = []
i = 0
while i < len(spacelessPT):
    letter1 = spacelessPT[i]
    if i + 1 == len(spacelessPT):
        doubles.append(letter1 + 'X')
        break

    letter2 = spacelessPT[i + 1]
    if letter1 == letter2:
        doubles.append(letter1 + 'X') # Küçük x yerine büyük X
        i += 1
    else: 
        doubles.append(letter1 + letter2)
        i += 2

#--------------------------------------
#encryptinon
crypted_double_list = []
for double in doubles:
    idx1 = square.index(double[0])
    idx2 = square.index(double[1])
    
    row1, column1 = idx1 // 5, idx1 % 5
    row2, column2 = idx2 // 5, idx2 % 5
    
    if row1 == row2:
        new_double1 = square[row1 * 5 + (column1 + 1) % 5]
        new_double2 = square[row2 * 5 + (column2 + 1) % 5]
    elif column1 == column2:
        new_double1 = square[((row1 + 1) % 5) * 5 + column1]
        new_double2 = square[((row2 + 1) % 5) * 5 + column2]
    else:
        new_double1 = square[row1 * 5 + column2]
        new_double2 = square[row2 * 5 + column1]
        
    crypted_double_list.append(new_double1 + new_double2)

cT = "".join(crypted_double_list)
print(cT)

#--------------------------------------
#decryption

crypted_doubles = [cT[i:i+2] for i in range(0, len(cT), 2)]

decrypted_double_list = []
for double in crypted_doubles:
    idx1 = square.index(double[0])
    idx2 = square.index(double[1])

    row1, column1 = idx1 // 5, idx1 % 5
    row2, column2 = idx2 // 5, idx2 % 5

    if row1 == row2:
        new_double1 = square[row1 * 5 + (column1 - 1) % 5]
        new_double2 = square[row2 * 5 + (column2 - 1) % 5]
    elif column1 == column2:
        new_double1 = square[((row1 - 1) % 5) * 5 + column1]
        new_double2 = square[((row2 - 1) % 5) * 5 + column2]
    else:
        new_double1 = square[row1 * 5 + column2]
        new_double2 = square[row2 * 5 + column1]

    decrypted_double_list.append(new_double1 + new_double2)

dT = "".join(decrypted_double_list)
clear_dT = dT.replace("X", "")

print(dT)




