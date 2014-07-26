def split4(textdoc, name):
	f = open(name + ".word","w")
	g = open(name + ".class","w")
	h = open(name + ".concept","w")
	j = open(name + ".mix","w")
	u = open(name + ".unk","w")

	with open (textdoc,"r") as myfile:
		i = 1
		newline = False
		d = {}

		for line in myfile:
			words=line[:-1].split()
			if i == 1:
				d[words[0]]= 0
				f.write(words[0])
				if words[0] in d.keys():
					word = "<unk>"
				else:
					word = words[0]
				u.write(word)
				g.write(words[1])
				h.write(words[2])
				if words[2] == "null":
					j.write(word)
				if words[2] 				
				else:
					j.write(words[2])
				newline = False
				i=2

			elif words == []:
				newline = True	
			else:
				if newline:
					f.write("\n" + words[0])
					g.write("\n" + words[1])
					h.write("\n" + words[2])
					if words[2] == "null":
						j.write("\n" + words[0])
					else:
						j.write("\n" + words[2])
					newline = False
					
				else:
					f.write(" " + words[0])
					g.write(" " + words[1])
					h.write(" " + words[2])
					if words[2] == "null":
						j.write(" " + words[0])
					else:
						j.write(" " + words[2])
					newline = False
					
					
			

	f.close()
	g.close()
	h.close()
	j.close()
	u.close()		

def split3(textdoc, name):
	f = open(name + ".word","w")
	g = open(name + ".class","w")
	h = open(name + ".concept","w")
	j = open(name + ".mix","w")
	u = open(name + ".unk","w")

	with open (textdoc,"r") as myfile:
		i = 1
		newline = False
		d = {}

		for line in myfile:
			words=line[:-1].split()
			if i == 1:
				f.write(words[0])
				g.write(words[1])
				h.write(words[2])
				if words[2] == "null":
					j.write(words[0])
				else:
					j.write(words[2])
				newline = False
				i=2

			elif words == []:
				newline = True	
			else:
				if newline:
					f.write("\n" + words[0])
					g.write("\n" + words[1])
					h.write("\n" + words[2])
					if words[2] == "null":
						j.write("\n" + words[0])
					else:
						j.write("\n" + words[2])
					newline = False
					
				else:
					f.write(" " + words[0])
					g.write(" " + words[1])
					h.write(" " + words[2])
					if words[2] == "null":
						j.write(" " + words[0])
					else:
						j.write(" " + words[2])
					newline = False
					
					
			

	f.close()
	g.close()
	h.close()
	j.close()		

def split2(textdoc, name):
	f = open(name + ".word","w")
	g = open(name + ".concept","w")
	j = open(name + ".mix","w")

	with open (textdoc,"r") as myfile:
		i = 1
		newline = False
		for line in myfile:
			words=line[:-1].split()

			if i == 1:
				f.write(words[0])
				g.write(words[1])
				newline = False
				i+= 2
			elif words == [] :
				newline = True	
			else:
				if newline:
					f.write("\n" + words[0])
					g.write("\n" + words[1])
					if words[1] == "null":
						j.write("\n" + words[0])
					else:
						j.write("\n" + words[1])
					newline = False
					
				else:
					f.write(" " + words[0])
					g.write(" " + words[1])
					if words[1] == "null":
						j.write(" " + words[0])
					else:
						j.write(" " + words[1])
					newline = False
					
					
				i+=1	

	
	f.close()
	g.close()
	j.close()
