
arr = []

for i in range(0, 10):
    arr.append(int(input("Enter the number: ")))


x = int(input("Enter the Search value: "))


# arr==array
# low== start Index
# high==end index
# x== search index
# mid ==midle index


def BinarySearch(arr, low, high, x):
    # chech the base case

    if high >= low:
        mid = (high+low)//2

        if arr[mid] == x:
            return mid

        elif arr[mid]:
            return BinarySearch(arr, low, mid-1, x)

        else:
            return BinarySearch(arr, mid+1, high, x)
    else:
        return -1


result = BinarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at the index:", result)
else:
    print("Element is not present in array")
