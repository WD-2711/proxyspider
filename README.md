# proxyspider

![](https://github.com/WD-2711/proxyspider/blob/main/proxyspider-v1-blue.svg)

------

This small demo is to crawl the proxy IP under https://www.kuaidaili.com/ and check whether the proxy IP can be used.

## Usage :

1. First install scrapy.

2. Make sure your system has telnet installed.

3. Change to the project directory and run

   ```
   scrapy crawl proxyspider -a page=20 -o proxy.json
   ```

   The above command line means to crawl 20 pages of proxy IP and save the result to the proxy.json file.

------

A small demo for network security rookies, the purpose is to learn scrapy, if you have any questions, please send an email to chuanlongxie@stu.xidian.edu.cn.

