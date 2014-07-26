# get lexicon either cutoff (without the stopwords) or not

def get_lexicon(textdoc, name, cutoff = False, stopdoc = None):
	
	if stopdoc is None:
		stopdoc = []

	with open (textdoc,"r") as myfile:
		txt1 = myfile.readlines()

	stoplist= []
	if cutoff:
		with open (stopdoc, "r") as mafile:
			for line in mafile:
				stoplist +=[line[:-1]]

	f = open(name + ".lex","w")
	f.write("<epsilon> 0\n<unk> 1\n<s> 2\n</s> 3\n")
	i = 4
	d={}
	for line in txt1:
		words=line[:-1].split()
		if cutoff:
			for w in words:
				if w not in stoplist:
					d[w] = 0
		else:
			for w in words:
				d[w] = 0

	for key in d:
		f.write(key + " " + str(i) + "\n")
		i+= 1

	f.close()

# adding words to the lexicon
def addwords(adddoc, lex):
	# lex and addoc need to end with a newline
	
	with open (adddoc,"r") as myfile:
		adds = myfile.readlines()

	with open(lex,"r") as mafile:
		index = 0
		for line in mafile:
			index +=1

	with open (lex, "a") as mefile:
		for word in adds:
			mefile.write(word[:-1] + " " + str(index) + "\n")
			index+=1



