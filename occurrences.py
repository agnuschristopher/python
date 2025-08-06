text = input("Enter text: ") + ' '
word = ''
count = {}

for char in text:
    if char != ' ':
        word += char
    else:
        if word:
            count[word] = count.get(word, 0) + 1
            word = ''

print(count)
