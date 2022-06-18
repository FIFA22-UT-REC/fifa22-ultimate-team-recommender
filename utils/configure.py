# Helper for connecting environment variables to config.yml
import yaml


def configure(config_file_path):
    with open(config_file_path, 'r') as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)
        config_dict = yaml.load(file, Loader=yaml.SafeLoader)
        custom_keys = set(config_dict.keys())
        for k in custom_keys:
            setattr(config, k, config_dict[k])
