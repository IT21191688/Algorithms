

arr = []

for i in range(0, 11):
    arr.append(int(input("Enter the Number :")))


def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    if low < high:
        q = partition(arr, low, high)
        quickSort(arr, low, q-1)
        quickSort(arr, q+1, high)


quickSort(arr, 0, len(arr)-1)

print("Sorted Array")

for i in range(len(arr)):
    print(arr[i])
