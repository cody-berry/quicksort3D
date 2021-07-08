# 2021.07.08 Cody
# quicksort3D
#
# v0.1 recursive quicksort in console
# v0.2 iterative quicksort in console
# v0.3 visualize iterative quicksort with rect() and yield+generators
# v0.4 element class for colors
# v0.5 3D boxes


# Import from random; important for sort
from random import *


# * recursive quicksort goes here: 

def recursive_quicksort(arr, start, stop):
    # Here, we start with base case: 
    if(start >= stop):
        return
    
    # Otherwise, we select a pivot index, piv_idx
    piv_idx = stop
    
    # Then, select a pivot element, which we will use to compare to other elements, or 
    # piv_ele
    piv_ele = arr[piv_idx]
    
    # Not nessecary until we randomize the pivot element.
    #arr[piv_idx], arr[len(arr) - 1] = arr[len(arr) - 1], larr[piv_idx}
    
    # Let's create a lesser than pointer, ltp, to keep track of where we are going to 
    # seperate the list when we recurse.
    ltp = start
    
    # Moving through the list
    for i in range(start, stop):
        if(arr[i] < piv_ele):
            # Oh no! We've found an element out of place! We need to swap that into the 
            # correct place. 
            arr[i], arr[ltp] = arr[ltp], arr[i]
            
            # Now that we've found an element lesser than the pivot, we can increase our 
            # lesser than pointer, ltp. 
            ltp += 1
            
    # Now we can swap the pivot element to the lesser than pointer, ltp, so that everything
    # lesser than the pivot is to the left of it and everything greater than it is to the 
    # right of it.
    # print("Swapping " + str(arr[ltp]) + " with " + str(arr[piv_idx]) + ".")
    arr[ltp], arr[stop] = arr[stop], arr[ltp]
    
    # Not everything is sorted to the left of the pivot and the right of the pivot. I mean
    # not nessesarely.
    
    recursive_quicksort(arr, start, ltp-1)
    recursive_quicksort(arr, ltp+1, stop)
        


def setup():
    len_list = 1000
    lst = []
    for i in range(0, len_list):
        lst.append(randint(3, 1100))
    recursive_quicksort(lst, 0, len(lst) - 1)
    print(lst)


def draw():
    pass
