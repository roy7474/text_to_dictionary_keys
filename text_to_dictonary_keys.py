
# tfile = input('Enter the name of the file you would like to open: ')

words_count = {}
fhandle = open('words.txt')             # open the file

for line in fhandle:
    words = line.split()                # split the text into words
#    words_count[words]= words_count.get(words,0) + 1
    for word in words:
        if word not in words_count:     #if the key word is not already in the dictionary. add it and add a value of 1
            words_count[word] = 1
        else:                           # else, add 1 to the key word
            words_count[word] += 1

print(words_count)
