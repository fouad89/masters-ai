---------------------------------------------------------

 JAVA OPENJDK 8 INSTALLATION

---------------------------------------------------------

In this section we discuss how to install Java OpenJDK 8. 

---------------------------------------------------------
TERMINAL
---------------------------------------------------------
(1)  $ sudo apt-get update
---------------------------------------------------------
(2)  $ sudo apt-get install openjdk-8-jdk
---------------------------------------------------------
(3)  $ sudo update-alternatives --config java
---------------------------------------------------------

We ensure that Java OpenJDK 8 is the selected Java version selected. 

There are 2 choices for the alternative java (providing /usr/bin/java).

  Selection    Path                                            Priority   Status
------------------------------------------------------------
  0            /usr/lib/jvm/java-11-openjdk-amd64/bin/java      1111      auto mode
  1            /usr/lib/jvm/java-11-openjdk-amd64/bin/java      1111      manual mode
* 2            /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java   1081      manual mode

---------------------------------------------------------
(4)  $ sudo update-alternatives --config javac
---------------------------------------------------------

We ensure that Java OpenJDK 8 is the selected Java version selected.

There are 2 choices for the alternative javac (providing /usr/bin/javac).

  Selection    Path                                          Priority   Status
------------------------------------------------------------
  0            /usr/lib/jvm/java-11-openjdk-amd64/bin/javac   1101      auto mode
  1            /usr/lib/jvm/java-11-openjdk-amd64/bin/javac   1101      manual mode
* 2            /usr/lib/jvm/java-8-openjdk-amd64/bin/javac    1081      manual mode

---------------------------------------------------------
(5)  $ sudo gedit ~/.bashrc
---------------------------------------------------------

Add an extra line exporting the variable JAVA_HOME. 
The value of the line will be the one from command (3), trimming the /bin/java part of it. 
Thus, in the case before the line will be:

export JAVA_HOME="/usr/lib/jvm/java-1.8.0-openjdk-amd64"
export PATH=$PATH:/usr/lib/jvm/java-1.8.0-openjdk-amd64/bin

