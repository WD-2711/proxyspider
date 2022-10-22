from email import header


#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
# @Time  : 2022/10/22 22:39:07
# @Author: wd-2711
'''
import json

def reduce(file):
    with open(file, 'r') as f:
        data = json.load(f)
        newdata = {}
        for d in data:
            newdata[d["ip"]] = d["port"]
    
    with open(file, 'w') as f:
        json.dump(newdata, f)
    return len(newdata)

if __name__ == "__main__":
    reduce("./proxyspider/proxy.json")
