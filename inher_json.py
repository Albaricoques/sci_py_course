import sys
import json 


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited)
    return visited


t = json.loads(input())


d=dict()
for i in t:
	if i['name'] not in d:
		d[i['name']]=list()
	for j in i['parents']:
		if j not in d:
			d[j]=list()
		d[j].append(i['name'])

d2 = dict()
for i in d:
	d2[i]=len(dfs(d,i, []))

for i in sorted(d2.keys()):
	print(i, ':', d2[i])
