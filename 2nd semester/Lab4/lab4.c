import turtle
import math
import random
from tkinter import *
from tkinter import messagebox
import sys

NUMBER_OF_VERTICES = 11
RANDOM_SEED = 3413
# 911

RECTANGLE_WIDTH = 600
RECTANGLE_HEIGHT = 600

RADIUS_OF_VERTICES = 15

length_between_vertices = min(RECTANGLE_WIDTH, RECTANGLE_HEIGHT) / (
        pow(2, math.floor(math.log2(NUMBER_OF_VERTICES))) / 2)


class Vertex:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y


# Функція для малювання вершини з номером
def draw_circle_with_number(x, y, number, radius_of_vertices):
    turtle.penup()
    turtle.goto(x, y - radius_of_vertices * 0.6)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("black")
    turtle.circle(radius_of_vertices)
    turtle.end_fill()
    turtle.penup()
    turtle.color("white")
    turtle.goto(x, y)
    turtle.write(number, align="center", font=("Arial", 12, "normal"))


# Генерація напрямленої матриці суміжності
def generate_directed_matrix(n, seed):
    random.seed(seed)

    random_matrix = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(random.uniform(0, 2))
        random_matrix.append(row)

    k = 1.0 - 1 * 0.01 - 3 * 0.01 - 0.3
    transformed_matrix = []
    for row in random_matrix:
        transformed_row = []
        for element in row:
            if element * k >= 1.0:
                transformed_row.append(1)
            else:
                transformed_row.append(0)
        transformed_matrix.append(transformed_row)

    return transformed_matrix


# Виведення напрямленої матриці суміжності
def print_directed_adjacency_matrix(adjacency_matrix):
    print()
    print("Directed Adjacency Matrix:")
    for row in adjacency_matrix:
        print(row)


# Генерація ненапрямленої матриці суміжності
def generate_undirected_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                matrix[j][i] = 1
                matrix[i][j] = 1
    return matrix


# Виведення ненапрямленої матриці суміжності
def print_undirected_adjacency_matrix(matrix):
    print()
    print("Undirected Adjacency Matrix:")
    for row in matrix:
        print(row)


# Функція перевірки наявності вершиин в масиві
def find_vertex_by_coordinates(vertices, x, y):
    for vertex in vertices:
        if vertex.x == x and vertex.y == y:
            return False
    else:
        return True


# Генерація позицій вершин
def generate_vertex_positions(num_vertices):
    vertices = []

    if num_vertices < 4:
        messagebox.showwarning(title='Warning!', message='Number of vertices must be more than 4 or equal 4')
        return

    else:
        # Додаємо вершини прямокутника
        vertex1 = Vertex(1, -RECTANGLE_WIDTH / 2, -RECTANGLE_HEIGHT / 2)
        vertex2 = Vertex(2, -RECTANGLE_WIDTH / 2, RECTANGLE_HEIGHT / 2)
        vertex3 = Vertex(3, RECTANGLE_WIDTH / 2, RECTANGLE_HEIGHT / 2)
        vertex4 = Vertex(4, RECTANGLE_WIDTH / 2, -RECTANGLE_HEIGHT / 2)
        vertices.extend([vertex1, vertex2, vertex3, vertex4])

        # Вершини посередині ребер прямокутника (5-8)
        if 4 <= num_vertices <= 8:
            for i in range(4, num_vertices):
                start_vertex = vertices[i - 4]
                end_vertex = vertices[(i - 3) % 4]
                middle_x = (start_vertex.x + end_vertex.x) / 2
                middle_y = (start_vertex.y + end_vertex.y) / 2
                middle_vertex = Vertex(i + 1, middle_x, middle_y)
                vertices.append(middle_vertex)

        else:
            for i in range(4, 8):
                start_vertex = vertices[i - 4]
                end_vertex = vertices[(i - 3) % 4]
                middle_x = (start_vertex.x + end_vertex.x) / 2
                middle_y = (start_vertex.y + end_vertex.y) / 2
                middle_vertex = Vertex(i + 1, middle_x, middle_y)
                vertices.append(middle_vertex)

            x = -RECTANGLE_WIDTH / 2
            y = -RECTANGLE_HEIGHT / 2

            current_number = 9

            for _ in range(current_number - 1, num_vertices):
                while x != RECTANGLE_WIDTH / 2 and current_number <= num_vertices and x < RECTANGLE_WIDTH / 2:
                    x += length_between_vertices
                    if find_vertex_by_coordinates(vertices, x, y):
                        welterweights = Vertex(current_number, x, y)
                        vertices.append(welterweights)
                        current_number += 1

                while y != RECTANGLE_HEIGHT / 2 and current_number <= num_vertices and y < RECTANGLE_HEIGHT:
                    y += length_between_vertices
                    if find_vertex_by_coordinates(vertices, x, y):
                        welterweights = Vertex(current_number, x, y)
                        vertices.append(welterweights)
                        current_number += 1

                while x != -RECTANGLE_WIDTH / 2 and current_number <= num_vertices and x > -RECTANGLE_WIDTH:
                    x -= length_between_vertices
                    if find_vertex_by_coordinates(vertices, x, y):
                        welterweights = Vertex(current_number, x, y)
                        vertices.append(welterweights)
                        current_number += 1

                while y != -RECTANGLE_HEIGHT / 2 and current_number <= num_vertices and y > -RECTANGLE_HEIGHT:
                    y -= length_between_vertices
                    if find_vertex_by_coordinates(vertices, x, y):
                        welterweights = Vertex(current_number, x, y)
                        vertices.append(welterweights)
                        current_number += 1

    return vertices


