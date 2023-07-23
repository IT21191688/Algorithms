
def selectionSort(arr):

    n = len(arr)

    for j in range(0, n-1):
        smallest = j

        for i in range(j+1, n):

            if arr[i] < arr[smallest]:
                smallest = i
            arr[j], arr[smallest] = arr[smallest], arr[j]

           #
        # print(arr)

    return arr


arr = []

for i in range(0, 10):
    arr.append(int(input("Enter the number:")))


print("Unsorted Array")
print(arr)

print("Sorted Array")
print(selectionSort(arr))
