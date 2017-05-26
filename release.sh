#!/bin/bash

PYTHON=$(which python)
TWINE=$(which twine)

CURRENT_VERSION="$(python setup.py --version)"
NEXT_VERSION="$1"

#Cleanup
rm -rf build/ dist/

#Update version
sed -i "s/'$CURRENT_VERSION'/'$NEXT_VERSION'/g" setup.py

#Generate artifacts
python setup.py sdist bdist_wheel

#Deploy artifacts
#twine upload dist/*

#Create git tag
git add setup.py
git ci -m "Bump version to $NEXT_VERSION for release"
git tag -a -m "Release $NEXT_VERSION" "$NEXT_VERSION"
#git push --tags
