MAX_CONSTANTS = 10

# Parse a formula, consult parseOutputs for return values.
def parse(fmla):
    # Remove any leading or trailing whitespace
    fmla = fmla.strip()

    # Helper functions to identify components
    propositions = {'p', 'q', 'r', 's'}
    variables = {'x', 'y', 'z', 'w'}
    predicates = {'P', 'Q', 'R', 'S'}
    connectives = {'/\\', '\\/', '=>'}
    quantifiers = {'Ax', 'Ay', 'Az', 'Aw', 'Ex', 'Ey', 'Ez', 'Ew'}

    # Function to check if string is a proposition
    def is_proposition(s):
        return s in propositions

    # Function to check if string is a variable
    def is_variable(s):
        return s in variables

    # Function to check if string is a predicate atom like P(x, y)
    def is_atom(s):
        if '(' in s and ')' in s:
            pred_part, args_part = s.split('(', 1)
            args_part = args_part[:-1]  # Remove the closing parenthesis
            args = args_part.split(',')
            if pred_part in predicates and all(is_variable(arg.strip()) for arg in args):
                return True
        return False

    # Base cases
    if is_proposition(fmla):
        return 6  # 'a proposition'

    if is_atom(fmla):
        return 1  # 'an atom'

    # Negation
    if fmla.startswith('~'):
        sub_fmla = fmla[1:]
        sub_parse = parse(sub_fmla)
        if sub_parse == 0:
            return 0  # 'not a formula'
        elif sub_parse in {1, 2, 3, 4, 5}:
            return 2  # 'a negation of a first order logic formula'
        elif sub_parse in {6, 7, 8}:
            return 7  # 'a negation of a propositional formula'
        else:
            return 0  # 'not a formula'

    # Quantifiers
    for quant in quantifiers:
        if fmla.startswith(quant):
            var = quant[1]
            sub_fmla = fmla[len(quant):]
            sub_parse = parse(sub_fmla)
            if sub_parse in {1, 2, 5}:
                if quant.startswith('A'):
                    return 3  # 'a universally quantified formula'
                else:
                    return 4  # 'an existentially quantified formula'
            else:
                return 0  # 'not a formula'

    # Binary Connectives
    if fmla.startswith('(') and fmla.endswith(')'):
        # Remove the outer parentheses
        inner_fmla = fmla[1:-1]
        # Now, we need to find the main connective
        # We can do this by scanning the formula and keeping track of parentheses
        depth = 0
        for i in range(len(inner_fmla)):
            if inner_fmla[i] == '(':
                depth += 1
            elif inner_fmla[i] == ')':
                depth -= 1
            elif depth == 0:
                # Possible connective position
                for conn in connectives:
                    if inner_fmla.startswith(conn, i):
                        lhs = inner_fmla[:i].strip()
                        rhs = inner_fmla[i+len(conn):].strip()
                        lhs_parse = parse(lhs)
                        rhs_parse = parse(rhs)
                        if lhs_parse == 0 or rhs_parse == 0:
                            return 0  # 'not a formula'
                        if lhs_parse in {6, 7, 8} and rhs_parse in {6, 7, 8}:
                            return 8  # 'a binary connective propositional formula'
                        elif lhs_parse in {1, 2, 3, 4, 5} and rhs_parse in {1, 2, 3, 4, 5}:
                            return 5  # 'a binary connective first order formula'
                        else:
                            return 0  # 'not a formula'
        return 0  # 'not a formula'

    return 0  # 'not a formula'


# Return the LHS of a binary connective formula
def lhs(fmla):
    return ''

# Return the connective symbol of a binary connective formula
def con(fmla):
    return ''

# Return the RHS symbol of a binary connective formula
def rhs(fmla):
    return ''


# You may choose to represent a theory as a set or a list
def theory(fmla):#initialise a theory with a single formula in it
    return None

#check for satisfiability
def sat(tableau):
#output 0 if not satisfiable, output 1 if satisfiable, output 2 if number of constants exceeds MAX_CONSTANTS
    return 0

#------------------------------------------------------------------------------------------------------------------------------:
#                   DO NOT MODIFY THE CODE BELOW. MODIFICATION OF THE CODE BELOW WILL RESULT IN A MARK OF 0!                   :
#------------------------------------------------------------------------------------------------------------------------------:

f = open('input.txt')

parseOutputs = ['not a formula',
                'an atom',
                'a negation of a first order logic formula',
                'a universally quantified formula',
                'an existentially quantified formula',
                'a binary connective first order formula',
                'a proposition',
                'a negation of a propositional formula',
                'a binary connective propositional formula']

satOutput = ['is not satisfiable', 'is satisfiable', 'may or may not be satisfiable']



firstline = f.readline()

PARSE = False
if 'PARSE' in firstline:
    PARSE = True

SAT = False
if 'SAT' in firstline:
    SAT = True

for line in f:
    if line[-1] == '\n':
        line = line[:-1]
    parsed = parse(line)

    if PARSE:
        output = "%s is %s." % (line, parseOutputs[parsed])
        if parsed in [5,8]:
            output += " Its left hand side is %s, its connective is %s, and its right hand side is %s." % (lhs(line), con(line) ,rhs(line))
        print(output)

    if SAT:
        if parsed:
            tableau = [theory(line)]
            print('%s %s.' % (line, satOutput[sat(tableau)]))
        else:
            print('%s is not a formula.' % line)