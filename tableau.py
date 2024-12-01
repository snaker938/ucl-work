import filecmp

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
    MAX_CONSTANTS = 10

    def substitute(fmla, var, const):
        result = ''
        i = 0
        while i < len(fmla):
            if fmla[i] == var and (i == 0 or not fmla[i-1].isalnum()) and (i+1 == len(fmla) or not fmla[i+1].isalnum()):
                result += const
                i += 1
            else:
                result += fmla[i]
                i += 1
        return result

    def simplify(f):
        f = f.strip()
        while f.startswith('~(') and f.endswith(')'):
            f = f[1:-1].strip()
        neg_count = 0
        while f.startswith('~'):
            neg_count += 1
            f = f[1:].strip()
        if neg_count % 2 == 1:
            f = '~' + f
        return f

    def flatten(lst):
        flat_list = []
        for item in lst:
            if isinstance(item, list):
                flat_list.extend(flatten(item))
            else:
                flat_list.append(item)
        return flat_list

    stack = []
    initial_formulas = flatten(tableau)
    initial_formulas = [simplify(f) for f in initial_formulas]
    stack.append((initial_formulas, [], set(), 0))

    while stack:
        formulas, constants, processed, constants_count = stack.pop()
        formulas = formulas.copy()
        constants = constants.copy()
        processed = processed.copy()
        index = 0
        while index < len(formulas):
            f = simplify(formulas[index])
            index += 1

            if f in processed:
                continue
            processed.add(f)

            if ('~' + f) in processed or ('~' + f) in formulas[index:]:
                break
            if f.startswith('~') and f[1:] in processed:
                break

            parsed_type = parse(f)
            if parsed_type == 0:
                break

            if parsed_type in [1, 6]:
                continue

            elif parsed_type in [2, 7]:
                sub_f = simplify(f[1:])
                sub_parsed_type = parse(sub_f)
                if sub_parsed_type in [1, 6]:
                    continue
                elif sub_parsed_type in [5, 8]:
                    lhs_f = lhs(sub_f)
                    rhs_f = rhs(sub_f)
                    conn = con(sub_f)
                    if conn == '/\\':
                        stack.append(([simplify('~' + lhs_f)] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                        stack.append(([simplify('~' + rhs_f)] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                        break
                    elif conn == '\\/':
                        formulas.extend([simplify('~' + lhs_f), simplify('~' + rhs_f)])
                    elif conn == '=>':
                        formulas.extend([lhs_f, simplify('~' + rhs_f)])
                elif sub_parsed_type == 3:
                    var = sub_f[1]
                    sub_sub_f = sub_f[2:].strip()
                    new_formula = 'E' + var + '~' + sub_sub_f
                    formulas.append(simplify(new_formula))
                elif sub_parsed_type == 4:
                    var = sub_f[1]
                    sub_sub_f = sub_f[2:].strip()
                    new_formula = 'A' + var + '~' + sub_sub_f
                    formulas.append(simplify(new_formula))
                else:
                    break

            elif parsed_type in [5, 8]:
                lhs_f = lhs(f)
                rhs_f = rhs(f)
                conn = con(f)
                if conn == '/\\':
                    formulas.extend([lhs_f, rhs_f])
                elif conn == '\\/':
                    stack.append(([lhs_f] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                    stack.append(([rhs_f] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                    break
                elif conn == '=>':
                    stack.append(([simplify('~' + lhs_f)] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                    stack.append(([rhs_f] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                    break

            elif parsed_type == 3:
                var = f[1]
                sub_f = f[2:].strip()
                if not constants:
                    if constants_count >= MAX_CONSTANTS:
                        return 2
                    new_const = 'c' + str(constants_count + 1)
                    constants.append(new_const)
                    constants_count += 1
                for c in constants:
                    instantiated_f = simplify(substitute(sub_f, var, c))
                    if instantiated_f not in processed:
                        formulas.append(instantiated_f)
                formulas.append(f)

            elif parsed_type == 4:
                var = f[1]
                sub_f = f[2:].strip()
                if constants_count >= MAX_CONSTANTS:
                    return 2
                new_const = 'c' + str(constants_count + 1)
                constants.append(new_const)
                constants_count += 1
                instantiated_f = simplify(substitute(sub_f, var, new_const))
                if instantiated_f not in processed:
                    formulas.append(instantiated_f)
            else:
                continue
        else:
            if constants_count >= MAX_CONSTANTS:
                return 2
            return 1
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
            

# clear the console
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Compare the output.txt with the expected_output.txt
if filecmp.cmp('output.txt', 'expected_output.txt', shallow=False):
    print("The output matches the expected output.")
else:
    print("The output does not match the expected output.")
    # Show the differences
    with open('output.txt', 'r') as output_file:
        output_lines = output_file.readlines()
    with open('expected_output.txt', 'r') as expected_file:
        expected_lines = expected_file.readlines()
    
    for i, (output_line, expected_line) in enumerate(zip(output_lines, expected_lines)):
        if output_line != expected_line:
            # print(f"Difference at line {i+1}:")
            print(f"Output: {output_line.strip()}")
            print(f"Expected: {expected_line.strip()}")
            
    # print out the number of mismatches
    num_mismatches = sum(1 for ol, el in zip(output_lines, expected_lines) if ol != el)
    print(f"Number of mismatches: {num_mismatches}")