s=input("Enter string:")
def char_Freq(s):
    dict={}
    for i in s:
        keys=dict.keys()
        if i in keys:
            dict[i] +=1
        else:
            dict[i]=1
    return dict

print(char_Freq(s))