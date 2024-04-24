import connectfour as main
import connectfour_lib as lib

def start_game():
    print("Hey 👋! Welcome to Connect Four")

    while True:
        try:
            columns = int(input("Enter the number of columns you want the game to have: "))
            rows = int(input("Enter the number of rows you want the game to have: "))
            if not main.MIN_COLUMNS <= columns <= main.MAX_COLUMNS or not main.MIN_ROWS <= rows <= main.MAX_ROWS:
                print("INVALID INPUT, PLEASE TRY AGAIN")
                continue
            break
        except:
            print("INVALID INPUT, PLEASE TRY AGAIN")
            continue
    game = main.new_game(columns, rows)
    while main.winner(game) == main.EMPTY:
        game = lib.ask_move_and_execute(game)
        if main.winner(game) != main.EMPTY:
            lib.print_game_board(game.board)
            lib.print_winner(main.winner(game))

start_game()