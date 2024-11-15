arr = [11,10,9,8,8,7,6,5,4,3,2,1]
def sort(lst):
    def swap(item1,item2):
        temp = item2
        item2 = item1
        item1 = temp
        return item1,item2
    sorting = lst
    correct = False
    while not correct:
        changes = 0
        for i in range(len(lst)-1):
            if sorting[i] > sorting[i+1]:
                sorting[i],sorting[i+1] = swap(sorting[i],sorting[i+1])
                print(sorting)
                changes += 1
        if changes == 0:
            correct = True
    return sorting


print(sort(arr))
#print(arr)

