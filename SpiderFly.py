# import the required modules
import random

# spider object
class spider:
    # init function
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # move function
    def move(self):
        # choose either 1, 2 or 3
        choice = random.randrange(1, 4)
        # x clockwise
        if choice == 1:
            self.x += 1
            if self.x == 5:
                self.x = 1
        # x anti-clockwise
        elif choice == 2:
            self.x -= 1
            if self.x == 0:
                self.x = 4
        # y up/down
        elif choice == 3:
            self.y += 1
            if self.y == 2:
                self.y = 0
                
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
    counter = 0
    total = 0
    limit = int(input("Enter the number of simulations: "))
    # program loop
    while counter < limit:
        # set up objects
        s = spider(2, 1)
        f = fly(4, 0)
        # process a simulation
        num = run(s, f)
        # change variables
        counter += 1
        total += num
    # return data to user
    print("Number of simulations: {}".format(counter))
    print("Number of moves: {}".format(total))
    print("Expected number of moves: {}".format(total / counter))

# check if this is first instance
if __name__ == "__main__":
    main()
else:
    print("Simulation is being ran indirectly")