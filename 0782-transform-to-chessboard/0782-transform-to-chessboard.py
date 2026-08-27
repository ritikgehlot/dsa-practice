class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)

        # Check whether the board has the required pattern.
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                    return -1

        # Count 1s in first row and first column.
        row_sum = sum(board[0])
        col_sum = sum(board[i][0] for i in range(n))

        # Number of 1s must be n/2 or (n+1)/2.
        if row_sum < n // 2 or row_sum > (n + 1) // 2:
            return -1

        if col_sum < n // 2 or col_sum > (n + 1) // 2:
            return -1

        # Count mismatches with 0101... pattern.
        row_moves = 0
        col_moves = 0

        for i in range(n):
            if board[i][0] != i % 2:
                row_moves += 1

            if board[0][i] != i % 2:
                col_moves += 1

        # For odd n, only one of the two patterns is possible.
        if n % 2:
            if row_moves % 2:
                row_moves = n - row_moves

            if col_moves % 2:
                col_moves = n - col_moves

        else:
            row_moves = min(row_moves, n - row_moves)
            col_moves = min(col_moves, n - col_moves)

        return (row_moves + col_moves) // 2