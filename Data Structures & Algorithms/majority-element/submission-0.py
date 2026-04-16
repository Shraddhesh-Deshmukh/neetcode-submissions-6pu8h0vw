class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=len(nums)/2

        data={}
        for i in nums:
            if i in data:
                data[i]+=1
            else:
                data[i]=1
        
        for num in data:
            if data[num]>maj:
                return num
        
        return -1