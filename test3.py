

def partition(arr, p, r):

    x = arr[r]

    i = p-1

    for j in range(p, r):
        if arr[j] <= x:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i+1


def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q-1)
        quickSort(arr, q+1, r)


arr = []

for i in range(0, 10):
    arr.append(int(input("Enter the Number :")))

quickSort(arr, 0, len(arr)-1)
for i in range(len(arr)):
    print(arr[i])
