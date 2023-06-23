# print("Hello sangram")
class A:
    def __init__(self, a, b, c):
        self.__a = a  # private member
        self._b = b  # protected member
        self.c = c  # public member

    def display(self):
        print("Values in class A:")
        print("a:", self.__a)
        print("b:", self._b)
        print("c:", self.c)


class B(A):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)  # Initialize base class A
        self.d = d

    def display(self):
        print("Values in class B:")
        print("a:", self._A__a)  # Access private member of class A using name mangling
        print("b:", self._b)
        print("c:", self.c)
        print("d:", self.d)


# Test the classes
try:
    a_obj = A(1, 2, 3)
    a_obj.display()

    b_obj = B(4, 5, 6, 7)
    b_obj.display()

except AttributeError as e:
    print("Error: Private member access attempted.")
#     Values in class A:
# a: 1
# b: 2
# c: 3
# Values in class B:
# a: 4
# b: 5
# c: 6
# d: 7
   