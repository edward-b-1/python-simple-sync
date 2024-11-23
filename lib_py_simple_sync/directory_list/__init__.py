# ./property-price-analysis-analysis/Rightmove-Analysis/combine_exported_data.py
# ./Land-Registry-Data-Ingestion/Land-Registry-Download/minio_upload_pp_monthly_update_files_from_devbox2.py
# ./polygon-fx/filesystem_helper_functions.py


import os


def get_directory_list(target: str) -> list[(str, str)]:

    if os.path.isfile(target):
        item_file = (target, 'f')
        items = [item_file]
        return items

    elif os.path.isdir(target):
        item_dir = (target, 'd')
        items = [item_dir]
        # TODO: map
        for item in os.listdir(target):
            full_path = os.path.join(target, item)
            more_items = get_directory_list(full_path)
            items.extend(more_items)
        return items

    return []


def fast_scandir(dirname: str) -> list[str]:
    subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders



