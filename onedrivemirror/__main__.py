import onedrivemirror
import argparse


def main():
    parser = argparse.ArgumentParser(description="Copy OneDrive folder to local path. Remember to set your "
                                                 "ONEDRIVEMIRROR_CLIENTID and ONEDRIVEMIRROR_CLIENT_SECRET "
                                                 "environment variables")
    parser.add_argument('--init', const=True, default=False, help='Pair your folder with OneDrive credentials')
    parser.add_argument('folders', nargs='2', help='[src] [dst]')
    args = parser.parse_args()
    sessions_file = ".onedrive.session"
    if args.init:
        onedrivemirror.create_session_file(session_file=sessions_file)
    else:
        client = onedrivemirror.MirrorClient(sessions_file)
        client.mirror(args.folders[0], args.folders[1])

if __name__ == '__main__':
    main()