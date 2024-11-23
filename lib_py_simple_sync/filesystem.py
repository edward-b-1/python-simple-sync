
import platformdirs

from lib.constants import APPLICATION_NAME_DIR

def get_linux_config_dir() -> str:
    return platformdirs.user_config_dir(APPLICATION_NAME_DIR)
