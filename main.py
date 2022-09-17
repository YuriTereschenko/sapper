import random


class Cell:
    def __init__(self):
        self.around_mines = 0
        self.mine = False
        self.fl_open = True


class GamePole:
    def count_mines(self):
        for i in range(self.pole_size):
            for j in range(self.pole_size):
                if self.pole[i][j].mine is False:
                    check_index = (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1)
                    self.pole[i][j].around_mines = sum((self.pole[i + x][j + y].mine for x, y in check_index if
                                                        0 <= i + x < self.pole_size and 0 <= j + y < self.pole_size))

    def set_mine(self):
        mine_index = random.sample([x for x in range(self.cell_quantity)], self.mine_quantity)
        for m in mine_index:
            row = m // self.pole_size
            column = m % self.pole_size
            self.pole[row][column].mine = True

    def __init__(self, pole_size, mine_quantity):
        self.cell_quantity = pole_size ** 2
        self.mine_quantity = mine_quantity
        self.pole_size = pole_size
        self.pole = [[Cell() for x in range(self.pole_size)] for _ in range(self.pole_size)]
        self.init()

    def init(self):
        self.set_mine()
        self.count_mines()

    def show(self):
        count = 0
        for x in self.pole:
            for j in x:
                if j.fl_open:
                    if j.mine:
                        print("*", end=" ")
                    else:
                        print(j.around_mines, end=" ")
                else:
                    print("#", end=" ")
            print()


pole = GamePole(3, 4)
pole.show()
