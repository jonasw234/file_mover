# file_mover
Moves/copies a number of random files from one directory to another.
Only files with a file name/path that doesn’t exist in the destination directory yet are transferred.

## Usage
```
Usage: file_mover [-h] [-c] SOURCE DESTINATION AMOUNT [-f]

Options:
    -h --help   Show this help text
    -c --copy   Copy, don’t move files
    -f --force  Force move even if there are fewer files in SOURCE than needed
```

### Example
```bash
$ tree testfiles
testfiles
└── src
    ├── Eegoo9na.txt
    ├── Ohng1Uec.txt
    ├── gah1aeK5.txt
    ├── ieHei3oo.txt
    ├── ko3Rioy4.txt
    ├── sbfldr1
    │   ├── Ao4Oog8j.txt
    │   ├── UN2eeghe.txt
    │   ├── ifue0Ohf.txt
    │   ├── ios2EeTh.txt
    │   └── ooPibee6.txt
    └── sbfldr2
        ├── AeRae2Ah.txt
        ├── Fiuth4Li.txt
        ├── beyoo4On.txt
        ├── pheiG9up.txt
        └── xahTh5if.txt

3 directories, 15 files
$ file_mover.py testfiles/src testfiles/dst 7
$ tree testfiles
testfiles
├── dst
│   ├── gah1aeK5.txt
│   ├── sbfldr1
│   │   ├── Ao4Oog8j.txt
│   │   ├── ifue0Ohf.txt
│   │   └── ooPibee6.txt
│   └── sbfldr2
│       ├── AeRae2Ah.txt
│       ├── beyoo4On.txt
│       └── xahTh5if.txt
└── src
    ├── Eegoo9na.txt
    ├── Ohng1Uec.txt
    ├── ieHei3oo.txt
    ├── ko3Rioy4.txt
    ├── sbfldr1
    │   ├── UN2eeghe.txt
    │   └── ios2EeTh.txt
    └── sbfldr2
        ├── Fiuth4Li.txt
        └── pheiG9up.txt

6 directories, 15 files
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

If you want to have nice aliases (e.g. `rcp` and `rmv` for random copy/move), create them like this and put them in your `.bashrc` or `.zshrc`:
```bash
alias rcp='file_mover -c'
alias rmv='file_mover'
```
