#!/usr/bin/env doit

import os
import glob
import subprocess

from doit.tools import run_once


def task_create():
    """Compile Qt UI files to python files"""
    for ui_file in glob.glob("widgets/*.ui"):
        py_file = f"{ui_file[:-3]}.py"
        yield {
            "name": py_file,
            "actions": ["pyside6-uic %s -o %s" % (ui_file, py_file)],
            "file_dep": [ui_file],
            "targets": [py_file],
            "clean": True,
        }


def task_start():
    """Run the app"""
    return {
        "actions": ["python main.py"],
        "file_dep": ["main.py"],
        "task_dep": ["create"],
    }
