from sys import stdout, stderr

class Clause:

    def __init__(self, var_indices, var_settings):
        clause_len = len(var_indices) 
        settings_len = len(var_settings)
        if clause_len != settings_len:
            stderr.write("Given {lits} literal(s) and {asgns} assignment(s);\n".format(
                lits=clause_len,
                asgns=settings_len,
            ))
            stderr.write("Assuming all unassigned variables are not negated in this clause.\n")
        self.clause_state = {}
        for vari in range(clause_len):
            if vari < clause_len:
                self.clause_state[var_indices[vari]] = bool(var_settings[vari])
            else:
                self.clause_state[var_indices[vari]] = True


    def write(self):
        stdout.write("(")
        bool_to_sym = {
                True: "+",
                False: "~",
        }
        for var_num, var_set in self.clause_state.iteritems():
            stdout.write(" {sym}X{num} ".format(
                sym=bool_to_sym[var_set],
                num=var_num,
            ))
        stdout.write(")\n")


a = Clause([1,4,5],[1,0,1])
a.write()
