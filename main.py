import chess  

#1. Piece values (material only)  
PIECE_VALUES = {  
    chess.PAWN: 1,  
    chess.KNIGHT: 3,  
    chess.BISHOP: 3,  
    chess.ROOK: 5,  
    chess.QUEEN: 9,  
    chess.KING: 0,  # We don't score the king directly  
}  
  
def evaluate_board(board: chess.Board) -> int:  
    """  
    Simple evaluation: positive means White is better,    negative means Black is better.    
    """    
    score = 0  
    for piece_type, value in PIECE_VALUES.items():  
        score += len(board.pieces(piece_type, chess.WHITE)) * value  
        score -= len(board.pieces(piece_type, chess.BLACK)) * value  
    return score  

#2. Minimax with Alpha-Beta  

def minimax(board: chess.Board, depth: int, alpha: float, beta: float, is_maximizing: bool) -> float:  
    """  
    Minimax from White's point of view:    - White tries to maximize the evaluation.    - Black tries to minimize the evaluation.    
    """    
    # Base case: depth 0 or game over  
    if depth == 0 or board.is_game_over():  
        return evaluate_board(board)  
  
    if is_maximizing:  
        max_eval = float('-inf')  
        for move in board.legal_moves:  
            board.push(move)  
            eval_score = minimax(board, depth - 1, alpha, beta, False)  
            board.pop()  
  
            max_eval = max(max_eval, eval_score)  
            alpha = max(alpha, eval_score)  
            if beta <= alpha:  
                break  # Beta cut-off  
        return max_eval  
    else:  
        min_eval = float('inf')  
        for move in board.legal_moves:  
            board.push(move)  
            eval_score = minimax(board, depth - 1, alpha, beta, True)  
            board.pop()  
  
            min_eval = min(min_eval, eval_score)  
            beta = min(beta, eval_score)  
            if beta <= alpha:  
                break  # Alpha cut-off  
        return min_eval  
  
# -----------------------------  
# 3. Choosing the best move  
# -----------------------------  
def find_best_move(board: chess.Board, depth: int) -> chess.Move | None:  
    """  
    Returns the best move for the side to move.    White tries to maximize evaluation.    Black tries to minimize evaluation.    
    """    
    best_move = None  
  
    if board.turn == chess.WHITE:  
        best_eval = float('-inf')  
        for move in board.legal_moves:  
            board.push(move)  
            eval_score = minimax(board, depth - 1, float('-inf'), float('inf'), False)  
            board.pop()  
  
            if eval_score > best_eval or best_move is None:  
                best_eval = eval_score  
                best_move = move  
    else:  
        best_eval = float('inf')  
        for move in board.legal_moves:  
            board.push(move)  
            eval_score = minimax(board, depth - 1, float('-inf'), float('inf'), True)  
            board.pop()  
  
            if eval_score < best_eval or best_move is None:  
                best_eval = eval_score  
                best_move = move  
  
    return best_move  
  
# -----------------------------  
# 4. Bot vs Bot (for testing)  
# -----------------------------  
def play_bot_vs_bot(depth: int = 3, max_moves: int = 40):  
    board = chess.Board()  
    move_count = 0  
  
    while not board.is_game_over() and move_count < max_moves:  
        print(board)  
        print("Turn:", "White" if board.turn == chess.WHITE else "Black")  
  
        best_move = find_best_move(board, depth)  
        if best_move is None:  
            break  
  
        print("Best move:", best_move)  
        board.push(best_move)  
        move_count += 1  
        print("-" * 30)  
  
    print(board)  
    print("Game over:", board.result(), "| Reason:", board.outcome())  
  
# -----------------------------  
# 5. Human vs Bot  
# -----------------------------  
def play_human_vs_bot(depth: int = 3, human_plays_white: bool = True):  
    board = chess.Board()  
  
    while not board.is_game_over():  
        print(board)  
  
        if (board.turn == chess.WHITE and human_plays_white) or (board.turn == chess.BLACK and not human_plays_white):  
            # Human move  
            move_uci = input("Your move (e.g., e2e4): ")  
            try:  
                move = chess.Move.from_uci(move_uci)  
                if move in board.legal_moves:  
                    board.push(move)  
                else:  
                    print("Illegal move, try again.")  
            except ValueError:  
                print("Invalid format, try again.")  
        else:  
            # Bot move  
            print("Bot is thinking...")  
            bot_move = find_best_move(board, depth)  
            if bot_move is None:  
                break  
            print("Bot move:", bot_move)  
            board.push(bot_move)  
  
    print(board)  
    print("Game over:", board.result(), "| Reason:", board.outcome())  
  
  
if __name__ == "__main__":  
    # Example: run a quick bot vs bot demo  
    play_bot_vs_bot(depth=3, max_moves=20)  
    # Or comment that out and try:  
    # play_human_vs_bot(depth=3, human_plays_white=True)
    