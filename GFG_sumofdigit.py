class Solution:
    def sumOfDigits(self, n):
        digit_list = [int(d) for d in str(n)]
        return sum(digit_list)
