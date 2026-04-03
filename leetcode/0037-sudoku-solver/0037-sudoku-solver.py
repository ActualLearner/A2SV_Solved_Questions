class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        rows_map = [set() for _ in range(rows)]
        cols_map = [set() for _ in range(cols)]
        box_map = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(rows):
            for c in range(cols):
                item = board[r][c]
                if item != ".":
                    rows_map[r].add(item)
                    cols_map[c].add(item)
                    box_map[r // 3][c // 3].add(item)
        
        def fill(i, j):
            nonlocal board
            nonlocal rows
            nonlocal cols
            nonlocal rows_map
            nonlocal cols_map

            if j == cols:
                return fill(i + 1, 0)
            elif i == rows:
                return True
            elif board[i][j] != ".":
                return fill(i, j + 1)

            box_ = box_map[i // 3][j // 3]
            for c in range(1, 10):
                num = str(c)
                if num in box_ or num in rows_map[i] or num in cols_map[j]:
                    continue
                
                rows_map[i].add(num)
                cols_map[j].add(num)
                box_map[i // 3][j // 3].add(num)
                board[i][j] = num

                if fill(i, j + 1):
                    return True
                
                rows_map[i].discard(num)
                cols_map[j].discard(num)
                box_map[i // 3][j // 3].discard(num)
                board[i][j] = "."
            
            return False
        fill(0, 0)
        return board