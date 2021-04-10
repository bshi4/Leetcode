class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistance(self, words, word1, word2):
        dist = len(words)
        i, index1, index2 = 0, None, None
        while i < len(words):
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i
            i += 1
            if index1 is not None and index2 is not None:
                dist = min(dist, abs(index1-index2))
        return dist

words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = 'coding'
word2 = 'makes'
ans = Solution().shortestDistance(words, word1, word2)