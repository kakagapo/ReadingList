# Inspired by https://github.com/antlr/grammars-v4/blob/master/_scripts/mkindex.py

import os
import sys
from pathlib import Path
from typing import Sequence

def path_exists(path):
    return os.path.exists(path)

def contains_md_files(files):
    for name in files:
        if name.endswith(".md"):
            return True
    return False

def get_title(filepath):
    #print(f"Getting title for {filepath}")
    with open(filepath, 'r', encoding="utf8") as fp:
        first_line = fp.readline().strip(" #\r\n")
    return first_line

def get_relative_path(root, filepath):
    # todo
    return filepath

def generate_toc(root : str) -> Sequence[dict]:
    for path, subdirs, files in os.walk(root):
        if contains_md_files(files):
            for filename in files:
                fullpath = os.path.join(path, filename)
                if filename.endswith(".md") and filename != "index.md":
                    title = get_title(fullpath)
                    relativepath = get_relative_path(root, fullpath)
                    print(f"- [{title}]({relativepath})")
    return


if __name__ == '__main__':
    if len(sys.argv) != 2:
        script_name = Path(__file__).name
        print(f"Usage: python {script_name} path")
        exit(1)

    print("# Table of Contents")
    print("")
    path = sys.argv[1]
    generate_toc(sys.argv[1])