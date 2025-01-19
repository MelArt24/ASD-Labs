import turtle
import math
import random
from tkinter import *
from tkinter import messagebox
import sys
import time
NUMBER_OF_VERTICES = 11
RANDOM_SEED = 3413
RECTANGLE_WIDTH = 600
RECTANGLE_HEIGHT = 600
RADIUS_OF_VERTICES = 15
length_between_vertices = min(RECTANGLE_WIDTH, RECTANGLE_HEIGHT) / (
 pow(2, math.floor(math.log2(NUMBER_OF_VERTICES))) / 2)
sum_of_weights = 0
class Vertex:
 def __init__(self, number, x, y):
 self.number = number
 self.x = x
 self.y = y
class Curve:
 def __init__(self, vertex1, vertex2, weight):
 self.vertex1 = vertex1
 self.vertex2 = vertex2
 self.weight = weight
# Функція для малювання вершини з номером
def draw_circle_with_number(x, y, number, radius_of_vertices, color):
 turtle.penup()
 turtle.goto(x, y - radius_of_vertices * 0.6)
 turtle.pendown()
 turtle.begin_fill()
 turtle.color(color)
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
 k = 1.0 - 1 * 0.01 - 3 * 0.005 - 0.05
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
 while x != RECTANGLE_WIDTH / 2 and current_number <= num_vertices and x < 
RECTANGLE_WIDTH / 2:
 x += length_between_vertices
 if find_vertex_by_coordinates(vertices, x, y):
 welterweights = Vertex(current_number, x, y)
 vertices.append(welterweights)
 current_number += 1
 while y != RECTANGLE_HEIGHT / 2 and current_number <= num_vertices and y < 
RECTANGLE_HEIGHT:
 y += length_between_vertices
 if find_vertex_by_coordinates(vertices, x, y):
 welterweights = Vertex(current_number, x, y)
 vertices.append(welterweights)
 current_number += 1
 while x != -RECTANGLE_WIDTH / 2 and current_number <= num_vertices and x > -
RECTANGLE_WIDTH:
 x -= length_between_vertices
 if find_vertex_by_coordinates(vertices, x, y):
 welterweights = Vertex(current_number, x, y)
 vertices.append(welterweights)
 current_number += 1
 while y != -RECTANGLE_HEIGHT / 2 and current_number <= num_vertices and y > -
RECTANGLE_HEIGHT:
 y -= length_between_vertices
 if find_vertex_by_coordinates(vertices, x, y):
 welterweights = Vertex(current_number, x, y)
 vertices.append(welterweights)
 current_number += 1
 return vertices
# Проведення лінії від точки до точки
def draw_line(x1, y1, x2, y2, color):
 turtle.color(color)
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
def draw_bezier_curve(p0, p1, p2, color):
 turtle.color(color)
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
 turtle.setheading(angle - 180) # Встановлення кута напрямку для стрілки
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
graph = [(-1, -1, math.inf)]
# Функція малювання ненапрямленого графа
def draw_undirected_graph(adjacency_matrix, vertex_positions, radius_of_vertices, weight_matrix):
 for vertex in vertex_positions:
 draw_circle_with_number(vertex.x, vertex.y, vertex.number, radius_of_vertices, "black")
 curves = []
 global graph
 turtle.color("black")
 rows = len(adjacency_matrix)
 cols = len(adjacency_matrix[0])
 for i in range(rows):
 for j in range(i, cols):
 if adjacency_matrix[i][j] == 1:
 weight = weight_matrix[i][j]
 curve_x = Curve(i, j, weight)
 curves.append(curve_x)
 graph.append((i + 1, j + 1, weight))
 x1 = vertex_positions[i].x
 y1 = vertex_positions[i].y
 x2 = vertex_positions[j].x
 y2 = vertex_positions[j].y
 point1 = (x1, y1)
 point2 = (x2, y2)
 if (x1 == x2 or y1 == y2) and (abs(x1 - x2) == length_between_vertices or
 abs(y1 - y2) == length_between_vertices):
 draw_line(x1, y1, x2, y2, "black")
 if x1 == x2:
 turtle.penup()
 x = x1 + 4
 y = (y1 + y2) / 2
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("black")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif y1 == y2:
 turtle.penup()
 y = y1 + 4
 x = (x1 + x2) / 2
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("black")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif (x1 == x2 or y1 == y2) and (abs(x1 - x2) != length_between_vertices or
 abs(y1 - y2) != length_between_vertices):
 if i < j:
 if x1 == x2 >= 0:
 point_between = (x1 + 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "black")
 turtle.penup()
 x = point_between[0] - 70
 y = point_between[1]
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("black")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif x1 == x2 < 0:
 point_between = (x1 - 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "black")
 turtle.penup()
 x = point_between[0] + 50
 y = point_between[1]
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("black")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif y1 == y2 >= 0:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2, "black")
 turtle.penup()
 x = point_between[0]
 y = point_between[1] - 70
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("black")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif y1 == y2 < 0:
 point_between = ((x1 + x2) / 2, y1 - 150)
 draw_bezier_curve(point1, point_between, point2, "black")
 turtle.penup()
 x = point_between[0]
 y = point_between[1] + 60
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("black")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif x1 != x2 or y1 != y2:
 draw_line(x1, y1, x2, y2, "black")
 turtle.penup()
 x = (x1 + x2) / 2
 y = (y1 + y2) / 2
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("black")
 turtle.write(curve_x.weight)
 turtle.penup()
 if i == j:
 if y1 == RECTANGLE_HEIGHT / 2 and x1 != RECTANGLE_WIDTH / 2 and x1 != -
