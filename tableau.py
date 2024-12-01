MAX_CONSTANTS = 10

# Parse a formula, consult parseOutputs for return values.
def parse(fmla):
    fmla = fmla.strip()
    
    # Helper components
    propositions = {'p', 'q', 'r', 's'}
    variables = {'x', 'y', 'z', 'w'}
    predicates = {'P', 'Q', 'R', 'S'}
    connectives = {'/\\', '\\/', '=>'}
    quantifiers = {'A', 'E'}
    
    # Helper functions
    def is_proposition(s):
        return s in propositions
    
    def is_variable(s):
        return s in variables
    
    def is_atom(s):
        if '(' in s and s.endswith(')'):
            pred_part, args_part = s.split('(', 1)
            args_part = args_part[:-1]  # Remove the closing parenthesis
            args = args_part.split(',')
            if pred_part in predicates and all(is_variable(arg.strip()) for arg in args):
                return True
        return False
    
    def split_binary(fmla):
        depth = 0
        i = 0
        while i < len(fmla):
            c = fmla[i]
            if c == '(':
                depth += 1
                i += 1
            elif c == ')':
                depth -= 1
                i += 1
            elif depth == 0:
                # Check for connectives starting at this position
                for conn in connectives:
                    if fmla.startswith(conn, i):
                        lhs = fmla[:i].strip()
                        rhs = fmla[i+len(conn):].strip()
                        return lhs, conn, rhs
                i += 1
            else:
                i += 1
        return None, None, None
    
    # Base cases
    # Handle parentheses around formulas
    if fmla.startswith('(') and fmla.endswith(')'):
        inner_fmla = fmla[1:-1].strip()
        # Attempt to parse as binary connective
        lhs, conn, rhs = split_binary(inner_fmla)
        if conn:
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
        else:
            # No main connective found, parse inner formula
            return parse(inner_fmla)
    
    if is_proposition(fmla):
        return 6  # 'a proposition'
    
    if is_atom(fmla):
        return 1  # 'an atom'
    
    # Negation
    if fmla.startswith('~'):
        sub_fmla = fmla[1:].strip()
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
    idx = 0
    quantifier_sequence = ''
    while idx < len(fmla) - 1:
        if fmla[idx] in quantifiers and fmla[idx + 1] in variables:
            quantifier_sequence += fmla[idx] + fmla[idx + 1]
            idx += 2
            # Skip any whitespace
            while idx < len(fmla) and fmla[idx].isspace():
                idx += 1
        else:
            break
    if quantifier_sequence:
        sub_fmla = fmla[idx:]
        sub_parse = parse(sub_fmla)
        if sub_parse in {1, 2, 3, 4, 5}:
            first_quant = quantifier_sequence[0]  # Use the first quantifier
            if first_quant == 'A':
                return 3  # 'a universally quantified formula'
            else:
                return 4  # 'an existentially quantified formula'
        else:
            return 0  # 'not a formula'
    
    # Binary Connectives
    lhs, conn, rhs = split_binary(fmla)
    if conn:
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
    
    # If none of the above, it's not a formula
    return 0  # 'not a formula'

# Helper function to split a binary connective formula into its components
def split_binary(fmla):
    fmla = fmla.strip()
    # Remove outermost parentheses if they enclose the entire formula
    if fmla.startswith('(') and fmla.endswith(')'):
        fmla = fmla[1:-1].strip()
    depth = 0
    i = 0
    connectives = ['/\\', '\\/', '=>']
    while i < len(fmla):
        c = fmla[i]
        if c == '(':
            depth += 1
            i += 1
        elif c == ')':
            depth -= 1
            i += 1
        elif depth == 0:
            # Check for connectives starting at this position
            for conn in connectives:
                conn_len = len(conn)
                if fmla.startswith(conn, i):
                    lhs = fmla[:i].strip()
                    conn_symbol = conn
                    rhs = fmla[i+conn_len:].strip()
                    return lhs, conn_symbol, rhs
            i += 1
        else:
            i += 1
    return '', '', ''

# Return the LHS of a binary connective formula
def lhs(fmla):
    left, _, _ = split_binary(fmla)
    return left

# Return the connective symbol of a binary connective formula
def con(fmla):
    _, connective, _ = split_binary(fmla)
    return connective

# Return the RHS of a binary connective formula
def rhs(fmla):
    _, _, right = split_binary(fmla)
    return right

def theory(fmla):
    return [fmla]

