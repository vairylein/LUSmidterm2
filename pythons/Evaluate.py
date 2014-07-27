import sys
import Levenshtein

mt1result = "../mt1result"
correct = "../splitted/test.concept"
finaltest = "../run/finaltest/final.txt"
documents = [mt1result,finaltest]
docnames = ["mt1result","finaltest"]


#gram6= "../run/6gram/final.txt"
#gram7= "../run/7gram/final.txt"
#gram3= "../run/3gram/final.txt"
#gram4= "../run/4gram/final.txt"
#gram5= "../run/5gram/final.txt"
#gram8= "../run/8gram/final.txt"
#correct = "../splitted/dev.concept"
#documents = [gram3, gram4, gram5, gram6, gram7, gram8]
#docnames = ["3gram","4gram","5gram","6gram","7gram", "8gram"]

def levensht(name):
	
	with open(correct, "r")as mefile:
		stan = mefile.readlines()
	
	f = open(name,"w")

	d=0

	print len(stan)


	for doc in documents:
		with open(doc,"r") as myfile:
			doct = myfile.readlines()
		print len(doct)
		levnotacc = []
		levacc = []
		unacc =[]
		l=0
		for line in doct:
			if line == "\n":
				levnotacc+=[len(stan[l].split())]
				unacc += [(l,stan[l])]
			else:
				
				levacc += [Levenshtein.levenshtein(stan[l].split(),line.split())]
			
			l+=1


		f.write("FILE: %s\nEdit distance of accepted strings %s\nTotal Edit distance: %s\nNumber of unaccepted sentences: %s \nUnaccepted sentences\n" % (docnames[d],sum(levacc)/float(len(levacc)),sum(levacc+levnotacc)/float(len(levacc+levnotacc)),len(levnotacc)))
		for (n,ua) in unacc:
			f.write(str(n) + "\t" + ua + "\n")
		f.write("\n")
		d+= 1

if __name__ == '__main__':
    levensht(sys.argv[1])
 
		