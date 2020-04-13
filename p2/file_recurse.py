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
                find_files(".c", fullpath)
            else:
                if fullpath.endswith(".c"):
                     print(fullpath)



find_files(".c", ".")