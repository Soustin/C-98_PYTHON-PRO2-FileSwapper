def swapFileData():
    file1Name = input("What is the name of the files you want to swap - ")
    file2Name = input("What is the name of the files you want to swap the file with - ")
    with open(file1Name, "r") as aR:
        data_a = aR.read()
    with open(file2Name, "r") as bR:
        data_b = bR.read()
    with open(file1Name, "w") as aW:
        aW.write(data_b)
        aWrite = aW
    with open(file2Name, "w") as bW:
        bW.write(data_a)
        bWrite = bW

swapFileData()
