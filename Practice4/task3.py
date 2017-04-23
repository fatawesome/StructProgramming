str1 = input()
str2 = input()
result = ''
for chr1 in str1:
    for chr2 in str2:
        if (chr1 == chr2):
            result = result + chr1

print(result)
