#!/bin/sh

pcp_serversdk_python/bin/pytest --cov=pcp_serversdk_python --cov-report xml --cov-report html tests/
