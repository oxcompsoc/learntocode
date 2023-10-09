"""
Snake Eater
Made with PyGame
"""

import pygame, sys, time, random

# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 25

# Window size
frame_size_x = 720
frame_size_y = 480

# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f"[!] Had {check_errors[1]} errors when initialising game, exiting...")
    sys.exit(-1)
else:
    print("[+] Game successfully initialised")


# Initialise game window
pygame.display.set_caption("Snake Eater")
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


# FPS (frames per second) controller
fps_controller = pygame.time.Clock()


# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100 - 10, 50], [100 - (2 * 10), 50]]

food_pos = [
    random.randrange(1, (frame_size_x // 10)) * 10,
    random.randrange(1, (frame_size_y // 10)) * 10,
]
food_spawn = True

direction = "RIGHT"
change_to = direction

score = 0


# Game Over
def game_over():
    my_font = pygame.font.SysFont("times new roman", 90)
    game_over_surface = my_font.render("YOU DIED", True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Score
def show_score(choice, color, size):
    score_font = pygame.font.SysFont("times", size)
    score_surface = score_font.render("Score : " + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()


def react_to_keypress():
    # W -> Up; S -> Down; A -> Left; D -> Right
    if event.key == pygame.K_UP or event.key == ord("w"):
        return "UP"
    """
    TODO - add ifs for the other directions
    """

    # Esc -> Create event to quit the game
    if event.key == pygame.K_ESCAPE:
        pygame.event.post(pygame.event.Event(pygame.QUIT))


def get_new_direction():
    """
    TODO - check if the change_to direction is not the opposite of
    the current direction and return the changed direction
    """


def move_snake():
    """
    TODO - change one of the coordinates of the snake by 10
    depending on the direction
    """


def grow_snake_and_remove_tail():
    """
    TODO - add the current position of the snake at the start of the snake body
    Use .copy() to get a copy of the position since otherwise we would be referencing
    the same array.
    Then check whether the current position is the same as the food position.
        - If they are the same we need to increase the score and make food_spawn = false
        to signal that we'll need to spawn the food again
        - Otherwise, use .pop() to remove the last element of the snake_body

    In order to change global variables use:
    global x

    and then x can be changed:
    x = 3
    """


def spawn_food_if_needed():
    """
    TODO - if food_spawn = False, change the location of the food to
    a random location (remember that all coordinates must be divisible by 10 by design).
    Then set food_spawn to True since the food is generated.
    """


def draw_snake_and_food():
    game_window.fill(black)

    """
    TODO - use this function - pygame.draw.rect(game_window, _color_you_want_, pygame.Rect(_x_, _y_, _width_, _height_))
    to draw the snake and its food

    You will need to use a for loop to iterate through all of the squares of the snake.
    """


def check_for_game_over():
    """
    TODO - check whether the front of the snake is out of the screen
    or whether it's in the same place as another part of the snake.

    You can use "for block in snake_body[1:]:" to iterate through all squares of the snake but
    the first one.
    """


# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            change_to = react_to_keypress()

    # Making sure the snake cannot move in the opposite direction instantaneously
    direction = get_new_direction()
    move_snake()
    grow_snake_and_remove_tail()
    spawn_food_if_needed()
    draw_snake_and_food()
    check_for_game_over()

    show_score(1, white, 20)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(difficulty)
