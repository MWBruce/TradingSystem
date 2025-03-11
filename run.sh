#!/bin/bash
set -e 

BUILD_DIR="build"
EXECUTABLE="TradingSystem" 

if [ -d "$BUILD_DIR" ]; then
    echo "Removing existing build directory..."
    rm -rf "$BUILD_DIR"
fi

echo "Creating build directory..."
mkdir "$BUILD_DIR"
cd "$BUILD_DIR"

echo "Running CMake..."
cmake ..
echo "Running Make..."
make

echo "Running the executable..."
./${EXECUTABLE}

cd ..
echo "Cleaning up: removing build directory..."
rm -rf "$BUILD_DIR"
