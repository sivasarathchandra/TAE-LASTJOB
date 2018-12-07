def capitalize(string):
    str2 = ''
    str12 = string.split(' ')
    for i in range(0, len(str12)):
        if str12[i].isalpha() == True:
            final = str12[i]
            if final != " ":
                txt = final[0].upper() + final[1:]
                str2 = str2 + txt + " "
        else:
            str2 = str2 + str12[i] + " "
    return str2


final = capitalize("sarath chandra chinatapalli")
print(final)

n = int(input())
for i in range(1, n + 1):
    print(i, end='')


a = input("Enter the 1st count of number: ")
a1 = input("now roll numbers: ")
a12 = a1.split(",")
for i in range(0,len(a12)):
    print(a12[i]+" ", end='')
b = input("Enter the 1st count of number: ")
b1 = input("new roll numbers: ")
b12 = b1.split(",")
for i in range(0,len(b12)):
    print(b12[i]+" ", end='')
l1 = set(b12).intersection(a12)
print(len(l1))