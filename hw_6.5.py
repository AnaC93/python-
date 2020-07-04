class Stationary:
    def __init__(self, title="Can draw"):
        self.title = title

    def draw(self):
        print(f"Start drawing {self.title}))")


class Pen(Stationary):
    def draw(self):
        print(f"Start drawing with a {self.title} pen")


stat = Stationary
stat.draw()
pen = Pen("Parker")
pen.draw()




