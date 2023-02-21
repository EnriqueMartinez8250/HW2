import time
import sys



###Here is my timeEfficieny algorithm, i added a new set of features
def timeEfficiency(funcName, maxNum):
    start_time = time.time()
    comparison = funcName(maxNum)   #problem 2-2 the comparison count
    stop_time = time.time()
    time_taken = stop_time - start_time
    print("Start time: {}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))))
    print("End time: {}".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stop_time))))
    print("Time efficiency: {:.6f} seconds".format(time_taken))
    print("The total comparisons: {}".format(comparison))


###Insertion sort Algorithm
def insertionSort(number):
    comparison = 0
    for i in range(1, len(number)):
        key = number[i]
        j = i-1
        while j >= 0 and key < number[j]:
            number[j+1] = number[j]
            j-=1
            comparison += 1
        number[j + 1] = key
    return comparison


###Merge sort Algorithm
def mergeSort(number):
    if len(number) > 1:
        mid = len(number)//2
        L = number[:mid]
        R = number[mid:]
        left_comparison = mergeSort(L)
        right_comparison = mergeSort(R)
        comparison = left_comparison + right_comparison

        i = j = k = 0

        while i < len(L) and j < len(R):  
            comparison += 1
            if L[i] <= R[j]:
                number[k] = L[i]
                i+=1
            else:
                number[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            number[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            number[k] = R[j]
            j += 1
            k +=1
        return comparison
    else:
        return 0




####Here is my driver code, it is a user input program as i decided that having the user pick which text file is probably most useful
def main():
    print("Algorithms homework problem #2")
    user_input = True

    while(user_input == True):
        print("Please select which file you wish to run: ")
        user_selection = int(input("1. rand1000000.txt\n2. rand1000.txt\n3. Exit\nUserSelection: "))
        if(user_selection == 1):
            file = open("rand1000000.txt","r")
            header = file.readline()
            list = file.read().split()
            print("The time for Insertionsort Algorithm is below")
            timeEfficiency(insertionSort,list)
            print("<----------------------------->")
            print("The time for Mergesort Algorithm is below")
            timeEfficiency(mergeSort,list)
            print("Sorted file: ",list)
            break
        if(user_selection ==2):
            file = open("rand1000.txt","r")
            header = file.readline()
            list = file.read().split()
            print("The time for Insertionsort Algorithm is below")
            timeEfficiency(insertionSort,list)
            print("<----------------------------->")
            print("The time for Mergesort Algorithm is below")
            timeEfficiency(mergeSort,list)
            print("Sorted file: ",list)
            break
        if(user_selection == 3):
            print("Exiting!")
            sys.exit(0)
main()



