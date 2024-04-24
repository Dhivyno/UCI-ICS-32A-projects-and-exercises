import connectfour as main

def find_player_letter(player_number: int):
    if player_number == main.RED:
        return "R"
    if player_number == main.YELLOW:
        return "Y"
    else:
        return "."
    
def print_whose_turn(player_number: int):
    if player_number == main.RED:
        print("\nIt is RED's turn")
    if player_number == main.YELLOW:
        print("\nIt is YELLOW's turn")
    
def print_winner(player_number: int):
    if player_number == main.RED:
        print("\nRED has won the game\n")
    if player_number == main.YELLOW:
        print("\nYELLOW has won the game\n")

def ask_move_and_execute(game: main.GameState):
    while True:
        print_game_board(game.board)
        print_whose_turn(game.turn)
        move = input("\nEnter your move type (pop or drop) followed by the column you would like to act on (eg: drop 12): ")

        try:
            move_array = move.strip().split(" ")
            move_type = move_array[0].strip().lower()
            column = move_array[1].strip()
        except:
            print("\nINVALID MOVE\n")
            continue
        if column.isdigit():
            column = int(column)
        else:
            print("\nINVALID MOVE\n")
            continue

        if column < 0 or column > main.columns(game)-1:
            print(f"\nINVALID MOVE, COLUMNS HAVE TO BE WITHIN 0 AND {main._board_columns(game.board)-1}\n")
            continue

        if move_type == "drop":
            try:
                game = main.drop(game, column)
                return game
            except: 
                print("\nINVALID MOVE\n")
                continue

        if move_type == "pop":
            try:
                game = main.pop(game, column)
                return game
            except:
                print("\nINVALID MOVE, YOU CAN'T POP YOUR OPPONENT'S PIECE\n")
                continue


def print_game_board(board : list) -> None:
    for col in range(main._board_columns(board)):
        if col < 9:
            print(col, end="  ")
        else:
            print(col, end=" ")
    print()
    for row in range(main._board_rows(board)):
        for col in range(main._board_columns(board)):
            if col == 0:
                print(find_player_letter(board[col][row]), end="")
            else:
                print("  " + find_player_letter(board[col][row]), end="")
        print()