#!/usr/bin/env python2

import argparse
import errno
import logging
import os
import shutil
import subprocess
import sys
import time

from distutils.dir_util import copy_tree

logger = logging.getLogger(__name__)

ASSET_DIRECTORIES = [
    'assets',
    'submodules',
]


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='Auto-generated description')
    parser.add_argument('--root', default=os.getcwd())
    parser.add_argument('--output_dir', default='build')
    parser.add_argument('--clean', action='store_true', default=False)

    # If `argv` is None,  will default to using `sys.argv`
    return parser.parse_args(args=argv)


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def pdf(infile):
    basename, extension = os.path.splitext(infile)
    if not extension:
        raise RuntimeError((
            'Attempted to add extension to a file with no existing extension. ',
            'This was probably a mistake.'))
    return basename + '.pdf'


def html(infile):
    basename, extension = os.path.splitext(infile)
    if not extension:
        raise RuntimeError((
            'Attempted to add extension to a file with no existing extension. ',
            'This was probably a mistake.'))
    return basename + '.html'


def pandoc_file(infile, outfile):
    cmd = [
        'pandoc',
        '--from',
        'markdown',
        '--section-divs',
        '--filter',
        'pandoc-sidenote',
        '--metadata',
        'title=Test Document',
        '--metadata',
        'subtitle=Subtitle of the Test Document',
        '--metadata',
        'author=Daniel Miller',
        '--metadata',
        'date=' + time.strftime("%m/%d/%y %H:%M:%S"),
        # '--no-highlight',
        '--template',
        # 'html/templates/chapter.html',
        'submodules/tufte-pandoc-css/tufte.html5',
        '--css',
        'tufte-pandoc-css/tufte-css/tufte.css',
        '--css',
        'tufte-pandoc-css/pandoc.css',
        '--css',
        'tufte-pandoc-css/pandoc-solarized.css',
        '--css',
        'tufte-pandoc-css/tufte-extra.css',
        '--output',
        outfile,
        infile,
    ]
    logger.info('Running pandoc: %s', ' '.join(cmd))
    try:
        subprocess.check_output(cmd)
    except subprocess.CalledProcessError as ex:
        logger.error(ex)
        logger.error(ex.message)
        logger.error(ex.output)
        sys.exit(ex.returncode)


def main(argv=None):
    args = parse_args(argv)

    build_root = os.path.abspath(os.path.join(args.root, args.output_dir))
    if args.clean:
        shutil.rmtree(build_root)

    input_file = os.path.abspath('test/content.md')
    output_file = html(os.path.join(build_root, os.path.split(input_file)[1]))

    mkdir_p(build_root)

    logger.info('Input file:  %s', input_file)
    logger.info('Output file: %s', output_file)

    pandoc_file(input_file, output_file)
    for asset in ASSET_DIRECTORIES:
        copy_tree(asset, build_root)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
