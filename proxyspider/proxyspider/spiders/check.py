#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
# @Time  : 2022/10/22 20:47:03
# @Author: wd-2711
'''

import socket
import func_timeout
from func_timeout import func_set_timeout

@func_set_timeout(1)
def is_port_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except Exception as e:
        pass
    return False

def check(ip, port):
    try:
        res = is_port_open(ip, port)
        return res
    except func_timeout.exceptions.FunctionTimedOut:
        return False