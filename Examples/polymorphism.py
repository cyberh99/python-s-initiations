class Animal:
    def __init__(self):

        print "It's an animal"

    def born(self):
        print "It's borning a new animal"

    def breathe(self):
        print "It's breathing"

class dog(Animal):
    def __init__(self):
        self.born()
        self.breathe()
        print "It's a dog :-) "

    def look_a_cat(self):
        print "The dog try to catch the cat"

class cat(Animal):
    def __init__(self):
        self.born()
        self.breathe()
        print "It's a cat"

    def look_a_cat(self):
        print "Tha cat fell in 'love'"

rayo = dog()
rayo.look_a_cat()
bigotes = cat()
bigotes.look_a_cat()
