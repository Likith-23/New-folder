#function to calculate the number that is odd occuring
def odd_occuring(arr):
    res = 0
    #traverse the array
    for element in arr:
        #Xor with the result
        res = res ^ element
    return res
#initialise our array
arr = []
#take array size as input
n = int(input("ENTER ARRAY SIZE..."))
#take array input 
while(n):
    num = int(input("ENTER NUMBER..."))
    arr.append(num)
    n -= 1
print("\nODD OCCURING NUMBER IS...", odd_occuring(arr))