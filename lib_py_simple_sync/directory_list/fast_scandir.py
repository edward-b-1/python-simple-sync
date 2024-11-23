

import os
from functools import reduce


"""Return all (relative) directory paths found in `target_dir`.
`target_dir` must be a directory. Does not work if the target
is a file.
"""
def fast_scandir(target_dir: str) -> list[str]:
    subfolders = [f.path for f in os.scandir(target_dir) if f.is_dir()]
    for target_dir in list(subfolders):
        subfolders.extend(fast_scandir(target_dir))
    return subfolders


"""Return all (relative) directory paths and (relative) file
paths in `target_dir`. Results are returned in sorted order.
`target_dir` must be a directory. Does not work if the target
is a file.
"""
def fast_scandir_2(target_dir: str) -> list[str]:
    items = []
    for f in os.scandir(target_dir):
        if f.is_dir():
            items.extend(fast_scandir_2(f.path))
        if f.is_file():
            items.append(f.path)
    items.sort()
    return items






# def _fast_scandir_3_impl(target:tuple[str, str]) -> list[tuple[str, str]]:
#     items:list[tuple[str, str]] = []
#     if os.path.isfile(target[1]):
#         item = ('f', target)
#         items.append(item)
#     elif os.path.isdir(target[1]):
#         item = ('d', target)
#         items.append(item)
#         for subtarget in os.listdir(target):
#             items.extend(_fast_scandir_3_impl(subtarget))
#     return items

# def _fast_scandir_3_fully_qualified_impl(target:tuple[str, str]) -> list[tuple[str, str]]:
#     return (
#         list(
#             map(
#                 lambda item: (item[0], os.path.abspath(item[1])),
#                 _fast_scandir_3_impl(target),
#             )
#         )
#     )

# def _fast_scandir_3_fully_qualified_sorted_impl(target:tuple[str, str]) -> list[tuple[str, str]]:
#     return sorted(_fast_scandir_3_fully_qualified_impl(target), key=lambda pair: pair[1])



