arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
smallers = []
for a in arr:
    a.sort()
    smallers.insert(0, a[0])
    


total = 0
for i in range(len(smallers)):
    newTotal = smallers[i] + total
    total = newTotal
print(total)
        