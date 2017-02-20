import onedrivemirror
import argparse
import functools

sessions_file = ".onedrive.session"

def main():
    parser = argparse.ArgumentParser(description="Copy OneDrive folder to local path. Remember to set your "
                                                 "ONEDRIVEMIRROR_CLIENTID and ONEDRIVEMIRROR_CLIENT_SECRET "
                                                 "environment variables")
    parser.set_defaults(func=functools.partial(help, parser))
    subparsers = parser.add_subparsers(help='sub-command help')
    init_parser = subparsers.add_parser('init', help='Pair your folder with OneDrive credentials')
    init_parser.set_defaults(func=init)
    copy_parser = subparsers.add_parser('cp', help='Mirror files')
    copy_parser.add_argument('path', nargs=2, help='[src] [dst]')
    copy_parser.set_defaults(func=copy)
    args = parser.parse_args()
    args.func(args)


def init(args):
    onedrivemirror.create_session_file(session_file=sessions_file)


def copy(args):
    client = onedrivemirror.MirrorClient(sessions_file)
    client.mirror(args.path[0], args.path[1])

def help(parser, args):
    parser.print_help()

if __name__ == '__main__':
    main()
