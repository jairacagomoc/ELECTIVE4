class ClubMembers:
    def __init__(self, name, birthday, age, favorite_food , goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def display1(self):
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("Age: ", self.age)
        print("Favorite food: ", self.favorite_food)
        print ("Goal: ", self.goal)

class ClubOfficers(ClubMembers):

    def __int__(self, name, age, birthday, favorite_food, goal, position):
        self.position = position
        ClubMembers.__init__(self, name, birthday, age, favorite_food,goal)

    def display2(self):
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("Age: ", self.age)
        print("Favorite food: ", self.favorite_food)
        print("Goal: ", self.goal)
        print("Position: ", self.position)

c_1 = ClubMembers("Tom", "January 14 ", 16, "Ice cream ", "To be happy")
c_4 = ClubMembers("Clara", "June 22", 14 , "Best stroganoff", "To be the world's greater chef")

c_1.display1()
c_4.display2()