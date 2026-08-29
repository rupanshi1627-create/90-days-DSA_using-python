def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)          # opening bracket -> push
        else:
            if not stack or stack[-1] != pairs[char]:
                return False             # koi opening nahi ya galat match
            stack.pop()                  # matched, so remove top
    
    return len(stack) == 0  # sab kuch match ho gaya toh stack empty hogi

# Example
print(is_valid("()[]{}"))   # True
print(is_valid("(]"))       # False
print(is_valid("([)]"))     # False (order galat hai)