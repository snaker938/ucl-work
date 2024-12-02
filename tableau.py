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

def parse_fmla(fmla):
    fmla = fmla.strip()
    if not fmla:
        return -1  # Empty formula

    # Handle negations
    if fmla.startswith('~'):
        sub_fmla = fmla[1:].strip()
        if sub_fmla:
            return 2  # Negation
        else:
            return -1  # Invalid formula

    # Handle universal quantifier
    if fmla.startswith('A') and len(fmla) > 1 and fmla[1].isalpha():
        var = fmla[1]
        sub_fmla = fmla[2:].strip()
        if sub_fmla:
            return 3  # Universal quantifier
        else:
            return -1  # Invalid formula

    # Handle existential quantifier
    if fmla.startswith('E') and len(fmla) > 1 and fmla[1].isalpha():
        var = fmla[1]
        sub_fmla = fmla[2:].strip()
        if sub_fmla:
            return 4  # Existential quantifier
        else:
            return -1  # Invalid formula

    # Handle binary connectives
    # Remove outer parentheses if they enclose the entire formula
    if fmla.startswith('(') and fmla.endswith(')'):
        fmla = fmla[1:-1].strip()

    # Find the main connective at the top level
    depth = 0
    for i in range(len(fmla)):
        if fmla[i] == '(':
            depth += 1
        elif fmla[i] == ')':
            depth -= 1
        elif depth == 0:
            # Look ahead for multi-character connectives
            if fmla[i:i+2] in ['/\\', '\\/', '=>']:
                conn = fmla[i:i+2]
                return 5  # Binary connective
            elif fmla[i:i+1] in ['/\\', '\\/', '=>']:
                conn = fmla[i:i+1]
                return 5  # Binary connective

    # If none of the above, it's an atom
    return 0  # Atom


