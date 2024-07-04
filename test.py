from yaml_config_manager import load_config, save_config, load_config_from_file
import sys

def main():
    config = load_config()
    print("Loaded Configuration:")
    print(config)
    
    print("Nested Configuration:")
    print(f"Max size: {config.logging.file.max_size}")
    print(f"Backup count: {config.logging.file.backup_count}")
    print(f"Store all: {config.logging.file.store_all}")
    print(f"Store all type: {type(config.logging.file.store_all)}")
    
    print("Saving Configuration to: stored_config.yaml")
    save_config(config, "stored_config.yaml")

if __name__ == '__main__':
    main()