def sat(tableau):
    # Output 0 if not satisfiable, 1 if satisfiable, 2 if constants exceed MAX_CONSTANTS
    constants = []
    processed = set()  # Track processed formulas
    
    # Helper function to substitute variable with constant
    def substitute(fmla, var, const):
        return fmla.replace(var, const)
    
    # Flatten the formulas list
    def flatten_formulas(lst):
        flat_list = []
        for item in lst:
            if isinstance(item, list):
                flat_list.extend(flatten_formulas(item))
            else:
                flat_list.append(item)
        return flat_list

    formulas = flatten_formulas(tableau.copy())  # Ensure formulas is a flat list of strings

    while formulas:
        f = formulas.pop(0)
        if f in processed:
            continue
        processed.add(f)

        # Check for closure
        if ('~' + f) in processed or ('~' + f) in formulas:
            return 0  # Not satisfiable
        if f.startswith('~') and f[1:] in processed:
            return 0  # Not satisfiable

        # Expand the formula
        parsed_type = parse(f)
        if parsed_type in [1, 6]:  # Atom or proposition
            continue  # Nothing to expand
        elif parsed_type in [2, 7]:  # Negation
            sub_f = f[1:].strip()
            sub_parsed_type = parse(sub_f)
            if sub_parsed_type == 0:
                return 0  # Not a formula
            if sub_parsed_type in [1, 6]:  # Negation of an atom or proposition
                continue  # Can't expand further
            else:
                # Apply De Morgan's laws or quantifier negation
                if sub_parsed_type in [5, 8]:  # Binary connective
                    lhs_f = lhs(sub_f)
                    rhs_f = rhs(sub_f)
                    conn = con(sub_f)
                    if conn == '/\\':
                        # Negation of conjunction becomes disjunction of negations
                        formulas.insert(0, '~' + lhs_f)
                        formulas.insert(0, '~' + rhs_f)
                    elif conn == '\\/':
                        # Negation of disjunction becomes conjunction of negations
                        formulas.append('~' + lhs_f)
                        formulas.append('~' + rhs_f)
                    elif conn == '=>':
                        # Negation of implication
                        formulas.insert(0, sub_f.lstrip('(').rstrip(')'))
                    else:
                        return 0  # Not satisfiable
                elif sub_parsed_type == 3:  # Negation of universal quantifier
                    var = sub_f[1]
                    sub_sub_f = sub_f[2:].strip()
                    new_formula = 'E' + var + '~' + sub_sub_f
                    formulas.insert(0, new_formula)
                elif sub_parsed_type == 4:  # Negation of existential quantifier
                    var = sub_f[1]
                    sub_sub_f = sub_f[2:].strip()
                    new_formula = 'A' + var + '~' + sub_sub_f
                    formulas.insert(0, new_formula)
                else:
                    return 0  # Not satisfiable
        elif parsed_type in [5, 8]:  # Binary connective
            lhs_f = lhs(f)
            rhs_f = rhs(f)
            conn = con(f)
            if conn == '/\\':
                # Conjunction: add both
                formulas.insert(0, lhs_f)
                formulas.insert(0, rhs_f)
            elif conn == '\\/':
                # Disjunction: process alternatives
                # Backup current state
                backup_formulas = formulas.copy()
                backup_processed = processed.copy()
                # Try left side
                formulas.insert(0, lhs_f)
                result = sat([formulas])
                if result == 1:
                    return 1  # Satisfiable
                # Restore state and try right side
                formulas = backup_formulas
                processed = backup_processed
                formulas.insert(0, rhs_f)
                result = sat([formulas])
                if result == 1:
                    return 1  # Satisfiable
                return 0  # Not satisfiable
            elif conn == '=>':
                # Implication: convert to disjunction
                formulas.insert(0, '~' + lhs_f)
                formulas.insert(0, rhs_f)
            else:
                return 0  # Not satisfiable
        elif parsed_type == 3:  # Universal quantifier
            var = f[1]
            sub_f = f[2:].strip()
            # For each existing constant, substitute and add
            if not constants:
                if len(constants) >= MAX_CONSTANTS:
                    return 2  # Exceeds MAX_CONSTANTS
                new_const = 'c' + str(len(constants) + 1)
                constants.append(new_const)
            for c in constants:
                instantiated_f = substitute(sub_f, var, c)
                if instantiated_f not in processed:
                    formulas.insert(0, instantiated_f)
        elif parsed_type == 4:  # Existential quantifier
            var = f[1]
            sub_f = f[2:].strip()
            # Introduce a new constant
            if len(constants) >= MAX_CONSTANTS:
                return 2  # Exceeds MAX_CONSTANTS
            new_const = 'c' + str(len(constants) + 1)
            constants.append(new_const)
            instantiated_f = substitute(sub_f, var, new_const)
            formulas.insert(0, instantiated_f)
        else:
            continue  # Can't expand further

    return 1  # Satisfiable



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
            