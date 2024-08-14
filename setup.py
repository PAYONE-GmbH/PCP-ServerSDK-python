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
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here, e.g.
        # 'requests>=2.25.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)