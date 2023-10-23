import time

from engine.engine2d import Rectangle, Circle, Triangle, Engine2D

engine = Engine2D(800, 600, "2D-движок")

rectangle = Rectangle('Прямоугольник', (255, 0, 0), (100, 200, 200, 100))
circle = Circle('Круг', (0, 255, 0), (400, 200, 100, 100))
triangle = Triangle('Треугольник', (0, 0, 255), (600, 200, 100, 100))


def test_rectangle_draw():
    engine.canvas.append(rectangle)
    engine.draw()
    time.sleep(1)

    assert rectangle in engine.canvas
    engine.canvas = []


def test_circle_draw():
    engine.canvas.append(circle)
    engine.draw()
    time.sleep(1)

    assert circle in engine.canvas
    engine.canvas = []


def test_triangle_draw():
    engine.canvas.append(triangle)
    engine.draw()
    time.sleep(1)

    assert triangle in engine.canvas
    engine.canvas = []


def test_change_color():
    engine.canvas.append(rectangle)
    engine.canvas.append(circle)
    engine.canvas.append(triangle)

    rectangle._change_color((0, 0, 255))  # Изменяем цвет прямоугольника на синий
    circle._change_color((255, 255, 0))  # Изменяем цвет круга на желтый

    engine.draw()
    time.sleep(1)

    assert rectangle.get_color() == (0, 0, 255), "Цвет прямоугольника не изменился на синий"
    assert circle.get_color() == (255, 255, 0), "Цвет круга не изменился на желтый"
    engine.canvas = []


def test_delete_figure():
    engine.canvas.append(rectangle)
    engine.canvas.append(circle)
    engine.canvas.append(triangle)

    engine.canvas.remove(triangle)  # Удаляем прямоугольник из canvas
    engine.draw()
    time.sleep(1)
    assert triangle not in engine.canvas, "Прямоугольник не был удален из canvas"

