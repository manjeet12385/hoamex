with open(r'c:\Users\Divyanshi123456\Music\hoamex\common.js', 'r', encoding='utf-8') as f:
    c = f.read()
import re
c = re.sub(r'//.*', '', c)
c = re.sub(r'/\*.*?\*/', '', c, flags=re.DOTALL)
c = re.sub(r'"(?:\\.|[^\\"])*"', '""', c)
c = re.sub(r"'(?:\\.|[^\\'])*'", "''", c)
c = re.sub(r'`(?:\\.|[^\\`])*`', '``', c)
open_braces = c.count('{')
close_braces = c.count('}')
open_parens = c.count('(')
close_parens = c.count(')')
print(f'Braces: {open_braces} - {close_braces}')
print(f'Parens: {open_parens} - {close_parens}')

stack = []
for i, char in enumerate(c):
    if char == '{':
        stack.append(i)
    elif char == '}':
        if stack:
            stack.pop()
        else:
            print(f'Extra close brace at {i}')
if stack:
    print(f'Unclosed brace at {stack[-1]}')
