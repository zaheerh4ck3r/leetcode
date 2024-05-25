class Solution:
    @staticmethod
    def wordBreak(s, wordDict):
        # Convert wordDict to set for faster lookup
        word_set = set(wordDict)
        
        # Memoization dictionary to store already computed results
        memo = {}
        
        def backtrack(index):
            # If the current index is already computed, return the result
            if index in memo:
                return memo[index]
            
            # If index reaches the end of the string, return an empty list
            if index == len(s):
                return ['']
            
            # Initialize an empty list to store all possible sentences from the current index
            sentences = []
            
            # Iterate through all possible end positions for the current substring
            for end in range(index + 1, len(s) + 1):
                # If the current substring is a valid word, recursively find sentences for the rest of the string
                if s[index:end] in word_set:
                    next_sentences = backtrack(end)
                    # Append the current word to all sentences obtained from the rest of the string
                    for sentence in next_sentences:
                        if sentence:
                            sentences.append(s[index:end] + ' ' + sentence)
                        else:
                            sentences.append(s[index:end])
            
            # Memoize the result for the current index
            memo[index] = sentences
            return sentences
        
        # Call the backtrack function starting from index 0
        return backtrack(0)

# Test cases
s1 = "catsanddog"
wordDict1 = ["cat","cats","and","sand","dog"]
print(Solution.wordBreak(s1, wordDict1))  
s2 = "pineapplepenapple"
wordDict2 = ["apple","pen","applepen","pine","pineapple"]
print(Solution.wordBreak(s2,wordDict2))
s3 = "catsandog"
wordDict3 = ["cats","dog","sand","and","cat"]
print(Solution.wordBreak(s3,wordDict3))
