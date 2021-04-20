#!/usr/bin/env python3

import argparse

database = {}


def main():
    parser = argparse.ArgumentParser()
    cmd = parser.add_subparser("Sub command")
    add_cmd = cmd.add_parser("add")


if __name__ == "__main__":
    main()
