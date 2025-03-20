import pgzrun
import random

WIDTH = 500
HEIGHT = 500

class RectanglePattern:
    def __init__(self, center_x, center_y, num_rects):
        self.center_x = center_x
        self.center_y = center_y
        self.num_rects = num_rects
        self.w = 50
        self.h = 50
        self.r = 255
        self.g = 0
        self.b = random.randint(120, 255)

    def draw(self):
        for _ in range(self.num_rects):
            rect = Rect((0, 0), (self.w, self.h))  # Create Rect
            rect.center = (self.center_x, self.center_y)  # Center the rect
            screen.draw.rect(rect, (self.r, self.g, self.b))  # Draw the rectangle
            
            self.w += 10
            self.h += 10

            self.r = max(0, self.r - 10)
            self.g = min(255, self.g + 10)


pattern = RectanglePattern(center_x=250, center_y=250, num_rects=20)

def draw():
    screen.clear()
    pattern.draw()

pgzrun.go()
