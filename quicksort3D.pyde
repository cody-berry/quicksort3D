# 2021.07.08 Cody
# quicksort3D
#
# v0.1   recursive quicksort in console *
# v0.2   iterative quicksort in console *
# v0.3   visualize iterative quicksort with rect() and yield+generators *
# v0.4   element class for colors *
# v0.5   3D boxes *
# v0.6   green done indicator boxes *
# v0.6.1 fix vertical alignment bug. clean up code *
# v0.7   replace green done indicator boxes with checkmark fragments

# Add PeasyCam
add_library("PeasyCam")

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
                lst[i].c = color(13, 2, 25, 69)
        if start <= len_list - 1:
            lst[start].c = color(151, 99, 50, 69)
        if stop >= 0:
            lst[stop].c = color(185, 85, 50, 69)
        yield
        if start >= stop:
            if start <= len_list - 1:
                lst[start].reset_color()
            if stop >= 0:
                lst[stop].reset_color()
            for i in range(start, len(arr)):
                if(i) >= 0:
                    lst[i].done = True
                    yield
            continue
        
        # Otherwise, we select a pivot index, piv_idx
        piv_idx = randint(start, stop)
        arr[piv_idx].c = color(65, 86, 94, 69)
        yield
        
        # Then, select a pivot element, which we will use to compare to other elements, or 
        # piv_ele
        piv_ele = arr[piv_idx]
        
        # Not nessecary until we randomize the pivot element.
        arr[piv_idx].c = color(341, 46, 93, 69)
        arr[stop].c = color(341, 46, 93, 69)
        arr[piv_idx], arr[stop] = arr[stop], arr[piv_idx]
        yield
        
        # Let's create a lesser than pointer, ltp, to keep track of where we are going to 
        # seperate the list when we recurse.
        ltp = start
        arr[piv_idx].reset_color()
        arr[stop].c = color(65, 86, 94, 69)
        yield
        
        # Moving through the list
        for i in range(start, stop):
            if(arr[i] < piv_ele):
                # Oh no! We've found an element out of place! We need to swap that into the 
                # correct place. 
                arr[i].c = color(341, 46, 93, 69)
                arr[ltp].c = color(341, 46, 93, 69)
                arr[i], arr[ltp] = arr[ltp], arr[i]
                yield
                
                # Now that we've found an element lesser than the pivot, we can increase our 
                # lesser than pointer, ltp. 
                ltp += 1
                arr[i].reset_color()
                arr[ltp].reset_color()
                arr[start].c = color(151, 99, 50, 69)
                yield
                
        # Now we can swap the pivot element to the lesser than pointer, ltp, so that everything
        # lesser than the pivot is to the left of it and everything greater than it is to the 
        # right of it.
        arr[ltp].c = color(341, 46, 93, 69)
        arr[stop].c = color(341, 46, 93, 69)
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
        arr[ltp].c = color(65, 86, 94, 69)
        yield
        call_stack.append((ltp+1, stop))
        
        for i in range(start, stop+1):
            lst[i].reset_color()
        yield
        


def setup():
    global len_list, lst, sorter, cam
    size(1400, 700, P3D)
    colorMode(HSB, 360, 100, 100, 100)
    len_list = 40
    lst = []
    cam = PeasyCam(this, 0, 0, 0, 500)
    for i in range(0, len_list):
        lst.append(Element(randint(0, 100)))
        # We need to create a generator so we can call .next() to see updates to the sorting.
        sorter = iterative_quicksort(lst, 0, len(lst)-1)
        
    
    # TODO: bug. this relationship should be linear, not exponential
    # frameRate(7**(len_list/67))
    if len_list > 10:
        frameRate(len_list)
    else:
        frameRate(10)
    
    # TODO: Fix error: Every few blocks, instead of having a background line between, 
    # they'll look squished together. Maybe this is a rounding error from division. We can 
    # fix this by creating a function that returns the optimal width that depends on the space
    # on the left side and right side, the number of pixels between each bar, and the width
    # of the canvas, with python's special width variable.
    

def draw():
    global len_list, lst, sorter
    background(209, 95, 23)
    noStroke()
    # The reason why we need the BOX_HEIGHT_SCALE to be a scale is because if it were a
    # constant, then the sort wouldn't be amazing because there would be no swaps.
    # In this case, I wasn't able to make the bottom blocks aligned while still 
    # keeping the height scale non-doubled, so the BOX_HEIGHT_SCALE assignment
    # will be half as much as the real value.
    
    BOX_WIDTH = 5
    BOX_HEIGHT_SCALE = 1
    BOX_DEPTH = 0
    BOX_WIDTH_SPACING = 1
    # I call the boxes underneath representing that the element box is done a donebox.
    DONEBOX_HEIGHT = BOX_WIDTH/2
    CHECKMARK_BASE = 200  # Base of the checkmark
    CHECKMARK_HEIGHT = 20  # Height of the checkmark fragment
    # The y difference between each fragment. Note that it will become negative once 
    # the checkmark reaches less than lst[i]/3 though.
    CHECKMARK_FRAGMENT_Y_DIFFERENCE = 5 
    
    
    # Visualizes the list to see changes to the sort over time with rectangles.
    for i in range(0, len_list):
        fill(lst[i].c)
        pushMatrix()
        # For the box, we will need to translate because the box only takes in the size, 
        # or else the arguments will be too crazy.
        
        # Because the box defaults to (0, 0), you need to translate or else the box with the 
        # maximum height will only show up. Defaulting to (0, 0) means that if you try to not 
        # translate at all, then you will end up with the center being (0, 0).
        translate(i*BOX_WIDTH+i*BOX_WIDTH_SPACING, -lst[i].value*BOX_HEIGHT_SCALE, 0)        
        box(BOX_WIDTH, lst[i].value*2*BOX_HEIGHT_SCALE, BOX_DEPTH)
        popMatrix()
        
        
        # green underline mode:
        #if lst[i].done:
            #pushMatrix()
            #fill(107, 78, 86, 40)
            ## Same as last comment, the default with not translated will be at the center. 
            ## Same when you translate!
            #translate(i*BOX_WIDTH+i*BOX_WIDTH_SPACING, DONEBOX_HEIGHT,  0)
            #box(BOX_WIDTH, DONEBOX_HEIGHT*2, BOX_DEPTH)
            #popMatrix()
            
        # checkmark fragment mode:
        if lst[i].done:
            fill(107, 78, 86, 40)
        else:
            fill(0, 78, 86, 40)
        
        # CHECKMARK_Y is the center of the checkmark at the y axis. Most checkmarks have a tip at the bottom
        # and I'm representing the tip as a bend in the abs() function. In desmos, you'll see that no matter
        # how close you zoom in to the point (0, 0), it is still a sharp point, so that's what representing
        # the tip here. Also, to ensure that the checkmark doesn't overlap with the element boxes, we need a
        # checkmark base that keeps track of the base of the checkmark, or CHECKMARK_BASE.
        CHECKMARK_Y = abs(len(lst)/3-i)*CHECKMARK_FRAGMENT_Y_DIFFERENCE + CHECKMARK_BASE
        
        # To align our checkmark properly, we need the checkmark fragment width to be the same
        # as the box width.
        pushMatrix()
        translate(i*BOX_WIDTH + i*BOX_WIDTH_SPACING, -CHECKMARK_Y, 0)
        box(BOX_WIDTH, CHECKMARK_HEIGHT, BOX_DEPTH)
        popMatrix()
            
            
            
        
    try:
        sorter.next()
    except StopIteration:
        pass
        
    
    
    
    
