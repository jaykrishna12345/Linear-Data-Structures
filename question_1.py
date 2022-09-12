def printPairs(arr, n, sum):
     
    mydict = dict()
 

    for i in range(n):
        temp = sum - arr[i]
        if temp in mydict:
            count = mydict[temp]
            for j in range(count):
                print("(", temp, ", ", arr[i],
                      ")", sep = "", end = '\n')
                       
        if arr[i] in mydict:
            mydict[arr[i]] += 1
        else:
            mydict[arr[i]] = 1
 
if __name__ == '__main__':
     
    arr = [ 1, 5, 7, -1, 5 ]
    n = len(arr)
    sum = 6
 
    printPairs(arr, n, sum)