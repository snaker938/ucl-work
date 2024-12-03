MAX_CONSTANTS = 10


def parse(fmla):
    """
    Parses a logical formula and returns an integer code representing its type.

    Return codes:
        0: Not a formula
        1: Atom (First-order logic)
        2: Negation of a first-order logic formula
        3: Universally quantified formula
        4: Existentially quantified formula
        5: Binary connective first-order formula
        6: Proposition (Propositional logic)
        7: Negation of a propositional formula
        8: Binary connective propositional formula
    """
    fmla = fmla.strip()

    # Define allowed symbols
    propositions = {'p', 'q', 'r', 's'}
    variables = {'x', 'y', 'z', 'w'}
    predicates = {'P', 'Q', 'R', 'S'}
    connectives = {'/\\', '\\/', '=>'}
    quantifiers = {'A', 'E'}

    # Helper functions
    def is_proposition(s):
        """Check if s is a propositional variable."""
        return s in propositions

    def is_variable(s):
        """Check if s is a variable."""
        return s in variables

    def is_atom(s):
        """Check if s is an atomic first-order formula (predicate with variables)."""
        if '(' in s and s.endswith(')'):
            pred_part, args_part = s.split('(', 1)
            args_part = args_part[:-1]  # Remove the closing parenthesis
            args = args_part.split(',')
            if pred_part in predicates and all(is_variable(arg.strip()) for arg in args):
                return True
        return False

    def split_binary(fmla):
        """Split formula into lhs, connective, and rhs if it has a top-level binary connective."""
        depth = 0
        i = 0
        while i < len(fmla):
            c = fmla[i]
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth < 0:
                    return None, None, None  # Unmatched closing parenthesis
            elif depth == 0:
                for conn in connectives:
                    if fmla.startswith(conn, i):
                        lhs = fmla[:i].strip()
                        rhs = fmla[i + len(conn):].strip()
                        return lhs, conn, rhs
            i += 1
        if depth != 0:
            return None, None, None  # Unmatched opening parenthesis
        return None, None, None

    # Handle formulas with parentheses
    if fmla.startswith('(') and fmla.endswith(')'):
        inner_fmla = fmla[1:-1].strip()
        lhs, conn, rhs = split_binary(inner_fmla)
        if conn:
            lhs_parse = parse(lhs)
            rhs_parse = parse(rhs)
            if lhs_parse == 0 or rhs_parse == 0:
                return 0  # Not a formula
            if lhs_parse > 5 and rhs_parse > 5:
                return 8  # Binary connective propositional formula
            elif lhs_parse <= 5 and rhs_parse <= 5:
                return 5  # Binary connective first-order formula
            else:
                return 0  # Not a formula
        else:
            return parse(inner_fmla)

    # Check for propositional variable
    if is_proposition(fmla):
        return 6  # Proposition

    # Check for first-order atom
    if is_atom(fmla):
        return 1  # Atom

    # Handle negation
    if fmla.startswith('~'):
        sub_fmla = fmla[1:].strip()
        sub_parse = parse(sub_fmla)
        if sub_parse == 0:
            return 0
        elif sub_parse <= 5:
            return 2  # Negation of first-order logic formula
        elif sub_parse >= 6:
            return 7  # Negation of propositional formula

    # Handle quantifiers
    if len(fmla) >= 2 and fmla[0] in quantifiers and fmla[1] in variables:
        idx = 2
        while idx < len(fmla) and fmla[idx].isspace():
            idx += 1
        sub_fmla = fmla[idx:]
        sub_parse = parse(sub_fmla)
        if sub_parse and sub_parse <= 5:
            return 3 if fmla[0] == 'A' else 4
        else:
            return 0

    # Check for binary connectives at the top level
    lhs, conn, rhs = split_binary(fmla)
    if conn:
        lhs_parse = parse(lhs)
        rhs_parse = parse(rhs)
        if lhs_parse == 0 or rhs_parse == 0:
            return 0
        if lhs_parse > 5 and rhs_parse > 5:
            return 8
        elif lhs_parse <= 5 and rhs_parse <= 5:
            return 5
        else:
            return 0

    # Not a valid formula
    return 0

