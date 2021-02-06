# file_mover
Moves a number of random files from one directory to another.
Only files with a file name/path that doesn’t exist in the destination directory yet are copied.

## Usage
```
Usage: file_mover [-h] SOURCE DESTINATION AMOUNT [-f]

Options:
    -h --help   Show this help text
    -f --force  Force move even if there are fewer files in SOURCE than needed
"""
```

## Installation
For the development version:
```
git clone https://github.com/jonasw234/file_mover
cd file_mover
python3 setup.py install
pip3 install -r dev-requirements.txt
```
For normal usage do the same but don’t include the last line or use [`pipx`](https://pypi.org/project/pipx/) and install with
```
pipx install git+https://github.com/jonasw234/file_mover
```
