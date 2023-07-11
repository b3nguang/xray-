import requests
import argparse
from time import time

print('''
 _    _____                                     
| |__|___ / _ __   __ _ _   _  __ _ _ __   __ _ 
| '_ \ |_ \| '_ \ / _` | | | |/ _` | '_ \ / _` |
| |_) |__) | | | | (_| | |_| | (_| | | | | (_| |
|_.__/____/|_| |_|\__, |\__,_|\__,_|_| |_|\__, |
                  |___/                   |___/ 
脚本，启动！！！！
''')

parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, default=None, required=False,
                    help='输入文件路径')
parser.add_argument('-u', type=str, default=None, required=False,
                    help='输入url')
args = parser.parse_args()

urls = []

if args.f:
    with open(args.f, 'r') as f:
        lines = f.readlines()
        urls = [line.strip() for line in lines if not line.startswith('https')]
elif args.u:
    urls.append(args.u)
else:
    parser.print_help()
    exit()

payload = {
    'username':'admin',
    'password':'admin',
}

success_targets = []
print("[+]任务开始.....")
start = time()

for url in urls:
    target=f'{url}/login'
    try:
        response = requests.post(url=target, data=payload, timeout=5)
        if '成功' in response.text:
            success_targets.append(target)
            print(f"\033[32;1m[+] success {url}\033[0m")
        else:
            print(f"\033[1;34m[*] fail {url}\033[0m")
    except Exception as e:
        print(e)

end = time()
print('任务完成,用时%ds.' % (end - start))

with open('success.txt', 'w') as f:
    for target in success_targets:
        f.write(target + '\n')