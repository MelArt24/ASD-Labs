import turtle
import math
import random
from tkinter import *
from tkinter import messagebox

NUMBER_OF_VERTICES = 11
RANDOM_SEED = 3413
RECTANGLE_WIDTH = 600
RECTANGLE_HEIGHT = 600
RADIUS_OF_VERTICES = 15

length_between_vertices = min(RECTANGLE_WIDTH, 
RECTANGLE_HEIGHT) / (pow(2,
math.floor(math.log2(NUMBER_OF_VERTICES))) / 2)

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
     
 k = 1.0 - 1 * 0.02 - 3 * 0.005 - 0.25
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


# I do not want to conntinue refactoring this code
  
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
 while x != RECTANGLE_WIDTH / 2 and current_number <= 
num_vertices and x < RECTANGLE_WIDTH / 2:
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
 while x != -RECTANGLE_WIDTH / 2 and current_number <= 
num_vertices and x > -RECTANGLE_WIDTH:
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
 for vertex in vertices:
 print("Вершина {}: координати ({}, {})".format(vertex.number, vertex.x, 
vertex.y))
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
def draw_undirected_graph(adjacency_matrix, vertex_positions, 
radius_of_vertices):
 for vertex in vertex_positions:
 draw_circle_with_number(vertex.x, vertex.y, vertex.number, 
radius_of_vertices)
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
 if (x1 == x2 or y1 == y2) and (abs(x1 - x2) == 
length_between_vertices or abs(y1 - y2) == length_between_vertices):
 draw_line(x1, y1, x2, y2)
 elif (x1 == x2 or y1 == y2) and (abs(x1 - x2) != 
length_between_vertices or abs(y1 - y2) != length_between_vertices):
 if i < j:
 if x1 == x2 >= 0:
 point_between = (x1 + 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2)
 elif x1 == x2 < 0:
 point_between = (x1 - 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2)
 elif y1 == y2 > 0:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2)
 elif y1 == y2 < 0:
 point_between = ((x1 + x2) / 2, y1 - 150)
 draw_bezier_curve(point1, point_between, point2)
 elif x1 != x2 or y1 != y2:
 draw_line(x1, y1, x2, y2)
 if i == j:
 if y1 == RECTANGLE_HEIGHT / 2 and x1 != 
RECTANGLE_WIDTH / 2 and x1 != -RECTANGLE_WIDTH / 2:
 draw_circle(x1, y1 + radius_of_vertices)
 elif y1 == -RECTANGLE_HEIGHT / 2 and x1 != 
RECTANGLE_WIDTH / 2 and x1 != -RECTANGLE_WIDTH / 2:
 draw_circle(x1, y1 - radius_of_vertices - 10)
 elif x1 == RECTANGLE_WIDTH / 2:
 draw_circle(x1 + radius_of_vertices, y1)
 elif x1 == -RECTANGLE_WIDTH / 2:
 draw_circle(x1 - radius_of_vertices, y1)
 for vertex in vertex_positions:
 draw_circle_with_number(vertex.x, vertex.y, vertex.number, 
radius_of_vertices)
  
