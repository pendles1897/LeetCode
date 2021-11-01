class Solution:
    def romanToInt(self, s):
        self.s = s
        romanNumerals = {
            "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,
            "M":1000,"IV":4,"IX":9,"XL":40,
            "XC":90,"CD":400,"CM":900}
        num = 0
        subList = ["IV","IX","XL","XC","CD","CM"]
        for i in subList:
            if i in s:
                num += romanNumerals[i]
                s = s.replace(i,"")
        for j in s:
            num += romanNumerals[j]
            s = s.replace(j,"")
        return num

num = Solution()
roman = "XL"
print(num.romanToInt(roman))
