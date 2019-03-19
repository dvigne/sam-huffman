import numpy as np

arr = np.array([.07, .2, .19, .36, .18])
encoded = np.zeros_like(arr, dtype="int64")
openFile = open("test.txt", "w+")

def doEncoding(arr, fileObj, curr, pos):
    if(max(arr) == 0):
        return
    if(arr[pos] == max(arr)):
        encoded[pos] = curr
        arr[pos] = 0
        doEncoding(arr, fileObj, curr = curr + 1, pos = 0)
    doEncoding(arr, fileObj, curr = curr, pos = pos + 1)

doEncoding(arr, openFile, 0, 0)
for x in encoded:
    openFile.writelines(bin(x)[2:] + "\n")