# Функція малювання напрямленого графа
def draw_directed_graph(adjacency_matrix, vertex_positions, num_of_vert, 
radius_of_vertices):
 for vertex in vertex_positions:
 draw_circle_with_number(vertex.x, vertex.y, vertex.number, 
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
length_between_vertices or abs(y1 - y2) == length_between_vertices):
 if i < j:
 draw_line_with_arrow(point1, point2,
RADIUS_OF_VERTICES)
 elif i > j:
 if x1 == x2:
 point_between = (x1 + 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2)
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif y1 == y2:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2)
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif (x1 == x2 or y1 == y2) and (abs(x1 - x2) != 
length_between_vertices or abs(y1 - y2) != length_between_vertices):
 if i < j:
 if x1 == x2 >= 0:
 point_between = (x1 + 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2)
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif x1 == x2 < 0:
 point_between = (x1 - 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2)
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif y1 == y2 > 0:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2)
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif y1 == y2 < 0:
 point_between = ((x1 + x2) / 2, y1 - 150)
 draw_bezier_curve(point1, point_between, point2)
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif i > j:
 if x1 == x2 >= 0:
 point_between = (x1 - 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2)
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif x1 == x2 < 0:
 point_between = (x1 + 150, (y1 + y2) / 2)
 draw_bezier_curve(point1, point_between, point2)
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif y1 == y2 > 0:
 point_between = ((x1 + x2) / 2, y1 - 150)
 draw_bezier_curve(point1, point_between, point2)
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif y1 == y2 < 0:
 point_between = ((x1 + x2) / 2, y1 + 150)
 draw_bezier_curve(point1, point_between, point2)
 draw_arrow(point2, bezier_curve(point1, point_between, 
point2, 0.99))
 elif x1 != x2 and y1 != y2:
 if i > j:
 draw_line_with_arrow(point1, point2, 
RADIUS_OF_VERTICES)
 elif i < j:
 point_between = ((x1 + x2) / 2 + 100, (y1 + y2) / 2 + 80)
 draw_bezier_curve(point1, point_between, point2)
 draw_arrow(point2, bezier_curve(point1, point_between, point2, 
0.99))
 if i == j:
 if y1 == RECTANGLE_HEIGHT / 2 and x1 != 
RECTANGLE_WIDTH / 2 and x1 != -RECTANGLE_WIDTH / 2:
 draw_circle_with_arrow(x1, y1 + radius_of_vertices)
 elif y1 == -RECTANGLE_HEIGHT / 2 and x1 != 
RECTANGLE_WIDTH / 2 and x1 != -RECTANGLE_WIDTH / 2:
 draw_circle_with_arrow(x1 - radius_of_vertices, y1 -
radius_of_vertices/2)
 elif x1 == RECTANGLE_WIDTH / 2:
 draw_circle_with_arrow(x1 + radius_of_vertices * 0.8, y1 + 
radius_of_vertices / 2)
 elif x1 == -RECTANGLE_WIDTH / 2:
 draw_circle_with_arrow(x1 - radius_of_vertices, y1)
  
def main():
 # Встановлення вікна turtle та швидкості
 turtle.setup(width=1200, height=800)
 turtle.speed(12)
 window = Tk()
 window.title("Choose type of graph")
 # Задати розмір вікна для кнопок
 window.geometry("200x80")
  
 def undirected_graph():
 directed_adjacency_matrix = 
generate_directed_matrix(NUMBER_OF_VERTICES, RANDOM_SEED)
 vertex_positions = generate_vertex_positions(NUMBER_OF_VERTICES)
 undirected_adjacency_matrix = 
generate_undirected_matrix(directed_adjacency_matrix)
 print_undirected_adjacency_matrix(undirected_adjacency_matrix)
 draw_undirected_graph(undirected_adjacency_matrix, vertex_positions, 
RADIUS_OF_VERTICES)

 def directed_graph():
 directed_adjacency_matrix = 
generate_directed_matrix(NUMBER_OF_VERTICES, RANDOM_SEED)
 vertex_positions = generate_vertex_positions(NUMBER_OF_VERTICES)
 print_directed_adjacency_matrix(directed_adjacency_matrix)
 draw_directed_graph(directed_adjacency_matrix, vertex_positions, 
NUMBER_OF_VERTICES, RADIUS_OF_VERTICES)

 def clear_canvas():
 turtle.clear()
 window.protocol("WM_DELETE_WINDOW", turtle.bye)
 undirected_button = Button(window, text="Undirected button", 
command=undirected_graph)
 undirected_button.pack()
 directed_button = Button(window, text=" Directed button ", 
command=directed_graph)
 directed_button.pack()
 clear_button = Button(window, text=" Clear all ", 
command=clear_canvas)
 clear_button.pack()
 window.mainloop()
   
# Виклик головної функції
if __name__ == "__main__":
 main()
