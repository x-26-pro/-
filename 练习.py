import tkinter
import sys, random, math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<Point>: (%f, %f)" % (self.x, self.y)

class Branch(object):
    def __init__(self, bottom, top, branches, level = 0):
        self.bottom = bottom
        self.top = top
        self.level = level
        self.branches = branches
        self.children = []

    def __str__(self):
        s = "Top: %s, Bottom: %s, Children Count: %d"
        (self.top, self.bottom, len(self.children))
        return s

    def nextGen(self, n=-1, rnd=1):
        if n <= 0: n = self.branches
        if rnd == 1:
            n = random.randint(n / 2, n * 2)
            if n <= 0: n = 1
        dx = self.top.x - self.bottom.x
        dy = self.top.y - self.bottom.y
        r = 0.20 + random.random() * 0.2
        if self.top.x == self.bottom.x:
            # 如果是一条竖线
            x = self.top.x
            y = dy * r + self.bottom.y
        elif self.top.y == self.bottom.y:
            # 如果是一条横线
            x = dx * r + self.bottom.y
            y = self.top.y
        else:
            x = dx * r
            y = x * dy / dx
            x += self.bottom.x
            y += self.bottom.y
        oldTop = self.top
        self.top = Point(x,y)
        a = math.pi / (2 * n)
        for i in range(n):
            a2 = -a * (n - 1) / 2 + a * i - math.pi
            a2 *= 0.9 + random.random() * 0.2
            self.children.append(self.mk)