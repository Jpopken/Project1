import pygame
import sys
import random
import time

class Game:
    def __init__(self):

        pygame.init()
        self.grid_size = (5, 5)

        # Set up the display screen
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Lost in the Woods Simulator")

        # Difficulty options
        self.difficulty_levels = ["EASY", "MEDIUM", "HARD"]
        self.selected_difficulty = 0

        # Rectangles for difficulty selection
        self.difficulty_rects = []

        for i, _ in enumerate(self.difficulty_levels):
            rect = pygame.Rect(0, 0, 100, 30)

            rect.center = (self.screen_width // 2, self.screen_height // 2 + 20 + 30 * i)
            self.difficulty_rects.append(rect)
        # Load font
        self.title_font = pygame.font.Font(None, 36)
        self.difficulty_font = pygame.font.Font(None, 24)



        # Characters for the wandering game

        self.cell_size = 50
        self.character1 = Character(0, 0, self.cell_size, (255, 0, 0), self.grid_size, "Red")  # Red character
        self.character2 = Character(4, 4, self.cell_size, (0, 0, 255), self.grid_size,"Blue")  # Blue character Reset the game
        self.character3 = Character(0, 4, self.cell_size, (0, 255, 0), self.grid_size, "Green")  # Green character
        self.character4 = Character(4, 0, self.cell_size, (255, 255, 0), self.grid_size, "Yellow")  # Yellow character
        self.reset_game()
        self.home_screen()

        # Game loop
        self.running = True

    def prompt_grid_size(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Render text to prompt user for grid size
        prompt_text = self.difficulty_font.render("Select grid size (3-10):", True, (255, 255, 255))
        prompt_text_rect = prompt_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
        self.screen.blit(prompt_text, prompt_text_rect)

        # Update the display
        pygame.display.flip()

        # Wait for user input
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        return (3, 3)
                    elif event.key == pygame.K_4:
                        return (4, 4)
                    elif event.key == pygame.K_5:
                        return (5, 5)
                    elif event.key == pygame.K_6:
                        return (6, 6)
                    elif event.key == pygame.K_7:
                        return (7, 7)
                    elif event.key == pygame.K_8:
                        return (8, 8)
                    elif event.key == pygame.K_9:
                        return (9, 9)
                    elif event.key == pygame.K_0:
                        return (10, 10)



    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_button = (self.selected_button - 1) % 2
                elif event.key == pygame.K_DOWN:
                    self.selected_button = (self.selected_button + 1) % 2
                elif event.key == pygame.K_RETURN:
                    if self.selected_button == 0:
                        self.start_game()
                elif event.key == pygame.K_RETURN:
                    if self.selected_button == 0:
                            self.start_game(self.selected_difficulty)  # Pass selected_difficulty here

                    else:
                        self.home_screen()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.difficulty_rects[0].collidepoint(mouse_pos):
                    self.selected_difficulty = 0
                elif self.difficulty_rects[1].collidepoint(mouse_pos):
                    self.selected_difficulty = 1
                elif self.difficulty_rects[2].collidepoint(mouse_pos):
                    self.selected_difficulty = 2
                elif self.play_again_rect.collidepoint(mouse_pos):
                    self.start_game()
                elif self.home_rect.collidepoint(mouse_pos):
                    self.home_screen()
    def run(self):
        while self.running:
            self.handle_events()
            self.render()

        self.quit()

    def home_screen(self):
        self.reset_game()
        self.selected_difficulty = None  # Set selected_difficulty to None to display the home screen

    def render_characters(self, num_players, game_area_x, game_area_y):
        if num_players >= 2:
            self.character1.draw(self.screen, game_area_x, game_area_y)
            self.character2.draw(self.screen, game_area_x, game_area_y)
        if num_players >= 3:
            self.character3.draw(self.screen, game_area_x, game_area_y)
        if num_players == 4:
            self.character4.draw(self.screen, game_area_x, game_area_y)

    def reset_game(self):
        self.selected_difficulty = 0
        if self.selected_difficulty == 0:  # Easy difficulty
            self.character1 = Character(0, 0, self.cell_size, (255, 0, 0), self.grid_size, "Red")  # Red character
            self.character2 = Character(4, 4, self.cell_size, (0, 0, 255), self.grid_size, "Blue")  # Blue character
            if self.character3 is None:
                self.character3 = Character(0, 4, self.cell_size, (0, 255, 0), self.grid_size,
                                            "Green")  # Green character
            if self.character4 is None:
                self.character4 = Character(4, 0, self.cell_size, (255, 255, 0), self.grid_size,
                                            "Yellow")  # Yellow character
        elif self.selected_difficulty == 1:  # Medium difficulty
            self.character1 = Character(0, 0, self.cell_size, (255, 0, 0), self.grid_size, "Red")  # Red character
            self.character2 = Character(4, 4, self.cell_size, (0, 0, 255), self.grid_size, "Blue")  # Blue character
            if self.character3 is None:
                self.character3 = Character(0, 4, self.cell_size, (0, 255, 0), self.grid_size,
                                            "Green")  # Green character
            if self.character4 is None:
                self.character4 = Character(4, 0, self.cell_size, (255, 255, 0), self.grid_size,
                                            "Yellow")  # Yellow character
        elif self.selected_difficulty == 2:  # Hard difficulty

            pass

        self.selected_button = 0  # 0 for play again, 1 for home
        self.play_again_selected = True
        self.home_selected = False
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_difficulty = (self.selected_difficulty - 1) % len(self.difficulty_levels)
                elif event.key == pygame.K_DOWN:
                    self.selected_difficulty = (self.selected_difficulty + 1) % len(self.difficulty_levels)
                elif event.key == pygame.K_RETURN:
                    if self.selected_difficulty == 0:
                        self.start_game(self.selected_difficulty)
                    elif self.selected_difficulty == 1:
                        self.start_game(self.selected_difficulty)
                    elif self.selected_difficulty == 2:
                        self.start_game(self.selected_difficulty)



            elif event.type == pygame.MOUSEBUTTONDOWN and self.selected_button != 1:  # only allow clicks in play again and home when game over
                mouse_pos = pygame.mouse.get_pos()
                if self.difficulty_rects[0].collidepoint(mouse_pos):
                    self.selected_difficulty = 0
                    self.start_game(self.selected_difficulty)
                elif self.difficulty_rects[1].collidepoint(mouse_pos):
                    self.selected_difficulty = 1
                    self.start_game(self.selected_difficulty)
                elif self.difficulty_rects[2].collidepoint(mouse_pos):
                    self.selected_difficulty = 2
                    self.start_game(self.selected_difficulty)

    def start_game(self, selected_difficulty):
        if selected_difficulty == 0:
            self.start_easy_game()
        elif selected_difficulty == 1:
            self.start_medium_game()
        elif selected_difficulty == 2:
            self.start_hard_game()

    def game_over_screen(self, moves, selected_difficulty):
        # Clear the screen with white color
        self.screen.fill((255, 255, 255))

        # Render game over text
        game_over_text = self.title_font.render("Game Over", True, (0, 0, 0))
        game_over_text_rect = game_over_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
        self.screen.blit(game_over_text, game_over_text_rect)

        # Render moves text
        moves_text = self.title_font.render("Moves: " + str(moves), True, (0, 0, 0))
        moves_text_rect = moves_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.screen.blit(moves_text, moves_text_rect)

        # Render buttons
        play_again_button = pygame.Rect(self.screen_width // 2 - 100, self.screen_height // 2 + 50, 200, 50)
        pygame.draw.rect(self.screen, (0, 255, 0), play_again_button)
        play_again_text = self.title_font.render("Play Again", True, (0, 0, 0))
        play_again_text_rect = play_again_text.get_rect(center=play_again_button.center)
        self.screen.blit(play_again_text, play_again_text_rect)

        home_button = pygame.Rect(self.screen_width // 2 - 100, self.screen_height // 2 + 120, 200, 50)
        pygame.draw.rect(self.screen, (255, 0, 0), home_button)
        home_text = self.title_font.render("Home", True, (0, 0, 0))
        home_text_rect = home_text.get_rect(center=home_button.center)
        self.screen.blit(home_text, home_text_rect)

        pygame.display.flip()

        # Wait for button click
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if play_again_button.collidepoint(mouse_pos):
                        # Restart the game with the same difficulty
                        self.start_game(self.selected_difficulty)
                        return
                    elif home_button.collidepoint(mouse_pos):
                        self.home_screen()
                        return

    def start_easy_game(self):
        print("Starting game with EASY difficulty")
        # Clear the screen with white color
        self.screen.fill((255, 255, 255))
        self.selected_num_players = 2  # Store the selected number of players

        # Calculate the size of the game area
        game_area_width = self.cell_size * 5
        game_area_height = self.cell_size * 5

        # Calculate the position of the game area to center it on the screen
        game_area_x = (self.screen_width - game_area_width) // 2
        game_area_y = (self.screen_height - game_area_height) // 2

        # Draw the game area boundary
        pygame.draw.rect(self.screen, (0, 0, 0), (game_area_x, game_area_y, game_area_width, game_area_height), 2)

        # Draw the grid lines within the game area
        for x in range(game_area_x, game_area_x + game_area_width, self.cell_size):
            pygame.draw.line(self.screen, (0, 0, 0), (x, game_area_y), (x, game_area_y + game_area_height))
        for y in range(game_area_y, game_area_y + game_area_height, self.cell_size):
            pygame.draw.line(self.screen, (0, 0, 0), (game_area_x, y), (game_area_x + game_area_width, y))

        # Create characters within the game area
        self.character1 = Character(0, 0, self.cell_size, (255, 0, 0), self.grid_size, "Red")  # Red character
        self.character2 = Character(4, 4, self.cell_size, (0, 0, 255), self.grid_size, "Blue")  # Blue character

        # Initialize player move counters
        player1_moves = 0
        player2_moves = 0


        # Flag to switch between players
        player1_turn = True

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if player1_turn:
                # Move character1
                self.character1.move()
                player1_moves += 1
            else:
                # Move character2
                self.character2.move()
                player2_moves += 1

            # Update the display to show the grid and move counters
            player_moves = [player1_moves, player2_moves, 0, 0]
            self.update_display(game_area_x, game_area_y, game_area_width, game_area_height, player_moves)

            # Pause for a moment
            time.sleep(0.5)

            # Check if both characters are in the same cell
            if self.character1.x == self.character2.x and self.character1.y == self.character2.y:
                print("Both characters are in the same cell after", player1_moves, "moves!")
                self.game_over_screen(player1_moves, self.selected_difficulty)
                return  # Exit the game loop

            # Switch players
            player1_turn = not player1_turn

    def update_display(self, game_area_x, game_area_y, game_area_width, game_area_height, move_counters):
        # Clear the screen
        self.screen.fill((255, 255, 255))

        # Draw the game area boundary and grid lines
        pygame.draw.rect(self.screen, (0, 0, 0), (game_area_x, game_area_y, game_area_width, game_area_height), 2)
        for x in range(game_area_x, game_area_x + game_area_width, self.cell_size):
            pygame.draw.line(self.screen, (0, 0, 0), (x, game_area_y), (x, game_area_y + game_area_height))
        for y in range(game_area_y, game_area_y + game_area_height, self.cell_size):
            pygame.draw.line(self.screen, (0, 0, 0), (game_area_x, y), (game_area_x + game_area_width, y))

        self.render_characters(self.selected_num_players, game_area_x, game_area_y)


        # Render move counters for active players
        move_font = pygame.font.Font(None, 24)
        for i, moves in enumerate(move_counters):
            if moves > 0:  # Only render move counter if player is active
                player_moves_text = move_font.render(f"Player {i + 1} Moves: {moves}", True, (0, 0, 0))
                player_moves_rect = player_moves_text.get_rect(
                    center=((i + 1) * self.screen_width // (len(move_counters) + 1), 20))
                self.screen.blit(player_moves_text, player_moves_rect)

        # Update the display
        pygame.display.flip()

    def prompt_num_players(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Render text to prompt user for number of players
        prompt_text = self.difficulty_font.render("Select number of players (2-4):", True, (255, 255, 255))
        prompt_text_rect = prompt_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
        self.screen.blit(prompt_text, prompt_text_rect)

        # Update the display
        pygame.display.flip()

        # Wait for user input
        num_players = None
        while num_players is None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_2:
                        num_players = 2
                    elif event.key == pygame.K_3:
                        num_players = 3
                    elif event.key == pygame.K_4:
                        num_players = 4

        return num_players

    def start_medium_game(self):
        print("Starting game with MEDIUM difficulty")
        num_players = self.prompt_num_players()
        print("Selected number of players:", num_players)
        player1_moves = 0
        player2_moves = 0
        player3_moves = 0
        player4_moves = 0

        self.selected_num_players = num_players

        grid_size = self.prompt_grid_size()
        print("Selected grid size:", grid_size)

        self.screen.fill((255, 255, 255))

        game_area_width = self.cell_size * grid_size[0]
        game_area_height = self.cell_size * grid_size[1]
        game_area_x = (self.screen_width - game_area_width) // 2
        game_area_y = (self.screen_height - game_area_height) // 2

        pygame.draw.rect(self.screen, (0, 0, 0), (game_area_x, game_area_y, game_area_width, game_area_height), 2)
        player_moves = [player1_moves, player2_moves, player3_moves, player4_moves]



        #player_moves = [0] * num_players
        self.update_display(game_area_x, game_area_y, game_area_width, game_area_height, player_moves)
        characters = []
        for i in range(num_players):
            if i == 0:
                self.character1 = Character(0, 0, self.cell_size, (255, 0, 0), grid_size, "Red")
            elif i == 1:
                self.character2 = Character(grid_size[0] - 1, grid_size[1] - 1, self.cell_size, (0, 0, 255), grid_size,
                                            "Blue")
            elif i == 2:
                self.character3 = Character(0, grid_size[1] - 1, self.cell_size, (0, 255, 0), grid_size, "Green")
            elif i == 3:
                self.character4 = Character(grid_size[0] - 1, 0, self.cell_size, (255, 255, 0), grid_size, "Yellow")
           # characters.append(character)

        player_turn = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if player_turn ==0:
                # Move character1
                self.character1.move()
                player1_moves += 1
            elif player_turn == 1:
                # Move character2
                self.character2.move()
                player2_moves += 1
            elif player_turn == 2:
                # Move character3
                self.character3.move()
                player3_moves += 1
            elif player_turn == 3:
                # Move character4
                self.character4.move()
                player4_moves += 1


            # Pause for a moment
            time.sleep(0.5)

            # Check if all characters are at the same location
            if len(set((character.x, character.y) for character in characters)) == 1:
                print("All characters are together!")
                self.game_over_screen(0, self.selected_difficulty)
                return


            if self.character1.x == self.character2.x and self.character1.y == self.character2.y:
                print("Character 1 and Character 2 are in the same cell!")
                self.character2 = self.character1

            if self.character1.x == self.character3.x and self.character1.y == self.character3.y:
                print("Character 1 and Character 3 are in the same cell!")
                self.character3 = self.character1

            if self.character1.x == self.character4.x and self.character1.y == self.character4.y:
                print("Character 1 and Character 4 are in the same cell!")
                self.character4 = self.character1

            if self.character2.x == self.character3.x and self.character2.y == self.character3.y:
                print("Character 1 and Character 2 are in the same cell!")

                self.character3 = self.character2

            if self.character2.x == self.character4.x and self.character2.y == self.character4.y:
                print("Character 1 and Character 2 are in the same cell!")
                self.character4 = self.character2

            if self.character3.x == self.character4.x and self.character3.y == self.character4.y:
                print("Character 1 and Character 2 are in the same cell!")
                self.character4 = self.character3

            if num_players == 2:
                if self.character1.x == self.character2.x and self.character1.y == self.character2.y:
                    print("Both characters are in the same cell after", player1_moves, "moves!")
                    self.game_over_screen(player1_moves, self.selected_difficulty)
            elif num_players == 3:
                if self.character1.x == self.character2.x == self.character3.x and self.character1.y == self.character2.y == self.character3.y:
                    print("Both characters are in the same cell after", player1_moves, "moves!")
                    self.game_over_screen(player1_moves, self.selected_difficulty)
            elif num_players == 4:
                if self.character1.x == self.character2.x == self.character3.x == self.character4.x and self.character1.y == self.character2.y == self.character3.y == self.character4.y:
                    print("Both characters are in the same cell after", player1_moves, "moves!")
                    self.game_over_screen(player1_moves, self.selected_difficulty)

            self.update_display(game_area_x, game_area_y, game_area_width, game_area_height, player_moves)



            # Move to the next player
            player_turn = (player_turn + 1) % num_players

        pygame.quit()
        sys.exit()
    def start_hard_game(self):
        print("Starting game with HARD difficulty")

    def render(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))

        if self.selected_difficulty is None:
            # Render title text in the center of the screen
            title_text = self.title_font.render("Lost in the Woods Simulator", True, (255, 255, 255))
            title_text_rect = title_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
            self.screen.blit(title_text, title_text_rect)

            # Render difficulty options below the title
            for i, difficulty in enumerate(self.difficulty_levels):
                text = self.difficulty_font.render(difficulty, True, (255, 255, 255))
                text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 20 + 30 * i))
                if i == self.selected_difficulty:
                    pygame.draw.rect(self.screen, (255, 255, 255), text_rect, 2)
                self.screen.blit(text, text_rect)

        # Update the display
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()

# Define a Character class
class Character:
    def __init__(self, x, y, cell_size, color, grid_size, identifier):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.color = color
        self.grid_size = grid_size
        self.identifier = identifier

    def move(self):
        valid_moves = []
        if self.y - 1 >= 0:  # Check if moving up is valid
            valid_moves.append(('up', self.x, self.y - 1))
        if self.y + 1 < self.grid_size[1]:  # Check if moving down is valid
            valid_moves.append(('down', self.x, self.y + 1))
        if self.x - 1 >= 0:  # Check if moving left is valid
            valid_moves.append(('left', self.x - 1, self.y))
        if self.x + 1 < self.grid_size[0]:  # Check if moving right is valid
            valid_moves.append(('right', self.x + 1, self.y))

        direction, new_x, new_y = random.choice(valid_moves)
        self.x, self.y = new_x, new_y

    def draw(self, screen, game_area_x, game_area_y):
        pygame.draw.rect(screen, self.color, (game_area_x + self.x * self.cell_size, game_area_y + self.y * self.cell_size, self.cell_size, self.cell_size))