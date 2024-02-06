# SQLIDetection
用来探测sql注入点
```

███████╗ ██████╗ ██╗     ██╗██████╗ ███████╗████████╗███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔═══██╗██║     ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
███████╗██║   ██║██║     ██║██║  ██║█████╗     ██║   █████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║
╚════██║██║▄▄ ██║██║     ██║██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║
███████║╚██████╔╝███████╗██║██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                            version 0.1
                                                                            Author  killeveee

usage: python SQLIDetection.py  [options]

Note: You need to put the parameters that need to be detected at the end！！！

options:
  -h, --help         show this help message and exit
  -u URL, --url URL  Target URL (e.g. 'http://www.site.com/vuln.php?id=1')
  -a, --all          Batch full scan,include GET and POST (must use --urls)
  --urls URLS_FILE   Target URLs (default urls.txt)
  --data DATA        Data string to be sent through POST (e.g. 'id=1')
```
