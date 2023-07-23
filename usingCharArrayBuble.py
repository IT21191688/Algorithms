

def bubleSort(arr):

    n = len(arr)

    for i in range(1, n):

        for j in range(1, n-i+1):

            if arr[j] < arr[j-1]:

                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


arr = []


for i in range(0, 10):

    arr.append(list(input("Enter the char character: ")))


print(bubleSort(arr))
