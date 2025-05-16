class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty_cells = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty_cells.append((i, j))
                else:
                    digit = board[i][j]
                    box_idx = (i // 3) * 3 + j // 3
                    rows[i].add(digit)
                    cols[j].add(digit)
                    boxes[box_idx].add(digit)

        self.backtrack(board, empty_cells, 0, rows, cols, boxes)

    def backtrack(
        self,
        board: list[list[str]],
        empty_cells: list[tuple[int, int]],
        pos: int,
        rows: list[set],
        cols: list[set],
        boxes: list[set],
    ) -> bool:
        if pos == len(empty_cells):
            return True

        i, j = empty_cells[pos]
        box_idx = (i // 3) * 3 + j // 3

        for k in range(1, 10):
            digit = str(k)
            if self.isValid(digit, i, j, box_idx, rows, cols, boxes):
                board[i][j] = digit
                rows[i].add(digit)
                cols[j].add(digit)
                boxes[box_idx].add(digit)

                if self.backtrack(board, empty_cells, pos + 1, rows, cols, boxes):
                    return True

                board[i][j] = "."
                rows[i].remove(digit)
                cols[j].remove(digit)
                boxes[box_idx].remove(digit)

        return False

    def isValid(
        self,
        digit: str,
        i: int,
        j: int,
        box_idx: int,
        rows: list[set],
        cols: list[set],
        boxes: list[set],
    ) -> bool:
        return (
            digit not in rows[i]
            and digit not in cols[j]
            and digit not in boxes[box_idx]
        )


S = Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

S.solveSudoku(board)


for row in board:
    print(row)
