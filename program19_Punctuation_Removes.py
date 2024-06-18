s=input("Enter String:")
import string
s=s.translate(str.maketrans('','',string.punctuation))
print(s)