def split_binary(fmla):
    """
    Splits a logical formula into its left-hand side (lhs), connective symbol, and right-hand side (rhs)
    if it contains a top-level binary connective.

    Parameters:
        fmla (str): The logical formula as a string.

    Returns:
        tuple: (lhs, connective, rhs) if a top-level binary connective is found,
               otherwise (None, None, None).
    """
    fmla = fmla.strip()
    connectives = ['/\\', '\\/', '=>']

    # Remove outermost parentheses if they enclose the entire formula
    if fmla.startswith('(') and fmla.endswith(')'):
        # Check if the outer parentheses enclose the entire formula
        depth = 0
        for i, c in enumerate(fmla):
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            if depth == 0 and i < len(fmla) - 1:
                break
        else:
            # Parentheses enclose the entire formula
            fmla = fmla[1:-1].strip()

    depth = 0
    i = 0
    while i < len(fmla):
        c = fmla[i]
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth < 0:
                # Unmatched closing parenthesis
                return None, None, None
        elif depth == 0:
            # Check for connectives at the current position
            for conn in connectives:
                if fmla.startswith(conn, i):
                    lhs = fmla[:i].strip()
                    rhs = fmla[i + len(conn):].strip()
                    return lhs, conn, rhs
        i += 1

    if depth != 0:
        # Unmatched opening parenthesis
        return None, None, None

    # No top-level binary connective found
    return None, None, None

def lhs(fmla):
    """
    Returns the left-hand side of a binary connective formula.

    Parameters:
        fmla (str): The logical formula as a string.

    Returns:
        str: The left-hand side formula, or None if not applicable.
    """
    left, _, _ = split_binary(fmla)
    return left

def con(fmla):
    """
    Returns the connective symbol of a binary connective formula.

    Parameters:
        fmla (str): The logical formula as a string.

    Returns:
        str: The connective symbol, or None if not applicable.
    """
    _, connective, _ = split_binary(fmla)
    return connective

def rhs(fmla):
    """
    Returns the right-hand side of a binary connective formula.

    Parameters:
        fmla (str): The logical formula as a string.

    Returns:
        str: The right-hand side formula, or None if not applicable.
    """
    _, _, right = split_binary(fmla)
    return right

def theory(fmla):
    """
    Constructs a theory from a given formula.

    Parameters:
        fmla (str): The logical formula as a string.

    Returns:
        list: A list containing the formula.
    """
    return [fmla]

