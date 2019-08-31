
class Fish:
    def __init__(self, first_name, last_name="Fish",
                 skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming.")


    def swim_backwards(self):
        print("The fish can swim backwards.")

class Trout(Fish):
    def __init__(self, water="freshwater"):
        self.water = water
        super().__init__(self)

class Clownfish(Fish):
    """docstring for Clownfish"""
    
    def live_with_anenome(self):
        print("The clownfish is coexisting with sea anenome.")
        


class Shark(Fish):
    """docstring for Shark"""
    def __init__(self, first_name, last_name="Shark",
                 skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")


        

# terry = Trout("Terry")
# print(terry.first_name + " " + terry.last_name)


# casey = Clownfish("Casey")
# print(casey.first_name + " " + casey.last_name)
# casey.swim()
# casey.live_with_anenome()


# sammy = Shark("Sammy")
# print(sammy.first_name + " " + sammy.last_name)
# sammy.swim()
# sammy.swim_backwards()
# print(sammy.eyelids)
# print(sammy.skeleton)

terry = Trout()
terry.first_name = "Terry"

print(terry.first_name + " " + terry.last_name)
print(terry.eyelids)
print(terry.water)


