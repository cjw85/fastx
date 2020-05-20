import os
import sys
from setuptools import setup, find_packages

__pkg_name__ = 'fastx'
__author__ = 'cwright'
__author_email__ = 'chris.wright@oxfordnanopore.tech'
__description__ = 'Just a simple kseq.h binding'

# Use readme as long description and say its github-flavour markdown
from os import path
this_directory = path.abspath(path.dirname(__file__))
kwargs = {'encoding':'utf-8'} if sys.version_info.major == 3 else {}
with open(path.join(this_directory, 'README.md'), **kwargs) as f:
    __long_description__ = f.read()
__long_description_content_type__ = 'text/markdown'

__path__ = os.path.dirname(__file__)
__pkg_path__ = os.path.join(os.path.join(__path__, __pkg_name__))
__version__ = "0.0.1"

# create requirements from requirements.txt
dir_path = os.path.dirname(__file__)
install_requires = []
with open(os.path.join(dir_path, 'requirements.txt')) as fh:
    reqs = (
        r.split('#')[0].strip()
        for r in fh.read().splitlines() if not r.strip().startswith('#')
    )
    for req in reqs:
        if req.startswith('git+https'):
            req = req.split('/')[-1].split('@')[0]
        install_requires.append(req)


if __name__ == '__main__':
    setup(
        name=__pkg_name__,
        version=__version__,
        url='https://github.com/cjw85/{}'.format(__pkg_name__),
        author=__author__,
        author_email=__author_email__,
        description=__description__,
        long_description=__long_description__,
        long_description_content_type=__long_description_content_type__,
        python_requires='>=3.5.*,',
        packages=find_packages(),
        cffi_modules=["build.py:ffibuilder"],
        install_requires=install_requires,
        zip_safe=False)
