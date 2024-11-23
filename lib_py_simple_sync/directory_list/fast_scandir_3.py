
import os
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


def _fast_scandir_3_impl_get_paths_recursive_old(target: str) -> list[str]:
    assert isinstance(target, str), f'target is not str: {target}, {type(target)}'

    def do_join(item):
        print('do_join')
        print(type(item))
        t = os.path.join(target, item)
        print(f't={t}')
        return t

    def do(item):
        print('do')
        print(type(item))
        tmp = _fast_scandir_3_impl_get_paths_recursive(item)
        print(f't={tmp}')
        return tmp

    print(f'target={target}')
    items:list[str] = []
    if os.path.isfile(target):
        items.append(target)
    elif os.path.isdir(target):
        items.append(target)

        joined_items = list(
            map(
                lambda item: os.path.join(target, item),
                os.listdir(target),
            )
        )
        print('joined_items')
        print(joined_items)

        new_items = (
            reduce(
                list.extend,
                map(
                    lambda item: do(item),
                    map(
                        lambda item: do_join(item),
                        os.listdir(target),
                    )
                ),
                []
            )
        )

        print('new_items:')
        print(new_items)

        items.extend(
            new_items
        )
    return items


def _fast_scandir_3_impl_get_paths_recursive(target: str) -> list[str]:
    assert isinstance(target, str), f'target is not str: {target}, {type(target)}'

    print(f'target={target}')

    items:list[str] = []
    if os.path.isfile(target):
        items.append(target)
    elif os.path.isdir(target):
        items.append(target)

        ld = os.listdir(target)
        print(f'ld={ld}')

        new_items = (
            list(
                map(
                    lambda item: _fast_scandir_3_impl_get_paths_recursive(os.path.join(target, item)),
                    ld,
                )
            )
        )

        print(f'new_items={new_items}')

        items.extend(
            new_items
        )
    print(f'return items={items}')
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


# def _fast_scandir_3_impl_convert_path_tuples_to_fully_qualified_path_tuples(
#     path_tuples:list[tuple[str, str]],
# ) -> list[tuple[str, str]]:
#     return (
#         list(
#             map(
#                 lambda path_tuple: (path_tuple[0], os.path.abspath(path_tuple[1])),
#                 path_tuples,
#             )
#         )
#     )


# def _fast_scandir_3_impl_sort_path_tuples(
#     path_tuples:list[tuple[str, str]],
# ) -> list[tuple[str, str]]:
#     return (
#         sorted(
#             path_tuples,
#             key=lambda path_tuple: path_tuple[1],
#         )
#     )


def fast_scandir_3(target:str) -> list[tuple[str, str]]:

    # get all paths
    paths = _fast_scandir_3_impl_get_paths_recursive(target)
    print(f'paths={paths}')

    # convert paths to tuple depending on type
    path_tuples = _fast_scandir_3_impl_convert_paths_to_path_tuples(paths)

    # # convert paths to fully qualified paths
    # fully_qualified_path_tuples = (
    #     _fast_scandir_3_impl_convert_path_tuples_to_fully_qualified_path_tuples(
    #         path_tuples,
    #     )
    # )

    # # sort by fully qualified path
    # sorted_fully_qualified_path_tuples = (
    #     _fast_scandir_3_impl_sort_path_tuples(fully_qualified_path_tuples)
    # )

    # return sorted_fully_qualified_path_tuples
    return path_tuples
