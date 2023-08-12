
# tfile = input('Enter the name of the file you would like to open: ')

words_count = {}
fhandle = open('words.txt')

for line in fhandle:
    words = line.split()
#    words_count[line]= words_count.get(line,0) + 1
#    word = lines.split()
    for word in words:
        if word not in words_count:
            words_count[word] = 1
        else:
            words_count[word] += 1

print(words_count)
        
