#Keely Hicks
#COMP 330
#Problem Set 1

import sys
import time
import math

def insertionSort(lst):
    for i in range(1, len(lst)):
        x=lst[i]
        j=i-1
        while (j>=0 and lst[j]>x):
            lst[j+1]=lst[j]
            j=j-1
        lst[j+1]=x

def mergeSort(lst):
    if len(lst)<=1:
        return lst
    else:
        mid = math.floor(len(lst)/2) #find the middle
        left = mergeSort(lst[0:mid]) #split list in two
        right = mergeSort(lst[mid:len(lst)])
        return merge(left, right); #merge them

def merge(m1, m2):
    m =[0]*(len(m1)+len(m2)) #cannot have empty list for this to work, so intialize to all zeros
    i=0
    j=0
    k=0
    while (i<len(m1) and j<len(m2)): #merge the two
        if m1[i]<=m2[j]:
           m[k]=m1[i]
           i=i+1
        else:
            m[k]=m2[j]
            j=j+1
        k=k+1
    while i<len(m1): #fill in with leftovers from m1
        m[k]=m1[i]
        k=k+1
        i=i+1
    while j<len(m2): #or fill in with leftovers from m2
        m[k]=m2[j]
        j=j+1
        k=k+1
    return m

def split(lst, first, last):
    pivot=lst[first] #calculate the pivot
    left=first
    right=last
    while left<right: #find elements on left and right of pivot
        while pivot<lst[right]:
            right=right-1
        while (left<right and lst[left]<=pivot):
            left=left+1
        if left<right:
            temp=lst[left]
            lst[left]=lst[right]
            lst[right]=temp
    pos=right
    lst[first]=lst[pos]
    lst[pos]=pivot
    return pos #return position

def quickSort(lst, first, last):
    if last<=first:
        return lst
    else:
        pos=split(lst, first, last)
        quickSort(lst, first, pos-1) #call quicksort on first half
        quickSort(lst, pos+1, last) #call quicksort on second half
    return lst
        

def parseFile(filename):
    infile = open(filename, 'r')
    lst=[int(i) for i in infile]
    return lst

def main():
    choice = input("Please enter which sorting algorithm: (i) Insertion sort, (m) Merge sort, or (q) Quick sort: ")
    
    fileName = input("Please enter the name of the input file: ")
    inputLst=parseFile(fileName)

    if choice=='i':
        start_time=time.clock()
        insertionSort(inputLst)
        elapsed_time= time.clock()-start_time
        print("Insertion sort takes: ", elapsed_time, "seconds.")
        #print(inputLst)
    elif choice=='m':
        start_time=time.clock()
        l=mergeSort(inputLst)
        elapsed_time=time.clock()-start_time
        print("Merge sort takes: ", elapsed_time, "seconds.")
        #print(l)
    elif choice=='q':
        start_time=time.clock()
        l=quickSort(inputLst, 0, len(inputLst)-1)
        elapsed_time=time.clock()-start_time
        print("Quick sort takes: ", elapsed_time, "seconds.")
        #print(l)
    else:
        print("Invalid choice")

main()
    
    