# Проведення лінії від точки до точки
def draw_line(x1, y1, x2, y2):
    turtle.color("black")
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


# p0 - point 1
# p2 - point 2
# p1 - another point


# Створення кривої Бізьє
def bezier_curve(p0, p1, p2, t):
    return ((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0],
            (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1])


# Малювання кривої Бізьє
def draw_bezier_curve(p0, p1, p2):
    turtle.color("black")

    # Підняти олівець та перемістити до першої точки
    turtle.penup()
    turtle.goto(p0[0], p0[1])
    turtle.pendown()

    # Малюємо криву
    t = 0
    while t <= 1:
        x, y = bezier_curve(p0, p1, p2, t)
        turtle.goto(x, y)
        t += 0.01


# Функція малювання кола
def draw_circle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black")
    turtle.circle(RADIUS_OF_VERTICES)


# Функція малювання стрілки
def draw_arrow(start, end):
    # Визначення кута між точками
    angle = math.degrees(math.atan2(end[1] - start[1], end[0] - start[0]))

    end_circle_x = end[0] + 5 * math.cos(math.radians(angle))
    end_circle_y = end[1] + 5 * math.sin(math.radians(angle))

    turtle.color("red")

    # Переміщення до початку стрілки
    turtle.penup()
    turtle.goto(end_circle_x, end_circle_y)
    turtle.setheading(angle - 180)  # Встановлення кута напрямку для стрілки
    turtle.pendown()

    # Малюємо стрілку
    turtle.stamp()


# Функція малювання лінії зі стрілкою
def draw_line_with_arrow(point1, point2, radius_of_vert):
    turtle.color("black")
    turtle.penup()
    turtle.goto(point1[0], point1[1])
    turtle.pendown()

    angle = math.degrees(math.atan2(point2[1] - point1[1], point2[0] - point1[0]))
    end_circle_x = point2[0] - radius_of_vert * math.cos(math.radians(angle))
    end_circle_y = point2[1] - radius_of_vert * math.sin(math.radians(angle)) + radius_of_vert / 2

    turtle.goto(end_circle_x, end_circle_y)

    turtle.color("red")
    turtle.setheading(angle)

    turtle.stamp()

    turtle.color("black")


