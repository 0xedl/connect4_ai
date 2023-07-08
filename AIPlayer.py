from Player import Player
import random


class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ put your docstring here
        """
        assert (checker == 'X' or checker == 'O')
        assert (tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert (lookahead >= 0)

        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        return "Player " + self.checker + " (" + self.tiebreak + ", " + str(self.lookahead) + ")"

    def max_score_column(self, scores):
        max_score = max(scores)
        indices = [index for index, score in enumerate(scores) if score == max_score]

        if self.tiebreak == 'LEFT':
            return indices[0]
        elif self.tiebreak == 'RIGHT':
            return indices[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(indices)

    def scores_for(self, board):
        scores = [0] * board.width

        for col in range(board.width):
            if board.can_add_to(col):
                if board.is_win_for(self.checker):
                    scores[col] = 100
                elif board.is_win_for(self.opponent_check()):
                    scores[col] = 0
                elif self.lookahead == 0:
                    scores[col] = 50
                else:
                    board.add_checker(self.checker, col)
                    opponent = AIPlayer(self.opponent_check(), self.tiebreak, self.lookahead - 1)
                    opponent_scores = opponent.scores_for(board)
                    if max(opponent_scores) == 0:
                        scores[col] = 100
                    elif max(opponent_scores) == 50:
                        scores[col] = 0
                    elif max(opponent_scores) == 100:
                        scores[col] = 50
                    board.remove_checker(col)
            else:
                scores[col] = -1

        return scores

    def next_move(self, board):
        scores = self.scores_for(board)
        best_move = self.max_score_column(scores)
        self.num_moves += 1
        return best_move
