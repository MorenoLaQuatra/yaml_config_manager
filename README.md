# YAML Config Manager

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`yaml_config_manager` is a Python package to manage YAML configurations with command line overrides. This package allows you to load a configuration from a YAML file and override or add parameters using command line arguments.

## Installation

Install the package using pip:

```
pip install yaml_config_manager
```

## Usage

First, create a configuration YAML file. For example, `config.yaml`:

```
model:
    name: "my_model"
    hidden_size: 768
training:
    batch_size: 32
    learning_rate: 0.001
```

Next, use the `yaml_config_manager` package in your Python script:

```python
from yaml_config_manager import load_config
config = load_config()
```

The configuration file path shoudl be specified using the `--config` argument. You can also override or add parameters using `--<key>=<value>` syntax. For example:

```sh
python your_script.py --config=config.yaml --model.hidden_size=512 --training.batch_size=64
```

The parameters in the configuration file can be accessed as follows:

```python
model_name = config.model.name
hidden_size = config.model.hidden_size
...
```

### Handling Edge Cases

- **Non-existent keys**: If a key specified in the command line does not exist in the YAML file, it will be added to the configuration.
- **Nested keys**: Nested keys can be overridden or added using the dot notation.

### License

This project is licensed under the MIT License.
