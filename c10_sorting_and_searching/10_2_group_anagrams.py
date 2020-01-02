# 10.2 Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
# each other.

# Solution: anagram  = words with same letters
#1.  we can sort all letters inide each word and then sort the results (but we have to keep a reference to the initial words)
#2. We can gust hash them and that would  work also (only grouping, not necesarily soted array of groups)

def group_anagrams(data):
     structure = [ (word, "".join(sorted(word))) for word in data]
     result = sorted(structure, key = lambda x : x[1])
     return([x[0] for x in result])

data = ["ara", "beta", "raa", "etab", "tt"]
print(group_anagrams(data))

