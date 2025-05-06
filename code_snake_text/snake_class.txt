# snake_class.py
import pygame
from settings import GRID_SIZE, UP, DOWN, LEFT, RIGHT, BLACK   # cập nhật từ "settings"

class Snake:   # khởi tạo lớp snake
    def __init__(self, color, head_shape, width, height):   # hàm cha khởi tạo các thuộc tính cơ bản
        self.length = 3   # chiều dài bắt đầu
        self.direction = RIGHT   # hướng bắt đầu
        head_x = width // 2   # vị trí đầu rắn bắt đầu
        head_y = height // 2
        self.positions = [   # vị trí đầu rắn đến đuôi
            (head_x, head_y),
            (head_x - GRID_SIZE, head_y),
            (head_x - 2 * GRID_SIZE, head_y)
        ]
        self.color = color   # gán màu sắc cho rắn
        self.head_shape = head_shape   # gán hình dạng đầu cho rắn

    def get_head_position(self):   # phương thức trả về vị trí đầu rắn
        return self.positions[0]

    def turn(self, point):   # phương thức thay đổi hướng di chuyển cho rắn
        if len(self.positions) > 1 and (point[0] * -1, point[1] * -1) == self.direction:   # hàm ngăn rắn quay 180 độ
            return
        else:
            self.direction = point    # cập nhật hướng di chuyển mới

    def move(self, width, height, wall_mode):   # phương thức di chuyển theo hướng hiện tại
        cur = self.get_head_position()   # lấy tọa độ đầu rắn
        x, y = self.direction   # lấy hướng di chuyển
        new = (cur[0] + x * GRID_SIZE, cur[1] + y * GRID_SIZE)   # tọa độ đầu rắn mới

        if wall_mode:   # chế độ tường
            if new[0] < 0 or new[0] >= width or new[1] < 0 or new[1] >= height:   # khi đầu rắn ra khỏi màn hình, rắn thua
                return False
        else:
            new = (new[0] % width, new[1] % height)

        if new in self.positions[1:]:   # nếu đầu rắn cắn vào thân, rắn thua
            return False

        self.positions.insert(0, new)   # thêm các vị trí mới vào đầu rắn
        if len(self.positions) > self.length:   # nếu độ dài vượt quá lý thuyết, loại bỏ phần cuối
            self.positions.pop()
        return True

    def reset(self, color, head_shape, width, height):   # hàm con để khởi tạo lại rắn
        self.__init__(color, head_shape, width, height)

    def draw(self, surface, width, height):   # hàm vẽ rắn
        for i, p in enumerate(self.positions):   # p là tọa độ, i là chỉ số
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))   # vẽ 1 hình chữ nhật tại các tọa độ p
            if i == 0:   # xét đầu rắn
                if self.head_shape == "Circle":   # nếu đầu tròn
                    pygame.draw.circle(surface, self.color, r.center, GRID_SIZE // 2)  # vẽ đầu tròn, tâm r của ô
                elif self.head_shape == "Arrow":   # nếu đầu tam giác
                    x, y = p   # lấy tọa độ đầu rắn
                    if self.direction == UP:   # nếu hướng di chuyển lên trên
                        points = [(x + GRID_SIZE // 2, y), (x, y + GRID_SIZE), (x + GRID_SIZE, y + GRID_SIZE)]   
                    elif self.direction == DOWN:   # nếu hướng di chuyển xuống dưới
                        points = [(x, y), (x + GRID_SIZE, y), (x + GRID_SIZE // 2, y + GRID_SIZE)]
                    elif self.direction == LEFT:   # nếu hướng di chuyển sang trái
                        points = [(x + GRID_SIZE, y), (x + GRID_SIZE, y + GRID_SIZE), (x, y + GRID_SIZE // 2)]
                    elif self.direction == RIGHT:   # nếu hướng di chuyển sang phải
                        points = [(x, y), (x + GRID_SIZE, y + GRID_SIZE // 2), (x, y + GRID_SIZE)]
                    pygame.draw.polygon(surface, self.color, points)  # vẽ đa giác theo công thức đã cho
                else:  
                    pygame.draw.rect(surface, self.color, r)   # vẽ hình hộp
                    
                eye_radius = 2   # bán kính mắt rắn
                cx, cy = r.center   # lấy tọa độ tâm
                if self.head_shape == "Arrow":   # nếu đầu tam giác
                    if self.direction == UP:
                        eye1 = (cx - 4, cy + 2)   # mắt trái
                        eye2 = (cx + 4, cy + 2)   # mắt phải
                    elif self.direction == DOWN:
                        eye1 = (cx - 4, cy - 2)
                        eye2 = (cx + 4, cy - 2)
                    elif self.direction == LEFT:
                        eye1 = (cx + 2, cy - 4)
                        eye2 = (cx + 2, cy + 4)
                    elif self.direction == RIGHT:
                        eye1 = (cx - 2, cy - 4)
                        eye2 = (cx - 2, cy + 4)
                else:  # nếu đầu vuông hoặc tròn
                    eye_offset = 5   # từ tâm đến mắt
                    if self.direction in [UP, DOWN]:
                        offset_y = -4 if self.direction == UP else 4  # điều chỉnh dưới/trên
                        eye1 = (cx - eye_offset, cy + offset_y)   # trái/trên
                        eye2 = (cx + eye_offset, cy + offset_y)   # phải/dưới
                    else:
                        offset_x = -4 if self.direction == LEFT else 4   # điều chỉnh phải/trái
                        eye1 = (cx + offset_x, cy - eye_offset)   # trên/trái
                        eye2 = (cx + offset_x, cy + eye_offset)   # dưới/phải
                pygame.draw.circle(surface, BLACK, eye1, eye_radius)
                pygame.draw.circle(surface, BLACK, eye2, eye_radius)
                
            elif i == len(self.positions) - 1:
                tail = self.positions[-1]   # xác định đuôi rắn
                before_tail = self.positions[-2]   # xác định đốt gần cuối
                dx = tail[0] - before_tail[0]   # tính toán sự thay đổi của 2 đốt
                dy = tail[1] - before_tail[1]
                x, y = tail   # lấy tọa độ cho đuối
                if dx == GRID_SIZE:   # nếu đuối hướng sang phải
                    points = [(x + GRID_SIZE, y + GRID_SIZE // 2), (x, y), (x, y + GRID_SIZE)]
                elif dx == -GRID_SIZE:   # nếu đuôi hướng sang trái
                    points = [(x, y + GRID_SIZE // 2), (x + GRID_SIZE, y), (x + GRID_SIZE, y + GRID_SIZE)]
                elif dy == GRID_SIZE:   # nếu đuôi hướng xuống
                    points = [(x + GRID_SIZE // 2, y + GRID_SIZE), (x, y), (x + GRID_SIZE, y)]
                elif dy == -GRID_SIZE:   # nếu đuôi hướng lên
                    points =[(x + GRID_SIZE // 2, y), (x, y + GRID_SIZE), (x + GRID_SIZE, y + GRID_SIZE)]
                else:
                    pygame.draw.rect(surface, self.color, r)   # vẽ đuôi chữ nhật nếu ko thể xác định
                    continue
                pygame.draw.polygon(surface, self.color, points)   # vẽ đuôi hình tam giác
            else:
                pygame.draw.rect(surface, self.color, r)   # nếu là đốt thân

            