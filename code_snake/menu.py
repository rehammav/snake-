# menu.py
import pygame
import sys
from settings import *

def main_menu(screen, width, height):   # tạo hàm để vẽ và xử lý menu
    while True:   # tạo vòng lặp
        screen.fill(BLACK)
        title = FONT.render("Snake Game", True, WHITE)   # tạo tiêu đề game
        start_text = FONT.render("Press S to Start", True, WHITE)   # dòng hướng dẫn cách bắt đầu game
        option_text = FONT.render("Press O for Options", True, WHITE)   # dòng hướng dẫn cách mở menu
        screen.blit(title, (width // 2 - 60, height // 3))   # vẽ dòng tiêu đề
        screen.blit(start_text, (width // 2 - 80, height // 2))   # vẽ dòng hướng dẫn cách bắt đầu game
        screen.blit(option_text, (width // 2 - 100, height // 2 + 40))   # vẽ dòng hướng dẫn cách mở menu
        pygame.display.update()   # cập nhật để hiện

        for event in pygame.event.get():   # kiểm tra các sự kiện
            if event.type == pygame.QUIT:   # nếu bấm thoát cửa 
                pygame.quit(); sys.exit()   # thoát game
            elif event.type == pygame.KEYDOWN:   # nếu ấn phím
                if event.key == pygame.K_s:   # phím s
                    return "start"   # bắt đầu game
                elif event.key == pygame.K_o:   # phím o
                    return "options"   # vào cài đặt lựa chọn

def options_menu(screen, selected):   # hàm xử lý khi bấm vào options
    while True:   # tạo vòng lặp
        screen.fill(BLACK)
        color_text = FONT.render(f"Snake Color: {SNAKE_COLOR_NAMES[selected['color']]} (Press C)", True, SNAKE_COLORS[selected['color']])
        shape_text = FONT.render(f"Head Shape: {SNAKE_HEAD_SHAPES[selected['shape']]} (Press H)", True, WHITE)
        wall_text = FONT.render(f"Wall Mode: {'On' if selected['wall'] else 'Off'} (Press W)", True, WHITE)
        size_text = FONT.render(f"Screen Size: {SCREEN_SIZES[selected['size']][0]} (Press S)", True, WHITE)
        back_text = FONT.render("Press B to go back", True, WHITE)   # vẽ các văn bản để lựa chọn

        screen.blit(color_text, (50, 100))   # vị trí của các lựa chọn
        screen.blit(shape_text, (50, 140))
        screen.blit(wall_text, (50, 180))
        screen.blit(size_text, (50, 220))
        screen.blit(back_text, (50, 260))
        pygame.display.update()   # cập nhật để hiện ra màn hình

        for event in pygame.event.get():   # kiểm tra các sự kiện người dùng
            if event.type == pygame.QUIT:   # nếu đóng cửa sổ
                pygame.quit(); sys.exit()   # thoát game
            elif event.type == pygame.KEYDOWN:   # nếu ấn phím
                if event.key == pygame.K_c:   # phím c
                    selected['color'] = (selected['color'] + 1) % len(SNAKE_COLORS)   # thay đổi màu rắn
                elif event.key == pygame.K_h:   # phím h
                    selected['shape'] = (selected['shape'] + 1) % len(SNAKE_HEAD_SHAPES)   # thay đổi hình dạng đầu rắn
                elif event.key == pygame.K_w:   # phím w
                    selected['wall'] = not selected['wall']    # thay đổi chế độ có/không có tường
                elif event.key == pygame.K_s:   # phím s
                    selected['size'] = (selected['size'] + 1) % len(SCREEN_SIZES)   # thay đổi kích thức cửa sổ
                elif event.key == pygame.K_b:   # phím b
                    return    # thoát vòng 
