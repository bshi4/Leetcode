class Solution:
    def findWords(self, words):
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        
        rows = [row1, row2, row3]
        res = []
        
        for word in words:
            for row in rows:
                if word[0].lower() in row:
                    target = row
                    flag = 0
                    break
            
            for i in range(1, len(word)):
                if word[i].lower() not in target:
                    flag = 1
            if flag == 0:
                res.append(word)
                
        return res
                
words = ["asdfghjkla","qwertyuiopq","zxcvbnzzm","asdfghjkla","qwertyuiopq","zxcvbnzzm"]
ans = Solution().findWords(words)