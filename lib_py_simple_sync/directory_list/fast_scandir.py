

import os

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


def _fast_scandir_3_impl_get_paths_recursive(target: str) -> list[str]:
    items:list[str] = []
    if os.path.isfile(target):
        items.append(target)
    elif os.path.isdir(target):
        items.append(target)
        # joined_items = list(
        #         map(
        #             lambda item: os.path.join(target, item),
        #             os.listdir(target),
        #         )
        # )
        # print('joined_items')
        # print(joined_items)
        # items.extend(
        #     map(
        #         _fast_scandir_3_impl_get_paths_recursive,
        #         joined_items
        #     )
        # )
        for item in os.listdir(target):
           item = os.path.join(target, item)
           more_items = _fast_scandir_3_impl_get_paths_recursive(item)
           items.extend(more_items)
    return items


def _fast_scandir_3_impl_convert_paths_to_path_tuples(paths:list[str]) -> list[tuple[str, str]]:
    def path_to_tuple(path:str) -> tuple[str, str]:
        if os.path.isfile(path):
            return ('f', path)
        elif os.path.isdir(path):
            return ('d', path)

    return (
        list(
            map(
                path_to_tuple,
                paths,
            )
        )
    )


def _fast_scandir_3_impl_convert_path_tuples_to_fully_qualified_path_tuples(
    path_tuples:list[tuple[str, str]],
) -> list[tuple[str, str]]:
    return (
        list(
            map(
                lambda path_tuple: (path_tuple[0], os.path.abspath(path_tuple[1])),
                path_tuples,
            )
        )
    )


def _fast_scandir_3_impl_sort_path_tuples(
    path_tuples:list[tuple[str, str]],
) -> list[tuple[str, str]]:
    return (
        sorted(
            path_tuples,
            key=lambda path_tuple: path_tuple[1],
        )
    )


def _fast_scandir_3_impl(target:tuple[str, str]) -> list[tuple[str, str]]:
    items:list[tuple[str, str]] = []
    if os.path.isfile(target[1]):
        item = ('f', target)
        items.append(item)
    elif os.path.isdir(target[1]):
        item = ('d', target)
        items.append(item)
        for subtarget in os.listdir(target):
            items.extend(_fast_scandir_3_impl(subtarget))
    return items

def _fast_scandir_3_fully_qualified_impl(target:tuple[str, str]) -> list[tuple[str, str]]:
    return (
        list(
            map(
                lambda item: (item[0], os.path.abspath(item[1])),
                _fast_scandir_3_impl(target),
            )
        )
    )

def _fast_scandir_3_fully_qualified_sorted_impl(target:tuple[str, str]) -> list[tuple[str, str]]:
    return sorted(_fast_scandir_3_fully_qualified_impl(target), key=lambda pair: pair[1])

def fast_scandir_3(target:str) -> list[tuple[str, str]]:

    # get all paths
    paths = _fast_scandir_3_impl_get_paths_recursive(target)

    # convert paths to tuple depending on type
    path_tuples = _fast_scandir_3_impl_convert_paths_to_path_tuples(paths)

    # convert paths to fully qualified paths
    fully_qualified_path_tuples = (
        _fast_scandir_3_impl_convert_path_tuples_to_fully_qualified_path_tuples(
            path_tuples,
        )
    )

    # sort by fully qualified path
    sorted_fully_qualified_path_tuples = (
        _fast_scandir_3_impl_sort_path_tuples(fully_qualified_path_tuples)
    )

    return sorted_fully_qualified_path_tuples

    # items:list[tuple[str, str]] = []
    # if os.path.isfile(target):
    #     item = ('f', target)
    #     items.append(item)
    #     items.extend(_fast_scandir_3_impl(item))
    # elif os.path.isdir(target):
    #     item = ('d', target)
    #     items.append(item)
    #     items.extend(_fast_scandir_3_impl(item))
    # return items