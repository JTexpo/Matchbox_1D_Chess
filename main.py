import pyscript
from pyscript import Element
import asyncio
import json

from matchbox_1d_chess.chess_board import Board, BLACK_TEAM_ID

board: Board = Board()
AI_MOVES_FILE = open("./assets/ai/white_moves.json", "r")
AI_MOVES = json.loads(AI_MOVES_FILE.read())
selected_tile: int = -1
is_ai_turn: bool = True
lock_actions: bool = True

board_0_element = Element("board_0")
board_1_element = Element("board_1")
board_2_element = Element("board_2")
board_3_element = Element("board_3")
board_4_element = Element("board_4")
board_5_element = Element("board_5")
board_6_element = Element("board_6")
board_7_element = Element("board_7")

turn_element = Element("turn")
held_piece_element = Element("held_piece")


async def sync_board_to_gui(board: Board, turn: str, held_piece: str):
    board_0_element.element.style = f"background-image:url(/assets/images/{board.board[0].name}.png); background-size:cover;"
    board_1_element.element.style = f"background-image:url(/assets/images/{board.board[1].name}.png); background-size:cover;"
    board_2_element.element.style = f"background-image:url(/assets/images/{board.board[2].name}.png); background-size:cover;"
    board_3_element.element.style = f"background-image:url(/assets/images/{board.board[3].name}.png); background-size:cover;"
    board_4_element.element.style = f"background-image:url(/assets/images/{board.board[4].name}.png); background-size:cover;"
    board_5_element.element.style = f"background-image:url(/assets/images/{board.board[5].name}.png); background-size:cover;"
    board_6_element.element.style = f"background-image:url(/assets/images/{board.board[6].name}.png); background-size:cover;"
    board_7_element.element.style = f"background-image:url(/assets/images/{board.board[7].name}.png); background-size:cover;"

    turn_element.element.innerHTML = f"Turn: {turn}"
    held_piece_element.element.innerHTML = f"Held Piece: {held_piece}"


def ai_move(board: Board):
    best_move = AI_MOVES[board.get_string_board()][0]
    board.move_pieces(start=best_move["start"], end=best_move["end"])


def select_tile(index: int):
    global board, selected_tile, is_ai_turn, lock_actions

    # not letting the player act on ai's turns or gui update
    if is_ai_turn or lock_actions:
        return

    # locking actions for gui updates
    lock_actions = True

    # if the player selected their own piece to drop the piece
    if index == selected_tile:
        selected_tile = -1
        return

    # if the player selected a piece and don't have anything in their hand
    if (selected_tile == -1) and (board.board[index].team_id == BLACK_TEAM_ID):
        selected_tile = index
        return

    # if the player is holding a piece, then we check if the move is valid
    is_valid_move = board.validate_move(start=selected_tile, end=index)

    # if the move is not valid, do not act
    if not is_valid_move:
        return

    # if the move is valid updating the board
    board.move_pieces(start=selected_tile, end=index)
    is_ai_turn = True

def reset():
    global board, selected_tile, is_ai_turn, lock_actions
    selected_tile = -1
    is_ai_turn = True
    lock_actions = True
    board.reset_board()

async def main():
    global is_ai_turn, lock_actions, board, selected_tile, BLACK_TEAM_ID

    while True:
        if lock_actions:
            if is_ai_turn:
                await sync_board_to_gui(board=board, turn="AI (White)", held_piece="")
            elif selected_tile == -1:
                await sync_board_to_gui(board=board, turn="You (Black)", held_piece="")
            elif board.board[selected_tile].team_id == BLACK_TEAM_ID:
                await sync_board_to_gui(
                    board=board,
                    turn="You (Black)",
                    held_piece=board.board[selected_tile]
                    .name.replace("_", " ")
                    .title(),
                )
            lock_actions = False

        elif is_ai_turn:
            ai_move(board=board)
            await sync_board_to_gui(board=board, turn="You (Black)", held_piece="")

            lock_actions = False
            is_ai_turn = False
            selected_tile = -1

        await asyncio.sleep(0.5)


pyscript.run_until_complete(main())
