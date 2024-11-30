
import turtle

SQUARE_SIZE=80
LINE_WIDTH=10

# Step 1.
# The code that draws the board has been completed for you
def draw_board():
    board = turtle.Turtle()
    board.hideturtle()
    board.pensize(LINE_WIDTH)
    board.speed(20)
    
    small_offset = (SQUARE_SIZE + LINE_WIDTH) / 2
    large_offset = SQUARE_SIZE * 1.5 + LINE_WIDTH / 2

    for x1,y1,x2,y2 in [
        ( small_offset,  large_offset,  small_offset, -large_offset),
        (-small_offset,  large_offset, -small_offset, -large_offset),
        ( large_offset,  small_offset, -large_offset,  small_offset),
        ( large_offset, -small_offset, -large_offset, -small_offset),
        ]:
        board.penup()
        board.goto(x1, y1)
        board.pendown()
        board.goto(x2, y2)


# Step 5. Drawing the move.
# You don't have to match this code exactly - how you draw your Xs and Os is up to you.

# Draws an O centered at (x,y) inside a box of size s
# You can optionally add an argument for line width:
def draw_o_at(turtle, x, y, s, w):
    turtle.pensize(w)
    turtle.penup()
    turtle.goto(x, y - 0.375 * s)
    turtle.seth(0)
    turtle.pendown()
    turtle.circle(s * 0.375)

# Draws an X centered at (x,y) inside a box of size s
# You can optionally add an argument for line width:
def draw_x_at(turtle, x, y, s, w):
    turtle.pensize(w)

    turtle.penup()
    turtle.goto(x - 0.375 * s, y - 0.375 * s)
    turtle.seth(45)
    turtle.pendown()
    turtle.forward(s * 0.75 * 1.414)

    turtle.penup()
    turtle.goto(x - 0.375 * s, y + 0.375 * s)
    turtle.seth(-45)
    turtle.pendown()
    turtle.forward(s * 0.75 * 1.414)
    pass

# End of step 5


def draw_o_in(turtle, numpad_input):
    # Requires 0 <= box_y, box_y <= 2
    box_x = (numpad_input - 1) % 3
    box_y = 2 - (numpad_input - 1) // 3
    target_x = (SQUARE_SIZE + LINE_WIDTH) * (box_x - 1)
    target_y = (SQUARE_SIZE + LINE_WIDTH) * (box_y - 1)
    draw_o_at(turtle, target_x, target_y, SQUARE_SIZE, LINE_WIDTH)

def draw_x_in(turtle, numpad_input):
    # Requires 0 <= box_y, box_y <= 2
    box_x = (numpad_input - 1) % 3
    box_y = 2 - (numpad_input - 1) // 3
    target_x = (SQUARE_SIZE + LINE_WIDTH) * (box_x - 1)
    target_y = (SQUARE_SIZE + LINE_WIDTH) * (box_y - 1)
    draw_x_at(turtle, target_x, target_y, SQUARE_SIZE, LINE_WIDTH)

def main():
    # We'll represent the board state using a list,
    # and represent the current player by their tile ("X" or "O".)
    board_state = [
        "", "", "",
        "", "", "",
        "", "", ""
    ]
    draw_board()
    current_player = "X"  
    turt = turtle.Turtle()

    while (True):
        # Steps 3 and 4. Get player input.
        # We'll ask the player for an input from 1 to 9, like a phone keypad. 
        place_square = None
        input_square = input("Where would you like to place your " + current_player + "?")
        
        while place_square == None:
            try:
                target_square = int(input_square)

                if target_square < 1 or target_square > 9:
                    input_square = input("That is out of bounds. Please try again: ")
                    continue

                if board_state[target_square - 1] != "":
                    input_square = input("That square is full. Please try again: ")
                    continue
                
                place_square = target_square

            except:
                input_square = input("That is not a valid input. Please try again: ")
 

        # Step 5. Update the board state and draw the player's move.
        board_state[place_square - 1] = current_player
        if current_player == "X":
            draw_x_in(turt, place_square)
        else:
            draw_o_in(turt, place_square)


        # Step 6. Checking to see if a player has won.
        player_won = set(current_player) in [set([board_state[x] for x in xs]) for xs in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]]  # Magic!
        if player_won:
            print("Player " + current_player + " won!")
            break
        

        # Step 2. Alternate between players until somone wins.
        if current_player == "O":
          current_player = "X"
        else:
          current_player = "O"
          
        
main()
