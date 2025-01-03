class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        ans = 0

        for i in range(len(nums)-1):
            leftSum += nums[i]
            rightSum -= nums[i]

            if leftSum >= rightSum:
                ans+=1
        return ans
