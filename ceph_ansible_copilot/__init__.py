
import sys

from .hosts import Host
from .utils import setup_ansible_cfg

__version__ = '0.9.6a9'

if sys.argv[0] == '/usr/bin/copilot':
    setup_ansible_cfg()
