st=input("Enter string:")
subst=input("Enter subtring to find:")
if subst in st:
    print(f"Yes! '{subst}' is present in '{st}'")
else:
    print(f"Oops! No '{subst}' found! Try Again...")