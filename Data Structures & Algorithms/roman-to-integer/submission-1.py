class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}
        last = 0
        total = 0
        for i in range(len(s)-1,-1,-1): #(start,stop,step)
        #for ch in s[::-1]: slicing does reverse also
           curr = roman[s[i]]
           if curr < last:
            total = total - curr
           else:
            total = total + curr
            last = curr
        return total