# Функція малювання кола зі стрілкою
def draw_circle_with_arrow(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black")
    turtle.circle(RADIUS_OF_VERTICES)
    turtle.color("red")
    turtle.stamp()
    turtle.color("black")


# Функція малювання ненапрямленого графа
def draw_undirected_graph(adjacency_matrix, vertex_positions, radius_of_vertices):
    for vertex in vertex_positions:
        draw_circle_with_number(vertex.x, vertex.y, vertex.number, radius_of_vertices)

    turtle.color("black")

    rows = len(adjacency_matrix)
    cols = len(adjacency_matrix[0])

    for i in range(rows):
        for j in range(i, cols):
            if adjacency_matrix[i][j] == 1:

                x1 = vertex_positions[i].x
                y1 = vertex_positions[i].y
                x2 = vertex_positions[j].x
                y2 = vertex_positions[j].y

                point1 = (x1, y1)
                point2 = (x2, y2)

                if (x1 == x2 or y1 == y2) and (abs(x1 - x2) == length_between_vertices or
                                               abs(y1 - y2) == length_between_vertices):
                    draw_line(x1, y1, x2, y2)

                elif (x1 == x2 or y1 == y2) and (abs(x1 - x2) != length_between_vertices or
                                                 abs(y1 - y2) != length_between_vertices):
                    if i < j:
                        if x1 == x2 >= 0:
                            point_between = (x1 + 150, (y1 + y2) / 2)
                            draw_bezier_curve(point1, point_between, point2)
                        elif x1 == x2 < 0:
                            point_between = (x1 - 150, (y1 + y2) / 2)
                            draw_bezier_curve(point1, point_between, point2)
                        elif y1 == y2 >= 0:
                            point_between = ((x1 + x2) / 2, y1 + 150)
                            draw_bezier_curve(point1, point_between, point2)
                        elif y1 == y2 < 0:
                            point_between = ((x1 + x2) / 2, y1 - 150)
                            draw_bezier_curve(point1, point_between, point2)

                elif x1 != x2 or y1 != y2:
                    draw_line(x1, y1, x2, y2)

                if i == j:
                    if y1 == RECTANGLE_HEIGHT / 2 and x1 != RECTANGLE_WIDTH / 2 and x1 != -RECTANGLE_WIDTH / 2:
                        draw_circle(x1, y1 + radius_of_vertices)
                    elif y1 == -RECTANGLE_HEIGHT / 2 and x1 != RECTANGLE_WIDTH / 2 and x1 != -RECTANGLE_WIDTH / 2:
                        draw_circle(x1, y1 - radius_of_vertices - 10)
                    elif x1 == RECTANGLE_WIDTH / 2:
                        draw_circle(x1 + radius_of_vertices, y1)
                    elif x1 == -RECTANGLE_WIDTH / 2:
                        draw_circle(x1 - radius_of_vertices, y1)
    for vertex in vertex_positions:
        draw_circle_with_number(vertex.x, vertex.y, vertex.number, radius_of_vertices)


# Функція малювання напрямленого графа
def draw_directed_graph(adjacency_matrix, vertex_positions, num_of_vert, radius_of_vertices):
    for vertex in vertex_positions:
        draw_circle_with_number(vertex.x, vertex.y, vertex.number, radius_of_vertices)

    turtle.color("black")

    for i in range(num_of_vert):
        for j in range(num_of_vert):
            if adjacency_matrix[i][j] == 1:

                x1 = vertex_positions[i].x
                y1 = vertex_positions[i].y
                x2 = vertex_positions[j].x
                y2 = vertex_positions[j].y

                point1 = (x1, y1)
                point2 = (x2, y2)

                if (x1 == x2 or y1 == y2) and (abs(x1 - x2) == length_between_vertices or
                                               abs(y1 - y2) == length_between_vertices):
                    if i < j:
                        draw_line_with_arrow(point1, point2, RADIUS_OF_VERTICES)
                    elif i > j:
                        if x1 == x2:
                            point_between = (x1 + 150, (y1 + y2) / 2)
                            draw_bezier_curve(point1, point_between, point2)
                            draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
                        elif y1 == y2:
                            point_between = ((x1 + x2) / 2, y1 + 150)
                            draw_bezier_curve(point1, point_between, point2)
                            draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))

                elif (x1 == x2 or y1 == y2) and (abs(x1 - x2) != length_between_vertices or
                                                 abs(y1 - y2) != length_between_vertices):
                    if i < j:
                        if x1 == x2 >= 0:
                            point_between = (x1 + 150, (y1 + y2) / 2)
                            draw_bezier_curve(point1, point_between, point2)
                            draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
                        elif x1 == x2 < 0:
                            point_between = (x1 - 150, (y1 + y2) / 2)
                            draw_bezier_curve(point1, point_between, point2)
                            draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
                        elif y1 == y2 > 0:
                            point_between = ((x1 + x2) / 2, y1 + 150)
                            draw_bezier_curve(point1, point_between, point2)
                            draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
                        elif y1 == y2 < 0:
                            point_between = ((x1 + x2) / 2, y1 - 150)
                            draw_bezier_curve(point1, point_between, point2)
                            draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
                    elif i > j:
                        if x1 == x2 >= 0:
                            point_between = (x1 - 150, (y1 + y2) / 2)
                            draw_bezier_curve(point1, point_between, point2)
                            draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
                        elif x1 == x2 < 0:
                            point_between = (x1 + 150, (y1 + y2) / 2)
                            draw_bezier_curve(point1, point_between, point2)
                            draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
                        elif y1 == y2 >= 0:
                            point_between = ((x1 + x2) / 2, y1 - 150)
                            draw_bezier_curve(point1, point_between, point2)
                            draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
                        elif y1 == y2 < 0:
                            point_between = ((x1 + x2) / 2, y1 + 150)
                            draw_bezier_curve(point1, point_between, point2)
                            draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))

                elif x1 != x2 and y1 != y2:
                    if i > j:
                        draw_line_with_arrow(point1, point2, RADIUS_OF_VERTICES)
                    elif i < j:
                        point_between = ((x1 + x2) / 2 + 100, (y1 + y2) / 2 + 80)
                        draw_bezier_curve(point1, point_between, point2)
                        draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))

                if i == j:
                    if y1 == RECTANGLE_HEIGHT / 2 and x1 != RECTANGLE_WIDTH / 2 and x1 != -RECTANGLE_WIDTH / 2:
                        draw_circle_with_arrow(x1, y1 + radius_of_vertices)
                    elif y1 == -RECTANGLE_HEIGHT / 2 and x1 != RECTANGLE_WIDTH / 2 and x1 != -RECTANGLE_WIDTH / 2:
                        draw_circle_with_arrow(x1 - radius_of_vertices, y1 - radius_of_vertices/2)
                    elif x1 == RECTANGLE_WIDTH / 2:
                        draw_circle_with_arrow(x1 + radius_of_vertices * 0.8, y1 + radius_of_vertices / 2)
                    elif x1 == -RECTANGLE_WIDTH / 2:
                        draw_circle_with_arrow(x1 - radius_of_vertices, y1)


