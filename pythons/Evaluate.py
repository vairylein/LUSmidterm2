import sys
import Levenshtein

mt1result = "../mt1result"
gram3= "../run/3gram/devfinal.txt"
correct = "../splitted/dev.concept"
documents = [gram3]
docnames = ["mt1result","gram3 simple"]

def levensht():
	
	with open(correct, "r")as mefile:
		stan = mefile.readlines()
	
	f = open("../../practise/Evaluationfile","w")

	d=0

	print len(stan)


	for doc in documents:
		with open(doc,"r") as myfile:
			doct = myfile.readlines()
		print (len(doct)-1)/3
		levnotacc = []
		levacc = []
		l=0
		for line in doct:
			if line == "\n":
				levnotacc+=[len(stan[l].split())]
			else:
				
				levacc += [Levenshtein.levenshtein(stan[l].split(),line.split())]
			
			l+=1

		for value in levacc:
			print value

		f.write("FILE: %s\nEdit distance of accepted strings %s\nTotal Edit distance: %s\nNumber of unaccepted sentences: %s \n\n" % (docnames[d],sum(levacc)/float(len(levacc)),sum(levacc+levnotacc)/float(len(levacc+levnotacc)),len(levnotacc)))
		d+= 1

	
		