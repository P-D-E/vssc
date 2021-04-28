#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------------
# @version: v0.1
# @created: 2021-04-28
# @author : Paolo D'Emilio
# @brief  : Converts savefiles from cp1252 encoding (used up to 0.5.x)
#               to utf-8 (used from 0.6 on)
#---------------------------------------------------------------------------------
#
# Vega Strike modding program for cp1252 to utf-8 conversion
# Copyright (C) 2008, 2021 Vega Strike team
# Internet: https://www.vega-strike.org/
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
#---------------------------------------------------------------------------------
# Features:
# converts single files, files matching a pattern, or entire directories
# moves the original files to a backup directory
#---------------------------------------------------------------------------------
# Requirements:
# python3
#---------------------------------------------------------------------------------

import argparse
import fnmatch
import os
import shutil


def dir_ok(path):
    """
    Checks the specified path is a writable directory.
    :param path: the path to check
    :return bool: True if the path is valid, False if not
    """
    if not os.path.exists(path):
        print(f'Error: {path} not found.')
        return False
    elif not os.path.isdir(path):
        print(f'Error: {path} is not a directory.')
        return False
    elif not os.access(path, os.W_OK):
        print(f'Error: {path} is not writable.')
        return False
    return True


def args_ok(args):
    """
    Checks the validity of the arguments, showing messages in case of errors.
    :param args: the arguments, specified via command line
    :return bool: True if the arguments are valid, False if not
    """
    result = dir_ok(args.dir_name)
    result = result and dir_ok(args.backup_dir)
    return result


def convert_files(args):
    """
    Converts the specified files to utf-8
    """
    print(f'Working directory: {args.dir_name}')
    files = os.listdir(args.dir_name)
    files.sort()
    for file_name in files:
        in_file_path = os.path.join(args.dir_name, file_name)
        if  os.path.isdir(in_file_path):
            continue
        if fnmatch.fnmatch(file_name, args.pattern):
            print(f'Converting file {file_name}')
            try:
                with open(in_file_path, encoding=args.encoding) as in_file:
                    text = in_file.read()
                shutil.copy2(in_file_path, args.backup_dir)
                with open(in_file_path, 'w', encoding='utf-8') as out_file:
                    out_file.write(text)
            except Exception as ex:
                print(ex)
        else:
            print(f'Skipping file {file_name}')
    print(f'All done. Original files moved to {args.backup_dir}')

    
def handle_command_line():
    """
    Handles the command line arguments and, if they're valid, converts the file(s).
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-d', '--dir', dest='dir_name', metavar='DIR', required=True, help='directory of files to convert')
    parser.add_argument('-p', '--pattern', default='*',
                        help='optional pattern of files to convert, e.g. -p "Bounty*" (used with -d)')
    parser.add_argument('-b', '--backup_dir', metavar='BACKUP_DIR', required=True, help='backup directory for the original files')
    parser.add_argument("-e", "--encoding", help="encoding of the text files", default='cp1252')
    args = parser.parse_args()
    if args_ok(args):
        convert_files(args)


if __name__ == "__main__":
    handle_command_line()
