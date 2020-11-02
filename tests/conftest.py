#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contextlib import contextmanager
import os
import shlex
import subprocess
import shutil
import stat

import pytest


def force_delete(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)


@pytest.fixture
def inside_dir():
    @contextmanager
    def _inside_dir(dirpath):
        """
        Execute code from inside the given directory
        :param dirpath: String, path of the directory the command is being run.
        """
        old_path = os.getcwd()
        try:
            os.chdir(dirpath)
            yield
        finally:
            os.chdir(old_path)

    return _inside_dir


@pytest.fixture
def bake_in_temp_dir():
    @contextmanager
    def _bake_in_temp_dir(cookies, *args, **kwargs):
        """
        Delete the temporal directory that is created when executing the tests
        :param cookies: pytest_cookies.Cookies,
            cookie to be baked and its temporal files will be removed
        """
        results = cookies.bake(*args, **kwargs)
        try:
            yield results
        finally:
            shutil.rmtree(str(results.project), onerror=force_delete)

    return _bake_in_temp_dir


@pytest.fixture
def run_inside_dir(inside_dir):
    def _run_inside_dir(command, dirpath):
        """
        Run a command from inside a given directory, returning the exit status
        :param command: Command that will be executed
        :param dirpath: String, path of the directory the command is being run.
        """
        with inside_dir(dirpath):
            return subprocess.check_call(shlex.split(command))

    return _run_inside_dir


@pytest.fixture
def package(cookies, bake_in_temp_dir, run_inside_dir):
    with bake_in_temp_dir(cookies) as results:
        run_inside_dir("pip3 install .", results.project)
        yield results
        run_inside_dir(
            f"pip3 uninstall -y {results.context['package_name']}", results.project,
        )
