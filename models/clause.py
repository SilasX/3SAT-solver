from sys import exit, stdout, stderr

class Clause:

    def __init__(self, var_indices, lit_settings):
        clause_len = len(var_indices) 
        settings_len = len(lit_settings)
        if clause_len != settings_len:
            stderr.write("Given {lits} literal(s) and {asgns} assignment(s);\n".format(
                lits=clause_len,
                asgns=settings_len,
            ))
            stderr.write("Assuming all unassigned variables are not negated in this clause.\n")
        self.clause_state = {}
        for vari in range(clause_len):
            if vari < clause_len:
                self.clause_state[var_indices[vari]] = bool(lit_settings[vari])
            else:
                self.clause_state[var_indices[vari]] = True

    def as_text(self):
        output = "("
        bool_to_sym = {
                True: "",
                False: "~",
        }
        output += " ".join(["{sym}X{num}".format(
                sym=bool_to_sym[lit_set],
                num=var_num,
        ) for var_num, lit_set in self.clause_state.iteritems()])
        output += ")"
        return output

    def show_vars_used(self):
        print ' '.join([str(x) for x in self.clause_state])

    def is_satisfied(self, var_stgs):
        """Input: var_stgs, a dict mapping vars to truth assignments;\nkeys should match variable indices stored in clause; all unassigned vars are assumed true
        """
        for var_num, lit_set in self.clause_state.iteritems():
            if var_num not in var_stgs:
                stderr.write("WARNING: Variable {num} not assigned; assuming it is set to True.\n".format(num=var_num))
                if lit_set == True:
                    return True
            else:
                if lit_set == var_stgs[var_num]:
                    return True
        return False

if __name__ == "__main__":
    a = Clause([1,4,5],[1,0,1])
    a.write()
    print a.is_satisfied({1:True,4:False})
    print a.is_satisfied({1:False,4:True,})
    a.show_vars_used()
