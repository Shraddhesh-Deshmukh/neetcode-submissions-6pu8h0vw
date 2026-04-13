class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def dictGenerator(string):
            dicts={}
            for i in range(len(string)):
                if string[i] in dicts:
                    dicts[string[i]]+=1
                else:
                    dicts[string[i]]=1
                
            return dicts
        
        dict1=dictGenerator(s)
        dict2=dictGenerator(t)

        return dict1==dict2