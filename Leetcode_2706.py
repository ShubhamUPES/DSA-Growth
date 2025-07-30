class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a=sorted(prices)
        for i in range(len(a)):
            if a[0]+a[1]<=money:
                return money-(a[0]+a[1])
            else:
                return money
        
