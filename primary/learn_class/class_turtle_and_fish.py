import random

  # 行走区域
legal_x = [0, 10]
legal_y = [0, 10]

class Turtle:
    def __init__(self, name='小乌龟'):
        global legal_x
        global legal_y
        self.__pos_x = random.randint(*legal_x)  # 初始化乌龟生成的位置
        self.__pos_y = random.randint(*legal_y)
        self.energy = 100
        self.name = name


    def __getDirection(self):
        return random.choice(['up', 'down', 'left', 'right'])


    def __getStep(self):
        return random.randint(1, 2)  # 乌龟的步长为1-2


    def getPositon(self):
        return (self.__pos_x, self.__pos_y)


    def getEnergy(self):
        print('%s 还剩 %d 点体力' % (self.name, self.energy))

        
    def move(self):
        global legal_x
        global legal_y
        direction = self.__getDirection()  # 获取走的方向
        step = self.__getStep()  # 获取走的步长
        
        if direction == 'right':
            self.__pos_x += step
            if self.__pos_x > legal_x[1]:  # 如果向右越界则向左掉头行走
                self.__pos_x = legal_x[1] + (legal_x[1] - self.__pos_x)
                
        elif direction == 'left':
            self.__pos_x -= step
            if self.__pos_x < legal_x[0]:  # 如果向左越界则向右掉头行走
                self.__pos_x = legal_x[0] + (legal_x[0] - self.__pos_x)
                
        elif direction == 'up':
            self.__pos_y += step
            if self.__pos_y > legal_y[1]:  # 如果向上越界则向下掉头行走
                self.__pos_y = legal_y[1] + (legal_y[1] - self.__pos_y)
                
        else:
            self.__pos_y -= step
            if self.__pos_y < legal_y[0]:  # 如果向下越界则向上掉头行走
                self.__pos_y = legal_y[0] + (legal_y[0] - self.__pos_y)

        self.energy -= 1  # 每移动一次，体力减少1


    def eat(self):
        self.energy += 20
        if self.energy > 100:
            self.energy = 100


class Fish:
    def __init__(self, name='小鱼'):
        global legal_x
        global legal_y
        self.__pos_x = random.randint(*legal_x)  # 初始化鱼生成的位置
        self.__pos_y = random.randint(*legal_y)
        self.name = name
        self.__step = 1


    def __getDirection(self):
        return random.choice(['up', 'down', 'left', 'right'])


    def getPositon(self):
        return (self.__pos_x, self.__pos_y)


    def move(self):
        global legal_x
        global legal_y
        direction = self.__getDirection()  # 获取走的方向
        step = self.__step
        
        if direction == 'right':
            self.__pos_x += step
            if self.__pos_x > legal_x[1]:  # 如果向右越界则向左掉头行走
                self.__pos_x = legal_x[1] + (legal_x[1] - self.__pos_x)
                
        elif direction == 'left':
            self.__pos_x -= step
            if self.__pos_x < legal_x[0]:  # 如果向左越界则向右掉头行走
                self.__pos_x = legal_x[0] + (legal_x[0] - self.__pos_x)
                
        elif direction == 'up':
            self.__pos_y += step
            if self.__pos_y > legal_y[1]:  # 如果向上越界则向下掉头行走
                self.__pos_y = legal_y[1] + (legal_y[1] - self.__pos_y)
                
        else:
            self.__pos_y -= step
            if self.__pos_y < legal_y[0]:  # 如果向下越界则向上掉头行走
                self.__pos_y = legal_y[0] + (legal_y[0] - self.__pos_y)


turtle = Turtle()
fish = []

for i in range(10):
    new_fish = Fish('小鱼_'+str(i))
    fish.append(new_fish)

while True:
    if not len(fish):
        print('鱼儿都被吃完啦，游戏结束！')
        break
    if not turtle.energy:
        print('乌龟没有体力抓鱼啦，游戏结束！')
        break

    turtle.move()
    turtle_pos = turtle.getPositon()
    print('小乌龟爬到了 (%d, %d)' % turtle_pos)
    
    for each_fish in fish[ : ]:
        each_fish.move()
        each_fish_pos = each_fish.getPositon()
        print('%s爬到了 (%d, %d)' % (each_fish.name, *each_fish_pos))
        
        if each_fish_pos == turtle_pos:
            turtle.eat()
            print('%s 被吃掉咯~' % each_fish.name)
            fish.remove(each_fish)
