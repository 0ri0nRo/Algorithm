# Counting sort

# This algoritm is usefull when we had a binary array and it's in the same level with "Fondi" in 
    # quicksort algorithm
#With satelite data the double elements are deteleted

def CountingSortSenzaDatiS(A):
    n = len(A)
    k = max(A)
    C = [0] * (k+1)
    for j in range(n):
        C[A[j]] += 1
    j = 0
    for i in range (k+1):
        while(C[i] > 0):
            A[j] = i
            j += 1
            C[i] -= 1
    print("CountingSortSenzaDatiS")
    print("A: ", A)
    return 

#This algorithm sort an array and the double elements remain in B

def CountingSort(A):
    size = len(A) - 1
    C = [0] * size
    m = max(A)
    B = [0] * m
    i = 0
    for i in range(0, size):
        B[A[i]] += 1
    for i in range(0, m):
        B[i] += B[i-1]
    i = size - 2
    while i >= 0:
        C[B[A[i]]-1] = A[i]
        B[A[i]] -= 1
        i -= 1
    print("CountingSortSenzaDatiS")
    print("A: ", A)
    print("B: ", B)
    return 


def quicksort(A, left, right):
    if left < right:
        partition_pos = partition(A, left, right)
        quicksort(A, left, partition_pos-1)
        quicksort(A, partition_pos+1, right)
    return "Quicksort",  A

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


    # funtion to divide the lists in the two sublists  
def merge_sort(list1, left_index, right_index):  
    if left_index >= right_index:  
        return  
    middle = (left_index + right_index)//2  
    merge_sort(list1, left_index, middle)  
    merge_sort(list1, middle + 1, right_index)          
    merge(list1, left_index, right_index, middle)
        # Defining a function for merge the list  
def merge(list1, left_index, right_index, middle):  
       # Creating subparts of a lists  
    left_sublist = list1[left_index:middle + 1]  
    right_sublist = list1[middle+1:right_index+1]  
      
        # Initial values for variables that we use to keep  
        # track of where we are in each list1  
    left_sublist_index = 0  
    right_sublist_index = 0  
    sorted_index = left_index  
      
        # traverse both copies until we get run out one element  
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):  
      
            # If our left_sublist has the smaller element, put it in the sorted  
            # part and then move forward in left_sublist (by increasing the pointer)  
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:  
            list1[sorted_index] = left_sublist[left_sublist_index]  
            left_sublist_index = left_sublist_index + 1  
            # Otherwise add it into the right sublist  
        else:  
            list1[sorted_index] = right_sublist[right_sublist_index]  
            right_sublist_index = right_sublist_index + 1  
            # move forward in the sorted part  
        sorted_index = sorted_index + 1 
        # we will go through the remaining elements and add them  
    while left_sublist_index < len(left_sublist):  
        list1[sorted_index] = left_sublist[left_sublist_index]  
        left_sublist_index = left_sublist_index + 1  
        sorted_index = sorted_index + 1  
      
    while right_sublist_index < len(right_sublist):  
        list1[sorted_index] = right_sublist[right_sublist_index]  
        right_sublist_index = right_sublist_index + 1  
        sorted_index = sorted_index + 1  


def binary_search(my_list, low, high, elem):
   if high >= low:
      mid = (high + low) // 2
      if my_list[mid] == elem:
         return mid
      elif my_list[mid] > elem:
         return binary_search(my_list, low, mid - 1, elem)
      else:
         return binary_search(my_list, mid + 1, high, elem)
   else:
      return -1

lst = [1, 9, 11, 21, 34, 54, 67, 90]
print(binary_search(lst, 0, len(lst)-1, 11))

lst = [5, 6, 2, 1, 5, 7, 8]
merge_sort(lst, 0, 6)
print(lst)

lst = [5, 6, 2, 1, 5, 7, 8]

print(quicksort(lst, 0, 6))
print(" ")
print(CountingSort(lst))
print(CountingSortSenzaDatiS(lst))
