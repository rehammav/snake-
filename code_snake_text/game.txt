# game.py
import pygame, sys
from snake_class import Snake
from food_class import Food
from settings import *
from utility import draw_background, show_message

def run_game(screen, width, height, selected):   # hàm điều khiển vòng lặp chính của trò chơi
    grid_width = width // GRID_SIZE   # tính độ lớn của màn hình
    grid_height = height // GRID_SIZE
    surface = pygame.Surface(screen.get_size()).convert()   # tạo bề mặt vẽ game

    clock = pygame.time.Clock()   # tạo đồng hồ để kiểm soát fps
    snake = Snake(SNAKE_COLORS[selected['color']], SNAKE_HEAD_SHAPES[selected['shape']], width, height)
    food = Food()   # tạo đối tượng snake và foood
    food.randomize_position(grid_width, grid_height, snake.positions)    # ngẫu nhiên food không trùng với snake
    score = 0   # khởi tạo điểm số, tốc độ và cơ chế tạm dừng
    speed = 5
    paused = False

    while True:   # tạo vòng lặp game
        clock.tick(speed)    # kiểm soát fps
        for event in pygame.event.get():   # kiểm tra các sự kiện 
            if event.type == pygame.QUIT:   # nếu bấm đóng cửa sổ
                pygame.quit(); sys.exit()   # thoát game
            elif event.type == pygame.KEYDOWN:   # nếu bấm phím
                if event.key == pygame.K_UP: snake.turn(UP)   # phím mũi tên để di chuyển
                elif event.key == pygame.K_DOWN: snake.turn(DOWN)
                elif event.key == pygame.K_LEFT: snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT: snake.turn(RIGHT)
                elif event.key == pygame.K_ESCAPE: return   # bấm phím esc để thoát về menu
                elif event.key == pygame.K_p: paused = not paused   # phím p để dừng lại hoặc tiếp tục nếu đang dừng lại

        if paused:   # nếu dừng lại
            show_message(screen, "Paused! Press P to resume.", width, height)   # hiện thông báo
            continue

        head_x, head_y = snake.get_head_position()   # xác định tọa độ đầu rắn
        dx, dy = snake.direction   # xác định hướng di chuyển của rắn
        new_head = (head_x + dx * GRID_SIZE, head_y + dy * GRID_SIZE)   # tính vị trí mới của đầu rắn

        if selected['wall']:   # chế độ tường
            if not (0 <= new_head[0] < width and 0 <= new_head[1] < height):   # đầu rắn ra ngoài màn hình, thua
                show_message(screen, "Game Over! Press R or ESC.", width, height)
                if not wait_restart(snake, food, selected, score, width, height, grid_width, grid_height): return
                continue

        if not snake.move(width, height, selected['wall']):   # nếu ko thể di chuyển, thua
            show_message(screen, "Game Over! Press R or ESC.", width, height)
            if not wait_restart(snake, food, selected, score, width, height, grid_width, grid_height): return
            continue

        if snake.get_head_position() == food.position:   # nếu đầu rắn trùng với food
            snake.length += 1   # chiều dài thêm 1
            score += 1    # điểm thêm 1
            speed = min(15, 5 + score // 5)   # tăng 1 fps mỗi 5 điểm thêm
            food.randomize_position(grid_width, grid_height, snake.positions)   # random lại vị trí thức ăn

        draw_background(surface, width, height)   # vẽ lại nền
        snake.draw(surface, width, height)   # vẽ lại rắn
        food.draw(surface)   # vẽ lại food
        screen.blit(surface, (0, 0))   # hiện thị game lên màn hình
        score_text = FONT.render(f"Score: {score}", True, WHITE)   # hiện thị điểm
        screen.blit(score_text, (5, 5))   # vị trí của điểm
        pygame.display.update()   # cập nhật màn hình để hiện thay đổi

def wait_restart(snake, food, selected, score, width, height, grid_width, grid_height):   # hàm để đợi người chơi ấn r hoặc esc sau khi thua
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    snake.reset(SNAKE_COLORS[selected['color']], SNAKE_HEAD_SHAPES[selected['shape']], width, height)
                    food.randomize_position(grid_width, grid_height, snake.positions)
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False
