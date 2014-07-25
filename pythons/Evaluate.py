import sys
import Levenshtein

mt1result = "../mt1result"
correct = "../atis.hlti.250.test"
documents = [mt1result]

def levensht():
	
	with open(correct, "r")as mefile:
		stan = mefile.readlines()
	
	for doc in documents:
		with open(doc,"r") as myfile:
			doct = myfile.readlines()
			notaccepted = 0
			levnotacc = 0
			levacc = 0
			i= 2
			l= 0
			while l < len(stan):
				
				if doct[i][0] == "\n":
					notaccepted +=1
					
					levnotacc+=len(stan[l].split())
				else:
					
					levacc += Levenshtein.levenshtein(stan[l].split(),doct[i].split())
				i+=3
				l+=1
	print(int(levnotacc))	
				
def main(function_type):
	if (function_type == 'lev'):
        	levensht()	
	elif (function_type == 'hamm'):
        	hammings()

if __name__ == '__main__':
	if len(sys.argv) == 2:
		main(sys.argv[1])
	else:
		levensht(documents,standard)
	
		