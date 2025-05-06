# main.py
import pygame
from settings import *
from menu import main_menu, options_menu
from game import run_game

def main():   # hàm chính để chạy toàn bộ chương trình
    selected = {   # tạo từ điển để lưu các cài đặt của người chơi
        'color': DEFAULT_SNAKE_COLOR_INDEX,
        'shape': DEFAULT_SNAKE_SHAPE_INDEX,
        'wall': DEFAULT_WALL_MODE,
        'size': DEFAULT_SIZE_INDEX
    }

    pygame.init()   # khởi tạo các module của pygame
    width, height = SCREEN_SIZES[selected['size']][1]   # lấy kích thước từ cài đặt của người chơi
    screen = pygame.display.set_mode((width, height))   # tạo cửa sổ
    pygame.display.set_caption("Snake Game")   # tiêu đề cửa sổ

    while True:   # vòng lặp giữa menu game, options và game
        choice = main_menu(screen, width, height)   # menu chính có kết quả của người chơi
        if choice == "options":   # nếu chọn options
            options_menu(screen, selected)   # hiện màn hình options
            width, height = SCREEN_SIZES[selected['size']][1]
            screen = pygame.display.set_mode((width, height))   # cập nhật lại để hiện game
        elif choice == "start":   # nếu chọn start
            run_game(screen, width, height, selected)   # chạy game

if __name__ == "__main__":   # đảm bảo chương trình chỉ chạy trực 
    main()
