# using insertion sort and binary search

# insertion sort completed


def insertionSort(arr):

    n = len(arr)

    for j in range(1, n):

        key = arr[j]

        i = j-1

        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]

            i = i-1

        arr[i+1] = key

    return arr


def BinarySearch(arr, min, max, key):

    if max < min:
        return -1

    else:
        mid = (min+max)//2

        if arr[mid] > key:
            return BinarySearch(arr, min, mid-1, key)
        elif arr[mid] < key:
            return BinarySearch(arr, mid+1, max, key)
        else:
            return mid


arr = []

for i in range(0, 10):
    arr.append(int(input("Enter the Number ")))


print("Unsorted Array ")
print(arr)


print("Sorted Array")
sorted = insertionSort(arr)
print(arr)

print("Find the value using Binary Treee")
y = int(input("Enter the Number what you need search: "))

result = BinarySearch(arr, 0, len(arr)-1, y)

if result != -1:
    print("Your Number is in this array index:", result)

else:
    print("Your number is not in this array")
