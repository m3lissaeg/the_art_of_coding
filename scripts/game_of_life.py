import pygame
import numpy as np

# --- Configuration ---
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 80
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 10

# Colors
COLOR_BG = (10, 10, 20)
COLOR_ALIVE = (0, 255, 150)
COLOR_TEXT = (240, 240, 240)

# Updated Tetrominoes based on your image
# Format: Key: (Name, Description, Coordinates)
TETROMINOES = {
    pygame.K_1: ("O-Tetromino", "Outcome: Stable (The Block)", [(0,0), (1,0), (0,1), (1,1)]),
    pygame.K_2: ("L-Tetromino (A)", "Outcome: Stable (The Beehive)", [(0,0), (1,0), (2,0), (0,1)]),
    pygame.K_3: ("I-Tetromino", "Outcome: Stable (The Tub)", [(0,0), (0,1), (0,2), (0,3)]),
    pygame.K_4: ("L-Tetromino (B)", "Outcome: Death (Extinction)", [(0,0), (1,0), (1,1), (1,2)]),
    pygame.K_5: ("T-Tetromino", "Outcome: Repeat (The Pulsar)", [(1,0), (0,1), (1,1), (2,1)]),
    pygame.K_6: ("S-Tetromino", "Outcome: Stable (The Lozenge)", [(1,0), (0,1), (1,1), (1,2)]),
}

def update_grid(grid):
    """Vectorized calculation for Conway's Rules."""
    neighbors = (
        np.roll(np.roll(grid, 1, 0), 1, 1) + np.roll(np.roll(grid, 1, 0), 0, 1) +
        np.roll(np.roll(grid, 1, 0), -1, 1) + np.roll(np.roll(grid, 0, 0), 1, 1) +
        np.roll(np.roll(grid, 0, 0), -1, 1) + np.roll(np.roll(grid, -1, 0), 1, 1) +
        np.roll(np.roll(grid, -1, 0), 0, 1) + np.roll(np.roll(grid, -1, 0), -1, 1)
    )
    birth = (neighbors == 3) & (grid == 0)
    survive = ((neighbors == 2) | (neighbors == 3)) & (grid == 1)
    new_grid = np.zeros_like(grid)
    new_grid[birth | survive] = 1
    return new_grid

def draw_grid(screen, grid):
    living_cells = np.argwhere(grid == 1)
    for r, c in living_cells:
        pygame.draw.rect(screen, COLOR_ALIVE, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life: Tetromino Fate")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Verdana", 20)
    title_font = pygame.font.SysFont("Verdana", 28, bold=True)

    grid = np.zeros((GRID_SIZE, GRID_SIZE))
    state = "MENU"
    current_label = ""
    current_outcome = ""

    running = True
    while running:
        screen.fill(COLOR_BG)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    state = "MENU"
                    grid = np.zeros((GRID_SIZE, GRID_SIZE))

                # Individual Patterns (1-6)
                elif event.key in TETROMINOES:
                    grid = np.zeros((GRID_SIZE, GRID_SIZE))
                    name, outcome, coords = TETROMINOES[event.key]
                    current_label, current_outcome = name, outcome
                    for dr, dc in coords:
                        grid[GRID_SIZE//2 + dr, GRID_SIZE//2 + dc] = 1
                    state = "RUNNING"

                # SHOW ALL (A)
                elif event.key == pygame.K_a:
                    grid = np.zeros((GRID_SIZE, GRID_SIZE))
                    current_label, current_outcome = "Comparing All Tetrominoes", "Observe different fates"
                    # Distributed positions in the matrix
                    positions = [(20, 20), (20, 55), (40, 20), (40, 55), (60, 20), (60, 55)]
                    for i, (key, (name, out, coords)) in enumerate(TETROMINOES.items()):
                        pr, pc = positions[i]
                        for dr, dc in coords:
                            grid[pr + dr, pc + dc] = 1
                    state = "RUNNING"

                # RANDOM (R)
                elif event.key == pygame.K_r:
                    grid = np.random.choice([0, 1], size=(GRID_SIZE, GRID_SIZE), p=[0.9, 0.1])
                    current_label, current_outcome = "Random Primordial Soup", "Emergent structures"
                    state = "RUNNING"

                elif event.key == pygame.K_SPACE:
                    state = "PAUSED" if state == "RUNNING" else "RUNNING"

        if state == "MENU":
            lines = [
                ("THE LIVES OF TETROMINOES", title_font),
                ("---------------------------------", font),
                ("1: O-Tetromino -> Stable Block", font),
                ("2: L-Tetromino (A) -> Beehive", font),
                ("3: I-Tetromino -> Tub", font),
                ("4: L-Tetromino (B) -> Extinction", font),
                ("5: T-Tetromino -> Oscillating Pulsar", font),
                ("6: S-Tetromino -> Lozenge", font),
                ("", font),
                ("A: Show All Simultaneously", font),
                ("R: Primordial Soup (Random)", font),
                ("M: Menu | Space: Pause", font)
            ]
            for i, (text, f) in enumerate(lines):
                img = f.render(text, True, COLOR_TEXT)
                screen.blit(img, (WIDTH//4, 100 + i * 40))

        else:
            if state == "RUNNING":
                grid = update_grid(grid)
            draw_grid(screen, grid)

            # Label overlay
            info = font.render(f"{current_label}: {current_outcome}", True, (255, 255, 255))
            screen.blit(info, (10, 10))
            back_info = font.render("Press 'M' for Menu", True, (150, 150, 150))
            screen.blit(back_info, (10, 40))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()