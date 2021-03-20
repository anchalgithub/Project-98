def swapFileData():
    print("This is for swapping information in 2 files.")
    fileNo1=input("Enter first file name: ")
    fileNo2=input("Enter second file name: ")

    with open(fileNo1,'r') as a:
        data_a=a.read()

    with open(fileNo2,'r') as b:
        data_b=b.read()

    with open(fileNo1,'w') as a:
        a.write(data_b)

    with open(fileNo2,'w') as b:
        b.write(data_a)

swapFileData()