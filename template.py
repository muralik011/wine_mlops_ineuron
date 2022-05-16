# Script to create project directory structure
import os

dirs = [
    os.path.join('data', 'raw'),
    os.path.join('data', 'processed'),
    'notebooks',
    'saved_models',
    'src',
    'data_given'
]

for dir in dirs:
    os.makedirs(dir, exist_ok=True)
    with open(os.path.join(dir, '.gitkeep'), 'w'):
        pass

files = [
    'dvc.yaml',
    'params.yaml',
    '.gitignore',
    os.path.join('src', '__init__.py'),
    'README.md'
]

for file in files:
    with open(file, 'w'):
        pass