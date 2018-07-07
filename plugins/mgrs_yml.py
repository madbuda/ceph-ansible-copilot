#!/usr/bin/env python2

import os
import shutil


description = "use the existing mgrs.yml, or create one from the sample"
yml_file = '/usr/local/ceph-ansible/group_vars/mgrs.yml'


def plugin_main(config=None):

    if not config:
        raise ValueError("Config object not received from caller")

    if not os.path.exists(yml_file):
        # create a copy from the sample file
        sample = '{}.sample'.format(yml_file)
        if os.path.exists(sample):
            shutil.copy2(sample, yml_file)
        else:
            raise EnvironmentError("sample file for mgrs.yml not found")

    return None


if __name__ == '__main__':
    pass
