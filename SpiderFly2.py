# Spider and fly on opposite vertices of a cube
# Spider has random movement to catch fly
# Need to find expected number of moves

# In this version the spider cannot go back on itself


# import the required modules
import random
import statistics
import math

# spider object
class spider:
    # set up variables
    prevx1 = 0
    prevy1 = 0
    prevx2 = 0
    prevy2 = 0
    counter = 1
    # init function
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # move function
    def move(self):
        # set up variables
        valid = False
        # store position for next check
        if self.counter == 1:
            self.prevx1 = self.x
            self.prevy1 = self.y
            self.counter = 2
        elif self.counter == 2:
            self.prevx2 = self.x
            self.prevy2 = self.y
            self.counter = 1
        # begin loop
        while valid == False:
            # set up local variables
            x = self.x
            y = self.y
            # choose either 1, 2 or 3
            choice = random.randrange(1, 4)
            # x clockwise
            if choice == 1:
                x += 1
                if x == 5:
                    x = 1
            # x anti-clockwise
            elif choice == 2:
                x -= 1
                if x == 0:
                    x = 4
            # y up/down
            elif choice == 3:
                y += 1
                if y == 2:
                    y = 0
            # check if valid move
            if (x != self.prevx1 or y != self.prevy1) and self.counter == 1:
                valid = True
            if (x != self.prevx2 or y != self.prevy2) and self.counter == 2:
                valid = True            
        # save new position to instance
        self.x = x
        self.y = y
                
# fly object
class fly:
    # init function
    def __init__(self, x, y):
        self.x = x
        self.y = y

# run function
def run(s, f):
    # set up variables
    found = False
    moves = 0
    # program loop
    while found == False:
        # move spider
        s.move()
        # increment variable
        moves += 1
        # check if spider found fly
        if s.x == f.x and s.y == f.y:
            found = True
    # return amount of moves required
    return moves

# main function
def main():
    # set up variables
    moves = []
    total = 0
    limit = int(input("Enter the number of simulations: "))
    # program loop
    for i in range(limit):
        # set up objects
        s = spider(2, 1)
        f = fly(4, 0)
        # process a simulation
        num = run(s, f)
        # change variables
        moves.append(num)
        total += num
    # calculate required values
    mode = statistics.mode(moves)
    mean = total / limit
    median = sorted(moves)[math.ceil((limit / 2))]
    p3 = moves.count(3) / limit
    p5 = moves.count(5) / limit
    p7 = moves.count(7) / limit
    p9 = moves.count(9) / limit
    p11 = moves.count(11) / limit
    p13 = moves.count(13) / limit
    # return data to user
    print("Likely value      mode    {}".format(mode))
    print("Expected value    mean    {}".format(mean))
    print("Middle value      median  {}".format(median))
    print(p3, p5, p7, p9, p11, p13)

# check if this is first instance
if __name__ == "__main__":
    main()
else:
    print("Simulation is being ran indirectly")
