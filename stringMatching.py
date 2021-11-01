"""
TO DO:
    1. Create additional method: arraySearch on par with stringMatching
    2. Call arraySearch twice for both searches
    NOTE:
        Ensure they are not nexted. Both within same class as separate methods.
"""


from typing import Sized
class Solution:
    from typing import List
    def stringMatching(self,words: List[str]) -> List[str]:
        size = len(words)
        substrings = []
        # Forward search
        for i in range(0,size):
            for j in range(1,size):
                if (words[i] != words[j]) and (words[j] not in words[i]):
                    pass
                elif (words[i] != words[j]) and (words[j] in words[i]) and (words[j] not in substrings):
                    substrings.append(words[j])
        # Backwards search
        reversedWords = words.reverse()
        for i in range(0,size):
            for j in range(1,size):
                if (words[i] != words[j]) and (words[j] not in words[i]):
                    pass
                elif (words[i] != words[j]) and (words[j] in words[i]) and (words[j] not in substrings):
                    substrings.append(words[j])
        
        return substrings

test = Solution()
words = ["mass","as","hero","superhero"]
print(test.stringMatching(words))
