class Solution:
    def summaryRanges(self, nums):
        left, right = 0, 0
        res = []
        while left < len(nums):
            while right < len(nums) - 1 and nums[right + 1] - nums[right] == 1:
                right += 1
            if left == right:
                res.append(str(nums[left]))
            else:
                res.append(f"{nums[left]}->{nums[right]}")
            left = right + 1
            right = left
        return res


if __name__ == '__main__':
    ss = Solution()
    nums = [0, 1, 2, 4, 5, 7]
    res = ss.summaryRanges(nums)
    print(res)

