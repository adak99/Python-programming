def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[high] = arr[high], arr[i]

    return i


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    size = int(input("Enter the size of the array: "))
    arr = []

    print("Enter the elements of the array: ")
    for _ in range(size):
        arr.append(int(input()))

    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array elements:", *arr)
