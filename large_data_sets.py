#!/usr/bin/env python
import time
import random
import json 
#import asyncio



def random_list(size):
	out = []
	for i in range(size):
		k= random.randrange(0,100)
		out.append(k)
	return out

def sorted_list(size):
	out = []
	for	i in range(10,size+size):
		out.append(i)
	return out			


def reverse_list(size):
	out = []
	for i in range(size+10,10,-1):
		out.append(i)
	return out	

def nearly_sorted(size,hop):
	out = []
	for i in range(size):
		if i % hop ==0:
			out.append(random.randrange(0,100))
		else:
			out.append(i)
	return out			

def fewunique(size,hop):
	out = []

	for i in range(0,size):
		if i % hop == 0 and i!=0:
			j = random.randrange(0,i)
			out.append(out[j])
		else:
			out.append(random.randrange(0,100))
	return out		





def generate_datasets():
	list_size = [1000000,2000000]
	json_arr = {}
	for i in range(len(list_size)):
		json_arr[list_size[i]]=random_list(list_size[i])
	
	with open("Lrandom.json",'w') as outfile:
		json.dump(json_arr,outfile)
	json_arr_fewunique={}	
	for i in range(len(list_size)):
		json_arr_fewunique[list_size[i]]=fewunique(list_size[i],5)
	with open("Lfewunique.json",'w') as outfile:
		json.dump(json_arr_fewunique,outfile)
	json_arr_nearly_sorted={}
	for i in range(len(list_size)):
		json_arr_nearly_sorted[list_size[i]]=nearly_sorted(list_size[i],5)
	with open("Lnearly_sorted.json",'w') as outfile:
		json.dump(json_arr_nearly_sorted,outfile)
	json_arr_reverse={}
	for i in range(len(list_size)):
		json_arr_reverse[list_size[i]] = reverse_list(list_size[i])
	with open("Lreverse_list.json",'w') as outfile:
		json.dump(json_arr_reverse,outfile)
	json_arr_sorted = {}
	for i in range(len(list_size)):
		json_arr_sorted[list_size[i]]=sorted_list(list_size[i])
	with open("Ldatasetssorted_list.json",'w') as outfile:
		json.dump(json_arr_sorted,outfile)	


def main():
	print ("Content-type: text/html")
	print
	print ("<p>Sorting Algorithms</p>")
	generate_datasets()


if __name__ == "__main__":
    main()

