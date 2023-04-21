import pygame
import random

class Point:
    def __init__(self, kind, x, y):
        self.kind = kind
        self.x = x
        self.y = y
        self.image = pygame.image.load(f"{kind}.png")
        self.image = pygame.transform.scale(self.image, (30, 30))

    def is_colliding(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5 < 30

    def collide(self, other):
        changed = False
        if self.kind == "가위" and other.kind == "바위":
            self.kind = "바위"
            self.image = other.image
            changed = True
        elif self.kind == "바위" and other.kind == "종이":
            self.kind = "종이"
            self.image = other.image
            changed = True
        elif self.kind == "종이" and other.kind == "가위":
            self.kind = "가위"
            self.image = other.image
            changed = True
        return changed

def generate_random_points(n, width, height):
    kinds = ["가위", "바위", "종이"]
    return [Point(random.choice(kinds), random.randint(0, width), random.randint(0, height)) for _ in range(n)]

def check_collision(point_a, point_b):
    return ((point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2) ** 0.5 < 30

def handle_collision(point_a, point_b):
    changed = False
    if point_a.kind == "가위" and point_b.kind == "바위":
        point_a.kind = "바위"
        point_a.image = point_b.image
        changed = True
    elif point_a.kind == "바위" and point_b.kind == "종이":
        point_a.kind = "종이"
        point_a.image = point_b.image
        changed = True
    elif point_a.kind == "종이" and point_b.kind == "가위":
        point_a.kind = "가위"
        point_a.image = point_b.image
        changed = True
    return changed

def main():
    screen_width = 800
    screen_height = 600
    random_points = generate_random_points(50, screen_width, screen_height)

    pygame.init()
    display = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("가위바위보 시뮬레이션")
    clock = pygame.time.Clock()

    running = True
    while running:
        display.fill((255, 255, 255))

        for point in random_points:
            display.blit(point.image, (point.x, point.y))

        pygame.display.flip()
        clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for i in range(len(random_points)):
            point_a = random_points[i]

            dx = random.randint(-10, 10)
            dy = random.randint(-10, 10)

            point_a.x = (point_a.x + dx) % screen_width
            point_a.y = (point_a.y + dy) % screen_height

            for j in range(len(random_points)):
                if i == j:
                    continue
                point_b = random_points[j]

                if check_collision(point_a, point_b):
                    handle_collision(point_a, point_b)

    pygame.quit()


if __name__ == "__main__":
    main()