RECTANGLE_WIDTH / 2:
 draw_circle(x1, y1 + radius_of_vertices)
 turtle.penup()
 x = x1 - 10
 y = y1 + 45
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("black")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif y1 == -RECTANGLE_HEIGHT / 2 and x1 != RECTANGLE_WIDTH / 2 and x1 != -
RECTANGLE_WIDTH / 2:
 draw_circle(x1, y1 - radius_of_vertices - 10)
 turtle.penup()
 x = x1 - 10
 y = y1 - 40
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("black")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif x1 == RECTANGLE_WIDTH / 2:
 draw_circle(x1 + radius_of_vertices, y1)
 turtle.penup()
 x = x1 + 35
 y = y1
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("black")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif x1 == -RECTANGLE_WIDTH / 2:
 draw_circle(x1 - radius_of_vertices, y1)
 turtle.penup()
 x = x1 - 50
 y = y1
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("black")
 turtle.write(curve_x.weight)
 turtle.penup()
 for vertex in vertex_positions:
 draw_circle_with_number(vertex.x, vertex.y, vertex.number, radius_of_vertices, "black")
 for curve in curves:
 print("Ребро між вершинами {} та {} має таку вагу: {}".format(curve.vertex1 + 1, curve.vertex2 + 1,
 curve.weight))
