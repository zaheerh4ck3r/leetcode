# Solution Class for Finding Common Characters
### count Method
The count method takes a word as input and returns a frequency array of size 26, where each index represents the frequency of a letter in the English alphabet. The method iterates over each character in the word, converts it to its corresponding index in the frequency array using the ASCII value of the character, and increments the count at that index.
intersection Method
The intersection method takes two frequency arrays as input and returns a new frequency array that represents the intersection of the two input arrays. This is done by taking the minimum count of each letter at the corresponding index in the two arrays.
commonChars Method
The commonChars method takes a list of words as input and returns a list of common characters among all the words. Here's how it works:
### Step 1: Initialize the Frequency Array
The method initializes the frequency array with the count of the first word in the list.
### Step 2: Update the Frequency Array
The method iterates over the remaining words in the list and updates the frequency array by taking the intersection of the current frequency array with the frequency array of the current word.
### Step 3: Construct the Result List
The method constructs the result list by iterating over the frequency array and appending each letter to the result list as many times as its count in the frequency array.
