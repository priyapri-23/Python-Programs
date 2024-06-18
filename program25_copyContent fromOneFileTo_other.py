with open('file2.txt','r') as file1, open('myfile.txt','a') as file2:
    for line in file1:
        file2.write(line)
