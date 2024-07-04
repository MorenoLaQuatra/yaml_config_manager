import yaml
import argparse
from addict import Dict

def parse_cli_args():
    parser = argparse.ArgumentParser(description='Load configuration.')
    parser.add_argument('--config', type=str, help='Path to the YAML config file', required=True)
    args, unknown = parser.parse_known_args()

    def convert_value(value):
        if value.lower() in ['true', 'false']:
            return value.lower() == 'true'
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value

    cli_args = {}
    for arg in unknown:
        if arg.startswith('--'):
            key, value = arg.lstrip('--').split('=')
            keys = key.split('.')
            d = cli_args
            for k in keys[:-1]:
                if k not in d:
                    d[k] = {}
                d = d[k]
            d[keys[-1]] = convert_value(value)
    return args.config, cli_args

def merge_dicts(a, b):
    for key, value in b.items():
        if isinstance(value, dict) and key in a:
            merge_dicts(a[key], value)
        else:
            a[key] = value

def load_config():
    config_path, cli_args = parse_cli_args()
    
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    config = Dict(config)
    merge_dicts(config, cli_args)
    return config

def save_config(config, filepath):
    with open(filepath, 'w') as file:
        yaml.dump(config.to_dict(), file)

def load_config_from_file(filepath):
    with open(filepath, 'r') as file:
        config = yaml.safe_load(file)
    return Dict(config)

if __name__ == '__main__':
    config = load_config()
    print(config)
