#Name    : Md. Ragib Asif
#ID      : 21101083
#Section : 06

#Task 1 on Key index Searching & Sorting

class keyIndex:

    def __init__(self, arr):
        self.min_max = [999999999999999999999999, -9999999999999999999999999999999]
        for i in arr:
            if i<self.min_max[0]:
                self.min_max[0] = i
            elif i>self.min_max[1]:
                self.min_max[1] = i
        if self.min_max[0]<0:
            self.arr=[0]*(abs(self.min_max[0])+self.min_max[1]+1)
            for j in arr:
                self.arr[j+abs(self.min_max[0])] += 1
        else:
            self.arr=[0]*(self.min_max[1]+1)
            for j in arr:
                self.arr[j] += 1

    def searching(self, element):
        if self.min_max[0]>element or self.min_max[1]<element:
            return False
        if self.min_max[0]<0:
            if self.arr[element+abs(self.min_max[0])] > 0:
                return True
        else:
            if self.arr[element] > 0:
                return True

        return False

    def sorting(self):
        sorted_arr=[]
        if self.min_max[0]<0:
            for j in range(len(self.arr)):
                if self.arr[j]>0:
                    sorted_arr += [j-abs(self.min_max[0])]
        else:
            for j in range(len(self.arr)):
                if self.arr[j]>0:
                    sorted_arr += [j]
        return sorted_arr


array1 = [5, 1, 3, -2, 8, 5, -1, 10]
obj1=keyIndex(array1)
print(obj1.searching(5))
print(obj1.sorting())

#---------------------------------------------------------------------------------------

#Task 2 on Hashing

string_array=[0]*9
def hashing(string):
    con, num = 0, 0
    for i in string:
        if i not in ('A', 'E', 'I', 'O', 'U'):
            con += 1
        if 47 < ord(i) < 58:
            num += int(i)

    index = (con*24 + num) %9

    while string_array[index] != 0:
        index += 1
        index = index%9

    string_array[index] = string

hashing("ST1E89B8A29")
hashing("ST1E89B8A32")
hashing("ST1E89B8A31")
hashing("ST1E89B8A35")
hashing("ST1E89B8A32")
hashing("ST1E89B8A43")
print(string_array)