import time

from engine.engine2d import Rectangle, Circle, Triangle

rectangle = Rectangle('Прямоугольник', (255, 0, 0), (100, 200, 200, 100))
circle = Circle('Круг', (0, 255, 0), (400, 200, 100, 100))
triangle = Triangle('Треугольник', (0, 0, 255), (600, 200, 100, 100))


def test_rectangle_draw(engine_object):
    engine_object.canvas.append(rectangle)
    engine_object.draw()
    time.sleep(1)
    assert rectangle in engine_object.canvas


def test_circle_draw(engine_object):
    engine_object.canvas.append(circle)
    engine_object.draw()
    time.sleep(1)

    assert circle in engine_object.canvas


def test_triangle_draw(engine_object):
    engine_object.canvas.append(triangle)
    engine_object.draw()
    time.sleep(1)

    assert triangle in engine_object.canvas


def test_change_color(engine_object):
    engine_object.canvas.append(rectangle)
    engine_object.canvas.append(circle)
    engine_object.canvas.append(triangle)

    rectangle._change_color((0, 0, 255))
    circle._change_color((255, 255, 0))

    engine_object.draw()
    time.sleep(1)

    assert rectangle.get_color() == (0, 0, 255), "Цвет прямоугольника не изменился на синий"
    assert circle.get_color() == (255, 255, 0), "Цвет круга не изменился на желтый"


def test_positions(engine_object):
    engine_object.canvas.append(rectangle)
    engine_object.canvas.append(circle)
    engine_object.canvas.append(triangle)
    engine_object.draw()
    time.sleep(1)

    assert rectangle.position == (100, 200, 200, 100)
    assert circle.position == (400, 200, 100, 100)
    assert triangle.position == (600, 200, 100, 100)


def test_delete_figure(engine_object):
    engine_object.canvas.append(rectangle)
    engine_object.canvas.append(circle)
    engine_object.canvas.append(triangle)

    engine_object.canvas.remove(triangle)
    engine_object.draw()
    time.sleep(1)
    assert triangle not in engine_object.canvas, "Прямоугольник не был удален из canvas"
