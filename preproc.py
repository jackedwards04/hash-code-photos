def proc(inputf,outputf):
	with open(inputf, 'r') as f2:
  	  data = f2.read()
	data = data.split('\n')
	data = data[1:]
	ndata = []
	for d in data:
		ndata.append(d[0] + d[3:] + '\n')
	with open(outputf,'w') as iw:
		for n in ndata:
			iw.write(n)