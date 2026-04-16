class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num,count=0,0

        for i in nums:
            if count == 0:
                num=i
            count+=(1 if num==i else -1)
        return num