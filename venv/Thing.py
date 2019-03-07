class Thing:
    def __init__(self, name = "Bob", height = 5, weight = 100):
        self.name = name
        self.height = height
        self.weight = weight
        self.speed = 10

    def print_name(self):
        print("My name is {}!".format(self.name))

    def print_height(self):
        print("I am {} feet tall!".format(self.height))

    def print_weight(self):
        print("I weigh {} pounds!".format(self.weight))

    def print_speed(self):
        print("I'm going {} mph!".format(self.speed))

    def accelerate(self):
        self.speed += 5
        print("zoom zoom zoom!")

    def brake(self):
        if self.speed < 5:
            self.speed = 0
            print("full and complete stop.")
        else:
            self.speed -= 5
            print("sloooowwwww down")

if __name__ == '__main__':
    my_thing = Thing()
    print("Hey I'm a thing!")
    while True:
        action = input("What do you wanna know or do? [N]ame, [H]eight, [W]eight, "
                       "check [S]peed, [A]ccelerate, [B]rake").upper()
        if action not in "NHWSAB" or len(action) != 1:
            print("Sorry, I don't know what you mean....")
            continue
        if action == 'N':
            my_thing.print_name()
        elif action == 'H':
            my_thing.print_height()
        elif action == 'W':
            my_thing.print_weight()
        elif action == 'S':
            my_thing.print_speed()
        elif action == 'A':
            my_thing.accelerate()
        elif action == 'B':
            my_thing.brake()

