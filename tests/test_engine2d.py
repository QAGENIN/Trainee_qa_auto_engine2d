from engine.engine2d import Rectangle, Circle, Triangle, Engine2D

engine = Engine2D(800, 600, "2D-движок")


def test_rectangle_draw():
    shape = Rectangle('Прямоугольник', (255, 0, 0), (100, 200, 200, 100))
    engine.canvas.append(shape)
    engine.draw()


def test_circle_draw():
    shape = Circle('Круг', (0, 255, 0), (400, 200, 100, 100))
    engine.canvas.append(shape)
    engine.draw()


def test_triangle_draw():
    shape = Triangle('Треугольник', (0, 0, 255), (600, 200, 100, 100))
    engine.canvas.append(shape)
    engine.draw()


def test_change_color():
    shape1 = Rectangle('Прямоугольник', (255, 0, 0), (100, 200, 200, 100))
    shape2 = Circle('Круг', (0, 255, 0), (400, 200, 100, 100))

    shape1.color = (0, 0, 255)  # Изменяем цвет прямоугольника на синий
    shape2.color = (255, 255, 0)  # Изменяем цвет круга на желтый

    engine.canvas.append(shape1)
    engine.canvas.append(shape2)

    engine.draw()


def test_delete_figure():
    shape1 = Rectangle('Прямоугольник', (255, 0, 0), (100, 200, 200, 100))
    shape2 = Circle('Круг', (0, 255, 0), (400, 200, 100, 100))

    engine.canvas.append(shape1)
    engine.canvas.append(shape2)

    engine.canvas.remove(shape1)  # Удаляем прямоугольник из canvas

    engine.draw()
