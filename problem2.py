# Q2 : String Manipulation

# Check If a Word Occurs As a Prefix of Any Word in a Sentence

# Given a sentence that consists of some words separated by a single space, and a searchWord.

# You have to check if searchWord is a prefix of any word in sentence.

# Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).

# If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

# A prefix of a string S is any leading contiguous substring of S.

 

# Example 1:

# Input: sentence = "i love eating burger", searchWord = "burg"
# Output: 4
# Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.



def search_prefix(sentence,prefix):
    words=sentence.split(' ')
    for i in range(len(words)):
        if words[i].startswith(prefix):
            return i
    return -1

Sentence='i love eating burger'

Sentence='Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed)'

words=Sentence.split(' ')

pre='search'

# print(words)

print(search_prefix(Sentence,'pre'))






# n=len(words)

# for i in range(n):
#     if words[i].startswith(pre):
#         print(i)
#         break








