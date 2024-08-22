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
    npm install
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

version() {
    # example: ./scripts.sh version 1.0.0
    if [ -z "$2" ]; then
        echo "Please provide the version."
        exit 1
    fi
    NEW_VERSION=$2
    SETUP_PY_PATH='./setup.py'
    SERVER_META_INFO_PATH='./pcp_serversdk_python/utils/ServerMetaInfo.py'
    SERVER_META_INFO_TEST_PATH='./tests/utils/test_ServerMetaInfo.py'
    echo "Getting the version..."
    sed -i '' "s/version=\"[0-9]*\.[0-9]*\.[0-9]*\",/version=\"$NEW_VERSION\",/" ${SETUP_PY_PATH}
    sed -i '' "s/PythonServerSDK\/v[0-9]*\.[0-9]*\.[0-9]*/PythonServerSDK\/v$NEW_VERSION/" ${SERVER_META_INFO_PATH}
    sed -i '' "s/PythonServerSDK\/v[0-9]*\.[0-9]*\.[0-9]*/PythonServerSDK\/v$NEW_VERSION/" ${SERVER_META_INFO_TEST_PATH}

    echo "Version complete."

    git add $SETUP_PY_PATH
    git add $SERVER_META_INFO_PATH
    git add $SERVER_META_INFO_TEST_PATH
    echo "Updated $SETUP_PY_PATH with version $NEW_VERSION"
    echo "Updated $SERVER_META_INFO_PATH with version $NEW_VERSION"
    echo "Updated $SERVER_META_INFO_TEST_PATH with version $NEW_VERSION"
    npm run changelog
    git add CHANGELOG.md
    git tag -a v$NEW_VERSION -m "Version $NEW_VERSION"
    echo "Updated CHANGELOG.md"
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

publish() {
    # example: ./scripts.sh publish <PyPI token>
    # check if the PyPI token is passed
    if [ -z "$2" ]; then
        echo "Please provide the PyPI token."
        exit 1
    fi
    echo "Uploading the package..."
    TOKEN=$2
    pcp_serversdk_python/bin/twine upload dist/* -u __token__ -p $TOKEN
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
version)
    version $@
    ;;
publish)
    publish $@
    ;;
*)
    echo "Usage: $0 {setup|install|build|test|lint|clear|version|publish}"
    exit 1
    ;;
esac
