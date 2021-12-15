import argparse
from update_categories import start

def initialize_parser():
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    parser_cats = subparsers.add_parser(
        "zs_cats",
        help="Update given custom category",
    )
    parser_cats.add_argument('-a', '--apikey',
                             help='ZIA API key',
                             required=True)
    parser_cats.add_argument('-u', '--username',
                             help='ZIA admin user',
                             required=True)
    parser_cats.add_argument('-p', '--password',
                             help='ZIA admin password',
                             required=True)
    parser_cats.add_argument('-cat', '--category',
                             help='Custom Category Name',
                             required=True)
    parser_cats.add_argument('-f', '--file',
                             help='File location',
                             required=True)
    parser_cats.add_argument('-c', '--cloud',
                             help='Zscaler cloud. Example zsapi.zscalerthree.net',
                             required=True)

    parser_version = subparsers.add_parser(
        "version",
        help="Plugin version",
    )
    args = parser.parse_args()
    plugin_selection(args)


def plugin_selection(args):
    """
    Selects the plugin to be used based on the parser
    :param args: parer arguments
    :return:
    """
    if args.command == 'version':
        print('Plugin version version 1.0')
    elif args.command == "zs_cats":
        start(args.apikey, args.username, args.password, args.cloud, args.category, args.file)
    else:
        print("invalid command")
        raise ValueError("Invalid command")
