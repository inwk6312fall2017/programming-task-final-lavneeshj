def longest_word(filename):
    
    with open(filename) as f:
        linenum = 1
        for line in f:
            words = line.split()
            longest = ''
            for word in words:
                if len(longest) < len(word):
                    longest = word
            print("Line", linenum, "has", longest, "as the longest word.")
            linenum += 1
            print(longest)


filename1='Book1.txt'
filename2='Book2.txt'
filename3='Book3.txt'

longest_word(filename1)

longest_word(filename2)

longest_word(filename3)

