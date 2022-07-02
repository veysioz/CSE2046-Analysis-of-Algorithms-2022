import time
import random
import statistics

# Generate 3 input sets
def generate_input(input):
    # Set-1 : In order
    col = []
    for i in range(1,1000):
        col.append(i)
    input.append(col)
    col = []
    
    # Set-2 : In reverse order
    for i in range(999,0,-1):
        col.append(i)
    input.append(col)
    
    # Set-3 : In random order
    input.append(random.sample(range(1,1000), 999))

# Insertion Sort Algorithm
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1 # Move elements that are greater than key
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

# Merge Sort Algorithm
def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2 # Find mid
        L = array[:mid] # Left side of array
        R = array[mid:] # Right side of array
        merge_sort(L) # Sort Left
        merge_sort(R) # Sort Right
        i = j = k = 0
        while i < len(L) and j < len(R): # Copy to temp L[] and R[]
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        while i < len(L): # Last Check
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R): # Last Check
            array[k] = R[j]
            j += 1
            k += 1

# Pivot is the first element
def first_element(array, low, high):
    pivot = array[low]
    i = high + 1

    for j in range(high, low, -1):
        if array[j] >= pivot:
            i = i - 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i - 1], array[low]) = (array[low], array[i - 1]) # Put pivot to its place
    return i - 1

# Pivot is the middle element
def middle_element(array, low, high):
    middle = int((high-low)/2)
    array[low], array[middle] = array[middle], array[low]
    pivot = array[low]
    i = high + 1

    for j in range(high, low, -1):
        if array[j] >= pivot:
            i = i - 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i - 1], array[low]) = (array[low], array[i - 1]) # Put pivot to its place
    return i - 1

# Pivot is the last element
def last_element(array, low, high):
    pivot = array[high]
    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1]) # Put pivot to its place
    return i + 1

# Select median of three
def median_of_three(array, low, high):
    middle = int((high-low)/2)
    median = statistics.median([array[low], array[middle], array[high]])

    # Call pivot functions according to median
    if median == array[low]:
        return first_element(array, low, high)
    elif median == array[middle]:
        return middle_element(array, low, high)
    elif median == array[high]:
        return last_element(array, low, high)

# Quick Sort Algorithm
def quick_sort(array, low, high):
    if low < high:
        pi = first_element(array, low, high)
        
        quick_sort(array, low, pi - 1) # Recursive for left
        quick_sort(array, pi + 1, high) # Recursive for right

# Partial Selection Sort Algorithm
def partial_selection_sort(array, k):
    for i in range(0, k): # Loop until k
        min_index = i
        min_value = array[i]
        for j in range(i+1, len(array)):
            if array[j] < min_value:
                min_index = j
                min_value = array[j]
                array[i], array[min_index] = array[min_index], array[i] # Find the minimum element and swap

# It heapifies for Partial Heap Sort
def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[largest] < array[l]: # Left child exists & Greater than root
        largest = l
    if r < n and array[largest] < array[r]: # Right child exists & Greater than root
        largest = r
    if largest != i: # Change root
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest) # Heapify root

# Partial Heap Sort Algorithm
def partial_heap_sort(array, k):
    n = len(array)
    for i in range(n//2 - 1, -1, -1): # Build maxheap
        heapify(array, n, i)
    for i in range(n-1, k-1, -1): # (n-k) times max removal
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array[0]

# Quick Select Algorithm
def quick_select(array, l, r, k, pivot):
    if (k > 0 and k <= r - l + 1):
        # Pivot is first or median-of-three according to pivot parameter
        if pivot == 0:
            index = first_element(array, l, r)
        if pivot == 1:
            index = median_of_three(array, l, r)

        if (index - l == k - 1):
            return array[index]
        if (index - l > k - 1):
            return quick_select(array, l, index - 1, k, pivot)
        
        return quick_select(array, index + 1, r, k - index + l - 1, pivot)

def main():
    input = []
    generate_input(input)
    x = 0 # Dataset ID | 0 : Best Case | 1 : Worst Case | 2 : Random
    k = 20 # kth smallest number
    
    for x in range(3): # Loop in 3 input file
        if x == 0:
            print("Best Case: ")
        elif x == 1:
            print("Worst Case: ")
        elif x == 2:
            print("Random Case: ")

        for y in range(7):
            try:
                dataset = input[x].copy()
                timer_start = time.time()

                if y == 0:
                    name = "Insertion Sort"
                    insertion_sort(dataset)
                    kth_smallest = str(dataset[k-1])
                elif y == 1:
                    name = "Merge Sort"
                    merge_sort(dataset)
                    kth_smallest = str(dataset[k-1])
                elif y == 2:
                    name = "Quick Sort (Pivot is First)"
                    quick_sort(dataset, 0, len(dataset) - 1)
                    kth_smallest = str(dataset[k-1])
                elif y == 3:
                    name = "Partial Selection Sort"
                    partial_selection_sort(dataset, k)
                    kth_smallest = str(dataset[k-1])
                elif y == 4:
                    name = "Partial Heap Sort"
                    kth_smallest = str(partial_heap_sort(dataset, k))
                elif y == 5:
                    name = "Quick Select (Pivot is First)"
                    kth_smallest = str(quick_select(dataset, 0, len(dataset)-1, k, 0))
                elif y == 6:
                    name = "Quick Select (Pivot is Median-of-Three)"
                    kth_smallest = str(quick_select(dataset, 0, len(dataset)-1, k, 1))

                timer_end = time.time()
                timer_result = timer_end - timer_start

                print("\n\t" + name + ":" + "\n\t\t" + str(k) + ". smallest element is " + kth_smallest + ". " + str(round((timer_result * 1000), 3)) + " Milliseconds")
            
            except:
                print("\n\t" + name + ":" + "\n\t\t" + "Could not be calculated.")
            
        print()

if __name__ == "__main__":
    main()