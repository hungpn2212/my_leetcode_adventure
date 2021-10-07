class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split(" ")
        n = len(words)
        vowels = ['a', 'e', 'i', 'o', 'u']
        index = 'a'
        res = []
        for word in words:
            if  word[0].lower() in vowels:
                word = word + 'ma'
            else:
                word = word[1:]+word[0]
                word = word + 'ma'
            word = word + index
            index = index + 'a'
            res.append(word)
        
        return " ".join(res)