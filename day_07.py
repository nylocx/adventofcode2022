#  --- Day :  ---
# %% Initialization
from anytree import Node, Resolver, RenderTree, PreOrderIter, findall

cwd = Node("root", is_dir=True)


def parse_input(line: str) -> None:
    global cwd
    r = Resolver()
    if line.startswith("$"):
        command = line[2:4]
        if command == "cd":
            _dir = line[5:]
            if _dir == "..":
                cwd = cwd.parent
            elif _dir == "/":
                cwd = cwd.root
            else:
                cwd = r.get(cwd, _dir)
        elif command == "ls":
            ...
        else:
            print("Unknown command")
    elif line.startswith("dir"):
        _dir = line[4:]
        Node(_dir, parent=cwd, is_dir=True)
    else:
        size, name = line.split()
        Node(name, parent=cwd, size=int(size), is_dir=False)


# %% Read input
with open("day_07_input.txt") as data:
    for _line in data:
        parse_input(_line.strip())
print(RenderTree(cwd.root))

# %% Part 1
acc = 0
for _dir in findall(cwd.root, filter_=lambda node: node.is_dir):
    size = sum(n.size for n in PreOrderIter(_dir, filter_=lambda node: not node.is_dir))
    if size < 100000:
        acc += size

print("Sum of all directories smaller than 100000:", acc)

# %% Part 2
free_space = 70000000 - sum(
    n.size for n in PreOrderIter(cwd.root, filter_=lambda node: not node.is_dir)
)

dir_sizes = []
for _dir in findall(cwd.root, filter_=lambda node: node.is_dir):
    dir_sizes.append(
        sum(n.size for n in PreOrderIter(_dir, filter_=lambda node: not node.is_dir))
    )

for s in sorted(dir_sizes):
    if s > (30000000 - free_space):
        print("Size of directory to delete: ", s)
        break
