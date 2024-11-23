
from lib_py_simple_sync.directory_list.fast_scandir_4 import fast_scandir_4

(
    files,
    paths,
) = fast_scandir_4('example-target-directory')

print(files)
print(paths)
