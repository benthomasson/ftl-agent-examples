#!/usr/bin/env python3

"""
Download modules using requests
"""

import urllib.request
import os

MODULES = [
    "https://raw.githubusercontent.com/ansible-collections/community.general/refs/heads/main/plugins/modules/slack.py"
]

MODULES_DIR = "modules"

def ensure_directory(directory):
    """
    Ensure directory exists
    """

    if not os.path.exists(directory):
        os.makedirs(directory)


def main():
    """
    Download modules using requests
    """

    ensure_directory(MODULES_DIR)

    for module in MODULES:
        name = os.path.basename(module)
        urllib.request.urlretrieve(module, os.path.join(MODULES_DIR, name))
        print('Downloaded {}'.format(name))

if __name__ == '__main__':
    main()
