import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Rock, Paper, Scissors')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
rock_img = pygame.image.load('stone.png')
paper_img = pygame.image.load('paper2.png')
scissors_img = pygame.image.load('scissor.png')

# Scale images
rock_img = pygame.transform.scale(rock_img, (100, 100))
paper_img = pygame.transform.scale(paper_img, (100, 100))
scissors_img = pygame.transform.scale(scissors_img, (100, 100))

# Game variables
choices = ["rock", "paper", "scissors"]
yourscore = 0
computerscore = 0

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    global yourscore, computerscore
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        yourscore += 1
        return "user"
    else:
        computerscore += 1
        return "computer"

def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

def main():
    global yourscore, computerscore
    running = True
    clock = pygame.time.Clock()
    user_choice = None
    computer_choice = None
    result = None

    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 100 < x < 200 and 500 < y < 600:
                    user_choice = "rock"
                elif 300 < x < 400 and 500 < y < 600:
                    user_choice = "paper"
                elif 500 < x < 600 and 500 < y < 600:
                    user_choice = "scissors"
                
                if user_choice:
                    computer_choice = get_computer_choice()
                    result = determine_winner(user_choice, computer_choice)
        
        # Draw choices
        screen.blit(rock_img, (100, 500))
        screen.blit(paper_img, (300, 500))
        screen.blit(scissors_img, (500, 500))

        # Display the computer's choice and result
        if computer_choice:
            draw_text(f"Computer chose: {computer_choice}", 36, BLACK, 300, 200)
        if result:
            if result == "draw":
                draw_text("It's a draw!", 48, BLACK, 350, 250)
            elif result == "user":
                draw_text("You win!", 48, BLACK, 350, 250)
            else:
                draw_text("Computer wins!", 48, BLACK, 350, 250)

        # Display the scores
        draw_text(f"Your Score: {yourscore}", 36, BLACK, 50, 50)
        draw_text(f"Computer Score: {computerscore}", 36, BLACK, 600, 50)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
