
from lib_py_simple_sync.directory_list.fast_scandir import fast_scandir
from lib_py_simple_sync.directory_list.fast_scandir import fast_scandir_2
from lib_py_simple_sync.directory_list.fast_scandir import fast_scandir_3
from lib_py_simple_sync.directory_list.fast_scandir import fast_scandir_3_fully_qualified
from lib_py_simple_sync.directory_list.fast_scandir import fast_scandir_3_fully_qualified_sorted

target = 'example-target-directory'
print(f'fast_scandir({target})')
directory_list = fast_scandir(target)
for item in directory_list:
    print(item)
print()

try:
    target = 'example-target-directory/example-file.txt'
    print(f'fast_scandir({target})')
    directory_list = fast_scandir(target)
    for item in directory_list:
        print(item)
    print()
except NotADirectoryError as exception:
    print(f'caught expected exception')
    print(exception)

# target = 'example-target-directory'
# print(f'fast_scandir_3_fully_qualified({target})')
# directory_list = fast_scandir_3_fully_qualified(target)
# for item in directory_list:
#     print(item)
# print()

# target = 'example-target-directory/example-file.txt'
# print(f'fast_scandir_3_fully_qualified_sorted({target})')
# directory_list = fast_scandir_3_fully_qualified_sorted(target)
# for item in directory_list:
#     print(item)
# print()
