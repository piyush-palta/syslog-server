# Syslog Server
Syslog Server is a python based server module used for syslogging of events. It is an integral part of Intrusion Detection System project & will be log authorization & autheuntication events, which will be used to train the expert system.


### Getting Started
To clone the project in your local systems: 
```console
$ git clone https://github.com/piyush-palta/syslog-server.git
```

### Prerequisites
Make sure you have installed all of the following prerequisites on your development machine:
* Git - [Download & Install Git](https://git-scm.com/downloads). OSX and Linux machines typically have this already installed.
* Python - [Download & Install Python](https://www.python.org/downloads/). For linux machines, you can also use this [Python Docs](https://docs.python-guide.org/starting/install3/linux/) to install Python.
* pip - [Download & Install pip](https://pip.pypa.io/en/stable/installing/). Make sure you've installed python first.

### Installing

The below command will start the syslog server :

```bash
$ python main.py
```
You can configure host, tcp_port, udp_port & log file location by changing them in main.py 
