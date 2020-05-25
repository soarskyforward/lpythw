class Parent (object):
    def override(self):
        print("PARENT override()")

    def implict(self):
        print("PARENT implict()")

    def altered(self):
        print("PARENT altered()")

class Child (Parent):
    def override(self):
        print("ghaha")

    def altered(self):
        print("hadhfadh")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implict()
son.implict()

dad.override()
son.override()

dad.altered()
son.altered()