# Степінь вершин для ненапрямленого графа
def degree_of_vertices_for_undirected(matrix, num_of_vertices):
    isolated_peaks = []  # ізольовані вершини
    hanging_peaks = []  # висячі вершини
    print()

    for i in range(num_of_vertices):
        degree = 0
        for j in range(num_of_vertices):
            if matrix[i][j] == 1:
                if i == j:
                    degree += 2
                else:
                    degree += 1
        if degree == 0:
            print("Вершина {} є ізольованою та має степінь {}".format(i + 1, degree))
            isolated_peaks.append(i + 1)
        elif degree == 1:
            hanging_peaks.append(i + 1)
            print("Вершина {} є висячою та має степінь {}".format(i + 1, degree))
        else:
            print("Вершина {} має степінь {}".format(i + 1, degree))
    print()

    if len(isolated_peaks) == 0:
        print("Ізольованих вершин немає")
    else:
        print("Ізольовані вершини:", isolated_peaks)

    if len(hanging_peaks) == 0:
        print("Висячих вершин немає")
    else:
        print("Висячі вершини:", hanging_peaks)


# Напiвстепенi виходу та заходу напрямленого графа
def number_of_half_powers(matrix, num_of_vertices):
    print()
    for i in range(num_of_vertices):
        num_of_enter = 0
        num_of_exit = 0
        for j in range(num_of_vertices):
            if matrix[i][j] == 1:
                num_of_exit += 1
            if matrix[j][i] == 1:
                num_of_enter += 1
        print("Вершина {} має напівстепінь виходу {} та напівстепінь входу {}".format(i + 1, num_of_exit, num_of_enter))


