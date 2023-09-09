class Solution:
        def sums():
            nums=[2,7,45,0]
            target=47
            preMap={}
            for i ,n in enumerate(nums):
                diff = target - n
                if diff in preMap:
                    return[print(preMap[diff],i)]
                preMap[n]=i
            return
                