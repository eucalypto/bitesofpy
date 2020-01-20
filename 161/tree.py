import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    files = 0
    directories = 0
    for entry in os.scandir(directory):
        if entry.is_dir():
            directories += 1
            more_directories, more_files = count_dirs_and_files(entry)
            files += more_files
            directories += more_directories
        elif entry.is_file():
            files += 1
    return directories, files


if __name__ == '__main__':
    print(count_dirs_and_files())
