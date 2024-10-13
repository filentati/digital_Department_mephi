def balanced(str):
    stack = []
    brackets = { ")": "(", "]": "[", "}": "{", ">": "<"}

    for char in str:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if (not stack) or brackets[char] != stack.pop():
                return False
    if not stack:
        return True
    else:
        return False
  
    

str = input()

if balanced(str):
  print("YES")
else:
  print("NO")

                                 