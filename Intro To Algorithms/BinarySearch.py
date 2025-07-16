
#**Binary Search**

#Binary search is an algorithm made to help parse a array/list to find a particular value.

#**How It Works**
def binary_search(arr, target):

    # Set the two inital pointers low and high to represent the start and end of the array.
    low=0
    high=len(arr)-1

    #Generally you will use a while loop to iterate through the array while also cutting arrays in half
        #The cuts are made to reduce the search space by checking whether the middle element is equal to, less than, or greater than the target value.
            #think of it as a game of "higher or lower" where you adjust your search range based on the comparison.
    while low <= high:
        mid = (low + high) // 2

        #Checks if the middle element is equal to the target value.
        if arr[mid] == target:
            return mid
        #If the middle element is less than the target, adjust the low pointer to search the right half.
        elif arr[mid] < target:
            low = mid + 1
        #If the middle element is greater than the target, adjust the high pointer to search the left half.
        else:
            high = mid - 1
    return "Not Found"

arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target=5
print(binary_search(arr, target))

#**Time Complexity**
#The time complexity of binary search is O(log n), where n is the number of elements in the array. This is because each iteration effectively halves the search space, leading to a logarithmic growth in the number of iterations required to find the target value.


#**Extra Notes**

#Binary search requires there to be a sorted array to work properly.
    #The algorithm is based on a game of higher or lower, if it is not sorted then the algorithm will not properly set the low/high pointers correctly based on the midpoint
#Binary search is efficient for large datasets, as it significantly reduces the number of comparisons needed to find a target value compared to linear search.