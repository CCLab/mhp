#!/usr/bin/env python

import os
import subprocess
import sys

BASE_DIR = os.path.dirname(__file__)
ESLINT_PATH = os.path.join(BASE_DIR, 'node_modules', '.bin', 'eslint')
ESLINT_CONFIG_PATH = os.path.join(BASE_DIR, '.eslintrc.yml')
STATIC_SOURCE_DIR_JS = os.path.join(BASE_DIR, 'src', 'static', 'js')

SASS_LINT_PATH = os.path.join(BASE_DIR, 'node_modules', '.bin', 'sass-lint')
SASS_LINT_CONFIG_PATH = os.path.join(BASE_DIR, '.sass-lint.yml')


def run_linters():
    has_error = False
    for root, dirs, filenames in os.walk(STATIC_SOURCE_DIR_JS):
        for filename in filenames:
            status_code = subprocess.call([ESLINT_PATH, '-c', ESLINT_CONFIG_PATH, os.path.join(root, filename)])
            if status_code != 0:
                has_error = True

    status_code = subprocess.call([SASS_LINT_PATH, '-c', SASS_LINT_CONFIG_PATH, '-v', '-q'])

    if status_code != 0:
        has_error = True

    if has_error:
        sys.exit(1)


if __name__ == '__main__':
    run_linters()
