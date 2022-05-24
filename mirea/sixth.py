import math
from random import randint
from tkinter import Tk, Canvas, Button
import numpy as np

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

NODE_R = 15

C1 = 2
C2 = 50
C3 = 20000
C4 = 0.1

DELAY = 10


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Node:
    def __init__(self, text):
        self.text = text
        self.targets = []
        self.vec = Vec(0, 0)

    def to(self, *nodes):
        for n in nodes:
            self.targets.append(n)
            n.targets.append(self)
        return self


class Graph:
    def __init__(self):
        self.nodes = []

    def add(self, text):
        self.nodes.append(Node(text))
        return self.nodes[-1]


class GUI:
    def __init__(self, root):
        self.canvas = Canvas(root, width=CANVAS_WIDTH,
                             height=CANVAS_HEIGHT, bg="white")
        self.draw_button = Button(root, text="Draw", command=self.start_draw)
        self.canvas.pack()
        self.draw_button.pack()
        self.nodes = None
        self.busy = None

    def draw_node(self, x, y, text, r=NODE_R):
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="MistyRose2")
        self.canvas.create_text(x, y, text=text)

    def draw_graph(self):
        for n in self.nodes:
            for t in n.targets:
                self.canvas.create_line(n.vec.x, n.vec.y, t.vec.x, t.vec.y)
        for n in self.nodes:
            self.draw_node(n.vec.x, n.vec.y, n.text)

    def start_draw(self):
        self.canvas.delete("all")
        if self.busy:
            root.after_cancel(self.busy)
        random_layout(self.nodes)
        self.animate()

    def animate(self):
        self.canvas.delete("all")
        force_layout(self.nodes)
        self.draw_graph()
        self.busy = root.after(5, self.animate)


def random_layout(nodes):
    for n in nodes:
        n.vec.x = randint(NODE_R * 4, CANVAS_WIDTH - NODE_R * 4 - 1)
        n.vec.y = randint(NODE_R * 4, CANVAS_HEIGHT - NODE_R * 4 - 1)


def f_spring(u: Vec, v: Vec):
    length = np.linalg.norm([u.x - v.x, u.y - v.y])
    unit = [v.x - u.x, v.y - u.y] / np.linalg.norm([u.x - v.x, u.y - v.y])
    return C1 * unit * math.log(length / C2)


def f_ball(u: Vec, v: Vec):
    length = np.linalg.norm([u.x - v.x, u.y - v.y])
    unit = [u.x - v.x, u.y - v.y] / length
    return unit * C3 / (length * length)


def force_layout(nodes):
    forces = {}
    force = [0] * 2
    for n in nodes:
        nodes_copy = nodes.copy()
        nodes_copy.remove(n)
        for j in n.targets:
            target = f_spring(n.vec, j.vec)
            force[0] += target[0]
            force[1] += target[1]
            nodes_copy.remove(j)
        for i in nodes_copy:
            target = f_ball(n.vec, i.vec)
            force[0] += target[0]
            force[1] += target[1]
        forces[n] = force
        force = [0] * 2
    for n in nodes:
        n.vec.x += forces[n][0] * C4
        n.vec.y += forces[n][1] * C4


g = Graph()
n1 = g.add("1")
n2 = g.add("2")
n3 = g.add("3")
n4 = g.add("4")
n5 = g.add("5")
n6 = g.add("6")
n7 = g.add("7")
n1.to(n2, n3, n4, n5)
n2.to(n5)
n3.to(n2, n4)
n6.to(n4, n1, n7)
n7.to(n5, n1)

root = Tk()
w = GUI(root)
w.nodes = g.nodes
root.mainloop()