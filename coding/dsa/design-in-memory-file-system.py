"""
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem()
Initializes the object of the system.

List[str] ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should be in lexicographic order.

void mkdir(String path)
Creates a new directory at the given path.
The given directory path does not exist.
If the middle directories in the path do not exist, you should create them as well.

void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing content.
If filePath already exists, appends the new content to the original content.

String readContentFromFile(String filePath)
Returns the content of the file at filePath.

fs = FileSystem()

print(fs.ls("/"))                      # []

fs.mkdir("/a/b/c")
fs.addContentToFile("/a/b/c/d", "hello")

print(fs.ls("/"))                      # ["a"]
print(fs.readContentFromFile("/a/b/c/d"))  # "hello"
"""
class TrieNode:
    def __init__(self):
        self.path = {}
        self.content = ""
        self.is_directory = False

class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        self.root.is_directory = True

    def ls(self, path: str) -> list[str]:
        if path == '/':
            return sorted(self.root.path.keys())
            # return [] if not self.root.path else list(self.root.path.keys())
        
        dirs = path.strip("/").split("/")
        curr = self.root
        for dir in dirs:
            if dir not in curr.path:
                return [] # no matching path exist
            curr = curr.path[dir]
        if curr.is_directory:
            return sorted(curr.path.keys())
        
        return [dirs[-1]] # return a file name

    def mkdir(self, path: str) -> None:
        dirs = path.strip("/").split("/")
        curr = self.root
        for dir in dirs:
            if dir not in curr.path:
                curr.path[dir] = TrieNode()
            curr = curr.path[dir]
            curr.is_directory = True

    def addContentToFile(self, filePath: str, content: str) -> None: 
        dirs = filePath.strip("/").split("/")
        curr = self.root
        for dir in dirs:
            if dir not in curr.path:
                curr.path[dir] = TrieNode()
            curr = curr.path[dir]
        curr.content += content
        curr.is_directory = False

    def readContentFromFile(self, filePath: str) -> str:
        dirs = filePath.strip("/").split("/")
        curr = self.root
        for dir in dirs:
            if dir not in curr.path:
                return "" # file doesn't exist
            curr = curr.path[dir]
        return curr.content

def test_file_system():
    fs = FileSystem()

    # Initial empty root
    assert fs.ls("/") == []

    # mkdir with intermediate directories
    fs.mkdir("/a/b/c")
    assert fs.ls("/") == ["a"]
    assert fs.ls("/a") == ["b"]
    assert fs.ls("/a/b") == ["c"]
    assert fs.ls("/a/b/c") == []

    # # Add content to a new file
    fs.addContentToFile("/a/b/c/d", "hello")
    assert fs.ls("/a/b/c") == ["d"]
    assert fs.readContentFromFile("/a/b/c/d") == "hello"

    # # Add another file in the same dir
    fs.addContentToFile("/a/b/c/e", "world")
    assert sorted(fs.ls("/a/b/c")) == ["d", "e"]

    # # Append to an existing file
    fs.addContentToFile("/a/b/c/d", "!!!")
    assert fs.readContentFromFile("/a/b/c/d") == "hello!!!"

    # # Create and list deeper nested structure
    fs.mkdir("/x/y/z")
    fs.addContentToFile("/x/y/z/file.txt", "sample")
    assert fs.ls("/x/y") == ["z"]
    assert fs.ls("/x/y/z") == ["file.txt"]
    assert fs.ls("/x/y/z/file.txt") == ["file.txt"]
    assert fs.readContentFromFile("/x/y/z/file.txt") == "sample"

    # # Lexicographic ordering
    fs.addContentToFile("/x/y/z/aaa.txt", "alpha")
    fs.addContentToFile("/x/y/z/zzz.txt", "omega")
    assert fs.ls("/x/y/z") == ["aaa.txt", "file.txt", "zzz.txt"]

    print("All test cases passed!")

# Run the test
test_file_system()
