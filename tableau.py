MAX_CONSTANTS = 10

# Parse a formula, consult parseOutputs for return values.
def parse(fmla):
    global tokens, index
    tokens = tokenize(fmla)
    index = 0
    try:
        node = parse_FMLA()
        if index != len(tokens):
            return 0  # not a formula
        if node['type'] == 'prop':
            return 6  # proposition
        elif node['type'] == 'negation':
            if node['sub']['logic'] == 'FOL':
                return 2  # negation of FOL formula
            else:
                return 7  # negation of propositional formula
        elif node['type'] == 'binary':
            if node['logic'] == 'FOL':
                return 5  # binary connective FOL formula
            else:
                return 8  # binary connective propositional formula
        elif node['type'] == 'quantifier':
            if node['quant'] == 'A':
                return 3  # universally quantified formula
            else:
                return 4  # existentially quantified formula
        elif node['type'] == 'atom':
            return 1  # atom
        else:
            return 0  # not a formula
    except:
        return 0  # not a formula

def lhs(fmla):
    global tokens, index
    tokens = tokenize(fmla)
    index = 0
    try:
        node = parse_FMLA()
        if node['type'] == 'binary':
            return to_string(node['left'])
        else:
            return ''
    except:
        return ''

def con(fmla):
    global tokens, index
    tokens = tokenize(fmla)
    index = 0
    try:
        node = parse_FMLA()
        if node['type'] == 'binary':
            return node['conn']
        else:
            return ''
    except:
        return ''

def rhs(fmla):
    global tokens, index
    tokens = tokenize(fmla)
    index = 0
    try:
        node = parse_FMLA()
        if node['type'] == 'binary':
            return to_string(node['right'])
        else:
            return ''
    except:
        return ''

def theory(fmla):
    return {'formulas': [parse_tree(fmla)], 'constants': [], 'closed': False}

def copy_formula(formula):
    if formula is None:
        return None
    new_formula = {}
    for key, value in formula.items():
        if key in ('sub', 'left', 'right'):
            new_formula[key] = copy_formula(value)
        else:
            new_formula[key] = value
    return new_formula

def copy_branch(branch):
    return {
        'formulas': [copy_formula(f) for f in branch['formulas']],
        'constants': branch['constants'][:],
        'closed': branch['closed'],
    }

def sat(tableau):
    while tableau:
        branch = tableau.pop()
        if branch['closed']:
            continue
        while branch['formulas']:
            formula = branch['formulas'].pop(0)
            if formula.get('processed', False):
                continue
            formula['processed'] = True
            typ = formula['type']
            if typ == 'prop':
                name = formula['name']
                if name in branch:
                    continue
                elif ('~' + name) in branch:
                    branch['closed'] = True
                    break
                else:
                    branch[name] = True
            elif typ == 'negation':
                sub = formula['sub']
                if sub['type'] == 'prop':
                    name = '~' + sub['name']
                    if name in branch:
                        continue
                    elif sub['name'] in branch:
                        branch['closed'] = True
                        break
                    else:
                        branch[name] = True
                else:
                    new_formula = negate(sub)
                    branch['formulas'].insert(0, new_formula)
            elif typ == 'binary':
                conn = formula['conn']
                left = formula['left']
                right = formula['right']
                if conn == '/\\':
                    branch['formulas'].insert(0, right)
                    branch['formulas'].insert(0, left)
                elif conn == '\\/':
                    left_branch = copy_branch(branch)
                    right_branch = copy_branch(branch)
                    left_branch['formulas'].insert(0, left)
                    right_branch['formulas'].insert(0, right)
                    tableau.append(left_branch)
                    tableau.append(right_branch)
                    break
                elif conn == '=>':
                    new_formula = negate(left)
                    branch['formulas'].insert(0, right)
                    branch['formulas'].insert(0, new_formula)
            elif typ == 'quantifier':
                if formula['quant'] == 'E':
                    if len(branch['constants']) >= MAX_CONSTANTS:
                        return 2
                    new_const = 'c' + str(len(branch['constants']) + 1)
                    branch['constants'].append(new_const)
                    new_formula = substitute(formula['sub'], formula['var'], new_const)
                    branch['formulas'].insert(0, new_formula)
                elif formula['quant'] == 'A':
                    if not branch['constants']:
                        if len(branch['constants']) >= MAX_CONSTANTS:
                            return 2
                        new_const = 'c' + str(len(branch['constants']) + 1)
                        branch['constants'].append(new_const)
                    new_formulas = []
                    for const in branch['constants']:
                        new_formula = substitute(formula['sub'], formula['var'], const)
                        new_formulas.append(new_formula)
                    branch['formulas'] = new_formulas + branch['formulas']
            elif typ == 'atom':
                atom_str = to_string(formula)
                if atom_str in branch:
                    continue
                elif ('~' + atom_str) in branch:
                    branch['closed'] = True
                    break
                else:
                    branch[atom_str] = True
            else:
                continue
        if not branch['closed'] and not branch['formulas']:
            return 1  # Satisfiable
        elif not branch['closed']:
            tableau.append(branch)
    return 0  # Not satisfiable

