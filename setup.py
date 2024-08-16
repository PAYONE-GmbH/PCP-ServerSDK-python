# setup.py

from setuptools import setup, find_packages

setup(
    name='pcp_serversdk_python',
    version='0.0.1',
    author='PAYONE-GmbH',
    author_email='',
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/PAYONE-GmbH/PCP-ServerSDK-python',
    keywords='payone, pcp, server, python, sdk',
    packages=find_packages(),
    install_requires=[
        'pytest>=8.3.2',
        'pytest-cov>=5.0.0',
        'twine>=5.1.1',
        'httpx>=0.27.0',
        'pydantic>=2.8.2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)