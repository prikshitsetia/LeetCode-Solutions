class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        def func(item):
            return item[1]
        boxTypes=sorted(boxTypes,key=func,reverse=True)
        print(boxTypes)
        count=0
        for i in boxTypes:
            if i[0]<=truckSize:
                count=count+(i[0]*i[1])
                truckSize=truckSize-i[0]
            else:
                count=count+truckSize*i[1]
                break
        return count