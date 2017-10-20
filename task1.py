#def longest_word(filename):
    
#    with open(filename) as f:
        
#        for line in f:
#            words = line.split('.')
#            longest = ''
#            for word in words:
#                if len(longest) < len(word):
#                   longest = word
#            print("Line has", longest, "as the longest word.")
           
 #           return(longest)


#filename1='Book1.txt'
#filename2='Book2.txt'
#filename3='Book3.txt'

#longest_word(filename1)

#longest_word(filename2)

#longest_word(filename3)


def longest_word(file):

	a= open(file,'r')
	l = a.readlines()
	string = l[0]
	stringsplit = string.split()

	a = []
	for i in stringsplit:
    		a.append(len(i))
    		e = max(a)
	for j in stringsplit:
    		if len(j) == e:
        		print("The longest word in", file,"is", j, "and it is", len(j),"characters long")

file1 = 'Book1.txt'
file2 = 'Book2.txt'
file3 = 'Book3.txt'

longest_word(file1)
