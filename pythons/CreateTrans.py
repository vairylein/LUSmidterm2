def maketransducer(textdoc, name):
	
	d = {}
	e = {}

	with open (textdoc,"r") as myfile:
		for line in myfile:
			words=line[:-1].split()
			if len(words) > 2:
				d[words[0] + " " + words[1]] = 0
				if words[2] == "null":
					e[words[1] + " " + words[1]] = 0
				else:
					e[words[1] + " " + words[2]] = 0

	f = open(name + ".g.fsa","w")
	g = open(name + ".w2c.fsa","w")

	for key in sorted(d.iterkeys()):
		word = key.split()
		f.write("0\t0\t" + word[0] + "\t" + word [1]+ "\n")
	print("g transducer for " + name +" written")

	
	for key in sorted(e.iterkeys()):
		word = key.split()
		g.write("0\t0\t" + word[0] + "\t" + word [1]+ "\n")
	print("w2c transducer for " + name +" written")

	f.write("0\t0\t<unk>\t<unk>\t\n")
	f.write("0\n")
	g.write("0\t0\t<unk>\t<unk>\t\n")
	g.write("0\n")

	f.close()
	g.close()