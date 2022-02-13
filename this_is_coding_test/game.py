map_height, map_width = map(int, input().split())
start_x, start_y, direction = map(int, input().split())
world = []
for _ in range(map_height):
    world.append(list(map(int, input().split())))

dir = [0, 1, 2, 3]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

class Human:
    def __init__(self, world, direction, x, y):
        self.status = True
        self.world = world
        self.direction = direction
        self.x = x
        self.y = y
        self.cnt = 0

    def turn_left(self):
        self.direction = (self.direction-1) % 4
        while self.world[self.y+dy[self.direction]][self.x+dx[self.direction]] != 0:
            self.direction = (self.direction-1) % 4

    def mark(self):
        if self.world[self.y][self.x] != 9:
            self.world[self.y][self.x] = 9
            self.cnt += 1

    def move(self):
        self.y += dy[self.direction]
        self.x += dx[self.direction]

    def step_back(self):
        self.y -= dy[self.direction]
        self.x -= dx[self.direction]

        if world[self.y-dy[self.direction]][self.x-dx[self.direction]] == 1:
            self.status = False

    def check_dir(self):
        if self.world[self.y+1][self.x] != 0 and \
            self.world[self.y-1][self.x] != 0 and \
            self.world[self.y][self.x+1] != 0 and \
            self.world[self.y][self.x-1] != 0:
            return False
        else:
            return True


human = Human(world, direction, start_x, start_y)
while human.status:

    print(human.x, human.y)
    print(human.direction)
    for i in range(map_height):
        print(human.world[i])
    human.mark()
    print(human.check_dir())

    if human.check_dir():
        human.turn_left()
        human.move()
    else:
        human.step_back()


print("finish")
print(human.cnt)
for i in range(map_height):
    print(human.world[i])
print(human.x, human.y)

'''
 6 6
1 1 0
1 1 1 1 1 1
1 0 1 0 0 1
1 0 0 0 1 1
1 1 0 1 0 1
1 0 0 0 0 1
1 1 1 1 1 1
'''
