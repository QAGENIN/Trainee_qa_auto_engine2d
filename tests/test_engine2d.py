import time

from engine.engine2d import Rectangle, Circle, Triangle, Engine2D

engine = Engine2D(800, 600, "2D-движок")

shape1 = Rectangle('Прямоугольник', (255, 0, 0), (100, 200, 200, 100))
shape2 = Circle('Круг', (0, 255, 0), (400, 200, 100, 100))
shape3 = Triangle('Треугольник', (0, 0, 255), (600, 200, 100, 100))


def test_rectangle_draw():
    engine.canvas.append(shape1)
    engine.draw()
    time.sleep(1)

    assert shape1 in engine.canvas
    engine.canvas = []


def test_circle_draw():
    engine.canvas.append(shape2)
    engine.draw()
    time.sleep(1)

    assert shape2 in engine.canvas
    engine.canvas = []


def test_triangle_draw():
    engine.canvas.append(shape3)
    engine.draw()
    time.sleep(1)

    assert shape3 in engine.canvas
    engine.canvas = []


def test_change_color():
    engine.canvas.append(shape1)
    engine.canvas.append(shape2)
    engine.canvas.append(shape3)

    shape1.color = (0, 0, 255)  # Изменяем цвет прямоугольника на синий
    shape2.color = (255, 255, 0)  # Изменяем цвет круга на желтый

    engine.draw()
    time.sleep(1)

    assert shape1.color == (0, 0, 255), "Цвет прямоугольника не изменился на синий"
    assert shape2.color == (255, 255, 0), "Цвет круга не изменился на желтый"
    engine.canvas = []


def test_delete_figure():
    engine.canvas.append(shape1)
    engine.canvas.append(shape2)
    engine.canvas.append(shape3)

    engine.canvas.remove(shape3)  # Удаляем прямоугольник из canvas
    engine.draw()
    time.sleep(1)
    assert shape3 not in engine.canvas, "Прямоугольник не был удален из canvas"

