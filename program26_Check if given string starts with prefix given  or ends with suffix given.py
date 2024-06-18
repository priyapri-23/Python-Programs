s=input("Enter string:")
prefix=input("Enter prefix:")
suffix=input("Enter suffix: ")
def starts_with(s, prefix):
    if len(prefix) > len(s):
        return False
    return s[:len(prefix)] == prefix

def ends_with(s, suffix):
    if len(suffix) > len(s):
        return False
    return s[-len(suffix):] == suffix

if starts_with(s, prefix):
    print(f"The string starts with '{prefix}'")
else:
    print(f"The string does not start with '{prefix}'")

if ends_with(s, suffix):
    print(f"The string ends with '{suffix}'")
else:
    print(f"The string does not end with '{suffix}'")
