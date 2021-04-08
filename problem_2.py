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
    found = []

    find_files_recursive(suffix, path, found);
    if len(found) == 0:
        return None
    return found

def find_files_recursive(suffix, path, found):
    if os.path.isdir(path):
        for item in os.listdir(path):
            find_files_recursive(suffix, os.path.join(path, item), found)
    elif os.path.isfile(path):
        (name, ext) = os.path.splitext(path) # More strict than an `endswith()` call
        if ext == suffix:
            found.append(path)

# Basic test -- make sure we find .c files in our given sample directory
print(find_files(".c", "./testdir"))
# Returns ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

# When no files are found
print(find_files("nope", "./testdir"))
# Returns None

# Absolute path rather than relative
print(find_files(".c", os.path.realpath("./testdir")))
# Returns ['/home/user/testdir/subdir1/a.c', '/home/user/testdir/subdir3/subsubdir1/b.c', '/home/user/testdir/subdir5/a.c', '/home/user/testdir/t1.c']

# Invalid directory
print(find_files(".c", "./does_not_exist"))
# Returns None

# Empty suffix
print(find_files("", "./testdir"))
# Returns ['./testdir/subdir2/.gitkeep', './testdir/subdir4/.gitkeep']