# Функція малювання напрямленого графа
def draw_directed_graph(adjacency_matrix, vertex_positions, num_of_vert, radius_of_vertices):
 for vertex in vertex_positions:
 draw_circle_with_number(vertex.x, vertex.y, vertex.number, radius_of_vertices, "black")
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
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
 elif y1 == y2:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
 elif (x1 == x2 or y1 == y2) and (abs(x1 - x2) != length_between_vertices or
 abs(y1 - y2) != length_between_vertices):
 if i < j:
 if x1 == x2 >= 0:
 point_between = (x1 + 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
 elif x1 == x2 < 0:
 point_between = (x1 - 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
 elif y1 == y2 >= 0:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
 elif y1 == y2 < 0:
 point_between = ((x1 + x2) / 2, y1 - 150)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
 elif i > j:
 if x1 == x2 >= 0:
 point_between = (x1 - 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
 elif x1 == x2 < 0:
 point_between = (x1 + 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
 elif y1 == y2 >= 0:
 point_between = ((x1 + x2) / 2, y1 - 150)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
 elif y1 == y2 < 0:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
 elif x1 != x2 and y1 != y2:
 if i > j:
 draw_line_with_arrow(point1, point2, RADIUS_OF_VERTICES)
 elif i < j:
 point_between = ((x1 + x2) / 2 + 100, (y1 + y2) / 2 + 80)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, point2, 0.99))
 if i == j:
 if y1 == RECTANGLE_HEIGHT / 2 and x1 != RECTANGLE_WIDTH / 2 and x1 != -
RECTANGLE_WIDTH / 2:
 draw_circle_with_arrow(x1, y1 + radius_of_vertices)
 elif y1 == -RECTANGLE_HEIGHT / 2 and x1 != RECTANGLE_WIDTH / 2 and x1 != -
RECTANGLE_WIDTH / 2:
 draw_circle_with_arrow(x1 - radius_of_vertices, y1 - radius_of_vertices / 2)
 elif x1 == RECTANGLE_WIDTH / 2:
 draw_circle_with_arrow(x1 + radius_of_vertices * 0.8, y1 + radius_of_vertices / 2)
 elif x1 == -RECTANGLE_WIDTH / 2:
 draw_circle_with_arrow(x1 - radius_of_vertices, y1)
# Створення матриці ваг
def generate_weight_matrix(n, seed, undirected_matrix):
 random.seed(seed)
 b_matrix = []
 for _ in range(n):
 row = []
 for _ in range(n):
 row.append(random.uniform(0, 2))
 b_matrix.append(row)
 b_c_matrix = []
 for row in b_matrix:
 transformed_row = []
 for element in row:
 transformed_row.append(math.ceil(element * 100))
 b_c_matrix.append(transformed_row)
 c_matrix = elementwise_matrix_multiply(b_c_matrix, undirected_matrix)
 d_matrix = []
 for row in c_matrix:
 d_row = []
 for element in row:
 if element > 0:
 d_row.append(1)
 else:
 d_row.append(0)
 d_matrix.append(d_row)
 n = len(d_matrix)
 h_matrix = [[0 for _ in range(n)] for _ in range(n)]
 for i in range(n):
 for j in range(n):
 if d_matrix[i][j] == d_matrix[j][i]:
 h_matrix[i][j] = h_matrix[j][i] = 0
 else:
 h_matrix[i][j] = 1
 w_matrix = elementwise_matrix_multiply(d_matrix, c_matrix)
 for i in range(len(w_matrix)):
 for j in range(i + 1, len(w_matrix)): # Проходимо тільки по верхньому трикутнику матриці
 w_matrix[j][i] = w_matrix[i][j]
 return w_matrix
# Виведення матриці ваг
def print_weight_matrix(matrix):
 print()
 print("Weight Matrix:")
 for row in matrix:
 print(row)
# Множення поелементно
def elementwise_matrix_multiply(matrix1, matrix2):
 result = []
 for i in range(len(matrix1)):
 row = []
 for j in range(len(matrix1[0])):
 row.append(matrix1[i][j] * matrix2[i][j])
 result.append(row)
 return result
# Отримання мінімального кістяка
def get_minimum(graph_in_gm, num_of_united_vertices):
 edge = (-1, -1, math.inf)
 for v in num_of_united_vertices:
 min_edge = min(graph_in_gm, key=lambda x: x[2] if (x[0] == v or x[1] == v) and
 (x[0] not in num_of_united_vertices or
 x[1] not in num_of_united_vertices) else math.inf)
 if edge[2] > min_edge[2]:
 edge = min_edge
 return edge
# Функція малювання ребер синім кольором
def draw_blue_edge(i, j, vertex_positions, radius_of_vertices, weight_matrix):
 curves = []
 turtle.color("blue")
 global sum_of_weights
 weight = weight_matrix[i][j]
 curve_x = Curve(i, j, weight)
 curves.append(curve_x)
 graph.append((i + 1, j + 1, weight))
 sum_of_weights += weight
 x1 = vertex_positions[i].x
 y1 = vertex_positions[i].y
 x2 = vertex_positions[j].x
 y2 = vertex_positions[j].y
 point1 = (x1, y1)
 point2 = (x2, y2)
 if (x1 == x2 or y1 == y2) and (abs(x1 - x2) == length_between_vertices or
 abs(y1 - y2) == length_between_vertices):
 draw_line(x1, y1, x2, y2, "blue")
 if x1 == x2:
 turtle.penup()
 x = x1 + 4
 y = (y1 + y2) / 2
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("blue")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif y1 == y2:
 turtle.penup()
 y = y1 + 4
 x = (x1 + x2) / 2
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("blue")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif (x1 == x2 or y1 == y2) and (abs(x1 - x2) != length_between_vertices or
 abs(y1 - y2) != length_between_vertices):
 if i < j:
 if x1 == x2 >= 0:
 point_between = (x1 + 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "blue")
 turtle.penup()
 x = point_between[0] - 70
 y = point_between[1]
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("blue")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif x1 == x2 < 0:
 point_between = (x1 - 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "blue")
 turtle.penup()
 x = point_between[0] + 50
 y = point_between[1]
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("blue")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif y1 == y2 >= 0:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2, "blue")
 turtle.penup()
 x = point_between[0]
 y = point_between[1] - 70
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("blue")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif y1 == y2 < 0:
 point_between = ((x1 + x2) / 2, y1 - 150)
 draw_bezier_curve(point1, point_between, point2, "blue")
 turtle.penup()
 x = point_between[0]
 y = point_between[1] + 60
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("blue")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif x1 != x2 or y1 != y2:
 draw_line(x1, y1, x2, y2, "blue")
 turtle.penup()
 x = (x1 + x2) / 2
 y = (y1 + y2) / 2
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("blue")
 turtle.write(curve_x.weight)
 turtle.penup()
 if i == j:
 if y1 == RECTANGLE_HEIGHT / 2 and x1 != RECTANGLE_WIDTH / 2 and x1 != -
RECTANGLE_WIDTH / 2:
 draw_circle(x1, y1 + radius_of_vertices)
 turtle.penup()
 x = x1 - 10
 y = y1 + 45
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("blue")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif y1 == -RECTANGLE_HEIGHT / 2 and x1 != RECTANGLE_WIDTH / 2 and x1 != -
RECTANGLE_WIDTH / 2:
 draw_circle(x1, y1 - radius_of_vertices - 10)
 turtle.penup()
 x = x1 - 10
 y = y1 - 40
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("blue")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif x1 == RECTANGLE_WIDTH / 2:
 draw_circle(x1 + radius_of_vertices, y1)
 turtle.penup()
 x = x1 + 35
 y = y1
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("blue")
 turtle.write(curve_x.weight)
 turtle.penup()
 elif x1 == -RECTANGLE_WIDTH / 2:
 draw_circle(x1 - radius_of_vertices, y1)
 turtle.penup()
 x = x1 - 50
 y = y1
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("blue")
 turtle.write(curve_x.weight)
 turtle.penup()
def main():
 # Встановлення вікна turtle та швидкості
 turtle.setup(width=1200, height=800)
 turtle.speed(12)
 window = Tk()
 window.title("Choose type of graph")
 # Задати розмір вікна для кнопок
 window.geometry("200x130")
 directed_adjacency_matrix = generate_directed_matrix(NUMBER_OF_VERTICES, RANDOM_SEED)
 undirected_adjacency_matrix = generate_undirected_matrix(directed_adjacency_matrix)
 vertex_positions = generate_vertex_positions(NUMBER_OF_VERTICES)
 w_matrix = generate_weight_matrix(NUMBER_OF_VERTICES, RANDOM_SEED, 
undirected_adjacency_matrix)
 print_weight_matrix(w_matrix)
 def undirected_graph():
 print_undirected_adjacency_matrix(undirected_adjacency_matrix)
 draw_undirected_graph(undirected_adjacency_matrix, vertex_positions, RADIUS_OF_VERTICES, 
w_matrix)
 def directed_graph():
 print_directed_adjacency_matrix(directed_adjacency_matrix)
 draw_directed_graph(directed_adjacency_matrix, vertex_positions, NUMBER_OF_VERTICES, 
RADIUS_OF_VERTICES)
 def clear_canvas():
 turtle.clear()
 def close_window():
 turtle.bye()
 sys.exit()
 def prim_algorithm():
 num_of_united_vertices = {1} # кількість поєднаних вершин # U
 list_of_edges = [] # список ребер кістяка # T
 while len(num_of_united_vertices) < NUMBER_OF_VERTICES:
 edge_with_min_weight = get_minimum(graph, num_of_united_vertices)
 if edge_with_min_weight[2] == math.inf:
 break
 list_of_edges.append(edge_with_min_weight)
 num_of_united_vertices.add(edge_with_min_weight[0])
 num_of_united_vertices.add(edge_with_min_weight[1])
 for vertex1 in vertex_positions:
 for vertex2 in vertex_positions:
 if vertex1.number == edge_with_min_weight[0] and vertex2.number == 
edge_with_min_weight[1]:
 print("vertex1.number: " + str(vertex1.number))
 print("vertex2.number: " + str(vertex2.number))
 print()
 time.sleep(2)
 draw_circle_with_number(vertex1.x, vertex1.y, vertex1.number, RADIUS_OF_VERTICES, 
"blue")
 draw_blue_edge(vertex1.number - 1, vertex2.number - 1, vertex_positions,
 RADIUS_OF_VERTICES, w_matrix)
 draw_circle_with_number(vertex2.x, vertex2.y, vertex2.number, RADIUS_OF_VERTICES, 
"blue")
 time.sleep(2)
 print("Список вершина1-вершина2-вага ребра: " + str(list_of_edges))
 print("Сума ваг ребер: " + str(sum_of_weights))
 window.protocol("WM_DELETE_WINDOW", turtle.bye)
 undirected_button = Button(window, text="Undirected button", command=undirected_graph, height=1, 
width=14)
 undirected_button.pack()
 directed_button = Button(window, text="Directed button", command=directed_graph, height=1, width=14)
 directed_button.pack()
 clear_button = Button(window, text="Clear all", command=clear_canvas, height=1, width=14)
 clear_button.pack()
 prim_algo = Button(window, text="Prims algorithm", command=prim_algorithm, height=1, width=14)
 prim_algo.pack()
 exit_button = Button(window, text="Stop and exit", command=close_window, height=1, width=14)
 exit_button.pack()
 window.mainloop()
# Виклик головної функції
if __name__ == "__main__":
 main()
