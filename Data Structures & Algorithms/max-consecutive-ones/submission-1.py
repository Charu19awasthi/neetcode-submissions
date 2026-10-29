class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count1=0
        count2=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                count1+=1
            elif nums[i]==0:
                if count1>count2:
                    count2=count1
                    count1=0
                else:
                    count1=0
        if count1>count2:
            return count1
        else:
            return count2



        