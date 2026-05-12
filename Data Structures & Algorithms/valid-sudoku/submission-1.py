class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        columns=defaultdict(set)
        squares=defaultdict(set)
        for r in range(9):
            for c in range(9):
                p=board[r][c]
                if p=='.':
                    continue

                if (p in rows[r] or
                    p in columns[c] or
                    p in squares[(r//3,c//3)]):
                    return False
                rows[r].add(p)
                columns[c].add(p)
                squares[(r//3,c//3)].add(p)
        return True

        