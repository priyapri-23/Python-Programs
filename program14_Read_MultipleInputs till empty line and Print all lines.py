lines=[]
while True:
    line=input("Enter a lines (Leave empty to finish): ")
    if line:
        lines.append(line)
    else:
        break
multiline_inputs='\n'.join(lines)
print("multiline_inputs:")
print(multiline_inputs)