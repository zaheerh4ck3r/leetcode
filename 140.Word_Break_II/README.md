# LeetCode Problem 140: Word Break II

## Description
This is a solution to the LeetCode problem "140. Word Break II". Given a string `s` and a dictionary of strings `wordDict`, the task is to add spaces in `s` to construct a sentence where each word is a valid dictionary word. The function should return all such possible sentences in any order.

## Example
Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []



## Constraints
- 1 <= s.length <= 20
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 10
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are unique.
- Input is generated in a way that the length of the answer doesn't exceed 10^5.

## Solution Explanation
The solution uses a backtracking approach with memoization to efficiently find all possible sentences. Here's a breakdown of the solution:

1. Convert `wordDict` to a set for faster lookup.
2. Define a memoization dictionary to store already computed results.
3. Define a `backtrack` function that takes an index as input.
4. Inside the `backtrack` function:
   - Check if the current index is already computed, return the result if so.
   - If the index reaches the end of the string, return an empty list.
   - Initialize an empty list `sentences` to store all possible sentences from the current index.
   - Iterate through all possible end positions for the current substring.
   - If the current substring is a valid word, recursively find sentences for the rest of the string.
   - Append the current word to all sentences obtained from the rest of the string.
   - Memoize the result for the current index.
5. Call the `backtrack` function starting from index 0.
