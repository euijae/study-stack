# Read from 'your_file.txt', write to 'output.txt'
def meta_tagged():
    with open("../meta-tagged-raw.txt", "r") as infile, open("../hellointerview-tagged.txt", "w") as outfile:
        for line in infile:
            line = line.strip()
            if line.startswith("Leetcode"):
                title = line.strip().split('. ')[-1]
                outfile.write(title + "\n")

def difference():
    setW = set()
    setH = set()

    # meta tagged
    with open("../meta-tagged.txt", "r") as infile:
        for line in infile:
            line = line.strip()
            setW.add(line)
    
    # hello interview tagged
    with open("../hellointerview-tagged.txt", "r") as infile, open("../intersection.txt", "w") as outfile, open("../only-hellointerview.txt", "w") as outfile1:
        for line in infile:
            line = line.strip()
            setH.add(line)

            if line in setW:
                outfile.write(line + "\n")
            else:
                outfile1.write(line + "\n")
                

meta_tagged()
difference()