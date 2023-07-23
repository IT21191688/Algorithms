

def paratition(A, p, r):

    x = A[r]

    i = p-1

    for j in range(p, r-1):

        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quickSort(A, p, r):

    if p < r:
        q = paratition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


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

    arr.append(int(input("Enter the Number: ")))

x = int(input("Please enter the what you need search: "))


quickSort(arr, 0, len(arr)-1)

print(arr)

result = binarySearch(arr, 0, len(arr)-1, x)


if result != -1:
    print("Your value in the Array: ", result)

else:
    print("Your value not in the array ")
