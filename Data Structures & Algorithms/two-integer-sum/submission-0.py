class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictonary={}
        
        for index,num in enumerate(nums):
            differ=target-num
            if differ in dictonary:
                return[dictonary[differ],index]
            dictonary[num]=index