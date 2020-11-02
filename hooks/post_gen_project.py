#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import call

call(["git", "init", "-b", "init_commit"])
call(["git", "add", "*"])
call(["git", "commit", "-m", "Initial commit"])
call(["git", "remote", "add", "origin", "{{ cookiecutter.git_url }}"])
