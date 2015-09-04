print "<title>Sorting Algorithms comparision</title>"
print "<p>Sorting Algorithms</p>"
print "<p>Insertion sort</p>"
arr = [5,1,6,2,4,4]
#insertion(arr)
print "<p>selection sort</p>"
#selection(arr)
print "<p>Bubble sort</p>"
#bubble(arr)
print "<p>Shell sort</p>"
#shell(arr)
print "<p>Merge sort</p>"
#merge(arr)
##print "<p>Heap sort</p>"
#heapsort(arr)
print "<p>quick sort</p>"
#quick(arr)

print "<p> 3 way quicksort</p>"
#arr = [5,1,6,2,4,4,9]
#quick3way(arr)

print "<p>Random Numbers</p>"
rands = []
rands = random_list(100)
insertion(rands)
#print rands

print "<p>Sorted List</p>"
sorts = []
sorts = sorted_list(100)
print sorts

print "<p>Reverse List</p>"
Reverse_list = []
Reverse_list = reverse_list(100)
print Reverse_list

print "<p>Nearly sorted</p>"
nearly_sorted_list = []
nearly_sorted_list = nearly_sorted(100,4)
print nearly_sorted_list


print "<p style='color:red'>Few Unique</p>"
fewunique_list = []
fewunique_list = fewunique(100,3)
print fewunique_list