def sat(tableau):
    MAX_CONSTANTS = 10
    constant_counter = 0  # To ensure unique constants

    def substitute(fmla, var, const):
        # Improved substitution function
        tokens = []
        i = 0
        while i < len(fmla):
            if fmla[i].isalpha():
                var_name = fmla[i]
                i += 1
                while i < len(fmla) and fmla[i].isalnum():
                    var_name += fmla[i]
                    i += 1
                if var_name == var:
                    tokens.append(const)
                else:
                    tokens.append(var_name)
            else:
                tokens.append(fmla[i])
                i += 1
        return ''.join(tokens)

    def simplify(f):
        f = f.strip()
        while f.startswith('~(') and f.endswith(')'):
            f = '~' + f[2:-1].strip()
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

    def has_nested_quantifiers(f):
        # Check if formula has nested quantifiers
        if len(f) < 2:
            return False
        sub_f = f[2:].strip() if f[0] in ['A', 'E'] else f
        return 'A' in sub_f or 'E' in sub_f

    stack = []
    initial_formulas = flatten(tableau)
    initial_formulas = [simplify(f) for f in initial_formulas]
    # print("Initial formulas:", initial_formulas)
    
    # Track universal formulas and their instantiations
    univ_formulas = {}  # formula -> set of constants used
    stack.append((initial_formulas, [], set(), 0))

    while stack:
        formulas, constants, processed, constants_count = stack.pop()
        # print("\nPopped from stack:")
        # print("Formulas:", formulas)
        # print("Constants:", constants)
        # print("Processed:", processed)
        # print("Constants count:", constants_count)

        formulas = formulas.copy()
        constants = constants.copy()
        processed = processed.copy()
        
        index = 0
        while index < len(formulas):
            f = simplify(formulas[index])
            # print("\nProcessing formula:", f)
            index += 1

            parsed_type = parse_fmla(f)
            # print("Parsed type:", parsed_type)

            # Special handling for nested quantifiers
            if has_nested_quantifiers(f):
                if constants_count >= MAX_CONSTANTS - 1:  # Need room for at least 2 constants
                    # print("Reached MAX_CONSTANTS with nested quantifiers remaining")
                    return 2

            if parsed_type == 3:  # Universal quantifier
                if f not in univ_formulas:
                    univ_formulas[f] = set()
                
                # If we have a nested quantifier and are close to MAX_CONSTANTS
                if has_nested_quantifiers(f) and constants_count >= MAX_CONSTANTS - 2:
                    # print("Insufficient constants remaining for nested quantifiers")
                    return 2

                # Process universal quantifier
                # print("Universal quantifier:", f)
                var = f[1]
                sub_f = f[2:].strip()
                # print("Variable:", var)
                # print("Subformula:", sub_f)

                # Vacuous quantifier handling
                if var not in sub_f:
                    # print(f"Variable {var} is not in subformula; simplifying vacuous quantifier.")
                    f = sub_f  # Replace quantifier with subformula
                    formulas[index - 1] = f  # Update current formula
                    index -= 1  # Reprocess this formula
                    continue  # Skip to next iteration

                # Try existing constants
                instantiated = False
                for c in constants:
                    if c not in univ_formulas[f]:
                        instantiated_f = simplify(substitute(sub_f, var, c))
                        if instantiated_f not in processed:
                            # print(f"Instantiating with existing constant {c}: {instantiated_f}")
                            formulas.append(instantiated_f)
                            univ_formulas[f].add(c)
                            instantiated = True

                # Create new constant if needed
                if not instantiated:
                    if constants_count >= MAX_CONSTANTS:
                        # print("Reached MAX_CONSTANTS with universal quantifier remaining")
                        return 2
                    new_const = f'c{constants_count + 1}'
                    constants.append(new_const)
                    constants_count += 1
                    # print("Introduced new constant:", new_const)
                    instantiated_f = simplify(substitute(sub_f, var, new_const))
                    # print("Adding instantiated formula:", instantiated_f)
                    formulas.append(instantiated_f)
                    univ_formulas[f].add(new_const)

                # Always re-add universal formula unless fully instantiated
                if len(univ_formulas[f]) < MAX_CONSTANTS:
                    formulas.append(f)
                    # print("Re-added universal formula for future instantiation")
                continue

            # Rest of the function
            if f in processed and parsed_type != 3:  # Don't skip universal formulas
                # print("Already processed:", f)
                continue

            if ('~' + f) in processed or ('~' + f) in formulas[index:]:
                # print("Contradiction found with formula:", f)
                break
            if f.startswith('~') and (f[1:] in processed or f[1:] in formulas[index:]):
                # print("Contradiction found with negation of formula:", f)
                break

            processed.add(f)
            # print("Processed set updated:", processed)

            if parsed_type == 0:
                # print("Assuming atom:", f)
                continue

            elif parsed_type == 2:
                # Negation handling (same as before)
                # print("Negation:", f)
                sub_f = simplify(f[1:])
                # print("Subformula after negation simplification:", sub_f)
                sub_parsed_type = parse_fmla(sub_f)
                # print("Subformula parsed type:", sub_parsed_type)
                if sub_parsed_type == 0:
                    # print("Assuming negated atom:", sub_f)
                    continue
                elif sub_parsed_type == 5:
                    lhs_f = lhs(sub_f)
                    rhs_f = rhs(sub_f)
                    conn = con(sub_f)
                    # print("Negation of binary connective:", sub_f)
                    if conn == '/\\':
                        # print("Adding branches for negation of conjunction")
                        stack.append(([simplify('~' + lhs_f)] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                        stack.append(([simplify('~' + rhs_f)] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                        break
                    elif conn == '\\/':
                        # print("Expanding negation of disjunction to conjunction of negations")
                        formulas.extend([simplify('~' + lhs_f), simplify('~' + rhs_f)])
                    elif conn == '=>':
                        # print("Expanding negation of implication to conjunction")
                        formulas.extend([lhs_f, simplify('~' + rhs_f)])

            elif parsed_type == 4:  # Existential quantifier
                var = f[1]
                sub_f = f[2:].strip()
                # print("Variable:", var)
                # print("Subformula:", sub_f)

                # Vacuous quantifier handling
                if var not in sub_f:
                    # print(f"Variable {var} is not in subformula; simplifying vacuous quantifier.")
                    f = sub_f  # Replace quantifier with subformula
                    formulas[index - 1] = f  # Update current formula
                    index -= 1
                    continue

                if constants_count >= MAX_CONSTANTS:
                    # print("Reached MAX_CONSTANTS")
                    return 2
                # Introduce a unique constant for this quantifier
                constant_counter += 1
                new_const = f'c_{var}_{constant_counter}'
                constants.append(new_const)
                constants_count += 1
                # print("Introduced new constant:", new_const)
                instantiated_f = simplify(substitute(sub_f, var, new_const))
                # print("Adding instantiated formula:", instantiated_f)
                if instantiated_f not in processed:
                    formulas.append(instantiated_f)
                continue

            elif parsed_type == 5:  # Binary connective
                # print("Binary connective:", f)
                lhs_f = lhs(f)
                rhs_f = rhs(f)
                conn = con(f)
                if conn == '/\\':
                    # print("Adding LHS and RHS to formulas")
                    formulas.extend([lhs_f, rhs_f])
                elif conn == '\\/':
                    # print("Adding branches for disjunction")
                    stack.append(([lhs_f] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                    stack.append(([rhs_f] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                    break
                elif conn == '=>':
                    # print("Adding branches for implication")
                    stack.append(([simplify('~' + lhs_f)] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                    stack.append(([rhs_f] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                    break

        else:
            # Check if we have universal quantifiers that need more constants
            for univ_f in univ_formulas:
                if len(univ_formulas[univ_f]) < MAX_CONSTANTS and has_nested_quantifiers(univ_f):
                    # print("Universal quantifier with nested quantifiers needs more constants")
                    return 2
                    
            # print("Open branch found")
            return 1

        # print("Branch closed due to contradiction")
    
    # print("All branches closed")
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