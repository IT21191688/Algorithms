

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


arr = []

for i in range(0, 10):
    arr.append(int(input("Enter the number: ")))


print(insertionSort(arr))
