import os

def analyze_inodes(path):
    inode_info = []
    for root, dirs, files in os.walk(path):
        for name in files:
            full_path = os.path.join(root, name)
            try:
                inode = os.stat(full_path).st_ino
                inode_info.append((inode, full_path))
            except Exception as e:
                print(f"Error accessing {full_path}: {e}")
    print(f"Total inodes found: {len(inode_info)}")  # Debug statement
    return inode_info