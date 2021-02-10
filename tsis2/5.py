class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        prod = 1
        while n!=0:
            a=n%10
            prod*=a
            sum+=a
            n//=10
        return prod-sum