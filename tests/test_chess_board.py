import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")

from matchbox_1d_chess.chess_board import Board, ChessPiece, WHITE_TEAM_ID, BLACK_TEAM_ID, ROOK_PIECE_ID, KING_PIECE_ID, KNIGHT_PIECE_ID, NULL_TEAM_ID, SPACE_PIECE_ID

class ChessBoardTestCase(unittest.TestCase):

    def test_reset_board(self):
        # INITALIZATION
        # -------------
        board = Board()
        board.board = []

        # ACTION
        # ------
        board.reset_board()

        # ASSERT
        # ------
        expected = Board()
        self.assertTrue( board.board[0].piece_id == expected.board[0].piece_id )
        self.assertTrue( board.board[1].piece_id == expected.board[1].piece_id )
        self.assertTrue( board.board[2].piece_id == expected.board[2].piece_id )
        self.assertTrue( board.board[3].piece_id == expected.board[3].piece_id )
        self.assertTrue( board.board[4].piece_id == expected.board[4].piece_id )
        self.assertTrue( board.board[5].piece_id == expected.board[5].piece_id )
        self.assertTrue( board.board[6].piece_id == expected.board[6].piece_id )
        self.assertTrue( board.board[7].piece_id == expected.board[7].piece_id )
        self.assertTrue( board.board[0].team_id == expected.board[0].team_id )
        self.assertTrue( board.board[1].team_id == expected.board[1].team_id )
        self.assertTrue( board.board[2].team_id == expected.board[2].team_id )
        self.assertTrue( board.board[3].team_id == expected.board[3].team_id )
        self.assertTrue( board.board[4].team_id == expected.board[4].team_id )
        self.assertTrue( board.board[5].team_id == expected.board[5].team_id )
        self.assertTrue( board.board[6].team_id == expected.board[6].team_id )
        self.assertTrue( board.board[7].team_id == expected.board[7].team_id )
        
    def test_rook_takes_rook(self):
        # INITALIZATION
        # -------------
        board = Board()
        start = 2
        end = 5

        # ACTION
        # ------
        board.move_pieces(start=start, end=end)

        # ASSERT
        # ------
        expected = Board()
        expected.board = [
            # Whites Side
            ChessPiece(name="King", team_id=WHITE_TEAM_ID, piece_id=KING_PIECE_ID),
            ChessPiece(name="Knight", team_id=WHITE_TEAM_ID, piece_id=KNIGHT_PIECE_ID),
            ChessPiece(name="space", team_id=NULL_TEAM_ID, piece_id=SPACE_PIECE_ID),
            # Spaces
            ChessPiece(name="space", team_id=NULL_TEAM_ID, piece_id=SPACE_PIECE_ID),
            ChessPiece(name="space", team_id=NULL_TEAM_ID, piece_id=SPACE_PIECE_ID),
            # Blacks Side
            ChessPiece(name="Rook", team_id=WHITE_TEAM_ID, piece_id=ROOK_PIECE_ID),
            ChessPiece(name="Knight", team_id=BLACK_TEAM_ID, piece_id=KNIGHT_PIECE_ID),
            ChessPiece(name="King", team_id=BLACK_TEAM_ID, piece_id=KING_PIECE_ID),
        ]
        
        self.assertTrue( board.board[0].piece_id == expected.board[0].piece_id )
        self.assertTrue( board.board[1].piece_id == expected.board[1].piece_id )
        self.assertTrue( board.board[2].piece_id == expected.board[2].piece_id )
        self.assertTrue( board.board[3].piece_id == expected.board[3].piece_id )
        self.assertTrue( board.board[4].piece_id == expected.board[4].piece_id )
        self.assertTrue( board.board[5].piece_id == expected.board[5].piece_id )
        self.assertTrue( board.board[6].piece_id == expected.board[6].piece_id )
        self.assertTrue( board.board[7].piece_id == expected.board[7].piece_id )
        self.assertTrue( board.board[0].team_id == expected.board[0].team_id )
        self.assertTrue( board.board[1].team_id == expected.board[1].team_id )
        self.assertTrue( board.board[2].team_id == expected.board[2].team_id )
        self.assertTrue( board.board[3].team_id == expected.board[3].team_id )
        self.assertTrue( board.board[4].team_id == expected.board[4].team_id )
        self.assertTrue( board.board[5].team_id == expected.board[5].team_id )
        self.assertTrue( board.board[6].team_id == expected.board[6].team_id )
        self.assertTrue( board.board[7].team_id == expected.board[7].team_id )
    
    def test_knight_opening(self):
        # INITALIZATION
        # -------------
        board = Board()
        start = 1
        end = 3

        # ACTION
        # ------
        board.move_pieces(start=start, end=end)

        # ASSERT
        # ------
        expected = Board()
        expected.board = [
            # Whites Side
            ChessPiece(name="King", team_id=WHITE_TEAM_ID, piece_id=KING_PIECE_ID),
            ChessPiece(name="space", team_id=NULL_TEAM_ID, piece_id=SPACE_PIECE_ID),
            ChessPiece(name="Rook", team_id=WHITE_TEAM_ID, piece_id=ROOK_PIECE_ID),
            # Spaces
            ChessPiece(name="Knight", team_id=WHITE_TEAM_ID, piece_id=KNIGHT_PIECE_ID),
            ChessPiece(name="space", team_id=NULL_TEAM_ID, piece_id=SPACE_PIECE_ID),
            # Blacks Side
            ChessPiece(name="Rook", team_id=BLACK_TEAM_ID, piece_id=ROOK_PIECE_ID),
            ChessPiece(name="Knight", team_id=BLACK_TEAM_ID, piece_id=KNIGHT_PIECE_ID),
            ChessPiece(name="King", team_id=BLACK_TEAM_ID, piece_id=KING_PIECE_ID),
        ]
        
        self.assertTrue( board.board[0].piece_id == expected.board[0].piece_id )
        self.assertTrue( board.board[1].piece_id == expected.board[1].piece_id )
        self.assertTrue( board.board[2].piece_id == expected.board[2].piece_id )
        self.assertTrue( board.board[3].piece_id == expected.board[3].piece_id )
        self.assertTrue( board.board[4].piece_id == expected.board[4].piece_id )
        self.assertTrue( board.board[5].piece_id == expected.board[5].piece_id )
        self.assertTrue( board.board[6].piece_id == expected.board[6].piece_id )
        self.assertTrue( board.board[7].piece_id == expected.board[7].piece_id )
        self.assertTrue( board.board[0].team_id == expected.board[0].team_id )
        self.assertTrue( board.board[1].team_id == expected.board[1].team_id )
        self.assertTrue( board.board[2].team_id == expected.board[2].team_id )
        self.assertTrue( board.board[3].team_id == expected.board[3].team_id )
        self.assertTrue( board.board[4].team_id == expected.board[4].team_id )
        self.assertTrue( board.board[5].team_id == expected.board[5].team_id )
        self.assertTrue( board.board[6].team_id == expected.board[6].team_id )
        self.assertTrue( board.board[7].team_id == expected.board[7].team_id )

if __name__ == "__main__":
    unittest.main()