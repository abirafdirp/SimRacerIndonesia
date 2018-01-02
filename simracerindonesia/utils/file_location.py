import os

script_path = os.path.realpath(__file__)


def get_full_path(relative_path_from_project_root):
    """
    Get full path, current working directory is root folder of this
    project
    """
    this_script_location = 'simracerindonesia/utils/file_location.py'
    return script_path.replace(
        this_script_location,
        relative_path_from_project_root
    )
