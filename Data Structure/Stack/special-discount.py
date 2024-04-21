# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
# Problem Statment
# 1475. Final Prices With a Special Discount in a Shop
# You are given an integer array prices where prices[i] is the price of the ith item in a shop.
# There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.
# Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.
# Example
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        stack = []
        for i in range(len(prices)):
            while stack and (prices[stack[-1]] >= prices[i]):
                prices[stack.pop()] -= prices[i]
            stack.append(i)
        return prices
        



        

        
