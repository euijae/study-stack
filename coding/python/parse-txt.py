with open("../file/example.txt", newline="") as f:
    data1 = f.read()
    data2 = f.readlines() # load the file all at once - good if you need all of them and a random access
    # iterate line by line
    for line in f:
        print(line, end="")