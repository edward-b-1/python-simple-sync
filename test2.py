
import os
import operator
from functools import reduce

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

def _fast_scandir_3_impl_get_paths_recursive(target: str) -> list[str]:
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

print(_fast_scandir_3_impl_get_paths_recursive('example-target-directory'))

print(
    _fast_scandir_3_impl_convert_paths_to_path_tuples(
        _fast_scandir_3_impl_get_paths_recursive('example-target-directory')
    )
)