import pygame


class Shape:
    def __init__(self, text, color, position):
        self.text = text
        self._color = color
        self.position = position

    def draw(self, screen):
        raise NotImplementedError

    def _change_color(self, new_color):
        self._color = new_color

    def get_color(self):
        return self._color


class Rectangle(Shape):
    def draw(self, screen):
        pygame.draw.rect(screen, self._color, self.position)
        font = pygame.font.Font(None, 20)
        text_surface = font.render(self.text, True, self._color)
        screen.blit(text_surface, (10, 40))

        print("Drawing Rectangle: {}, color: {}, position: {}".format(self.text, self._color, self.position))


class Circle(Shape):
    def draw(self, screen):
        pygame.draw.ellipse(screen, self._color, self.position)
        font = pygame.font.Font(None, 20)
        text_surface = font.render(self.text, True, self._color)
        screen.blit(text_surface, (10, 60))

        print("Drawing Circle: {}, color: {}, position: {}".format(self.text, self._color, self.position))
        return self


class Triangle(Shape):
    def draw(self, screen):
        points = [
            (self.position[0] + self.position[2] / 2, self.position[1]),
            (self.position[0], self.position[1] + self.position[3]),
            (self.position[0] + self.position[2], self.position[1] + self.position[3])
        ]
        pygame.draw.polygon(screen, self._color, points)
        font = pygame.font.Font(None, 20)
        text_surface = font.render(self.text, True, self._color)
        screen.blit(text_surface, (10, 80))

        print("Drawing Triangle: {}, color: {}, position: {}".format(self.text, self._color, self.position))


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
        self.canvas.clear()