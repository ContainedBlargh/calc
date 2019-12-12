from math import *
from numpy import array
from numpy.linalg import det, inv
from sys import argv, stdin
import re
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def main(argv):
    split = True
    if argv[1] == '-w':
        split = False
        argv.pop(1)
    if len(argv) > 1:
        expr = ' '.join(argv[1:])
    else:
        expr = "$"
    
    if '$' in expr:
        lines = []
        for line in stdin:
            lines.append(line)
        var = ''.join(lines).strip()
        if split:
            var = var.split()[0]
        expr = expr.replace('$', str(var))
    words = re.findall(r"[a-zA-Z]{2,}", expr)
    bad_words = list(filter(lambda w: w not in globals(), words))
    no_bad_words = expr
    for bad_word in bad_words:
        no_bad_words = no_bad_words.replace(bad_word, '')
    arrays = r"(\[[\[\]\(\)\d\w, ]*\])"
    np_arrays = re.sub(arrays, r"array(\1)", no_bad_words)
    try:
        result = eval(np_arrays)
        print(result)
        pass
    except SyntaxError as e:
        print("SyntaxError:", e.msg)
        pass

if __name__ == "__main__":
    main(argv)
    pass
