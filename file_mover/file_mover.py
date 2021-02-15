#!/usr/bin/env python3
"""
file_mover

Moves a number of random files from one directory to another.
Only files with a file name/path that doesn’t exist in the destination directory yet are copied.

Usage: file_mover [-h] [-c] SOURCE DESTINATION AMOUNT [-f]

Options:
    -h --help   Show this help text
    -c --copy   Copy, don’t move files
    -f --force  Force move even if there are fewer files in SOURCE than needed
"""
import logging
import os
import random
import shutil

from docopt import docopt
from schema import And, Optional, Schema, Use

logging.basicConfig(level=logging.INFO)


def folder_contents(folder: str) -> list:
    """
    Return the contents of a folder.

    Parameters
    ----------
    folder : str
        The source folder whose contents will be returned

    Returns
    -------
    list
        The list of files with their relative path
    """
    contents = set()
    for root, _, files in os.walk(folder):
        for name in files:
            contents.add(os.path.join(root, name))
    return contents


def relative_path(basepath: str, fullpath: str) -> str:
    """
    Remove `basepath` from `fullpath` if `fullpath` begins with it.

    Parameters
    ----------
    basepath : str
        The basepath to remove
    fullpath : str
        The fullpath to remove the `basepath` from

    Returns
    -------
    str
        The relative path
    """
    if fullpath.startswith(basepath):
        return fullpath[len(basepath) + 1 :]
    return fullpath


def transfer_files(src: str, dst: str, filenames: list, move=True):
    """
    Transfer files in `filenames` from `src` to `dst`.

    Parameters
    ----------
    src : str
        Source directory
    dst : str
        Destination directory
    filenames : list
        List of files to move
    move : bool
        Whether to move (default) or copy files
    """
    for filename in filenames:
        dst_path = os.path.join(dst, relative_path(src, os.path.dirname(filename)))
        if not os.path.isdir(dst_path):
            os.makedirs(dst_path, exist_ok=True)
        transfer_func = shutil.move
        if not move:
            transfer_func = shutil.copy
        transfer_func(os.path.join(src, relative_path(src, filename)), dst_path)


def main():
    """Main function.  Check arguments and run the appropriate functions."""
    args = docopt(__doc__)
    schema = Schema(
        [
            {
                Optional("--help"): Use(bool),
                "--copy": Use(bool),
                "SOURCE": And(Use(str), lambda n: os.path.isdir(n)),
                "DESTINATION": Use(str),
                "AMOUNT": And(Use(int), lambda n: n > 0),
                "--force": Use(bool),
            }
        ]
    )
    args = schema.validate([args])[0]
    src_contents = folder_contents(args["SOURCE"])
    dst_contents = folder_contents(args["DESTINATION"])
    files_to_transfer = src_contents - dst_contents
    try:
        sample = random.sample(files_to_transfer, int(args["AMOUNT"]))
        transfer_files(args["SOURCE"], args["DESTINATION"], sample, args["--copy"])
    except ValueError:
        logging.warning(
            "There were fewer unique file names in the source directory than you told me to transfer."
        )
        if args["--force"]:
            logging.info("Moving the rest of them because you activated force mode.")
            transfer_files(args["SOURCE"], args["DESTINATION"], files_to_transfer, args["--copy"])


if __name__ == "__main__":
    main()
