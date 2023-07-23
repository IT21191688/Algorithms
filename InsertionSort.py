# sort wena ewa mulata ekthu wei

arr = []


for i in range(1, 11):
    arr.append(int(input("Enter The Number")))

print(arr)


def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

    return arr


print(InsertionSort(arr))
