# https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = dict((n, nums.count(n)) for n in set(nums))
        return min(hashMap, key=hashMap.get)