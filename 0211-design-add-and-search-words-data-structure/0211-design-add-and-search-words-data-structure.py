class WordDictionary:

    def __init__(self):
        self.words=set()

    def addWord(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        cnt=word.count('.')
        
        if cnt==0:
            return word in self.words
        
        if cnt==1:
            index=word.index('.')
            for i in range(26):
                if word[:index]+chr(97+i)+word[index+1:] in self.words:
                    return True
            return False
        
        if cnt==2:
            index1=word.index('.')
            index2=len(word)-1-word[::-1].index('.')
            for i in range(26):
                for j in range(26):
                    w =word[:index1]+chr(97+i)+word[index1+1:index2]+chr(97+j)+word[index2+1:]
                    if w in self.words:
                        return True
            return False
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)