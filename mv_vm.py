#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: wu hsuan
# Time: 2020/5/7下午 05:15
# File: mv_vm.py

import os


def move():
    log = '/root/potvm_for_ubuntu/etc/cowrie/log_backup'
    file = '/root/potvm_for_ubuntu/etc/cowrie/file_backup'
    des = '/tmp/backup'

    for i in os.listdir(log):
        try:
            os.system(f'mkdir -p {des}/{i}/cowrie')
            os.system(f'tar zcf {des}/{i}/cowrie/cowrie_log_{i}.tar.gz {log}/{i}')
            os.system(f'rm -rf {log}/{i}')
            print('log tar to /tmp ok!')
        except:
            os.system(f'tar zcf {des}/{i}/cowrie/cowrie_log_{i}.tar.gz {log}/{i}')
            os.system(f'rm -rf {log}/{i}')
            print('log tar to /tmp ok!')

def mov():
    log = '/root/potvm_for_ubuntu/etc/cowrie/log_backup'
    file = '/root/potvm_for_ubuntu/etc/cowrie/file_backup'
    des = '/tmp/backup'
    for i in os.listdir(file):
        try:
            os.system(f'mkdir -p {des}/{i}/cowrie')
            os.system(f'tar zcf {des}/{i}/cowrie/cowrie_log_{i}.tar.gz {file}/{i}')
            os.system(f'rm -rf {file}/{i}')
            print('file tar to /tmp ok!')
        except:
            os.system(f'tar zcf {des}/{i}/cowrie/cowrie_log_{i}.tar.gz {file}/{i}')
            os.system(f'rm -rf {file}/{i}')
            print('file tar to /tmp ok!')

if __name__ == "__main__":
    move()
    mov()
