#!/usr/bin/env python
import time
import random
import json
import BaseHTTPServer
import cgi
import cgitb; cgitb.enable()
import sys 
		
def merge(arr):
	if len(arr)>1:
		mid = len(arr)//2
		lefthalf = arr[:mid]
		righthalf = arr[mid:]
		merge(lefthalf)
		merge(righthalf)
		#mergeArrays(arr,p,mid,q)
		#temp = []
		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				arr[k]=lefthalf[i]
				i=i+1
		#k=k+1
			else:
				arr[k]=righthalf[j]
				j=j+1
			k=k+1
				#k=k+1	#k=k+1
		while i<len(lefthalf):
			arr[k]=lefthalf[i]
			i=i+1
			k=k+1
		while j<len(righthalf):
			arr[k]=righthalf[j]
			k=k+1
			j=j+1
		#print arr		

def swap(arr,first,last):
	temp = arr[first]
	arr[first]=arr[last]
	arr[last]=temp

def mergesort(arr):
	start = time.clock();
	merge(arr)
	return(str(round((time.clock() - start)*1000,5)))



def sort_on_data(size):

	with open("random.json") as ip:
		data = json.load(ip)
	arr = data[str(size)]
	dicts = {}
	ts = mergesort(arr)
	dicts["random"]=ts

	with open("datasetssorted_list.json") as ip1:
		data_ss = json.load(ip1)
	arr_sl = data_ss[str(size)]
	tss = mergesort(arr_sl)	
	dicts["sorted"]=tss; 

	with open("reverse_list.json") as ip2:
		data_rs = json.load(ip2)
	arr_rs = data_rs[str(size)]
	trs = mergesort(arr_rs)	
	dicts["reverse"]=trs; 

	with open("nearly_sorted.json") as ip3:
		data_ns = json.load(ip3)
	arr_ns = data_ns[str(size)]
	tns = mergesort(arr_ns)	
	dicts["nearly_sorted"]=tns; 

	with open("fewunique.json") as ip4:
		data_fw = json.load(ip4)
	arr_fw = data_fw[str(size)]
	tfw = mergesort(arr_fw)	
	dicts["fewunique"]=tfw; 

	return dicts

def Lsort_on_data(size):

	with open("Lrandom.json") as ip:
		data = json.load(ip)
	arr = data[str(size)]
	dicts = {}
	ts = mergesort(arr)
	dicts["random"]=ts

	with open("Ldatasetssorted_list.json") as ip1:
		data_ss = json.load(ip1)
	arr_sl = data_ss[str(size)]
	tss = mergesort(arr_sl)	
	dicts["sorted"]=tss; 

	with open("Lreverse_list.json") as ip2:
		data_rs = json.load(ip2)
	arr_rs = data_rs[str(size)]
	trs = mergesort(arr_rs)	
	dicts["reverse"]=trs; 

	with open("Lnearly_sorted.json") as ip3:
		data_ns = json.load(ip3)
	arr_ns = data_ns[str(size)]
	tns = mergesort(arr_ns)	
	dicts["nearly_sorted"]=tns; 

	with open("Lfewunique.json") as ip4:
		data_fw = json.load(ip4)
	arr_fw = data_fw[str(size)]
	tfw = mergesort(arr_fw)	
	dicts["fewunique"]=tfw; 

	return dicts


def main():
	
	print ("Content-type: text/html")
	print
	#print "<p>Sorting Algorithms</p>"
	form = cgi.FieldStorage()
	if form.has_key("param1"):
		if form["param1"].value == "1000000" or form["param1"].value == "2000000" :
			sys.setrecursionlimit(2000009)
			print Lsort_on_data(form["param1"].value)
	 	else:
	 		print sort_on_data(form["param1"].value)

	


if __name__ == "__main__":
    main()

