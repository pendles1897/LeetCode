class Solution:
    def isPalindrome(self, a: int) -> bool:
        self.a = a
        if (a<0):
            return False
        elif str(a) == (str(a)[::-1]):
            return True
        else:
            return False
a = 121
num = Solution()
print(num.isPalindrome(a))