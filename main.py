import pygame
import sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN


def calculate_slope(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0]) if p2[0] != p1[0] else None


def is_within_grid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def main():
    pygame.init()

    n, m = 4, 4
    cell_size = 100
    width, height = n * cell_size, m * cell_size

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Grid Game')

    grid_color = (200, 200, 200)
    point_color = (255, 0, 0)
    font_color = (0, 0, 0)

    distinct_points = []
    distinct_slopes = []

    font = pygame.font.Font(None, 36)

    clock = pygame.time.Clock()

    game_over = False
    message = ""

    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                point = (x // cell_size, y // cell_size)

                if point in distinct_points:
                    message = "You entered a duplicate point. You lost the game."
                    game_over = True
                    break

                if not is_within_grid(point[0], point[1], n, m):
                    message = "The point is outside the grid. You lost the game."
                    game_over = True
                    break

                distinct_points.append(point)

                if len(distinct_points) > 1:
                    xs, ys = zip(*[(p[0] * cell_size, p[1] * cell_size) for p in distinct_points])
                    if len(set(xs)) < len(xs):
                        message = "Repeated row. You lost the game."
                        game_over = True
                        break
                    if len(set(ys)) < len(ys):
                        message = "Repeated column. You lost the game."
                        game_over = True
                        break

                    for i in range(len(distinct_points) - 1):
                        slope = calculate_slope(distinct_points[i], point)
                        if slope in distinct_slopes:
                            message = "You lost for related slope."
                            game_over = True
                            break
                        distinct_slopes.append(slope)

        screen.fill((255, 255, 255))

        for i in range(n):
            pygame.draw.line(screen, grid_color, (i * cell_size, 0), (i * cell_size, height))
        for i in range(m):
            pygame.draw.line(screen, grid_color, (0, i * cell_size), (width, i * cell_size))

        for point in distinct_points:
            pygame.draw.circle(screen, point_color,
                               (point[0] * cell_size + cell_size // 2, point[1] * cell_size + cell_size // 2),
                               cell_size // 3)

        if game_over:
            text = font.render(message, True, font_color)
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))

        pygame.display.update()
        clock.tick(30)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()