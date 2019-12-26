import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    return (file.name
            for file in os.scandir(dirname)
            if file.stat().st_size >= size_in_kb * ONE_KB)


if __name__ == '__main__':
    print(get_files('.', 1))
