# Apriori algorithm implementation

import itertools
import csv

fileh=open('apriori.txt','r')
items=list()

reader = csv.reader(fileh, delimiter=',')
for row in reader:
    items.append(row)

#items=[['bread','milk'],['bread','diapers','beer','eggs'],['milk','diapers','beer','cola'],['bread','milk','diapers','beer'],['bread','milk','diapers','cola']]

print 'Enter the support threshold percentage:'
per=input()
sup=(per/float(100))*len(items)

def sortItems(items):
	for i in items:
		i.sort()
	return items

def calcInitialFset(items):
	d=dict()
	for i in items:
		for j in i:
			if j not in d:
				d[j]=1
			else:
				d[j]+=1
	for (k,v) in d.items():
		if d[k]<sup:
			del d[k]
	return d

items=sortItems(items)

f1=calcInitialFset(items)

def pruning(nl,n):
	i=0
	while i<len(n):
		if n[i]<sup:
			del nl[i]
			del n[i]
		else:
			i+=1
	return nl,n

def findfreq(items,l):
	n=list()
	for i in range(len(l)):
		n.append(0)
	for i in items:
		for j in range(len(l)):
			if set(l[j])<=set(i):
				n[j]+=1
	return n

def apriorigenfirst(a):
	l=list(itertools.combinations(a, 2))
	nl=list()
	for i in l:
		nl.append(list(i))
	nl=sortItems(nl)
	n=findfreq(items,nl)
	nl,n=pruning(nl,n)
	global f1
	f1=[]
	return nl,n

def removedup(l):
	nl=list()
	for i in l:
		if i not in nl:
			nl.append(i)
	return nl
def apriorigen(a,k):
	l=list()
	if k==2:
		return apriorigenfirst(a)
	else:
		for i in a:
			for j in a:
				if i!=j and i[0]==j[0]:
					l1=list(set(i)|set(j))
					l1.sort()
					l.append(l1)
					l.sort()
		l=removedup(l)
		n=findfreq(items,l)
		l,n=pruning(l,n)
		return l,n

k=1
while True:
	k+=1
	c1,count1=apriorigen(f1,k)
	if len(c1)<=0:
		break
	f1=c1

if f1==[]:
	print '\nNo item can be bought with this support threshold'
else:
	print '\nThe items that are frequently bought together(using the specified support threshold):\n'
	print f1
