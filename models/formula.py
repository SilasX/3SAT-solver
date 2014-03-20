from sys import stderr
import clause

class Formula:

    def __init__(self, clauses=[]):
        self.clauses = clauses


    def is_satisfied(self, var_stgs):
        return all([x.is_satisfied(var_stgs) for x in self.clauses])


my_clauses = [
        clause.Clause([1,4,5],[1,0,1]),
        clause.Clause([2,3],[1,1]),
]

if __name__ == "__main__":
    f1 = Formula(my_clauses)
    print f1.is_satisfied({
        1: True,
        2: True,
        3: True,
        4: True,
        5: True,
    })
    print f1.transform_with()