# Степінь вершин для напрямленого графа
def degree_of_vertices_for_directed(matrix, num_of_vertices):
    isolated_peaks = []  # ізольовані вершини
    hanging_peaks = []  # висячі вершини
    print()

    for i in range(num_of_vertices):
        num_of_enter = 0
        num_of_exit = 0
        for j in range(num_of_vertices):
            if matrix[i][j] == 1:
                num_of_exit += 1
            if matrix[j][i] == 1:
                num_of_enter += 1
        if num_of_enter + num_of_exit == 0:
            print("Вершина {} є ізольованою та має степінь {}".format(i + 1, num_of_enter + num_of_exit))
            isolated_peaks.append(i + 1)
        elif num_of_enter + num_of_exit == 1:
            print("Вершина {} є висячою та має степінь {}".format(i + 1, num_of_enter + num_of_exit))
            hanging_peaks.append(i + 1)
        else:
            print("Вершина {} має степінь {}".format(i + 1, num_of_enter + num_of_exit))

    print()

    if len(isolated_peaks) == 0:
        print("Ізольованих вершин немає")
    else:
        print("Ізольовані вершини:", isolated_peaks)

    if len(hanging_peaks) == 0:
        print("Висячих вершин немає")
    else:
        print("Висячі вершини:", hanging_peaks)


# Перевірка чи є граф регулярним (однорідним)
def is_graph_regular(matrix, num_of_vertices):
    print()
    degrees = []
    for i in range(num_of_vertices):
        degree = 0
        for j in range(num_of_vertices):
            if matrix[i][j] == 1:
                if i == j:
                    degree += 2
                else:
                    degree += 1
            degrees.append(degree)
    if len(set(degrees)) == 1:
        homogeneous_degree = degrees[0]
        print("Цей граф однорідний {} степеня".format(homogeneous_degree))
    else:
        print("Цей граф неоднорідний")


# Генерація нової матриці для пункту 4 лр №4
def generate_new_directed_matrix(n, seed):
    random.seed(seed)

    random_matrix = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(random.uniform(0, 2))
        random_matrix.append(row)

    k = 1.0 - 1 * 0.005 - 3 * 0.005 - 0.27
    transformed_matrix = []
    for row in random_matrix:
        transformed_row = []
        for element in row:
            if element * k >= 1.0:
                transformed_row.append(1)
            else:
                transformed_row.append(0)
        transformed_matrix.append(transformed_row)

    return transformed_matrix


# Дві функції для встановлення усіх шляхів довжини 2
def find_paths(matrix, start):
    paths = []
    for i in range(len(matrix[start - 1])):
        if matrix[start - 1][i] == 1:  # Перевіряємо наявність ребра між вершинами start і i
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:  # Перевіряємо наявність ребра між вершинами i і j
                    paths.append([start, i + 1, j + 1])  # Додаємо шлях до списку шляхів
    return paths


def find_all_paths(matrix):
    all_paths = []
    for start_vertex in range(1, len(matrix) + 1):
        paths = find_paths(matrix, start_vertex)
        all_paths.extend(paths)
    return all_paths


# Дві функції для встановлення усіх шляхів довжини 3
def find_paths_3(matrix, start):
    paths = []
    for i in range(len(matrix[start - 1])):
        if matrix[start - 1][i] == 1:  # Перевіряємо наявність ребра між вершинами start і i
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:  # Перевіряємо наявність ребра між вершинами i і j
                    for k in range(len(matrix[j])):
                        if matrix[j][k] == 1:  # Перевіряємо наявність ребра між вершинами j і k
                            paths.append([start, i + 1, j + 1, k + 1])  # Додаємо шлях до списку шляхів
    return paths