def tokenize(s):
    s = s.replace('(', ' ( ').replace(')', ' ) ').replace('~', ' ~ ').replace('/\\', ' /\\ ').replace('\\/', ' \\/ ').replace('=>', ' => ').replace('E', 'E ').replace('A', 'A ').replace(',', ' , ')
    return s.split()

def parse_FMLA():
    global tokens, index
    if index >= len(tokens):
        raise Exception('Unexpected end')
    token = tokens[index]
    if token == '~':
        index += 1
        sub = parse_FMLA()
        return {'type': 'negation', 'sub': sub, 'logic': sub['logic']}
    elif token == 'E' or token == 'A':
        quant = token
        index += 1
        if index >= len(tokens):
            raise Exception('Expected variable')
        var = tokens[index]
        index += 1
        sub = parse_FMLA()
        return {'type': 'quantifier', 'quant': quant, 'var': var, 'sub': sub, 'logic': 'FOL'}
    elif token == '(':
        index += 1
        left = parse_FMLA()
        if index >= len(tokens):
            raise Exception('Expected connective')
        conn = tokens[index]
        if conn not in ['/\\', '\\/', '=>']:
            raise Exception('Invalid connective')
        index += 1
        right = parse_FMLA()
        if index >= len(tokens) or tokens[index] != ')':
            raise Exception('Expected )')
        index += 1
        logic = 'FOL' if left['logic'] == 'FOL' or right['logic'] == 'FOL' else 'PL'
        return {'type': 'binary', 'conn': conn, 'left': left, 'right': right, 'logic': logic}
    elif is_predicate(token):
        pred = token
        index += 1
        if index >= len(tokens) or tokens[index] != '(':
            raise Exception('Expected (')
        index += 1
        if index >= len(tokens):
            raise Exception('Expected variable')
        var1 = tokens[index]
        index += 1
        if index >= len(tokens) or tokens[index] != ',':
            raise Exception('Expected ,')
        index += 1
        if index >= len(tokens):
            raise Exception('Expected variable')
        var2 = tokens[index]
        index += 1
        if index >= len(tokens) or tokens[index] != ')':
            raise Exception('Expected )')
        index += 1
        return {'type': 'atom', 'pred': pred, 'args': [var1, var2], 'logic': 'FOL'}
    elif is_proposition(token):
        index += 1
        return {'type': 'prop', 'name': token, 'logic': 'PL'}
    else:
        raise Exception('Invalid token')

def is_predicate(token):
    return token in ['P', 'Q', 'R', 'S']

def is_proposition(token):
    return token in ['p', 'q', 'r', 's']

def to_string(node):
    if node['type'] == 'prop':
        return node['name']
    elif node['type'] == 'negation':
        return '~' + to_string(node['sub'])
    elif node['type'] == 'binary':
        return '(' + to_string(node['left']) + node['conn'] + to_string(node['right']) + ')'
    elif node['type'] == 'quantifier':
        return node['quant'] + node['var'] + to_string(node['sub'])
    elif node['type'] == 'atom':
        return node['pred'] + '(' + node['args'][0] + ',' + node['args'][1] + ')'
    else:
        return ''

def parse_tree(fmla):
    global tokens, index
    tokens = tokenize(fmla)
    index = 0
    node = parse_FMLA()
    node['processed'] = False
    return node

def negate(node):
    if node['type'] == 'negation':
        return node['sub']
    else:
        return {'type': 'negation', 'sub': node, 'logic': node['logic'], 'processed': False}

def substitute(node, var, const):
    if node['type'] == 'atom':
        args = [const if arg == var else arg for arg in node['args']]
        return {'type': 'atom', 'pred': node['pred'], 'args': args, 'logic': node['logic'], 'processed': False}
    elif node['type'] == 'negation':
        sub = substitute(node['sub'], var, const)
        return {'type': 'negation', 'sub': sub, 'logic': node['logic'], 'processed': False}
    elif node['type'] == 'binary':
        left = substitute(node['left'], var, const)
        right = substitute(node['right'], var, const)
        return {'type': 'binary', 'conn': node['conn'], 'left': left, 'right': right, 'logic': node['logic'], 'processed': False}
    elif node['type'] == 'quantifier':
        if node['var'] == var:
            return node
        else:
            sub = substitute(node['sub'], var, const)
            return {'type': 'quantifier', 'quant': node['quant'], 'var': node['var'], 'sub': sub, 'logic': node['logic'], 'processed': False}
    else:
        return node

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