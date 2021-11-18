import yaml
import logging.config
import os


def setup_logging(default_path="./logging.yaml", default_level=logging.INFO):
    try:
        path = default_path
        if os.path.exists(path):
            with open(path, "r") as f:
                config = yaml.load(f, Loader=yaml.FullLoader)
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
    except Exception as e:
        print(e)

