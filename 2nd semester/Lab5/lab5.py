# Code doesn't work correct

import turtle
import math
import random
from tkinter import *
from tkinter import messagebox
import sys
import collections
NUMBER_OF_VERTICES = 11
RANDOM_SEED = 3413
RECTANGLE_WIDTH = 600
RECTANGLE_HEIGHT = 600
RADIUS_OF_VERTICES = 15
length_between_vertices = min(RECTANGLE_WIDTH, 
RECTANGLE_HEIGHT) / (
 pow(2, math.floor(math.log2(NUMBER_OF_VERTICES))) / 2)
class Vertex:
 def __init__(self, number, x, y):
 self.number = number
 self.x = x
 self.y = y
# Функція для малювання вершини з номером
def draw_circle_with_number(x, y, number, radius_of_vertices, color):
 turtle.penup()
 turtle.goto(x, y - radius_of_vertices / 2)
 turtle.begin_fill()
 turtle.pendown()
 # turtle.pendown()
 # turtle.begin_fill()
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
 k = 1.0 - 1 * 0.01 - 3 * 0.005 - 0.15
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
 offset_x = 0 # Змінна для збереження значення на скільки потрібно 
зменшити x кожної вершини
 if num_vertices < 4:
 messagebox.showwarning(title='Warning!', message='Number of vertices must be more than 4 or equal 4')
 return
 else:
 # Додаємо вершини прямокутника
 vertex1 = Vertex(1, -RECTANGLE_WIDTH / 2 - offset_x, -
RECTANGLE_HEIGHT / 2)
 vertex2 = Vertex(2, -RECTANGLE_WIDTH / 2 - offset_x, 
RECTANGLE_HEIGHT / 2)
 vertex3 = Vertex(3, RECTANGLE_WIDTH / 2 - offset_x, 
RECTANGLE_HEIGHT / 2)
 vertex4 = Vertex(4, RECTANGLE_WIDTH / 2 - offset_x, -
RECTANGLE_HEIGHT / 2)
 vertices.append(vertex1)
 vertices.append(vertex2)
 vertices.append(vertex3)
 vertices.append(vertex4)
 # vertices.extend([vertex1, vertex2, vertex3, vertex4])
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
 x = -RECTANGLE_WIDTH / 2 - offset_x
 y = -RECTANGLE_HEIGHT / 2
 current_number = 9
 for _ in range(current_number - 1, num_vertices):
 while (x != RECTANGLE_WIDTH / 2 - offset_x
 and current_number <= num_vertices and x < 
RECTANGLE_WIDTH / 2 - offset_x):
 x += length_between_vertices
 if find_vertex_by_coordinates(vertices, x, y):
 welterweights = Vertex(current_number, x, y)
 vertices.append(welterweights)
 current_number += 1
 while y != RECTANGLE_HEIGHT / 2 and current_number <= 
num_vertices and y < RECTANGLE_HEIGHT:
 y += length_between_vertices
 if find_vertex_by_coordinates(vertices, x, y):
 welterweights = Vertex(current_number, x, y)
 vertices.append(welterweights)
 current_number += 1
 while (x != -RECTANGLE_WIDTH / 2 - offset_x and 
current_number <= num_vertices
 and x > -RECTANGLE_WIDTH - offset_x):
 x -= length_between_vertices
 if find_vertex_by_coordinates(vertices, x, y):
 welterweights = Vertex(current_number, x, y)
 vertices.append(welterweights)
 current_number += 1
 while y != -RECTANGLE_HEIGHT / 2 and current_number <= 
num_vertices and y > -RECTANGLE_HEIGHT:
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
 turtle.penup()
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
 turtle.penup()
# Функція малювання кола
def draw_circle(x, y):
 turtle.penup()
 turtle.goto(x, y)
 turtle.pendown()
 turtle.color("black")
 turtle.circle(RADIUS_OF_VERTICES)
 turtle.penup()
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
 turtle.penup()
