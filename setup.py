# setup.py

from setuptools import setup, find_packages

setup(
    name='yaml_config_manager',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyYAML',
        'addict'
    ],
    entry_points={
        'console_scripts': [
            'yaml-config-manager=yaml_config_manager:load_config',
        ],
    },
    author='Moreno La quatra',
    author_email='moreno.laquatra@gmail.com',
    description='A package to manage YAML configuration with command line overrides',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MorenoLaQuatra/yaml_config_manager',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)