

import os


def fast_scandir_2(dirname: str) -> list[str]:
    files = []
    for f in os.scandir(dirname):
        if f.is_dir():
            files.extend(fast_scandir_2(f.path))
        if f.is_file():
            files.append(f.path)
    files.sort()
    return files