# Функція малювання лінії зі стрілкою
def draw_line_with_arrow(point1, point2, radius_of_vert):
 turtle.color("black")
 turtle.penup()
 turtle.goto(point1[0], point1[1])
 turtle.pendown()
 angle = math.degrees(math.atan2(point2[1] - point1[1], point2[0] -
point1[0]))
 end_circle_x = point2[0] - radius_of_vert * math.cos(math.radians(angle))
 end_circle_y = point2[1] - radius_of_vert * math.sin(math.radians(angle)) + 
radius_of_vert / 2
 turtle.goto(end_circle_x, end_circle_y)
 turtle.color("red")
 turtle.setheading(angle)
 turtle.stamp()
 turtle.color("black")
 turtle.penup()
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
 turtle.penup()
# Функція малювання напрямленого графа
def draw_directed_graph(adjacency_matrix, vertex_positions, num_of_vert, 
radius_of_vertices):
 for vertex in vertex_positions:
 draw_circle_with_number(vertex.x, vertex.y, vertex.number, 
radius_of_vertices, "black")
 # draw_circle_with_number(vertex.x, vertex.y, vertex.number, 
radius_of_vertices)
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
 if (x1 == x2 or y1 == y2) and (abs(x1 - x2) == 
length_between_vertices or
 abs(y1 - y2) == length_between_vertices):
 if i < j:
 draw_line_with_arrow(point1, point2, 
RADIUS_OF_VERTICES)
 elif i > j:
 if x1 == x2:
 point_between = (x1 + 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif y1 == y2:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif (x1 == x2 or y1 == y2) and (abs(x1 - x2) != 
length_between_vertices or
 abs(y1 - y2) != length_between_vertices):
 if i < j:
 if x1 == x2 >= 0:
 point_between = (x1 + 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif x1 == x2 < 0:
 point_between = (x1 - 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif y1 == y2 >= 0:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif y1 == y2 < 0:
 point_between = ((x1 + x2) / 2, y1 - 150)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif i > j:
 if x1 == x2 >= 0:
 point_between = (x1 - 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif x1 == x2 < 0:
 point_between = (x1 + 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif y1 == y2 >= 0:
 point_between = ((x1 + x2) / 2, y1 - 150)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif y1 == y2 < 0:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif x1 != x2 and y1 != y2:
 if i > j:
 draw_line_with_arrow(point1, point2, 
RADIUS_OF_VERTICES)
 elif i < j:
 point_between = ((x1 + x2) / 2 + 100, (y1 + y2) / 2 + 80)
 draw_bezier_curve(point1, point_between, point2, "black")
 draw_arrow(point2, bezier_curve(point1, point_between, point2, 
0.99))
 if i == j:
 if y1 == RECTANGLE_HEIGHT / 2 and x1 != 
RECTANGLE_WIDTH / 2 and x1 != -RECTANGLE_WIDTH / 2:
 draw_circle_with_arrow(x1, y1 + radius_of_vertices)
 elif y1 == -RECTANGLE_HEIGHT / 2 and x1 != 
RECTANGLE_WIDTH / 2 and x1 != -RECTANGLE_WIDTH / 2:
 draw_circle_with_arrow(x1 - radius_of_vertices, y1 -
radius_of_vertices / 2)
 elif x1 == RECTANGLE_WIDTH / 2:
 draw_circle_with_arrow(x1 + radius_of_vertices * 0.8, y1 + 
radius_of_vertices / 2)
 elif x1 == -RECTANGLE_WIDTH / 2:
 draw_circle_with_arrow(x1 - radius_of_vertices, y1)
# Перетворення матриці суміжності в список
def matrix_to_adjacency_list(matrix):
 graph = {}
 num_rows, num_cols = len(matrix), len(matrix[0])
 for i in range(num_rows):
 graph[i] = []
 for j in range(num_cols):
 if matrix[i][j] == 1:
 graph[i].append(j)
 return graph
# BFS algorithm
def bfs(graph, root):
 visited, queue = set(), collections.deque([root])
 visited.add(root)
 bfs_result = [] # Створюємо список для зберігання результату BFS
 while queue:
 vertex = queue.popleft()
 bfs_result.append(vertex + 1)
 for neighbour in graph[vertex]:
 if neighbour not in visited:
 visited.add(neighbour)
 queue.append(neighbour)
 return bfs_result
# DFS algorithm
def dfs(graph, start, visited=None, result=None):
 if visited is None:
 visited = set()
 if result is None:
 result = []
 visited.add(start)
 result.append(start)
 for next_vertex in graph[start]:
 if next_vertex not in visited:
 dfs(graph, next_vertex, visited, result)
 return result
def find_path_to_target(graph, current_vertex, target_vertex, visited):
 if current_vertex == target_vertex:
 return [current_vertex]
 visited.add(current_vertex)
 for next_vertex in graph[current_vertex]:
 if next_vertex not in visited:
 path = find_path_to_target(graph, next_vertex, target_vertex, visited)
 if path:
 return [current_vertex] + path
 return None
# Функція для пошуку першої вершини, з якої виходить дуга
def find_first_vertex(matrix):
 num_vertices = len(matrix)
 start_vertex = 0
 for i in range(start_vertex, num_vertices):
 if 1 in matrix[i]:
 return i
 return None
def find_vertex_by_number(vertices, number):
 for vertex in vertices:
 if vertex.number == number:
 return vertex
 return None
def draw_colored_circle_with_number(x, y, number, radius_of_vertices, color):
 turtle.penup()
 turtle.goto(x - 5, y + 20)
 turtle.pendown()
 turtle.begin_fill()
 turtle.color(color) # Змініть колір на необхідний
 turtle.circle(radius_of_vertices)
 turtle.end_fill()
 turtle.penup()
 turtle.color("white")
 turtle.goto(x, y)
 turtle.write(number, align="center", font=("Arial", 12, "normal"))
 turtle.penup()
def draw_directed_edge(i, j, vertex_positions, adjacency_matrix):
 if adjacency_matrix[i][j]:
 x1, y1 = vertex_positions[i].x, vertex_positions[i].y
 x2, y2 = vertex_positions[j].x, vertex_positions[j].y
 point1 = (x1, y1)
 point2 = (x2, y2)
 turtle.color("blue")
 if (x1 == x2 or y1 == y2) and (abs(x1 - x2) == length_between_vertices or
 abs(y1 - y2) == length_between_vertices):
 if i < j:
 draw_line(x1, y1, x2, y2, "blue")
 elif i > j:
 if x1 == x2:
 point_between = (x1 + 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "blue")
 elif y1 == y2:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2, "blue")
 elif (x1 == x2 or y1 == y2) and (abs(x1 - x2) != length_between_vertices 
or
 abs(y1 - y2) != length_between_vertices):
 if i < j:
 if x1 == x2 >= 0:
 point_between = (x1 + 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "blue")
 elif x1 == x2 < 0:
 point_between = (x1 - 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "blue")
 elif y1 == y2 >= 0:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2, "blue")
 elif y1 == y2 < 0:
 point_between = ((x1 + x2) / 2, y1 - 150)
 draw_bezier_curve(point1, point_between, point2, "blue")
 elif i > j:
 if x1 == x2 >= 0:
 point_between = (x1 - 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "blue")
 elif x1 == x2 < 0:
 point_between = (x1 + 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2, "blue")
 elif y1 == y2 >= 0:
 point_between = ((x1 + x2) / 2, y1 - 150)
 draw_bezier_curve(point1, point_between, point2, "blue")
 elif y1 == y2 < 0:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2, "blue")
 elif x1 != x2 and y1 != y2:
 if i > j:
 draw_line(x1, y1, x2, y2, "blue")
 elif i < j:
 point_between = ((x1 + x2) / 2 + 100, (y1 + y2) / 2 + 80)
 draw_bezier_curve(point1, point_between, point2, "blue")
def adjacency_matrix_from_traversal(traversal):
 vertices = set(traversal)
 size = len(vertices)
 matrix = [[0] * size for _ in range(size)]
 for i in range(len(traversal) - 1):
 current_vertex = traversal[i]
 next_vertex = traversal[i + 1]
 matrix[current_vertex - 1][next_vertex - 1] = 1
 return matrix
index_dfs = 0
index_bfs = 0
current_vertex_index = 0
current_bfs_index = 0
current_bfs_vertex = 0
visited_neighbours_bfs = []
min_neighbour = 0
neighbours = []
def main():
 # Встановлення вікна turtle та швидкості
 turtle.setup(width=1200, height=800)
 turtle.speed(12)
 window = Tk()
 window.title("Choose type of graph")
 # Задати розмір вікна для кнопок
 window.geometry("200x130")
 print()
 directed_adjacency_matrix = 
generate_directed_matrix(NUMBER_OF_VERTICES, RANDOM_SEED)
 graph = matrix_to_adjacency_list(directed_adjacency_matrix)
 print("Список")
 for vertex, neighbors in graph.items():
 print(f"{vertex + 1}: {[neighbor + 1 for neighbor in neighbors]}")
 print()
 def directed_graph():
 vertex_positions = generate_vertex_positions(NUMBER_OF_VERTICES)
 print_directed_adjacency_matrix(directed_adjacency_matrix)
 draw_directed_graph(directed_adjacency_matrix, vertex_positions, 
NUMBER_OF_VERTICES, RADIUS_OF_VERTICES)
 def breadth_first_search():
 first_vertex = find_first_vertex(directed_adjacency_matrix)
 bfs_result = bfs(graph, first_vertex)
 vertices = generate_vertex_positions(NUMBER_OF_VERTICES)
 initial_neighbours = graph[first_vertex]
 global index_bfs
 global current_bfs_index
 global current_bfs_vertex
 global visited_neighbours_bfs
 global min_neighbour
 global neighbours
 if index_bfs == 0:
 matrix = adjacency_matrix_from_traversal(bfs_result)
 print(bfs_result)
 print("Матриця сумiжностi дерева обходу для BFS")
 for row in matrix:
 print(row)
 print()
 print("BFS:", end=" ")
 if current_bfs_index < len(bfs_result):
 if index_bfs % 2 == 0:
 current_vertex_number = bfs_result[current_bfs_index]
 current_vertex = find_vertex_by_number(vertices, 
current_vertex_number)
 x, y = current_vertex.x, current_vertex.y
 print(current_vertex_number, end="")
 draw_colored_circle_with_number(x, y, current_vertex_number, 
RADIUS_OF_VERTICES, "blue")
 visited_neighbours_bfs.append(current_vertex_number)
 current_bfs_index += 1
 index_bfs += 1
 else:
 print(" - ", end="")
 current_vertex = bfs_result[current_bfs_vertex]
 next_vertex = bfs_result[current_bfs_index]
 neighbours = [neighbour_vertex + 1 for neighbour_vertex in 
initial_neighbours]
 if current_vertex not in visited_neighbours_bfs:
 visited_neighbours_bfs.append(current_vertex)
 if next_vertex in neighbours:
 draw_directed_edge(current_bfs_vertex, next_vertex - 1, vertices, 
directed_adjacency_matrix)
 else:
 min_neighbour = min(neighbours)
 while min_neighbour in neighbours:
 if any(neighbour not in visited_neighbours_bfs for neighbour in 
graph[min_neighbour]):
 current_bfs_vertex = min_neighbour
 draw_directed_edge(current_bfs_vertex, next_vertex - 1, 
vertices, directed_adjacency_matrix)
 break
 else:
 neighbours.remove(min_neighbour)
 min_neighbour = min(neighbours)
 index_bfs += 1
 def depth_first_search():
 global index_dfs
 global current_vertex_index
 first_vertex = find_first_vertex(directed_adjacency_matrix)
 visited_nodes = dfs(graph, first_vertex)
 visited_nodes_plus_one = [node + 1 for node in visited_nodes]
 visited_vertices = []
 vertices = generate_vertex_positions(NUMBER_OF_VERTICES)
 if index_dfs == 0:
 matrix = adjacency_matrix_from_traversal(visited_nodes_plus_one)
 print(visited_nodes_plus_one)
 print("Матриця сумiжностi дерева обходу для DFS")
 for row in matrix:
 print(row)
 print()
 # print(visited_nodes_plus_one)
 print("DFS:", end=" ")
 if current_vertex_index < len(visited_nodes_plus_one):
 if index_dfs % 2 == 0:
 current_vertex_number = 
visited_nodes_plus_one[current_vertex_index] # Враховуємо індексацію від 
0
 current_vertex = find_vertex_by_number(vertices, 
current_vertex_number)
 x, y = current_vertex.x, current_vertex.y
 print(current_vertex_number, end="")
 draw_colored_circle_with_number(x, y, current_vertex_number, 
RADIUS_OF_VERTICES, "blue")
 current_vertex_index += 1
 index_dfs += 1
 visited_vertices.append(current_vertex)
 else:
 print(" - ", end="")
 current_vertex = visited_nodes[current_vertex_index - 1]
 next_vertex = visited_nodes[current_vertex_index]
 # Перевірка, чи існує зв'язок між поточною вершиною та 
наступною
 if next_vertex in graph[current_vertex]:
 draw_directed_edge(current_vertex, next_vertex, vertices, 
directed_adjacency_matrix)
 else:
 # Пошук шляху від поточної вершини до наступної
 path_to_next_vertex = find_path_to_target(graph, current_vertex, 
next_vertex, set())
 # Малювання дуг, якщо шлях знайдено
 if path_to_next_vertex:
 for i in range(len(path_to_next_vertex) - 1):
 draw_directed_edge(path_to_next_vertex[i], 
path_to_next_vertex[i + 1], vertices,
 directed_adjacency_matrix)
 index_dfs += 1
 else:
 # Перевірка чи всі вершини були відвідані
 if len(visited_nodes) < NUMBER_OF_VERTICES:
 # Вибір вершини з найменшим номером серед непройдених
 next_vertex = 
min(set(range(NUMBER_OF_VERTICES)).difference(set(visited_nodes)))
 # Знайдемо шлях від поточної вершини до обраної
 path = dfs(graph, next_vertex)
 # Додамо нові вершини до відвіданих
 visited_nodes.extend(path)
 # Відновлення лічильників
 current_vertex_index = 0
 index_dfs = 0
 else:
 print("\nThe end", end="")
 def clear_canvas():
 turtle.clear()
 def close_window():
 turtle.bye()
 sys.exit()
 window.protocol("WM_DELETE_WINDOW", turtle.bye)
 directed_button = Button(window, text="Directed button", 
command=directed_graph, height=1, width=14)
 directed_button.pack()
 bfs_button = Button(window, text="BFS", command=breadth_first_search, 
height=1, width=14)
 bfs_button.pack()
 dfs_button = Button(window, text="DFS", command=depth_first_search, 
height=1, width=14)
 dfs_button.pack()
 clear_button = Button(window, text="Clear all", command=clear_canvas, 
height=1, width=14)
 clear_button.pack()
 exit_button = Button(window, text="Stop and exit", 
command=close_window, height=1, width=14)
 exit_button.pack()
 window.mainloop()
# Виклик головної функції
if __name__ == "__main__":
 main()
