# Implements a sorted list.
# CSC 202, Lab 5
# Given code, Summer '19


class SortedList:
    """
    A sorted collection of elements
    NOTE: Do not alter this class.
    """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this sorted list:
        self.size = 0

    def __eq__(self, other):
        if type(other) != SortedList or self.size != other.size:
            return False

        for idx in range(self.size):
            if self.array[idx] != other.array[idx]:
                return False

        return True

    def __repr__(self):
        return "SortedList(%d, %r, %d)"\
               % (self.capacity, self.array, self.size)


def size(lst):
    """
    Calculate the size of a sorted list.
    TODO: Implement this function. It must have O(1) complexity.

    :param lst: A SortedList
    :return: The number of elements in the sorted list
    """
    return lst.size


def get(lst, idx):
    """
    Get the element at an index.
    TODO: Implement this function. It must have O(1) complexity.

    :param lst: A SortedList
    :param idx: An index at which to get an element
    :return: The element in the sorted list at the index
    :raise IndexError: If the index is out-of-bounds
    """
    if idx >= lst.size or idx < 0:
        raise IndexError
    return lst.array[idx]


def insert(lst, value):
    """
    Insert an element in sorted order, doubling capacity first if necessary.
    TODO: Implement this function. It must have O(n) complexity.

    :param lst: A SortedList
    :param value: A comparable value to insert as an element
    """
    # If the size is equal to the capacity, then:
    #     Set the capacity to capacity * 2.
    #     Create a new array of that capacity.
    #     (copy the elements from the old array into the new array)
    #     Set the array to the new array.
    #
    # Start with i being the size.
    # While i - 1 is greater than or equal to zero
    #  and the element at i - 1 is greater than the given value, do:
    #     Set the element at i in the array to the element at i - 1.
    #     Decrement i.
    #
    # Set the element at i in the array to the given value.
    # Increment the size.

    if lst.size == lst.capacity:
        lst.capacity = lst.capacity * 2
        new_lst = SortedList()
        new_lst.capacity = lst.capacity
        new_lst.size = lst.size
        new_lst.array = [None] * new_lst.capacity
        for i in range(lst.size):
            new_lst.array[i] = lst.array[i]
        lst.array = new_lst.array

    i = lst.size
    while (i - 1) >= 0 and lst.array[i - 1] >= value:
        lst.array[i] = lst.array[i - 1]
        i -= 1

    lst.array[i] = value
    lst.size += 1


def remove(lst, idx):
    """
    Remove the element at an index.
    TODO: Implement this function. It must have O(n) complexity.

    :param lst: A SortedList
    :param idx: An index at which to remove an element
    :return: The removed element
    :raise IndexError: If the index is out-of-bounds
    """
    # For i from the given idx to the size - 1, do:
    #     Set the element at i in the array to the element at i + 1.
    #
    # Decrement the size.
    if idx >= lst.size or idx < 0:
        raise IndexError
    removed = lst.array[idx]
    for i in range(idx, lst.size - 1):
        lst.array[i] = lst.array[i + 1]

    lst.size -= 1
    return removed


def find(lst, value):
    """
    Find the index of an element.
    TODO: Implement this function. It must have O(log n) complexity.

    :param lst: A SortedList
    :param value: A comparable value to find as an element
    :return: The index of an element equal to the value
    :raise ValueError: If no element is equal to the value
    """
    # Start with the low index being 0 and the high index being size - 1.
    #
    # While the low index is less than or equal to the high index, do:
    #     Set the mid index to (high + low) // 2.
    #     If the element at mid in the array is equal to the given value, then:
    #         Return mid.
    #     Else if the element at mid is less than the given value, then:
    #         Set the low index to mid + 1.
    #     Else, do:
    #         Set the high index to mid - 1.
    #
    # Return (the given value is not in the given list).
    low = 0
    high = lst.size - 1

    while low <= high:
        mid = (high + low) // 2
        if lst.array[mid] == value:
            return mid
        elif lst.array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    raise ValueError


def create(array, size):
    """
    Create a new sorted list from an array.
    TODO: Implement this function. It must have O(n log n) complexity.

    :param array: An unsorted array of comparable values
    :param size: A length of a given array
    :return: A new SortedList containing the array's values in sorted order
    """
    # Sort the given array: low is 0, high is size - 1.
    # Return a new sorted list containing the sorted array.
    sorted_array = sort(array, 0, size - 1)
    sorted_list = SortedList()
    for val in sorted_array:
        insert(sorted_list, val)
    return sorted_list

def sort(array, low, high):
    # NOTE: It is possible to write an iterative merge sort -- it is possible
    #       to write *anything* iteratively -- but a merge sort lends itself
    #       naturally to recursion. We must repeatedly identify and sort
    #       smaller arrays: smaller versions of the same problem.
    #
    # If low is equal to high:
    #     Return (a new array containing the element at low in the array).
    # Else, do:
    #     Set the mid index to (high + low) // 2.
    #     Recursively sort the left half: low is low, high is mid.
    #     Recursively sort the right half: low is mid + 1, high is high.
    #     Merge the sorted halves.
    #     Return the merged array.
    if low == high:
        new_array = [None] * 1
        new_array[0] = array[low]
        return new_array
    else:
        mid = (high + low) // 2
        left = sort(array, low, mid)
        right = sort(array, mid + 1, high)

        size_a = mid - low + 1
        size_b = high - mid
        merged = merge(left, size_a, right, size_b)
        return merged

def merge(array_a, size_a, array_b, size_b):
    # Create a new array of capacity size_a + size_b.
    # Start with indices i, j, and k all being 0.
    #
    # While i is less than size_a or j is less than size_b, do:
    #     If i is greater than or equal to size_a, then:
    #         Set element k of the new array to element j of array_b.
    #         Increment j and k.
    #     Else if j is greater than or equal to size_b, then:
    #         Set element k of the new array to element i of array_a.
    #         Increment i and k.
    #     Else if element j of array_b is less than element i of array_a, then:
    #         Set element k of the new array to element j of array_b.
    #         Increment j and k.
    #     Else, do:
    #         Set element k of the new array to element i of array_a.
    #         Increment i and k.
    #
    # Return the new array.
    new_array = [None] * (size_a + size_b)
    i, j, k = 0, 0, 0

    while i < size_a or j < size_b:
        if i >= size_a:
            new_array[k] = array_b[j]
            j += 1
            k += 1
        elif j >= size_b:
            new_array[k] = array_a[i]
            i += 1
            k += 1
        elif array_b[j] < array_a[i]:
            new_array[k] = array_b[j]
            j += 1
            k += 1
        else:
            new_array[k] = array_a[i]
            i += 1
            k += 1
    return new_array

