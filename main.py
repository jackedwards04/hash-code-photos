import preproc
import interestalg as ia
import itertools
'''
TO-DO:

Fix/improve interest alg
Improve preproc
Make the program not suck ;)

DON'T COMMIT IF IT DOESN'T WORK
'''
nodes = 5
pairs = [
	[1,2],
	[1,3],
	[1,4],
	[1,5],
	[2,3],
	[2,4],
	[2,5],
	[3,4],
	[3,5],
	[4,5]
]
graph = ia.gen(pairs,nodes)
igraph = graph[1]
graph = graph[0]



def finalize(graph):
	out = []
	out.append([i for i in ia.flatten(graph) if ia.flatten(graph).count(i)==1][0])
	for n in range(0,len(graph)):
		try:
			out.append([a[1] for a in graph if a[1] not in out and a[0]==out[-1]][0])
		except:
			out.append([a[0] for a in graph if a[0] not in out and a[1]==out[-1]][0])
	for i in range(0,len(out)-1):
		print(str(out[i])+'--|'+str(igraph[i])+'|--',end='')
	print(out[-1])
	print('Total:')
	return(sum(igraph))
print(finalize(graph))