def find_all_paths_3(matrix):
    all_paths = []
    for start_vertex in range(1, len(matrix) + 1):
        paths = find_paths_3(matrix, start_vertex)
        all_paths.extend(paths)
    return all_paths


# Створення матриці досяжності
def multiply_matrices(matrix1, matrix2):
    # Створення матриці з 0
    result_matrix = []
    for _ in range(len(matrix1)):
        row = [0] * len(matrix2[0])
        result_matrix.append(row)

    # Перемноження матриць
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix


def add_matrices(matrix1, matrix2):
    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(row)

    return result_matrix


# Функція для створення матриці досяжності
def matrix_of_reachability(num_of_vertices, matrix):
    identity_matrix = []
    for i in range(num_of_vertices):
        row = [0] * num_of_vertices
        row[i] = 1  # Задаємо значення 1 на головній діагоналі
        identity_matrix.append(row)

    end_result = matrix  # Встановлюємо початкове значення для кінцевого результату

    result = matrix  # Встановлюємо початкове значення результату

    for _ in range(num_of_vertices - 2):
        result = multiply_matrices(result, matrix)  # Множимо поточний результат на початкову матрицю

        end_result = add_matrices(end_result, result)  # Додаємо результат до кінцевого результату

    # Додаємо одиничну матрицю
    end_result = add_matrices(end_result, identity_matrix)

    # Створення нової матриці
    new_matrix = []
    for row in end_result:
        new_row = []
        for element in row:
            if element >= 1:
                new_row.append(1)
            else:
                new_row.append(0)
        new_matrix.append(new_row)

    return new_matrix


# Функція для виведення матриці досяжності
def print_matrix_of_reachability(matrix):
    print("Кінцева матриця досяжності з булевим відображенням:")
    for row in matrix:
        print(row)


# Функція для транспонування матриці
def transpose_matrix(matrix):
    # Отримуємо розмір матриці
    rows = len(matrix)
    cols = len(matrix[0])

    # Створюємо порожню матрицю для результату
    result = []
    for _ in range(cols):
        row = []
        for _ in range(rows):
            row.append(0)
        result.append(row)

    # Транспонуємо матрицю
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


# Виведення матриці сильної зв'язності
def matrix_of_strong_connectivity(matrix):
    reach_matrix = matrix
    print("reach_matrix")
    for row in reach_matrix:
        print(row)

    print("trans_matrix")
    trans_matrix = transpose_matrix(matrix)
    for row in trans_matrix:
        print(row)

    print("Матриця сильної зв'язності")
    strong_connectivity_matrix = elementwise_matrix_multiply(trans_matrix, reach_matrix)
    for row in strong_connectivity_matrix:
        print(row)

    return strong_connectivity_matrix


# Множення поелементно
def elementwise_matrix_multiply(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] * matrix2[i][j])
        result.append(row)

    return result


# Функція для знаходження компонент сильної зв'язності
def find_scc(matrix):
    transposed = transpose_matrix(matrix)
    visited = [False] * len(matrix)
    stack = []

    def dfs(row_dfc):
        visited[row_dfc] = True
        for col, value in enumerate(matrix[row_dfc]):
            if value == 1 and not visited[col]:
                dfs(col)
        stack.append(row_dfc)

    for i in range(len(matrix)):
        if not visited[i]:
            dfs(i)

    visited = [False] * len(matrix)
    scc_components = []

    def dfs_scc(row_dfs_scc, component_dfs_scc):
        visited[row_dfs_scc] = True
        component_dfs_scc.append(row_dfs_scc)
        for col, value in enumerate(transposed[row_dfs_scc]):
            if value == 1 and not visited[col]:
                dfs_scc(col, component_dfs_scc)

    while stack:
        cur_row = stack.pop()
        if not visited[cur_row]:
            cur_component = []
            dfs_scc(cur_row, cur_component)
            scc_components.append(cur_component)

    return scc_components


