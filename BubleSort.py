
def sortAlgorthm(arr):
    n = len(arr)

    for i in range(1, n):

        # starting 1 value and compare nera one
        for j in range(1, n-i+1):

            if arr[j] < arr[j-1]:

                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


arr = []

for i in range(0, 10):
    arr.append(int(input("Enter The Number ")))

print(sortAlgorthm(arr))
