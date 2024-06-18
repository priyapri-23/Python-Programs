s1=input("Enter string 1:")
s2=input("Enter string 2:")
def check_Anagrams(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("Strings are Anagrams")
    else:
        print("Strings are not Anagrams")

check_Anagrams(s1,s2)