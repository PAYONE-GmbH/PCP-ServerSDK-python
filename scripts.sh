#!/bin/sh

setup() {
    echo "Setting up the environment..."
    python3 -m venv pcp_serversdk_python
    pcp_serversdk_python/bin/pip install setuptools
    echo "Environment set up."
}

# Function to install dependencies
install() {
    echo "Installing dependencies..."
    pcp_serversdk_python/bin/pip install setuptools
    pcp_serversdk_python/bin/python3 setup.py install
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
publish)
    publish
    ;;
*)
    echo "Usage: $0 {setup|install|build|test|publish}"
    exit 1
    ;;
esac
