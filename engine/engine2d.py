import pygame


class Rectangle:
    def __init__(self, text, color, position):
        self.text = text
        self.color = color
        self.position = position

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.position)
        font = pygame.font.Font(None, 20)
        text_surface = font.render(self.text, True, self.color)
        screen.blit(text_surface, (10, 40))


class Circle:
    def __init__(self, text, color, position):
        self.text = text
        self.color = color
        self.position = position

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.position)
        font = pygame.font.Font(None, 20)
        text_surface = font.render(self.text, True, self.color)
        screen.blit(text_surface, (10, 60))


class Triangle:
    def __init__(self, text, color, position):
        self.text = text
        self.color = color
        self.position = position

    def draw(self, screen):
        points = [
            (self.position[0] + self.position[2] / 2, self.position[1]),
            (self.position[0], self.position[1] + self.position[3]),
            (self.position[0] + self.position[2], self.position[1] + self.position[3])
        ]
        pygame.draw.polygon(screen, self.color, points)
        font = pygame.font.Font(None, 20)
        text_surface = font.render(self.text, True, self.color)
        screen.blit(text_surface, (10, 80))


class Engine2D:
    def __init__(self, width, height, title):
        pygame.init()
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.canvas = []

    def draw(self):
        self.screen.fill((255, 255, 255))  # Заполнить экран белым цветом

        for shape in self.canvas:
            shape.draw(self.screen)

        pygame.display.flip()  # Обновить экран