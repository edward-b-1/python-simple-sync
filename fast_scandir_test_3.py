
from lib_py_simple_sync.directory_list.fast_scandir_3 import fast_scandir_3
from lib_py_simple_sync.directory_list.fast_scandir_3 import _fast_scandir_3_impl_get_paths_recursive

# target = 'example-target-directory'
# print(f'running _fast_scandir_3_impl_get_paths_recursive({target})')
# directory_list = _fast_scandir_3_impl_get_paths_recursive(target)
# print(f'results:')
# for item in directory_list:
#     print(item)
# print()


target = 'example-target-directory'
print(f'running fast_scandir_3({target})')
directory_list = fast_scandir_3(target)
print(f'results:')
for item in directory_list:
    print(item)
print()