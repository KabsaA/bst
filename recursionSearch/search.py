#!python

def linear_search(array, item,index):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    #return linear_search_recursive(array, item,0)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index):
    if index < len(array): # only if index is less then the amount of elements in array
        if array[index] == item:
            return index
        else:
            return linear_search_recursive(array, item, index+1)
    else:
        return None

#print(linear_search_recursive([1,2,3,6,9],6,0))
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return binary_search_recursive(array, item,0,len(array)-1)
    return binary_search_iterative(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left = 0
    right = len(array) - 1
    mid = 0

    while left <= right:
        mid = (right + left) // 2

        if array[mid] < item:
                left = mid + 1

        elif array[mid] > item:
                right = mid - 1

        else:
            return mid

    return None


#print(str(binary_search_iterative([1,2, 3, 4, 10, 40 ] , 10)))


def binary_search_recursive(array, item,left,right):

    if left > right:
        return None

    mid = left + (right - left) // 2
    middle = array[mid]

    if middle == item:
        return mid

    elif middle < item:
        return binary_search_recursive(array, item, mid + 1, right)

    else:
        return binary_search_recursive(array, item, left, mid - 1)


#array = [2,3,4,10,12]
#print(str(binary_search_recursive(array,10, 0, len(array)-1)))
