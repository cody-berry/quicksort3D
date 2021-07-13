# 2021.07.08 Cody
# quicksort3D
#
# v0.1 recursive quicksort in console *
# v0.2 iterative quicksort in console *
# v0.3 visualize iterative quicksort with rect() and yield+generators
# v0.4 element class for colors
# v0.5 3D boxes


# Import from random; important for sort
from random import *
from Element import *


# * recursive quicksort goes here: 
def recursive_quicksort(arr, start, stop):
    # Here, we start with base case: 
    if(start >= stop):
        return
    
    # Otherwise, we select a pivot index, piv_idx
    piv_idx = randint(start, stop)
    
    # Then, select a pivot element, which we will use to compare to other elements, or 
    # piv_ele
    piv_ele = arr[piv_idx]
    
    # Not nessecary until we randomize the pivot element.
    arr[piv_idx], arr[stop] = arr[stop], arr[piv_idx]
    
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
    arr[ltp], arr[stop] = arr[stop], arr[ltp]
    
    # Not everything is sorted to the left of the pivot and the right of the pivot. I mean
    # not nessesarely.
    
    recursive_quicksort(arr, start, ltp-1)
    recursive_quicksort(arr, ltp+1, stop)


# There are yields here because we are going to visualize it. In order to see changes over time
# we have to place yields to call the .next() on the generator.
def iterative_quicksort(arr, start, stop):
    global len_list
    # Call stack to keep track of calls:
    call_stack = [(start, stop)]    
    
    # While loop so that we can keep iterating
    
    while call_stack:
        # Here, we start with base case: 
        start, stop = call_stack.pop()
        for i in range(start, stop):
            if i > stop and i < start:
                lst[i].c = (13, 2, 50)
        if start <= len_list - 1:
            lst[start].c = color(151, 99, 50)
        if stop >= 0:
            lst[stop].c = color(185, 85, 50)
        yield
        if(start >= stop):
            if start <= len_list - 1:
                lst[start].reset_color()
            if start >= 0:
                lst[stop].reset_color()
            continue
        
        # Otherwise, we select a pivot index, piv_idx
        piv_idx = randint(start, stop)
        arr[piv_idx].c = color(65, 86, 94)
        yield
        
        # Then, select a pivot element, which we will use to compare to other elements, or 
        # piv_ele
        piv_ele = arr[piv_idx]
        
        # Not nessecary until we randomize the pivot element.
        arr[piv_idx].c = color(341, 46, 93)
        arr[stop].c = color(341, 46, 93)
        arr[piv_idx], arr[stop] = arr[stop], arr[piv_idx]
        yield
        
        # Let's create a lesser than pointer, ltp, to keep track of where we are going to 
        # seperate the list when we recurse.
        ltp = start
        arr[piv_idx].reset_color()
        arr[stop].c = color(65, 86, 94)
        yield
        
        # Moving through the list
        for i in range(start, stop):
            if(arr[i] < piv_ele):
                # Oh no! We've found an element out of place! We need to swap that into the 
                # correct place. 
                arr[i].c = color(341, 46, 93)
                arr[ltp].c = color(341, 46, 93)
                arr[i], arr[ltp] = arr[ltp], arr[i]
                yield
                
                # Now that we've found an element lesser than the pivot, we can increase our 
                # lesser than pointer, ltp. 
                ltp += 1
                arr[i].reset_color()
                arr[ltp].reset_color()
                arr[start].c = color(151, 99, 50)
                yield
                
        # Now we can swap the pivot element to the lesser than pointer, ltp, so that everything
        # lesser than the pivot is to the left of it and everything greater than it is to the 
        # right of it.
        arr[ltp].c = color(341, 46, 93)
        arr[stop].c = color(341, 46, 93)
        arr[ltp], arr[stop] = arr[stop], arr[ltp]
        yield
        
        # Not everything is sorted to the left of the pivot and the right of the pivot. I mean
        # not nessesarely.
        # But since we aren't doing it recursively, instead of this:
        # recursive_quicksort(arr, start, ltp-1)
        # recursive_quicksort(arr, ltp+1, stop)
        # We do this. We'll have to do some base casing becuase less than 2 elements means
        # that there is nothing to sort. This idea of being sorted prevents an infinite
        # loop.
        
        call_stack.append((start, ltp-1))
        arr[stop].reset_color()
        arr[ltp].c = color(65, 86, 94)
        yield
        call_stack.append((ltp+1, stop))
        
        for i in range(start, stop+1):
            lst[i].reset_color()
        yield
        


def setup():
    global len_list, lst, sorter
    size(1000, 200)
    colorMode(HSB, 360, 100, 100, 100)
    len_list = 150
    lst = []
    for i in range(0, len_list):
        lst.append(Element(randint(55, 100)))
        # We need to create a generator so we can call .next() to see updates to the sorting.
        sorter = iterative_quicksort(lst, 0, len(lst)-1)
        
    
    # TODO: bug. this relationship should be linear, not exponential
    # frameRate(7**(len_list/67))
    frameRate(len_list/2)
    
    # TODO: Fix error: Every few blocks, instead of having a background line between, 
    # they'll look squished together. Maybe this is a rounding error from division. We can 
    # fix this by creating a function that returns the optimal width that depends on the space
    # on the left side and right side, the number of pixels between each bar, and the width
    # of the canvas, with python's special width variable.
    

def draw():
    global len_list, lst, sorter
    background(209, 95, 66)
    noStroke()
    
    spacing = 3 # len_list needs to be a multiple of len_list-spacing
    
    
    # Visualizes the list to see changes to the sort over time with rectangles.
    for i in range(0, len(lst)):
        fill(lst[i].c)
        # For the top one, the corner that we actually place the
        rect(i*round((width - spacing*2)/len_list) + spacing,
             height - 50 - lst[i].value, 
             (width - spacing*2)/len_list-1, 
             lst[i].value)
        
    try:
        sorter.next()
    except StopIteration:
        pass
        
    
    
    
    
