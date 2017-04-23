import sys
text = input()
count = 1
max_count = -sys.maxsize - 1

for i in range(1, len(text)):
    if (text[i - 1] == text[i]):
        count = count + 1
        if (count > max_count):
            max_count = count
    else:
        count = 1

print(max_count)
