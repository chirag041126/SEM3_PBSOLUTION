stack=[]
pair={')':'(', ']':'[','}':'{'}
s='{()()'
for ch in s:
    if ch in '({[':
        stack.append(ch)
    elif ch in ')}]':
        if len(stack)==0 or stack[-1]!=pair[ch]:
            print("Invalid")
            break
        else:
            stack.pop()
    else:
        continue
else:
    if len(stack)==0:
        print("Valid")
    else:
        print("Invalid") 