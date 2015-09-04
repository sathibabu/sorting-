#!/usr/bin/env python
import time
import random
import json
import BaseHTTPServer
import cgi
import cgitb; cgitb.enable()
import sys 
		
def swap(arr,first,last):
	temp = arr[first]
	arr[first]=arr[last]
	arr[last]=temp


def partition(arr,first,last):
	pivot = first+random.randrange(last-first+1)
	swap(arr,pivot,last)
	for i in range(first,last):
		if arr[i]<=arr[last]:
			swap(arr,i,first)
			first=first+1
	swap(arr,first,last)
	return first			

def quicksort(arr,first,last):
	if first < last:
		pivot = partition(arr,first,last)
		quicksort(arr,first,pivot-1)
		quicksort(arr,pivot+1,last)

def quick(arr):
	start = time.clock();
	quicksort(arr,0,len(arr)-1)
	return(str(round((time.clock() - start)*1000,5)))



def sort_on_data(size):

	with open("random.json") as ip:
		data = json.load(ip)
	arr = data[str(size)]
	dicts = {}
	ts = quick(arr)
	dicts["random"]=ts

	with open("datasetssorted_list.json") as ip1:
		data_ss = json.load(ip1)
	arr_sl = data_ss[str(size)]
	tss = quick(arr_sl)	
	dicts["sorted"]=tss; 

	with open("reverse_list.json") as ip2:
		data_rs = json.load(ip2)
	arr_rs = data_rs[str(size)]
	trs = quick(arr_rs)	
	dicts["reverse"]=trs; 

	with open("nearly_sorted.json") as ip3:
		data_ns = json.load(ip3)
	arr_ns = data_ns[str(size)]
	tns = quick(arr_ns)	
	dicts["nearly_sorted"]=tns; 

	with open("fewunique.json") as ip4:
		data_fw = json.load(ip4)
	arr_fw = data_fw[str(size)]
	tfw = quick(arr_fw)	
	dicts["fewunique"]=tfw; 

	return dicts

def Lsort_on_data(size):

	with open("Lrandom.json") as ip:
		data = json.load(ip)
	arr = data[str(size)]
	dicts = {}
	ts = quick(arr)
	dicts["random"]=ts

	with open("Ldatasetssorted_list.json") as ip1:
		data_ss = json.load(ip1)
	arr_sl = data_ss[str(size)]
	tss = quick(arr_sl)	
	dicts["sorted"]=tss; 

	with open("Lreverse_list.json") as ip2:
		data_rs = json.load(ip2)
	arr_rs = data_rs[str(size)]
	trs = quick(arr_rs)	
	dicts["reverse"]=trs; 

	with open("Lnearly_sorted.json") as ip3:
		data_ns = json.load(ip3)
	arr_ns = data_ns[str(size)]
	tns = quick(arr_ns)	
	dicts["nearly_sorted"]=tns; 

	with open("Lfewunique.json") as ip4:
		data_fw = json.load(ip4)
	arr_fw = data_fw[str(size)]
	tfw = quick(arr_fw)	
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
	#sort_on_random(10)

	


if __name__ == "__main__":
    main()

