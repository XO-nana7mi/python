def check(string):
    a = '({['
    b = ')]}'
    match = {'}':'{',']':'[',')':'('}
    stack = []
    for char in string:
        if char in a:
            stack.append(char)
        if char in b:
            if stack == []:
                return False
            else:
                if match[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
    
    
    return stack == []
string1='()'
print(check(string1))


