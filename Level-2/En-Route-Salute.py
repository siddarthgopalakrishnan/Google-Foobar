def answer(s):
	salutes = 0
	l = list(s)
	for i in xrange(len(l)):
		if l[i] == '>':
			for j in xrange(i,len(l)):
				if l[j] == '<':
					salutes += 2
	return salutes