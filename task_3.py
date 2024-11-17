def quick_sort(array):
    arr_len = len(array)

    # Base condition
    if arr_len < 2:
        return array

    # Choosing middle element as pivot
    pivot = arr_len // 2
    pivot_el = array[pivot]

    # Separating left and right array of pivot
    left = [i for i in array if i < pivot_el]
    right = [i for i in array if i > pivot_el]

    # Separate array for all the element which are equal to pivot element
    mid = [i for i in array if i == pivot_el]

    # Call quick_sort recursively on left and right array
    return quick_sort(left) + mid + quick_sort(right)


def main():
    n = int(input("Enter number of integers to be entered: "))
    arr = []
    for i in range(n):
        el = int(input(f"Enter integer ({i + 1}): "))
        arr.append(el)

    print(f"Unsorted array: {arr}")
    arr = quick_sort(arr)
    print(f"Sorted array: {arr}")


main()
