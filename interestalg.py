import random
graph = []
nodes = 5
interests = [
    ]
iout = []
#TO BE CHANGED
def nodeInterest(node):
	return(random.randint(0,20))

def nInterests(graph):
	out = []
	for i in range(0,len(graph)):
		out.append(nodeInterest(graph[i]))
	return(out)

def getPairInterest(pair):
  return([i[2] for i in interests if i[0:2]==pair])

def flatten(lis):
  return([sublist[0] for sublist in lis]+[sublist[1] for sublist in lis])

def isGraph(graph):
  return(len([g for g in flatten(graph) if flatten(graph).count(g) < 3])==len(flatten(graph)) and len([g for g in flatten(graph) if flatten(graph).count(g) == 1]) == 2)

def allNode(graph,size):
  return((size*2)-2 == len(flatten(graph)))

def nextNode(interestIn):
  return(max(interestIn, key = lambda s: s[2]))

def graphGen(interests,node):
	print(interests)
	while not allNode(graph,node):
			tNode = nextNode(interests)
			if (isGraph(graph+[tNode])):
				graph.append(tNode[0:2])
				iout.append(interests[interests.index(tNode)][2])
			interests.pop(interests.index(tNode))
    
def gen(inte,nod):
	interests = inte
	interests = [n+[nodeInterest(n)] for n in interests]
	nodes = nod
	graphGen(interests,nodes)
	return([graph,iout])