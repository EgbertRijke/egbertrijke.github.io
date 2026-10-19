#!/usr/bin/env python3
"""Stage website sources without the old/generated book page for Jekyll.

Staging lets the initial deployment be prepared while the old source page
remains live. Delete number-theory-notes.md from Git after switching Pages.
"""
import argparse
from pathlib import Path
import shutil


def prepare(source, output):
    if output.exists():
        raise ValueError(f'Output already exists: {output}')
    skip = {'.git', '.github', '_site', '_deploy', '_website-build-source',
            '__pycache__', 'scripts', 'docs', 'number-theory-notes.md'}
    output.mkdir(parents=True)
    for item in source.iterdir():
        if item.name in skip or item.resolve() == output.resolve():
            continue
        if item.is_symlink():
            raise ValueError(f'Refusing website source symlink: {item}')
        if item.is_dir():
            if item.name == 'notes':
                shutil.copytree(item, output / item.name,
                                ignore=lambda directory, names: ['number-theory']
                                if Path(directory) == item and 'number-theory' in names else [])
            else:
                shutil.copytree(item, output / item.name)
        elif item.is_file():
            shutil.copy2(item, output / item.name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=Path('.'))
    parser.add_argument('--output', type=Path, default=Path('_website-build-source'))
    args = parser.parse_args()
    prepare(args.source, args.output)
