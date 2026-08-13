class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 2147483647
        
        reversed_num = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            digit = x % 10
            if reversed_num > y // 10:
                return 0
            if reversed_num == y // 10:
                if sign == 1 and digit > 7:
                    return 0
                if sign == -1 and digit > 8:
                    return 0
            reversed_num = reversed_num * 10 + digit
            x //= 10
        return sign * reversed_num