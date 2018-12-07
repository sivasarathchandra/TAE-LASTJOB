import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="An argparse example")

    parser.add_argument('action', help='The action to take (e.g. install, remove, etc.)')
    parser.add_argument('foo-bar', help='Hyphens are cumbersome in positional arguments')

    args = parser.parse_args()

    if args.action == "install":
        print("You asked for installation")
    else:
        print("You asked for something other than installation")

    # The following do not work:
    # print(args.foo-bar)
    # print(args.foo_bar)

    # But this works:
    print(getattr(args, 'foo-bar'))
