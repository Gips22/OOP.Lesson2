class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.coords = list((LineTo(0, 0),) + args)


    def get_path(self):
        return self.coords[1:]

    def get_length(self):
        g = ((self.coords[i - 1], self.coords[i]) for i in range(1, len(self.coords)))
        print()
        return sum(map(lambda t: ((t[1].x - t[0].x) ** 2 + (t[1].y - t[0].y) ** 2) ** 0.5, g))

    def add_line(self, line):
        self.coords.append(line)

p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()

