
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
# Complete the code below.
# Useful functions include:
# turtle.circle(radius) to make the turtle draw a circle, starting from the bottom edge.
# turtle.seth(angle) to make the turtle face any direction you want:
# 0 - right, 90 - up, 180 - left, 270 - down

# Draws an O centered at (x,y) inside a box of size s
# You can optionally add an argument for line width:
# def draw_o_at(turtle, x, y, s, w)
def draw_o_at(turtle, x, y, s):
    pass

# Draws an X centered at (x,y) inside a box of size s
# You can optionally add an argument for line width:
# def draw_x_at(turtle, x, y, s, w)
def draw_x_at(turtle, x, y, s):
    pass

# End of step 5


def draw_o_in(turtle, numpad_input):
    # Requires 0 <= box_y, box_y <= 2
    box_x = (numpad_input - 1) % 3
    box_y = 2 - (numpad_input - 1) // 3
    target_x = (SQUARE_SIZE + LINE_WIDTH) * (box_x - 1)
    target_y = (SQUARE_SIZE + LINE_WIDTH) * (box_y - 1)
    draw_o_at(turtle, target_x, target_y, SQUARE_SIZE)  # LINE_WIDTH)

def draw_x_in(turtle, numpad_input):
    # Requires 0 <= box_y, box_y <= 2
    box_x = (numpad_input - 1) % 3
    box_y = 2 - (numpad_input - 1) // 3
    target_x = (SQUARE_SIZE + LINE_WIDTH) * (box_x - 1)
    target_y = (SQUARE_SIZE + LINE_WIDTH) * (box_y - 1)
    draw_x_at(turtle, target_x, target_y, SQUARE_SIZE)  # LINE_WIDTH)


def main():
    # We'll represent the board state using a list,
    # and represent the current player by their tile ("X" or "O".)
    board_state = [
        "", "", "",
        "", "", "",
        "", "", ""
    ]
    draw_board()
    current_player = "X"  # Optional extension: Let the first player choose if they want Xs or Os
    turt = turtle.Turtle()

    while (True):
        # Steps 3 and 4. Get player input.
        # Let the current player input a square. OPTIONAL extension: Check that the chosen square is an integer and that it's in bounds.
        # We'll ask the player for an input from 1 to 9, like a phone keypad. 
        # Complete the code below:
        place_square = None
        input_square = input()

        while place_square == None:
            # check that the chosen square is empty here
                # set place_square to the chosen square if both checks pass
                place_square = input_square
            # else get a new input


        # Step 5.  Update the board state and draw the player's move.
        # You can use the draw_x_in(turtle, numpad_input) and draw_o_in(turtle, numpad_input) functions here.
        # Complete the code below:
        if current_player == "X":
            pass
        else:
            pass


        # Step 6. Checking to see if a player has won.
        # Complete the code below:
        player_won = False
        # This is a bit tedious since you need to check 8 sets of 3 things,
        # for example on the NW/SE diagonal, whether element[0][0] == element[1][1] == element[2][2], etc...
        # so you can choose to skip it by using the code below:
        # player_won = set(current_player) in [set([board_state[x] for x in xs]) for xs in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]]  # Magic!

        # Then, complete the code below:
        if player_won:
            pass
            # print a victory message
            # exit the loop
        

        # Step 2. Alternate between players until somone wins.
        # The "until someone wins" bit has been done for you: it's the while (True).
        # If the current player is "X", set the current player to "O", and vice versa.
        # Complete the code below:
        current_player = ""


main()
