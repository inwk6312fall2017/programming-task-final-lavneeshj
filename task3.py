
def func(file):

	
	with open(file) as d:
		text = d.readlines()
		for line in text:
			words = line.split()
			print(words.replace('172','192'))



file1='running-config.cfg'
func(file1)


dict={}


