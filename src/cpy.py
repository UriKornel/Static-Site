import os, shutil

# src = static
# dest = public

def cpy(src, dest):
    src = os.path.abspath(src)
    dest = os.path.abspath(dest)

    print(src)
    print(dest)

    if os.path.exists(dest):
        shutil.rmtree(dest)
        os.mkdir(dest)
        print(f"created: {dest}")
    elif not os.path.exists(dest):
        os.mkdir(dest)
        print(f"created: {dest}")
    if not os.path.exists(src):
        raise ValueError(f"src path does not exist {src}")

    src_files = os.listdir(src)
    print(src_files)
    for file in src_files:
        path = os.path.join(src, file)
        print(path)
        if os.path.isdir(path):
            os.mkdir(os.path.join(dest, file))
            cpy(path, os.path.join(dest, file))
        else:
            # shutil.copy(path, os.path.join(dest, file))
            shutil.copy(path, dest)
            print(f"Copied: {path}")
