class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high = 0
        max = high
        for i in gain:
            high+=i
            if high > max:
                max=high
        return max