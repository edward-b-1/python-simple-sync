
import os
import operator
from pathlib import Path

def _fast_scandir_4_impl(target: str) -> tuple[list[str], list[str]]:
    files: list[str] = []
    dirs: list[str] = []

    target: Path = Path(target).expanduser().resolve()

    if target.is_file():
        files.append(str(target))
    elif target.is_dir():
        dirs.append(str(target))
        for item in target.rglob('*'):
            if item.is_file():
                files.append(str(item))
            elif item.is_dir():
                dirs.append(str(item))

    return files, dirs


# def _fast_scandir_4_impl_convert_paths_to_fully_qualified_paths(
#     paths:list[str],
# ) -> list[str]:
#     return (
#         list(
#             map(
#                 os.path.abspath,
#                 paths,
#             )
#         )
#     )


def _fast_scandir_4_impl_sort_paths(
    paths:list[str],
) -> list[str]:
    return (
        sorted(
            paths,
        )
    )


def fast_scandir_4(target:str) -> list[tuple[str, str]]:

    # get all files and directorys
    files, dirs = _fast_scandir_4_impl(target)

    # convert paths to fully qualified paths
    # fully_qualified_file_paths = (
    #     _fast_scandir_4_impl_convert_paths_to_fully_qualified_paths(
    #         files,
    #     )
    # )
    # fully_qualified_dir_paths = (
    #     _fast_scandir_4_impl_convert_paths_to_fully_qualified_paths(
    #         dirs,
    #     )
    # )

    # sort by fully qualified path
    sorted_files = (
        _fast_scandir_4_impl_sort_paths(files)
    )
    sorted_dirs = (
        _fast_scandir_4_impl_sort_paths(dirs)
    )

    return (sorted_files, sorted_dirs)
