# https://leetcode.com/problems/two-sum/
# Problem Statment
# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicMap = {}
        for i in range( len(nums)):
            toFind = target - nums[i]
            if toFind in dicMap:
                return [dicMap[toFind], i]
            dicMap[nums[i]] = i
        return []
