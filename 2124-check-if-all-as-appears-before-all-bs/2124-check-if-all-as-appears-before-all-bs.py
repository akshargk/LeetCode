class Solution(object):
    def checkString(self, s):
       
        x = False
        for char in s:
            if char == 'b':
                x = True
            elif char == 'a' and x:
                return False
        return True