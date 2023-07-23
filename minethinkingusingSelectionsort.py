

def selectionSort(arr):

    n = len(arr)

    for j in range(0, n-1):

        smallest = j

        for i in range(j+1, n):
            if arr[i] < arr[smallest]:
                smallest = i

        arr[j], arr[smallest] = arr[smallest], arr[j]

    return arr


def binarySearch(A, min, max, key):

    if max < min:
        return -1

    else:
        mid = (min+max)//2

        if A[mid] > key:

            return binarySearch(A, min, mid-1, key)

        elif A[mid] < key:
            return binarySearch(A, mid+1, max, key)
        else:
            return mid


arr = []


for i in range(0, 10):
    arr.append(int(input("Enter the number: ")))


selectionSort(arr)


x = int(input("Enter the What you need search : "))


result = binarySearch(arr, 0, len(arr)-1, x)


if result != -1:
    print("your value in the array that index is ", result)


else:
    print("Your value not in this array")
