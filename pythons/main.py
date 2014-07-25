import sys
import SplitData as sd
import CreateTrans as ct
import CreateLex as cl

TRAIN = '../MT2_Data/ATIS.train.txt'
TEST = '../MT2_Data/ATIS.train.txt'
DEV = '../MT2_Data/ATIS.dev.txt'
STOPW = '../english.stop.txt'
TRAINCO= '../MT2_Data/ATIS.train.txt.co'

def lexicons():
	cl.get_lexicon(TRAIN,"../fst/train")
	cl.get_lexicon(TRAIN,"../fst/trainco",True,STOPW)

def splitdata():
	sd.split3(TRAIN,"../splitted/train")
	sd.split3(TRAINCO,"../splitted/trainco")
	sd.split3(TEST,"../splitted/test")
	sd.split2(DEV,"../splitted/dev")

def createtrans():
	ct.maketransducer(TRAIN,"../fst/train")
	ct.maketransducer(TRAINCO,"../fst/trainco")	
	ct.maketransducer(TRAIN,"../fst/test")

def main(function_type):
	if (function_type == 'lex'):
        	lexicons()	
	elif (function_type == 'splits'):
        	splitdata()
    	elif (function_type == 'trans'):
        	createtrans()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
	lexicons
        splitdata()
        createtrans()