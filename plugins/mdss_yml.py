#!/usr/bin/env python2

import os
import shutil
from ceph_ansible_copilot.utils import get_used_roles

description = "use the existing mdss.yml, or create one from the sample"
yml_file = '/usr/local/ceph-ansible/group_vars/mdss.yml'


def plugin_main(config=None):

    if not config:
        raise ValueError("Config object not received from caller")

    used_roles = get_used_roles(config)
    if "mds" not in used_roles:
        return None

    if not os.path.exists(yml_file):
        # create a copy from the sample file
        sample = '{}.sample'.format(yml_file)
        if os.path.exists(sample):
            shutil.copy2(sample, yml_file)
        else:
            raise EnvironmentError("sample file for mdss.yml not found")

    return None


if __name__ == '__main__':
    pass
