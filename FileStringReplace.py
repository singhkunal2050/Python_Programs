fin = open("file.txt", "rt")
fout=open("out.txt","wt")

if(not(fin) or not(fout)) :
    print('File/Files Not Opened!!') 
else :
    print('Files Opened')
    
    for line in fin :
        print(line);
        fout.write(line);
        print('Line written ')

fin.close()
fout.close()

