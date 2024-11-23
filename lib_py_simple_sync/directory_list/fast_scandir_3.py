
import os
import operator
from functools import reduce


def _fast_scandir_3_impl_get_paths_recursive_for_loop(target: str) -> list[str]:
    items:list[str] = []
    if os.path.isfile(target):
        items.append(target)
    elif os.path.isdir(target):
        items.append(target)
        for item in os.listdir(target):
           item = os.path.join(target, item)
           more_items = _fast_scandir_3_impl_get_paths_recursive_for_loop(item)
           items.extend(more_items)
    return items


def _fast_scandir_3_impl_get_paths_recursive(target: str) -> list[str]:
    assert isinstance(target, str), f'target is not str: {target}, {type(target)}'

    items:list[str] = []
    if os.path.isfile(target):
        items.append(target)
    elif os.path.isdir(target):
        items.append(target)
        items.extend(
            reduce(
                operator.add,
                map(
                    _fast_scandir_3_impl_get_paths_recursive,
                    map(
                        lambda item: os.path.join(target, item),
                        os.listdir(target),
                    )
                ),
                [],
            )
        )
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


def fast_scandir_3(target:str) -> list[tuple[str, str]]:

    # get all paths
    paths = _fast_scandir_3_impl_get_paths_recursive(target)
    print(f'paths={paths}')

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
