#!/bin/sh

git init
echo "Setting https://github.com/TDA/"$1".git as origin"
git rad "https://github.com/TDA/"$1".git" #remote add origin master