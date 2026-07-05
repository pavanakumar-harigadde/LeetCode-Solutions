#3110. Score of a String

class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Initializing a variable with value 0
        ans =0

        #looping through the string to find absolute differences and sum up them
        for i in range(len(s)-1):
            #adding absolute differences of charaters as given
            ans += abs(ord(s[i])-ord(s[i+1]))
        return ans #returning final answer to STDOUT

        #End of the program 
