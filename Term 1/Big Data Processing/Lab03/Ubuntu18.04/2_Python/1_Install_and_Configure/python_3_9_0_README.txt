----------------------------------------------------------------------------

 PYTHON 3.9.0. INSTALLATION

----------------------------------------------------------------------------

In this section we discuss how to install Python 3.9.0.

---------------------------------------------------------
TERMINAL
---------------------------------------------------------
(1) $ sudo apt update
---------------------------------------------------------
(2) $ sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
---------------------------------------------------------
(3) $ wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz
---------------------------------------------------------

We download Python from https://www.python.org/downloads/ or we get it via ftp.

---------------------------------------------------------
(4) $ tar -xf Python-3.9.0.tgz
---------------------------------------------------------
(5) $ cd Python-3.9.0
---------------------------------------------------------
(6) $ ./configure --enable-optimizations
---------------------------------------------------------

We run the configure script which looks for dependencies. 

---------------------------------------------------------
(7) $ make -j $(nproc)
---------------------------------------------------------

We run the make accross the number of processors we have. 

---------------------------------------------------------
(8) $ sudo make altinstall
---------------------------------------------------------

We use altinstall instead of install so as to allow Python 3.9. to co-exist with other potential versions installed in the computer. 

---------------------------------------------------------
(9) $ sudo python3.9 -m pip install -U pip
---------------------------------------------------------

We upgrade pip to the most recent version so as to download packages for Python3.9.

---------------------------------------------------------
(10) $ which python3.9
---------------------------------------------------------

We get the location of Python3.9 in our computer.
/usr/local/bin/python3.9

---------------------------------------------------------
(11) $ python3.9
---------------------------------------------------------

Check whether you are getting the following output:

Python 3.9.0 (default, Oct  8 2020, 15:20:42) 
[GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 




