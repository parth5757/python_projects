import pygame
import sys
import math
import pickle
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
BOARD_COLOR = (255, 223, 186)
POCKET_COLOR = (0, 0, 0)
STRIKER_COLOR = (255, 0, 0)
BLACK_PIECE_COLOR = (0, 0, 0)
WHITE_PIECE_COLOR = (255, 255, 255)
AIM_COLOR = (0, 255, 0)
FPS = 60
FRICTION = 0.995
STRIKER_RADIUS = 15
PIECE_RADIUS = 10
POCKET_RADIUS = 20
POWER_MULTIPLIER = 0.2
MAX_POWER = 100
SAVE_FILE = 'carrom_save.pickle'

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Carrom')

# Clock to control the frame rate
clock = pygame.time.Clock()

# Classes for game objects
class Piece:
    def __init__(self, position, color, radius=PIECE_RADIUS):
        self.position = list(position)
        self.velocity = [0, 0]
        self.color = color
        self.radius = radius

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.velocity[0] *= FRICTION
        self.velocity[1] *= FRICTION

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)

    def check_collision_with_wall(self):
        if self.position[0] - self.radius < 0 or self.position[0] + self.radius > SCREEN_WIDTH:
            self.velocity[0] = -self.velocity[0]
        if self.position[1] - self.radius < 0 or self.position[1] + self.radius > SCREEN_HEIGHT:
            self.velocity[1] = -self.velocity[1]

    def check_collision_with_piece(self, other):
        dx = self.position[0] - other.position[0]
        dy = self.position[1] - other.position[1]
        distance = math.hypot(dx, dy)
        if distance < self.radius + other.radius:
            angle = math.atan2(dy, dx)
            total_velocity = math.hypot(self.velocity[0] - other.velocity[0], self.velocity[1] - other.velocity[1])
            self.velocity[0] = math.cos(angle) * total_velocity
            self.velocity[1] = math.sin(angle) * total_velocity
            other.velocity[0] = -math.cos(angle) * total_velocity
            other.velocity[1] = -math.sin(angle) * total_velocity

class Striker(Piece):
    def __init__(self, position):
        super().__init__(position, STRIKER_COLOR, STRIKER_RADIUS)

# Function to draw the carrom board
def draw_board():
    screen.fill(BOARD_COLOR)
    pockets = [
        (POCKET_RADIUS, POCKET_RADIUS),
        (SCREEN_WIDTH - POCKET_RADIUS, POCKET_RADIUS),
        (POCKET_RADIUS, SCREEN_HEIGHT - POCKET_RADIUS),
        (SCREEN_WIDTH - POCKET_RADIUS, SCREEN_HEIGHT - POCKET_RADIUS)
    ]
    for pocket in pockets:
        pygame.draw.circle(screen, POCKET_COLOR, pocket, POCKET_RADIUS)

def is_piece_in_pocket(piece):
    pockets = [
        (POCKET_RADIUS, POCKET_RADIUS),
        (SCREEN_WIDTH - POCKET_RADIUS, POCKET_RADIUS),
        (POCKET_RADIUS, SCREEN_HEIGHT - POCKET_RADIUS),
        (SCREEN_WIDTH - POCKET_RADIUS, SCREEN_HEIGHT - POCKET_RADIUS)
    ]
    for pocket in pockets:
        if math.hypot(piece.position[0] - pocket[0], piece.position[1] - pocket[1]) < POCKET_RADIUS:
            return True
    return False

def save_game(state):
    with open(SAVE_FILE, 'wb') as f:
        pickle.dump(state, f)

def load_game():
    try:
        with open(SAVE_FILE, 'rb') as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return None

def main():
    # Load saved game state or initialize a new game
    game_state = load_game()
    if game_state:
        striker, pieces, player_turn, scores, aiming, power, moving = game_state
    else:
        striker = Striker((SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
        pieces = [
            Piece((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50), BLACK_PIECE_COLOR),
            Piece((SCREEN_WIDTH // 2 + 30, SCREEN_HEIGHT // 2 - 30), WHITE_PIECE_COLOR)
        ]
        player_turn = 1
        scores = [0, 0]
        aiming = False
        power = 0
        moving = False

    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game((striker, pieces, player_turn, scores, aiming, power, moving))
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if event.key == pygame.K_s:
                    save_game((striker, pieces, player_turn, scores, aiming, power, moving))
            if event.type == pygame.MOUSEBUTTONDOWN and not moving and not paused:
                aiming = True
            if event.type == pygame.MOUSEBUTTONUP and aiming:
                if not moving:
                    mouse_x, mouse_y = event.pos
                    angle = math.atan2(mouse_y - striker.position[1], mouse_x - striker.position[0])
                    striker.velocity = [power * math.cos(angle), power * math.sin(angle)]
                    aiming = False
                    power = 0
                    moving = True

        if aiming:
            power = min(MAX_POWER, power + 1)

        # Update positions
        if moving:
            striker.move()
            striker.check_collision_with_wall()
            for piece in pieces:
                piece.move()
                piece.check_collision_with_wall()
                piece.check_collision_with_piece(striker)
                for other in pieces:
                    if piece != other:
                        piece.check_collision_with_piece(other)
            
            # Check if all pieces have stopped moving
            if all(math.hypot(p.velocity[0], p.velocity[1]) < 0.1 for p in pieces + [striker]):
                moving = False
                # Remove pieces that fall into pockets and update scores
                for piece in pieces[:]:
                    if is_piece_in_pocket(piece):
                        if piece.color == BLACK_PIECE_COLOR:
                            scores[player_turn - 1] += 10
                        else:
                            scores[player_turn - 1] += 5
                        pieces.remove(piece)
                # Switch turns
                player_turn = 3 - player_turn

        # Draw everything
        draw_board()
        striker.draw()
        for piece in pieces:
            piece.draw()
        
        if aiming:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            pygame.draw.line(screen, AIM_COLOR, striker.position, (mouse_x, mouse_y), 2)
            pygame.draw.circle(screen, AIM_COLOR, striker.position, int(power * POWER_MULTIPLIER), 1)

        # Display scores and current player
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Player 1: {scores[0]}  Player 2: {scores[1]}", True, (0, 0, 0))
        turn_text = font.render(f"Player {player_turn}'s turn", True, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        screen.blit(turn_text, (20, 60))

        if paused:
            pause_text = font.render("Game Paused - Press 'P' to Resume", True, (255, 0, 0))
            screen.blit(pause_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))

        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()