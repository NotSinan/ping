import argparse


def read_user_cli_args():
    parser = argparse.ArgumentParser(prog='ping', description='check availability of a website.')
    parser.add_argument("-u",
                        "--urls",
                        metavar="urls",
                        nargs="+",
                        type=str,
                        default=[],
                        help="enter one or more website urls"
                        )
    return parser.parse_args()


def display_check_result(result, url, error=""):
    print(f'The status of "{url}" is:', end=" ")
    if result:
        print('Online!')
    else:
        print(f'Offline!')
