from distutils.core import setup

setup(
  name='pyTelegram'
  , version='0.0.1'
  , packages=['pyTelegram']
  , description='Pure python implementation of telegram'
  , author='Byoungwoo Song'
  , author_email='sbw228@gmail.com'
  , url='http://chidea.github.io/pyTelegram'
  , download_url='https://github.com/chidea/pyTelegram/zipball/master'
  , keywords=['telegram', 'messenger']
  , classifiers=[
    'Programming Language :: Python'
    , 'Programming Language :: Python :: 3 :: Only'
    , 'Development Status :: 1 - Planning'
    , 'Environment :: Console'
    , 'Intended Audience :: Developers'
    , 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    , 'Operating System :: OS Independent'
    , 'Topic :: Software Development :: Libraries :: Python Modules'
    , 'Topic :: Communications :: Chat'
  ]
  , long_description="""\
pyTelegram
==========
Pure python implementation of telegram

prerequisites
=============
Python 3.4
  PyCrypto
"""
)