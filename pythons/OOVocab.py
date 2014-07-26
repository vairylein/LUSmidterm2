import os


def firstunk(doc,name):

	with open(doc,"r") as myfile:
		txt = myfile.readlines()

	f = open(name, "w")
	d = {}

	for line in txt:
		words = line.split(" ")[:-1]
		sentence =[]
		for word in words:
			if word in d.keys():
				sentence+= [word]
			else:
				sentence+= ["<unk>"]
				d[word] = 0
		f.write(" ".join(sentence) + "\n")

	f.close()