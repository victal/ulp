#!/bin/bash

PIPENV=$(which pipenv)

if [ -z "$PIPENV" ]
    echo "pipenv not found. Install pipenv with 'pip3 install --user pipenv' before running this script"
    exit 1
fi

$PIPENV install --dev

CURRENT_VERSION="$(python setup.py --version)"
NEXT_VERSION="$1"
if [ -z "$NEXT_VERSION" ]
then
    echo "Next version not provided, releasing a new bugfix version"
    NEXT_VERSION="$(echo $CURRENT_VERSION | awk 'BEGIN{FS=OFS="."}{$NF++;print;}')"
fi

#Cleanup
rm -rf build/ dist/

#Update version
sed -i "s/'$CURRENT_VERSION'/'$NEXT_VERSION'/g" setup.py

#Generate artifacts
python setup.py sdist bdist_wheel

#Deploy artifacts
twine upload dist/*

#Create git tag
git add setup.py
git ci -m "Bump version to $NEXT_VERSION for release"
git tag -a -m "Release $NEXT_VERSION" "$NEXT_VERSION"
git push --tags
