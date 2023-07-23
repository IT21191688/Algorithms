# using buble sort algorthm

# buble sort completed


def bubleSort(arr):

    n = len(arr)

    for i in range(1, n):
        for j in range(1, n-i+1):

            if arr[j] < arr[j-1]:

                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


def binarySearch(arr, min, max, key):

    if max < min:
        return -1

    else:

        mid = (min+max)//2

        if arr[mid] > key:
            return binarySearch(arr, min, mid-1, key)
        elif arr[mid] < key:
            return binarySearch(arr, mid+1, max, key)
        else:
            return mid


arr = []

for i in range(0, 10):
    arr.append(int(input("Enter the number: ")))

# unsorted array
print(arr)


# after the sorting
print(bubleSort(arr))


key = int(input("Enter the Number:"))


# afte the Binary search

result = binarySearch(arr, 0, len(arr)-1, key)

if result != -1:
    print("Serch value found: ", result)
else:
    print("Search value not found ")