def sat(tableau):
    """
    Determines the satisfiability of a logical formula using the tableau method.

    Parameters:
        tableau (list): A list containing the initial formula(s).

    Returns:
        int: 1 if the formula is satisfiable,
             0 if the formula is not satisfiable,
             2 if the satisfiability is indeterminate due to resource limits.
    """

    def parse_fmla(fmla):
        """
        Parses a logical formula and returns a code representing its type.

        Return codes:
            -1: Invalid formula
             0: Atom
             2: Negation
             3: Universal quantifier
             4: Existential quantifier
             5: Binary connective
        """
        fmla = fmla.strip()
        if not fmla:
            return -1  # Invalid (empty) formula

        # Handle negation
        if fmla.startswith('~'):
            sub_fmla = fmla[1:].strip()
            if sub_fmla:
                return 2  # Negation
            else:
                return -1  # Invalid formula

        # Handle universal quantifier
        if fmla.startswith('A') and len(fmla) > 1 and fmla[1].isalpha():
            sub_fmla = fmla[2:].strip()
            if sub_fmla:
                return 3  # Universal quantifier
            else:
                return -1  # Invalid formula

        # Handle existential quantifier
        if fmla.startswith('E') and len(fmla) > 1 and fmla[1].isalpha():
            sub_fmla = fmla[2:].strip()
            if sub_fmla:
                return 4  # Existential quantifier
            else:
                return -1  # Invalid formula

        # Handle binary connectives
        if fmla.startswith('(') and fmla.endswith(')'):
            # Remove outer parentheses if they enclose the entire formula
            depth = 0
            balanced = True
            for c in fmla:
                if c == '(':
                    depth += 1
                elif c == ')':
                    depth -= 1
                    if depth < 0:
                        balanced = False
                        break
            if balanced and depth == 0:
                fmla = fmla[1:-1].strip()

        # Check for main connective at the top level
        depth = 0
        i = 0
        while i < len(fmla):
            c = fmla[i]
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth < 0:
                    return -1  # Unbalanced parentheses
            elif depth == 0:
                # Check for binary connectives
                for conn in ['/\\', '\\/', '=>']:
                    if fmla.startswith(conn, i):
                        return 5  # Binary connective
            i += 1

        # If none of the above, it's an atom
        return 0  # Atom

    def substitute(fmla, var, const):
        """
        Substitutes all occurrences of a variable with a constant in the formula.

        Parameters:
            fmla (str): The formula.
            var (str): The variable to replace.
            const (str): The constant to replace with.

        Returns:
            str: The formula with substitutions made.
        """
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
        """
        Simplifies a formula by removing unnecessary negations and parentheses.

        Parameters:
            f (str): The formula.

        Returns:
            str: The simplified formula.
        """
        f = f.strip()
        # Remove negations over parentheses
        while f.startswith('~(') and f.endswith(')'):
            f = '~' + f[2:-1].strip()
        # Simplify multiple negations
        neg_count = 0
        while f.startswith('~'):
            neg_count += 1
            f = f[1:].strip()
        if neg_count % 2 == 1:
            f = '~' + f
        return f

    def flatten(lst):
        """
        Flattens a nested list into a single list.

        Parameters:
            lst (list): The nested list.

        Returns:
            list: The flattened list.
        """
        flat_list = []
        for item in lst:
            if isinstance(item, list):
                flat_list.extend(flatten(item))
            else:
                flat_list.append(item)
        return flat_list

    def has_nested_quantifiers(f):
        """
        Checks if a formula contains nested quantifiers.

        Parameters:
            f (str): The formula.

        Returns:
            bool: True if nested quantifiers are present, False otherwise.
        """
        if len(f) < 2:
            return False
        sub_f = f[2:].strip() if f[0] in ['A', 'E'] else f
        return 'A' in sub_f or 'E' in sub_f

    # Initialize the tableau stack and processing variables
    stack = []
    initial_formulas = flatten(tableau)
    initial_formulas = [simplify(f) for f in initial_formulas]

    univ_formulas = {}  # Tracks universal formulas and their constants
    stack.append((initial_formulas, [], set(), 0))  # (formulas, constants, processed, constants_count)

    while stack:
        formulas, constants, processed, constants_count = stack.pop()

        # Copy to prevent side effects
        formulas = formulas.copy()
        constants = constants.copy()
        processed = processed.copy()

        index = 0
        while index < len(formulas):
            f = simplify(formulas[index])
            index += 1

            parsed_type = parse_fmla(f)

            # If nested quantifiers, check for termination
            if has_nested_quantifiers(f) and constants_count >= MAX_CONSTANTS - 1:
                return 2  # Indeterminate due to resource limitations

            if parsed_type == 3:  # Universal quantifier
                if f not in univ_formulas:
                    univ_formulas[f] = set()

                # If nested quantifiers, check for termination
                if has_nested_quantifiers(f) and constants_count >= MAX_CONSTANTS - 2:
                    return 2

                var = f[1]
                sub_f = f[2:].strip()

                # Handle vacuous quantifiers (variables that do not appear in the subformula)
                if var not in sub_f:
                    f = sub_f  # Remove the quantifier since it's vacuous
                    formulas[index - 1] = f  # Replace the formula in the list
                    index -= 1  # Adjust index to reprocess the simplified formula
                    continue  # Move to the next iteration

                instantiated = False  # Flag to check if we've instantiated the formula
                for c in constants:
                    if c not in univ_formulas[f]:
                        # Substitute the variable with an existing constant
                        instantiated_f = simplify(substitute(sub_f, var, c))
                        if instantiated_f not in processed:
                            formulas.append(instantiated_f)  # Add the instantiated formula for processing
                            univ_formulas[f].add(c)  # Record that this constant has been used
                            instantiated = True  # Mark that instantiation has occurred

                if not instantiated:
                    # Introduce a new constant if no instantiation occurred
                    if constants_count >= MAX_CONSTANTS:
                        return 2  # Indeterminate due to resource limitations
                    constants_count += 1
                    new_const = f'c{constants_count}'  # Generate a new constant
                    constants.append(new_const)  # Add it to the list of constants
                    # Substitute the variable with the new constant
                    instantiated_f = simplify(substitute(sub_f, var, new_const))
                    formulas.append(instantiated_f)  # Add the instantiated formula for processing
                    univ_formulas[f].add(new_const)  # Record that this constant has been used

                if len(univ_formulas[f]) < MAX_CONSTANTS:
                    # Re-add the universal formula for further instantiation if needed
                    formulas.append(f)
                continue  # Proceed to the next formula

            # Skip already processed formulas except universals
            if f in processed and parsed_type != 3:
                continue

            # Check for contradictions
            if ('~' + f) in processed or ('~' + f) in formulas[index:]:
                break  # Contradiction found
            if f.startswith('~') and (f[1:] in processed or f[1:] in formulas[index:]):
                break  # Contradiction found

            processed.add(f)

            if parsed_type == 0:  # Atom
                continue

            elif parsed_type == 2:  # Negation
                sub_f = simplify(f[1:])
                sub_parsed_type = parse_fmla(sub_f)

                if sub_parsed_type == 0:
                    continue  # Negated atom, nothing to decompose
                elif sub_parsed_type == 5:
                    # De Morgan's laws for negation of binary connectives
                    lhs_f = lhs(sub_f)
                    rhs_f = rhs(sub_f)
                    conn = con(sub_f)
                    if conn == '/\\':
                        # Negation of conjunction splits into two branches
                        stack.append(([simplify('~' + lhs_f)] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                        stack.append(([simplify('~' + rhs_f)] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                        break
                    elif conn == '\\/':
                        # Negation of disjunction adds both negated parts
                        formulas.extend([simplify('~' + lhs_f), simplify('~' + rhs_f)])
                    elif conn == '=>':
                        # Negation of implication becomes antecedent and negated consequent
                        formulas.extend([lhs_f, simplify('~' + rhs_f)])

            elif parsed_type == 4:  # Existential quantifier
                var = f[1]
                sub_f = f[2:].strip()

                # Handle vacuous quantifiers
                if var not in sub_f:
                    f = sub_f
                    formulas[index - 1] = f
                    index -= 1
                    continue

                if constants_count >= MAX_CONSTANTS:
                    return 2

                constants_count += 1
                new_const = f'c_{var}_{constants_count}'
                constants.append(new_const)
                instantiated_f = simplify(substitute(sub_f, var, new_const))
                if instantiated_f not in processed:
                    formulas.append(instantiated_f)
                continue

            elif parsed_type == 5:  # Binary connective
                lhs_f = lhs(f)
                rhs_f = rhs(f)
                conn = con(f)
                if conn == '/\\':
                    # Conjunction adds both parts
                    formulas.extend([lhs_f, rhs_f])
                elif conn == '\\/':
                    # Disjunction splits into two branches
                    stack.append(([lhs_f] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                    stack.append(([rhs_f] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                    break
                elif conn == '=>':
                    # Implication splits into two branches with negation
                    stack.append(([simplify('~' + lhs_f)] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                    stack.append(([rhs_f] + formulas[index:], constants.copy(), processed.copy(), constants_count))
                    break

        else:
            # Open branch found; satisfiable
            return 1

    # All branches closed; unsatisfiable
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