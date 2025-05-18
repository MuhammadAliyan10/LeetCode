class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not word:
            return True
        if len(board) == 0 or len(board[0]) == 0:
            return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(
        self, board: list[list[str]], word: str, i: int, j: int, index: int
    ) -> bool:
        if index == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] == "#" or board[i][j] != word[index]:
            return False
        temp = board[i][j]
        board[i][j] = "#"
        found = (
            self.dfs(board, word, i - 1, j, index + 1)  #! Up
            or self.dfs(board, word, i + 1, j, index + 1)  #! Down
            or self.dfs(board, word, i, j - 1, index + 1)  #! Left
            or self.dfs(board, word, i, j + 1, index + 1)  #! Right
        )

        board[i][j] = temp
        return found


S = Solution()
print(
    S.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB",
    )
)