# Функція для виведення компонент сильної зв'язності
def print_scc(scc):
    print("Компоненти сильної зв'язності:")
    for i, component in enumerate(scc, 1):
        if len(component) == 1:
            print(f"Компонента №{i}: {component[0] + 1}")
        else:
            print(f"Компонента №{i}: {', '.join(str(row + 1) for row in component)}")


# Функція для створення матриці графа конденсації
def create_condensation_graph_matrix(matrix, scc_components):
    num_components = len(scc_components)
    condensation_graph_matrix = [[0] * num_components for _ in range(num_components)]

    for i in range(num_components):
        for j in range(num_components):
            if i != j:  # Ігноруємо випадок, коли компоненти сильної зв'язності ідентичні
                for vertex_i in scc_components[i]:
                    for vertex_j in scc_components[j]:
                        if matrix[vertex_i][vertex_j] == 1:
                            condensation_graph_matrix[i][j] = 1
                            break  # Завершуємо пошук, якщо знайдено зв'язок

    return condensation_graph_matrix


# Функція для виведення матриці графа конденсації
def print_condensation_graph(condensation_graph_matrix):
    print("Матриця суміжності графа конденсації:")
    for row in condensation_graph_matrix:
        print(row)


# Функція для генерації позиції графа конденсації
def generate_vertex_positions_for_condensation_graph(num_vertices, rectangle_width, rectangle_height):
    fixed_vertices = [
        Vertex(1, -rectangle_width / 2, 0),
        Vertex(2, rectangle_width / 2, 0),
        Vertex(3, 0, rectangle_height / 2),
        Vertex(4, 0, -rectangle_height / 2)
    ]

    # Додаємо вершини з фіксованого списку в залежності від значення num_vertices
    vertices = fixed_vertices[:num_vertices]

    return vertices


# Функція для малювання графа конденсації (максимальна кількість можливих вершин - 4)
def draw_condensation_graph(condensation_graph_matrix, vertex_positions, radius_of_vertices, num_of_vert):
    for vertex in vertex_positions:
        draw_circle_with_number(vertex.x, vertex.y, vertex.number, radius_of_vertices)

    if 1 <= num_of_vert <= 4:
        for i in range(num_of_vert):
            for j in range(num_of_vert):
                if condensation_graph_matrix[i][j] == 1:
                    x1 = vertex_positions[i].x
                    y1 = vertex_positions[i].y
                    x2 = vertex_positions[j].x
                    y2 = vertex_positions[j].y

                    point1 = (x1, y1)
                    point2 = (x2, y2)

                    draw_line_with_arrow(point1, point2, RADIUS_OF_VERTICES)

    else:
        messagebox.showwarning(title='Warning!', message='Number of vertices must be less than 5 and more than 0')
        return


