#Create a tree
def create_tree(height):
    for a, b in enumerate(range(1, height + 1)):
        spaces = ' ' * (height - b)
        stars = '*' * b
        print(f"{spaces}{stars} | {stars}")

#Set the height of the tree
tree_height = 10

#Create and print the tree
create_tree(tree_height)
