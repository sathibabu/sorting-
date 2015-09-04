#!/usr/bin/env python
import time
import random
import json
import BaseHTTPServer
import cgi
import cgitb; cgitb.enable()
import sys 
R = random.Random(42)
import random
R = random.Random(42)

def qsort(L):
	start = time.clock()
	quicksort(L,0,len(L))
	return(str(round((time.clock() - start)*1000,5)))

def quicksort(L,start,stop):
	if stop - start < 2: return
	key = L[R.randrange(start,stop)]
	e = u = start
	g = stop
	while u < g:
		if L[u] < key:
			swap1(L,u,e)
			e = e + 1
			u = u + 1
		elif L[u] == key:
			u = u + 1
		else:
			g = g - 1
			swap1(L,u,g)
	quicksort(L,start,e)
	quicksort(L,g,stop)

def swap1(A,i,j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

def swap(arr,first,last):
	temp = arr[first]
	arr[first]=arr[last]
	arr[last]=temp


def quick3waySort(arr,first,last):
	if last - first<2:
		return
	key = arr[R.randrange(first,last)]
	#key = arr[first]
	p=first
	q=first
	r=last
	while q < r:
		if arr[q] < key:
			swap(arr,p,q)
			q=q+1
			p = p+1
		elif  arr[q]==key:
			q=q+1
		else:
			r = r-1
			swap(arr,q,r)
		quick3waySort(arr,first,p)
		quick3waySort(arr,q,last)			

def quick3way(arr):
	start = time.clock();
	quick3waySort(arr,0,len(arr))
	return(str(round((time.clock() - start)*1000,5)))



def sort_on_data(size):

	with open("random.json") as ip:
		data = json.load(ip)
	arr = data[str(size)]
	dicts = {}
	ts = qsort(arr)
	dicts["random"]=ts

	with open("datasetssorted_list.json") as ip1:
		data_ss = json.load(ip1)
	arr_sl = data_ss[str(size)]
	tss = qsort(arr_sl)	
	dicts["sorted"]=tss; 

	with open("reverse_list.json") as ip2:
		data_rs = json.load(ip2)
	arr_rs = data_rs[str(size)]
	trs = qsort(arr_rs)	
	dicts["reverse"]=trs; 

	with open("nearly_sorted.json") as ip3:
		data_ns = json.load(ip3)
	arr_ns = data_ns[str(size)]
	tns = qsort(arr_ns)	
	dicts["nearly_sorted"]=tns; 

	with open("fewunique.json") as ip4:
		data_fw = json.load(ip4)
	arr_fw = data_fw[str(size)]
	tfw = qsort(arr_fw)	
	dicts["fewunique"]=tfw; 

	return dicts

def Lsort_on_data(size):

	with open("Lrandom.json") as ip:
		data = json.load(ip)
	arr = data[str(size)]
	dicts = {}
	ts = qsort(arr)
	dicts["random"]=ts

	with open("Ldatasetssorted_list.json") as ip1:
		data_ss = json.load(ip1)
	arr_sl = data_ss[str(size)]
	tss = qsort(arr_sl)	
	dicts["sorted"]=tss; 

	with open("Lreverse_list.json") as ip2:
		data_rs = json.load(ip2)
	arr_rs = data_rs[str(size)]
	trs = qsort(arr_rs)	
	dicts["reverse"]=trs; 

	with open("Lnearly_sorted.json") as ip3:
		data_ns = json.load(ip3)
	arr_ns = data_ns[str(size)]
	tns = qsort(arr_ns)	
	dicts["nearly_sorted"]=tns; 

	with open("Lfewunique.json") as ip4:
		data_fw = json.load(ip4)
	arr_fw = data_fw[str(size)]
	tfw = qsort(arr_fw)	
	dicts["fewunique"]=tfw; 

	return dicts


def main():
	
	print ("Content-type: text/html")
	print
	#print "<p>Sorting Algorithms</p>"
	sys.setrecursionlimit(2000009)
	form = cgi.FieldStorage()
	if form.has_key("param1"):
		if form["param1"].value == "1000000" or form["param1"].value == "2000000" :
			sys.setrecursionlimit(2000009)
			print Lsort_on_data(form["param1"].value)
	 	else:
	 		print sort_on_data(form["param1"].value)

	


if __name__ == "__main__":
    main()

