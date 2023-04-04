from checker import site_is_online
from cli import read_user_cli_args, display_check_result

if __name__ == '__main__':
    args = read_user_cli_args()
    urls = args.urls
    for url in urls:
        try:
            is_online = site_is_online(url=url, timeout=3)
            display_check_result(is_online, url)
        except Exception as e:
            display_check_result(False, url, str(e))
