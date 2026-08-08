class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                if not is_palindrome(start, end):
                    continue

                path.append(s[start:end + 1])
                dfs(end + 1, path)
                path.pop()

        dfs(0, [])
        return result