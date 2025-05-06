# settings.py
import pygame

# các kích thước màn hình của game
SCREEN_SIZES = [
    ["Small", (400, 400)],
    ["Medium", (480, 480)],
    ["Large", (760, 640)]
]
DEFAULT_SIZE_INDEX = 1   # cài đặt mặc định là "Medium"

# kích thước mỗi ô lưới
GRID_SIZE = 20

# màu sắc có trong game
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 105, 180)
GREY = (40, 40, 40)

# cài đặt cho rắn
SNAKE_COLORS = [GREEN, RED, WHITE, BLUE, YELLOW, PINK]   # các màu của rắn
SNAKE_COLOR_NAMES = ["Green", "Red", "White", "Blue", "Yellow", "Pink"]
SNAKE_HEAD_SHAPES = ["Square", "Circle", "Arrow"]   # các hình dạng cho đầu rắn
DEFAULT_SNAKE_COLOR_INDEX = 0
DEFAULT_SNAKE_SHAPE_INDEX = 0

# chế độ tường
DEFAULT_WALL_MODE = False

# hướng di chuyển của rắn
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# font chữ của game
pygame.init()   # khởi tạo fond chữ 
FONT = pygame.font.Font(None, 30)