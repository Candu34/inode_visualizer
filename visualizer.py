import matplotlib.pyplot as plt

def plot_inodes(inode_info):
    if not inode_info:
        print("No inodes to display.")  # Debug statement
        return

    inodes = [info[0] for info in inode_info]
    paths = [info[1] for info in inode_info]

    plt.figure(figsize=(10, 6))
    plt.scatter(inodes, range(len(inodes)), marker='o')
    plt.title('Inode Allocation')
    plt.xlabel('Inode Number')
    plt.ylabel('Files')
    plt.show()
    print("Inodes plotted successfully.")  # Debug statement