def main():
    # Встановлення вікна turtle та швидкості
    turtle.setup(width=1200, height=800)
    turtle.speed(12)

    window = Tk()
    window.title("Choose type of graph")

    # Задати розмір вікна для кнопок
    window.geometry("200x160")

    def undirected_graph():
        directed_adjacency_matrix = generate_directed_matrix(NUMBER_OF_VERTICES, RANDOM_SEED)
        vertex_positions = generate_vertex_positions(NUMBER_OF_VERTICES)
        undirected_adjacency_matrix = generate_undirected_matrix(directed_adjacency_matrix)
        print_undirected_adjacency_matrix(undirected_adjacency_matrix)
        degree_of_vertices_for_undirected(undirected_adjacency_matrix, NUMBER_OF_VERTICES)
        is_graph_regular(undirected_adjacency_matrix, NUMBER_OF_VERTICES)
        draw_undirected_graph(undirected_adjacency_matrix, vertex_positions, RADIUS_OF_VERTICES)

    def directed_graph():
        directed_adjacency_matrix = generate_directed_matrix(NUMBER_OF_VERTICES, RANDOM_SEED)
        vertex_positions = generate_vertex_positions(NUMBER_OF_VERTICES)
        print_directed_adjacency_matrix(directed_adjacency_matrix)
        degree_of_vertices_for_directed(directed_adjacency_matrix, NUMBER_OF_VERTICES)
        number_of_half_powers(directed_adjacency_matrix, NUMBER_OF_VERTICES)
        is_graph_regular(directed_adjacency_matrix, NUMBER_OF_VERTICES)
        draw_directed_graph(directed_adjacency_matrix, vertex_positions, NUMBER_OF_VERTICES, RADIUS_OF_VERTICES)

    def clear_canvas():
        print()
        print("=================================================================")
        turtle.clear()

    def close_window():
        turtle.bye()
        sys.exit()

    def new_graph():
        directed_adjacency_matrix = generate_new_directed_matrix(NUMBER_OF_VERTICES, RANDOM_SEED)
        vertex_positions = generate_vertex_positions(NUMBER_OF_VERTICES)
        print_directed_adjacency_matrix(directed_adjacency_matrix)
        number_of_half_powers(directed_adjacency_matrix, NUMBER_OF_VERTICES)
        all_paths_2 = find_all_paths(directed_adjacency_matrix)
        all_paths_2.sort(key=lambda x: (x[0], x[2]))
        print()
        print("Усі шляхи довжини 2:")
        for path in all_paths_2:
            print(" - ".join(str(vertex) for vertex in path))
        print()
        all_paths3 = find_all_paths_3(directed_adjacency_matrix)
        all_paths3.sort(key=lambda x: (x[0], x[3]))
        print("Усі шляхи довжини 3:")
        for path3 in all_paths3:
            print(" - ".join(str(vertex) for vertex in path3))
        print()
        reachability_matrix = matrix_of_reachability(NUMBER_OF_VERTICES, directed_adjacency_matrix)
        print_matrix_of_reachability(reachability_matrix)
        print()
        matrix_of_strong_connectivity(reachability_matrix)
        scc = find_scc(reachability_matrix)
        print()
        print_scc(scc)
        print()
        condensation_graph_matrix = create_condensation_graph_matrix(directed_adjacency_matrix, scc)
        print_condensation_graph(condensation_graph_matrix)
        draw_directed_graph(directed_adjacency_matrix, vertex_positions, NUMBER_OF_VERTICES, RADIUS_OF_VERTICES)

    def for_drawing_condensation_graph():
        directed_adjacency_matrix = generate_new_directed_matrix(NUMBER_OF_VERTICES, RANDOM_SEED)

        reachability_matrix = matrix_of_reachability(NUMBER_OF_VERTICES, directed_adjacency_matrix)
        scc = find_scc(reachability_matrix)
        condensation_graph_matrix = create_condensation_graph_matrix(directed_adjacency_matrix, scc)

        num_of_vert = len(condensation_graph_matrix)

        vertex_positions = generate_vertex_positions_for_condensation_graph(num_of_vert, RECTANGLE_WIDTH,
                                                                            RECTANGLE_HEIGHT)
        draw_condensation_graph(condensation_graph_matrix, vertex_positions, RADIUS_OF_VERTICES, num_of_vert)

    window.protocol("WM_DELETE_WINDOW", turtle.bye)

    undirected_button = Button(window, text="  Undirected button  ", command=undirected_graph)
    undirected_button.pack()
    directed_button = Button(window, text="     Directed button    ", command=directed_graph)
    directed_button.pack()
    clear_button = Button(window, text="            Clear all          ", command=clear_canvas)
    clear_button.pack()
    exit_button = Button(window, text="        Stop and exit     ", command=close_window)
    exit_button.pack()
    new_graph = Button(window, text="         New graph        ", command=new_graph)
    new_graph.pack()
    condensation_graph_button = Button(window, text=" Condensation graph", command=for_drawing_condensation_graph)
    condensation_graph_button.pack()

    window.mainloop()


# Виклик головної функції
if __name__ == "__main__":
    main()
