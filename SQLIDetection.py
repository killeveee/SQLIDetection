import requests
import argparse
from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S /%Y-%m-%d/")
GREEN = '\033[92;1m'
RED = '\033[91;1m'
BULE = '\033[94;1m'
RESET = '\033[0m'

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

testdate = ['\'', '\"', ' and 1=2', ' or 1=1']


def detect_get(urls):  # GET Method
    for u in urls:
        print("\nTarget URL: " + u)

        print(f"[{BULE}{current_time[:8]}{RESET}] " + "testing connection to the target URL")
        try:
            r = requests.get(url=u, proxies=proxies)
            r.raise_for_status()
        except requests.RequestException:
            print(
                f"[{BULE}{current_time[:8]}{RESET}] " + f"[{RED}Error{RESET}] " + "Please check your network connection")
            return
        # parsed_url = urlparse(u)
        # query_params = parse_qs(parsed_url.query)
        # for key, value in query_params.items():
        #     print(f"[{BULE}{current_time[:8]}{RESET}] "+f"testing GET parameter '{key}'")
        #     print(f"- {key}: {', '.join(value)}")
        for d in testdate:
            payload = u + d
            rr = requests.get(url=payload, proxies=proxies)

            if r.text == rr.text:
                print(f"[{BULE}{current_time[:8]}{RESET}] " + f"[{RED}NO{RESET}] " + payload)
                continue
            print(f"[{BULE}{current_time[:8]}{RESET}] " + f"[{GREEN}OK{RESET}] " + payload)
            print('GET parameter is vulnerable.')
            break


def detect_post(urls, data):  # POST Method
    for u in urls:
        print("\nTarget URL: " + u)

        print(f"[{BULE}{current_time[:8]}{RESET}] " + "testing connection to the target URL")
        try:
            r = requests.post(url=u, data=data, headers=headers, proxies=proxies)
            r.raise_for_status()
        except requests.RequestException:
            print(
                f"[{BULE}{current_time[:8]}{RESET}] " + f"[{RED}Error{RESET}] " + "Please check your network connection")
            return

        for d in testdate:
            payload = data + d
            rr = requests.post(url=u, data=payload, headers=headers, proxies=proxies)
            if r.text == rr.text:
                print(f"[{BULE}{current_time[:8]}{RESET}] " + f"[{RED}NO{RESET}] " + payload)
                continue
            print(f"[{BULE}{current_time[:8]}{RESET}] " + f"[{GREEN}OK{RESET}] " + payload)
            print('POST parameter is vulnerable.')
            break


# def modify_url(url, param_to_change, new_value):
#     parsed_url = urlparse(url)
#     query_params = parse_qs(parsed_url.query)
#     query_params[param_to_change] = [new_value]
#     modified_query = urlencode(query_params, doseq=True)
#     modified_url = parsed_url._replace(query=modified_query).geturl()
#     return modified_url

def banner():
    print('''                                                                                               
Usage: python SQLIDetection.py  [options]
Options:
    -h, --help            Show basic help message and exit
    -u URL, --url=URL     Target URL (e.g. "http://www.site.com/vuln.php?id=1")
    --urls=urls.txt       Target URLs (default urls.txt)
    --data=DATA           Data string to be sent through POST (e.g. "id=1")
    -a, --all             Batch full scan,include GET and POST (must use --urls)

Note: You need to put the parameters that need to be detected at the end！！！
    ''')


def parse_arguments():
    parser = argparse.ArgumentParser(usage=argparse.SUPPRESS)
    parser.add_argument("-u", "--url", dest="url", action="append",
                        help="Target URL (e.g. 'http://www.site.com/vuln.php?id=1')")
    parser.add_argument("-a", "--all", dest="all", action='store_true',
                        help="Batch full scan,include GET and POST (must use --urls)")
    parser.add_argument("--urls", dest="urls_file", help="Target URLs (default urls.txt)")
    parser.add_argument("--data", dest="data", help="Data string to be sent through POST (e.g. 'id=1')")
    args = parser.parse_args()

    if not args.url and not args.urls_file:
        parser.error('At least one of --url or --urls must be provided.')

    return args


def read_urls_from_file(file_path):
    urls = []
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    return urls


if __name__ == "__main__":
    print('''

███████╗ ██████╗ ██╗     ██╗██████╗ ███████╗████████╗███████╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██╔═══██╗██║     ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
███████╗██║   ██║██║     ██║██║  ██║█████╗     ██║   █████╗  ██║        ██║   ██║██║   ██║██╔██╗ ██║
╚════██║██║▄▄ ██║██║     ██║██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   ██║██║   ██║██║╚██╗██║
███████║╚██████╔╝███████╗██║██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                            version 0.1
                                                                            Author  killeveee
''')

    # recive args
    args = parse_arguments()
    target_url = args.url if args.url else None
    data_string = args.data if args.data else None
    urls_from_file = read_urls_from_file(args.urls_file) if args.urls_file else None

    if '-h' in vars(args) or '--help' in vars(args):
        banner()
        exit()

    print(f"[*] starting @ {current_time}")

    if target_url is not None and data_string is None:  # 纯GET请求
        detect_get(target_url)
    if target_url is not None and data_string is not None:  # 纯Post请求
        detect_post(target_url, data_string)
    if urls_from_file is not None and data_string is None:  # 批量Get请求
        detect_get(urls_from_file)
    if urls_from_file is not None and data_string is not None and args.all is not True:  # 批量Post请求
        detect_post(urls_from_file, data_string)
    if urls_from_file is not None and data_string is not None and args.all is True:  # 批量Get&Post请求
        detect_get(urls_from_file)
        detect_post(urls_from_file, data_string)

    print(f"\n[*] ending @ {current_time}\n")
    exit()
