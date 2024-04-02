def find_repeated(arr):
    arrUnique = [arr[0]]
    arrRepeat = []
    for e in arr[1:]:
        if not (e in arrRepeat):
            if e in arrUnique:
                arrUnique.remove(e)
                arrRepeat.append(e)
            else:
                arrUnique.append(e)
    return arrUnique, arrRepeat

'''
print("run test --------------------------------------------------------------------")
array = []
array.append([1, 18, 2, 3, 1, 1, 3, 4, 5, 1, 5, 6, 6, 7, 8, 9, 8])
array.append([1, 2, 3, 2, 1, 3, 4, 5, 1, 5, 6, 6, 7, 9, 8])
array.append([8])
array.append([8, 8])

for a in array:
    print("Input Array\t: ", a)
    arrUnique, arrRepeat = find_repeated(a)
    print("Unique Array\t: ", arrUnique)
    print("Repeated Array\t: ", arrRepeat)
'''
