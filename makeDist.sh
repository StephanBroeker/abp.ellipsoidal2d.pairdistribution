#!/bin/bash

# -- Shell script for collecting files for distribution --

# Check for self to see if directory is correct
if [ ! -f "./makeDist.sh" ]; then
  echo "Error: Please cd to /supp."
  exit
fi
# Clean old dist
if [ -d "dist" ]; then
  echo "Removing old /dist..."
  rm -r "dist"
fi
# Make doc
echo "Creating documentation..."
. makeDoc.sh
# Collect files
echo "Collecting files..."
mkdir "dist"
cp -R "abellipsoids2d" "dist"
if [ -d "dist/abellipsoids2d/__pycache__" ]; then
  rm -r "dist/abellipsoids2d/__pycache__"
fi
cp "demo.py" "dist/"
cp -R "doc/abellipsoids2d" "dist/doc"
cp "abellipsoids2d/Interpolation_parameters.csv" "dist/"
cp "README.md" "dist/"

echo "Done!"
