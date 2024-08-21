#!/bin/sh

setup() {
    echo "Setting up the environment..."
    python3 -m venv pcp_serversdk_python
    pcp_serversdk_python/bin/pip cache purge
    pcp_serversdk_python/bin/pip install setuptools
    pcp_serversdk_python/bin/pip install --upgrade setuptools pip
    echo "Environment set up."
}

# Function to install dependencies
install() {
    echo "Installing dependencies..."
    pcp_serversdk_python/bin/pip install -r requirements.txt
    echo "Dependencies installed."
}

# Function to build the package
build() {
    echo "Building the package..."
    pcp_serversdk_python/bin/python3 setup.py sdist bdist_wheel
    echo "Build complete."
}

# Function to run tests
test() {
    echo "Running tests..."
    pcp_serversdk_python/bin/pytest --cov=pcp_serversdk_python --cov-report xml --cov-report html tests/
    echo "Tests complete."
}

lint() {
    echo "Running lint..."
    pcp_serversdk_python/bin/ruff check ./pcp_serversdk_python
    pcp_serversdk_python/bin/ruff check ./tests
    echo "Lint complete."
}

clear() {
    echo "Removing __pycache__ directories..."
    find . -type d -name "__pycache__" -exec rm -rf {} +
    rm -rf pcp_serversdk_python/bin
    rm -rf pcp_serversdk_python/include
    rm -rf pcp_serversdk_python/lib
    rm -f pcp_serversdk_python/pyvenv.cfg
    rm -rf pcp_serversdk_python.egg-info
    rm -f .coverage
    rm -f coverage.xml
    rm -rf htmlcov
    rm -rf dist
    rm -rf build
    rm -rf .pytest_cache
    rm .rf .eggs
    rm -rf .ruff_cache

    echo "All __pycache__ directories have been removed."
}

# Function to publish the package
publish() {
    # check if the PyPI token is passed
    if [ -z "$2" ]; then
        echo "Please provide the PyPI token."
        exit 1
    fi
    echo "Uploading the package..."
    pcp_serversdk_python/bin/twine upload dist/* -u __token__ -p $2
    echo "Upload complete."
}

# Check the first argument passed to the script
case "$1" in
setup)
    setup
    ;;
install)
    install
    ;;
build)
    build
    ;;
test)
    test
    ;;
lint)
    lint
    ;;
clear)
    clear
    ;;
publish)
    publish
    ;;
*)
    echo "Usage: $0 {setup|install|build|test|publish}"
    exit 1
    ;;
esac
