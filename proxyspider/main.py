#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
# @Time  : 2022/10/22 22:41:22
# @Author: wd-2711
'''
import os
import reduce
import time

if __name__ == "__main__":

    st = time.time()
    pageNum = 10
    outFile = "proxy.json"
    cmd = f"cd proxyspider & scrapy crawl proxyspider -a page={pageNum} -o {outFile}"
    os.system(cmd)
    time.sleep(2)
    ipNum = reduce.reduce("./proxyspider/" + outFile)
    print(f"[+] Total IP number is {ipNum}. Saved in {outFile}.")
    nested_format = ".2f"
    print(f"[+] Time: {time.time() - st:{nested_format}} s.")

