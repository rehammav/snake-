# food_class.py
import pygame
import random
from settings import GRID_SIZE, RED

class Food:   # khởi tạo lớp food
    def __init__(self):   # hàm cha khởi tạo các thuộc tính cơ bản
        self.color = RED   # gán màu sắc
        self.position = (0, 0)   # gán vị trí food bắt đầu

    def randomize_position(self, grid_width, grid_height, snake_positions):   # phương thức tạo ngẫu nhiên food
        while True:
            pos = (
                random.randint(0, grid_width - 1) * GRID_SIZE,   # tọa độ x ngẫu nhiên
                random.randint(0, grid_height - 1) * GRID_SIZE   # tọa độ y ngẫu nhiên
            )
            if pos not in snake_positions:   # kiểm tra xem có bị trùng với rắn
                self.position = pos   # tạo vị trí khác
                break

    def draw(self, surface):   # hàm con để vẽ food
        center = (self.position[0] + GRID_SIZE // 2, self.position[1] + GRID_SIZE // 2)  # tính tọa độ tâm của ô
        pygame.draw.circle(surface, self.color, center, GRID_SIZE // 2)   # vẽ 
