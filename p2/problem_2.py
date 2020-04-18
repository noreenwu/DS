import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """


    if os.path.isdir(path):
        files = os.listdir(path)
        for f in files:
            fullpath = "{}/{}".format(path, f)
            if os.path.isdir(fullpath):
                find_files(suffix, fullpath)
            else:
                if fullpath.endswith(suffix):
                     print(fullpath)


print("find files ending in .c")
find_files(".c", ".")


# output should match what is found with find

# $ find . -name \*.c
# ./a.c
# ./testdir/subdir3/subsubdir1/b.c
# ./testdir/t1.c
# ./testdir/subdir5/cat.c
# ./testdir/subdir5/a.c
# ./testdir/subdir1/a.c
# ./testdir/dog.c



print("\n\nfind files ending in .py")
find_files(".py", ".")

# $ find . -name \*.py
# ./problem_2.py
# ./ex.py


print("\n\nfind files ending in .h")
find_files(".h", ".")

# $ find . -name *\.h
# ./testdir/subdir3/subsubdir1/b.h
# ./testdir/subdir5/a.h
# ./testdir/t1.h
# ./testdir/subdir1/a.h