class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols=set()
        dia1=set()
        dia2=set()

        def backtrack(row):
            if row == n:
                return 1

            count=0
            for col in range(n):
                if col in cols or (row-col) in dia1 or (row+col) in dia2:
                    continue
            
                cols.add(col)
                dia1.add(row-col)
                dia2.add(row+col)

                count+= backtrack(row+1)

                cols.remove(col)
                dia1.remove(row-col)
                dia2.remove(row+col)

            return count
        return backtrack(0)
        