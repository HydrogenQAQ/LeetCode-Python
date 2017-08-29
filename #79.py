# Author: Jin


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, i, j, word):
            # 所有的单词都已经访问完了
            if len(word) == 0:
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[0] != board[i][j]:
                return False
            temp = board[i][j]
            board[i][j] = '#'
            res = dfs(board, i + 1, j, word[1:]) or dfs(board, i - 1, j, word[1:]) or \
                dfs(board, i, j - 1, word[1:]) or dfs(board, i, j + 1, word[1:])
            board[i][j] = temp
            return res
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True
        return False

s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "SEE"
print(s.exist(board, word))