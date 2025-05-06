# utility.py
import pygame
from settings import BLACK, GREY, GRID_SIZE, FONT, RED

def draw_background(surface, width, height):  # hàm vẽ nền
    surface.fill(BLACK)   # màu đen
    for x in range(0, width, GRID_SIZE):   # vẽ các đường ngang
        pygame.draw.line(surface, GREY, (x, 0), (x, height))
    for y in range(0, height, GRID_SIZE):   # vẽ các đường dọc
        pygame.draw.line(surface, GREY, (0, y), (width, y))

def show_message(screen, message, width, height):   # hàm hiển thị các thông báo
    text = FONT.render(message, True, RED)   # tạo văn bản
    text_rect = text.get_rect(center=(width // 2, height // 2))   # lấy vị trí giữa màn hình
    screen.blit(text, text_rect)   # vẽ lên màn hình 
    pygame.display.update()   # cập nhật để hiện
