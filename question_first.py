class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        flag = False
      
        for i in range(97, 123):
            ch = chr(i)
            for j in range(len(sentence)):
                cd = sentence[j]
                if ch == cd:
                    flag = True
                    break
                else:
                    flag = False
            if not flag:
                break
                
        return flag

def main():
    s = Solution()
    sentence = "the quick brown fox jumps over the lazy dog"
    result = s.checkIfPangram(sentence)
    print(result)

if __name__ == "__main__":
    main()
    