# https://leetcode.com/problems/baseball-game/
# Problem Statment
# 682. Baseball Game
# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = []

        for i in operations:
            if i.lstrip('-+').isdigit():
                x.append(int(i))
                print(x)
            elif i == "+":
                if len(x) > 1:
                    x.append(x[-1]+x[-2])
                print(x)
            elif i == "D":
                if len(x) > 0:
                    x.append(x[-1]*2)
                print(x)
            elif i == "C":
                if len(x) > 0:
                    x.pop()
                print(x)
                    
        return sum(x)
