Dependencies
============

bookex is tested to work under Python 2.6+ and Python 3.3+
(using the same codebase thanks to an embedded copy of `six <http://pythonhosted.org/six/>`_).

The required dependencies to build the software is virtualenv >= 1.10 and django >= 1.5

For running the examples Postgresql >= 9.3.2 is required 

This configuration matches the Ubuntu 10.04 LTS release from April 2010.


Install
=======

This package uses distutils, which is the default way of installing
python modules. To install in your home directory, use::

  python setup.py install --user

To install for all users on Unix/Linux::

  sudo python setup.py install

