#!/usr/bin/env python
import time
import random
import json
import BaseHTTPServer
import cgi
import cgitb; cgitb.enable()
import sys  
		
def gapInsertion(pos,arr,gap):
	for i in range(pos+gap,len(arr),gap):
		current = arr[i]
		curr_pos=i
		while curr_pos>=gap and arr[curr_pos-gap] > current:
			arr[curr_pos]=arr[curr_pos-gap]
			curr_pos = curr_pos-gap
		arr[curr_pos]=current
			

def shell(arr):
	start = time.clock();
	subarr = len(arr)//2
	while subarr >0 :
		for i in range(subarr):
			gapInsertion(i,arr,subarr)
		subarr = subarr//2
	return(str(round((time.clock() - start)*1000,5)))

def sort_on_data(size):

	with open("random.json") as ip:
		data = json.load(ip)
	arr = data[str(size)]
	dicts = {}
	ts = shell(arr)
	dicts["random"]=ts

	with open("datasetssorted_list.json") as ip1:
		data_ss = json.load(ip1)
	arr_sl = data_ss[str(size)]
	tss = shell(arr_sl)	
	dicts["sorted"]=tss; 

	with open("reverse_list.json") as ip2:
		data_rs = json.load(ip2)
	arr_rs = data_rs[str(size)]
	trs = shell(arr_rs)	
	dicts["reverse"]=trs; 

	with open("nearly_sorted.json") as ip3:
		data_ns = json.load(ip3)
	arr_ns = data_ns[str(size)]
	tns = shell(arr_ns)	
	dicts["nearly_sorted"]=tns; 

	with open("fewunique.json") as ip4:
		data_fw = json.load(ip4)
	arr_fw = data_fw[str(size)]
	tfw = shell(arr_fw)	
	dicts["fewunique"]=tfw; 

	return dicts

def Lsort_on_data(size):

	with open("Lrandom.json") as ip:
		data = json.load(ip)
	arr = data[str(size)]
	dicts = {}
	ts = shell(arr)
	dicts["random"]=ts

	with open("Ldatasetssorted_list.json") as ip1:
		data_ss = json.load(ip1)
	arr_sl = data_ss[str(size)]
	tss = shell(arr_sl)	
	dicts["sorted"]=tss; 

	with open("Lreverse_list.json") as ip2:
		data_rs = json.load(ip2)
	arr_rs = data_rs[str(size)]
	trs = shell(arr_rs)	
	dicts["reverse"]=trs; 

	with open("Lnearly_sorted.json") as ip3:
		data_ns = json.load(ip3)
	arr_ns = data_ns[str(size)]
	tns = shell(arr_ns)	
	dicts["nearly_sorted"]=tns; 

	with open("Lfewunique.json") as ip4:
		data_fw = json.load(ip4)
	arr_fw = data_fw[str(size)]
	tfw = shell(arr_fw)	
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

