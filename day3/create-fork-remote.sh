#!/usr/bin/bash
git remote add upstream https://github.com/ktbyers/pynet-ons-nov16
git fetch upstream
git rebase upstream/master
branch = git branch
git push origin master
print branch
